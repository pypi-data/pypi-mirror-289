import duckdb

con = duckdb.connect("../out/storage.db")
rel = con.sql("SELECT * FROM range(5) tbl(id)")
rel.create('"../soething/name.txt"')
