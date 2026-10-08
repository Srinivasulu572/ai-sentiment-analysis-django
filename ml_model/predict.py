import joblib
from prediction_preprocessing import clean_text

#load the saved model
model=joblib.load("ml_model/sentiment_model.pkl")

#load the tfidf vectorizer..
vectorizer=joblib.load("ml_model/tfidf_vectorizer.pkl")

#get new customer from user
review=input("Enter your review: ")

#clean the text of new_review.
review=clean_text(review)


#convert text into numerical
review_tfidf=vectorizer.transform([review])

#predict sentiment..
prediction=model.predict(review_tfidf)

print("Sentiment: ",prediction[0])

#load model and vectortfidf-> new review->cont tfidf->predict
