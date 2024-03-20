# %%
#  import polars as pl

# %%
file = "/data/datasets/2019-Oct.csv"
# "/data/datasets/2019-OCT-half.csv"
# "/data/datasets/2019-OCT-half.parquet"
# "/data/datasets/kappiccino/general_ledger_details.csv"
# %%
# 2.8 GB File
# 5.3 GB file
ledger = pl.read_csv(file, has_header=True, ignore_errors=True, rechunk=False)
# 363 MB file
# ledger = pl.read_parquet(file)
# %% count of rows - 21224381 rows
ledger.count()
# %% run some filter condition
ledger.filter((pl.col("price") < 35.50) & (pl.col("brand") == "jbl"))
