from django.shortcuts import render
import joblib
from .models import CustomerFeedback
def home(request):
    return render(request,'home.html')
#stroing feedbacks
def history(request):
    feedbacks=CustomerFeedback.objects.all().order_by("-created_at") #saved all reviews from mysql
    
    return render(request,"history.html",{"feedbacks":feedbacks})

#this predicting sentiments
def predict_sentiment(request):
    #load model and tfidf
    model=joblib.load("ml_model/sentiment_model.pkl")
    vectorizer=joblib.load("ml_model/tfidf_vectorizer.pkl")
    
    #request type..
    if request.method=="POST":
        review=request.POST.get("review")
        if not review or not review.strip():
            return render(request,"home.html",{"error": "please enter a review before predicting."})
        #convert to tfidf
        review_tfidf=vectorizer.transform([review])
        #predict the reviewtfidf
        prediction=model.predict(review_tfidf)
        
        #adding customer feedback and sentiment to save here
        CustomerFeedback.objects.create(
            review=review,
            sentiment=prediction[0]
        )
        
        return render(request,"predict.html",{"review":review, "sentiment":prediction[0]})
    return render(request,"home.html")

