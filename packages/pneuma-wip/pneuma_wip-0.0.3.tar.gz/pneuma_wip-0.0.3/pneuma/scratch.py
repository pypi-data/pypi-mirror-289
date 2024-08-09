import chromadb

client = chromadb.PersistentClient("out/indexes")

collection = client.get_collection("sample_index")
print(collection)
print(collection.count())
print(collection.query("hello"))
