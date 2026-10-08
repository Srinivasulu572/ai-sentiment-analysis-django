import pandas as pd
import joblib 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#open or read dataset.
df=pd.read_csv("dataset/processed/cleaned_dataset.csv")

#separate text and sentiment..
texts=df["text"]
labels=df["sentiment"]

#split the data..

x_train,x_test,y_train, y_test=train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42
)
print("Training data:")
print(x_train)

print("\nTraining labels:")
print(y_train)

print("\nTesting data:")
print(x_test)

print("\nTesting labels:")
print(y_test)
# convert text into numericals..
vectorizer=TfidfVectorizer()

x_train_tfidf=vectorizer.fit_transform(x_train)
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
x_test_tfidf=vectorizer.transform(x_test)

#create the ml model
model=LogisticRegression(max_iter=1000)#it works as numerical feature produced by tfidf.

#train the model
model.fit(x_train_tfidf,y_train)
#save the model of text and tfidf..
joblib.dump(model,"ml_model/sentiment_model.pkl")
joblib.dump(vectorizer,"ml_model/tfidf_vectorizer.pkl")

model=joblib.load("ml_model/sentiment_model.pkl")
model=joblib.load("ml_model/tfidf_vectorizer.pkl")


print("Training completed!")
print("Model and vectorized saved!")

