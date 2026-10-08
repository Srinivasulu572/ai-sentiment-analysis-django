import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#read the data..
df=pd.read_csv("dataset/processed/cleaned_dataset.csv")

#separate the text and sentiment..
texts=df["text"]
lables=df["sentiment"]

#split the data in same way as training..
x_train,x_test,y_train,y_test=train_test_split(
    texts,lables,test_size=0.2,random_state=42
)
#load the saved model and tfidf vectorizer..
model=joblib.load("ml_model/sentiment_model.pkl")
vectorizer=joblib.load("ml_model/tfidf_vectorizer.pkl")

#we have to convert text into numericals..
x_test_tfidf=vectorizer.transform(x_test)

#make predictions..
y_pred=model.predict(x_test_tfidf)
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))

#calculate the accuracy..
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy: ",accuracy)

# above test data->tfidf->saved model->prediction->compare with acutal answers->accuracy
