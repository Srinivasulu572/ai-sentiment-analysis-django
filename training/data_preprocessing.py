import pandas as pd

def clean_text(text):
    text=text.lower()
    text= text.replace("!","")
    text=text.replace(".","")
    text=text.replace(",","")
    text=text.strip()
    return text

#read the data
df=pd.read_csv("dataset/raw/dataset.csv")

#clean the text.
df["text"]= df["text"].apply(clean_text)

#save the cleaned text.
df.to_csv("dataset/processed/cleaned_dataset.csv",index=False)
print("Data preprocessing complete!")
print(df.head()) #