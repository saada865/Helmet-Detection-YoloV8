
from sklearn.model_selection import train_test_split

from datasets import load_dataset

ds = load_dataset("/Users/saadahmadmalik/Documents/Coding/WORK/archive (1)")

ds_split_train_test = train_test_split(test_size=0.15)

train_ds, test_ds = ds_split_train_test["train"], ds_split_train_test["test"]

ds_split_train_val = train_test_split(test_size=0.15/0.85)

train_ds, val_ds = ds_split_train_test["train"], ds_split_train_test["test"]
