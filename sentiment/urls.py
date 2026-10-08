from django.urls import path
from . import  views #we are importing view in that app

urlpatterns = [
    path('',views.home,name='home'),
    path("predict/",views.predict_sentiment,name="predict_sentiment"),
    path("history/",views.history,name="history"),
    
    
]
