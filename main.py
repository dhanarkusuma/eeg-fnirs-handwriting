from huggingface_hub import hf_hub_download
import os
import pandas as pd

def define_auth():
    os.environ["HF_TOKEN"] = ""

def get_raw_data():
    return hf_hub_download(
        repo_id="lasfk/EEG-fNIRS-based-Handwriting-Trajectory-Dataset",
        repo_type="dataset",
        filename="raw.zip"
    )

def get_dataset(type="train"):
    splits = {'train': 'train_meta.csv', 'test': 'test_meta.csv'}
    df = pd.read_csv("hf://datasets/lasfk/EEG-fNIRS-based-Handwriting-Trajectory-Dataset/" + splits[type])
    return df

def main():
    define_auth()
    print(get_raw_data())
    df_train = get_dataset(type="train")
    print(df_train.head())



if __name__ == '__main__':
    main()
