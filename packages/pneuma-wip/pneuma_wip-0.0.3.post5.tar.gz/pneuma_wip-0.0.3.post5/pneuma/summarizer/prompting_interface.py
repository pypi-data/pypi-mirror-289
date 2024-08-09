import logging

from transformers import set_seed
from transformers.pipelines.text_generation import TextGenerationPipeline
from transformers.tokenization_utils_base import PreTrainedTokenizerBase

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("prompting_interface.py")


def truncate_text(
    tokenizer: PreTrainedTokenizerBase,
    conversation: list[dict[str, str]],
    context_length: int,
    max_new_tokens: int,
):
    """
    Truncate the text of a conversation according to context_length and max_new_tokens

    ### Parameters:
    - tokenizer (PreTrainedTokenizerBase): A PreTrainedTokenizerBase from HuggingFace
    - conversation (list[dict[str, str]]): A conversation
    - context_length (int): The context length of a model
    - max_new_tokens (int): Max new tokens to be generated

    ### Returns:
    - text (str): The truncated text
    """
    base = [{"role": "user", "content": ""}]
    base_len = len(
        tokenizer.apply_chat_template(base, tokenize=True, add_generation_prompt=True)
    )
    max_tokens = context_length - base_len - max_new_tokens
    tokens = tokenizer.tokenize(conversation[0]["content"])[:max_tokens]
    return tokenizer.convert_tokens_to_string(tokens)


def is_within_context_length(
    tokenizer: PreTrainedTokenizerBase,
    conversation: list[dict[str, str]],
    context_length: int,
):
    """
    Check whether a conversation is within context_length

    ### Parameters:
    - tokenizer (PreTrainedTokenizerBase): A PreTrainedTokenizerBase from HuggingFace
    - conversation (list[dict[str, str]]): A conversation
    - context_length (int): The context length of a model

    ### Returns:
    - check_result (bool): Indicator of whether the check result is True
    """
    conv_len = len(
        tokenizer.apply_chat_template(
            conversation, tokenize=True, add_generation_prompt=True
        )
    )
    return conv_len <= context_length


def remove_unset_generation_configs(generation_configs: dict[str, any]):
    """
    Check whether a conversation is within context_length

    ### Parameters:
    - generation_configs (dict[str, any]): A dictionary of generation configs
    """
    if generation_configs["top_k"] == 0:
        del generation_configs["top_k"]
    if generation_configs["top_p"] == 1.0:
        del generation_configs["top_p"]
    if generation_configs["penalty_alpha"] == 0.0:
        del generation_configs["penalty_alpha"]
    if generation_configs["temperature"] == 0.0:
        del generation_configs["temperature"]


def prompt_pipeline(
    pipe: TextGenerationPipeline,
    conversations: list[list[dict[str, str]]],
    batch_size=2,
    context_length=8192,
    max_new_tokens=512,
    do_sample=False,
    top_k=0,
    top_p=1.0,
    penalty_alpha=0.0,
    temperature=0.0,
):
    """
    Prompt the pipeline with a conversation

    ### Parameters:
    - pipe (TextGenerationPipeline): An initialized pipeline.
    - conversations (list[list[dict[str, str]]]): The data type of the model
    - batch_size (int): The batch size to process conversations
    - context_length (int): The LLM's context length
    - max_new_tokens (int): Max number of tokens generated for each prompt
    - do_sample (bool): Perform sampling or not
    - top_k (int): The number of tokens to consider when sampling
    - top_p (float): Minimum cumulative probability of tokens being considered
    - penalty_alpha (float): The amount of focus being put to ensure non-repetitiveness
    - temperature (float): Control how sharp the distribution (smaller means sharper)

    ### Returns:
    - conversations (list[list[dict[str, str]]]): The conversations appended with the model's outputs
    """
    generation_configs = {
        "max_new_tokens": max_new_tokens,
        "top_k": top_k,
        "top_p": top_p,
        "do_sample": do_sample,
        "penalty_alpha": penalty_alpha,
        "temperature": temperature,
        "pad_token_id": pipe.tokenizer.eos_token_id,
    }
    remove_unset_generation_configs(generation_configs)
    try:
        for conversation in conversations:
            if not is_within_context_length(
                pipe.tokenizer, conversation, context_length
            ):
                truncated_text = truncate_text(
                    pipe.tokenizer, conversation, context_length, max_new_tokens
                )
                conversation[0]["content"] = truncated_text
        set_seed(42)  # Enhance reproducibility for when using sampling
        answers = pipe(
            conversation, truncation=True, batch_size=batch_size, **generation_configs
        )
        conversations = []
        if isinstance(answers[0], dict):
            answers = [answers]
        for answer in answers:
            conversations.append(answer[0]["generated_text"])
        return conversations
    except Exception as error:
        logger.warning(error)
        return [[{"role": "user", "content": ""}]]


if __name__ == "__main__":
    import torch

    from .pipeline_initializer import initialize_pipeline

    pipe = initialize_pipeline("meta-llama/Meta-Llama-3-8B-Instruct", torch.bfloat16)
    conversations = [[{"role": "user", "content": "Tell me about Illinois!"}]]
    output = prompt_pipeline(pipe, conversations, 1, 8192)

    assert len(output) == 2
    assert output[0][-1]["role"] == "assistant"
