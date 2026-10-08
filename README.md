# AI-Based Sentiment Analysis Web Application

## Project Overview

This project is a web-based sentiment analysis application developed using Django, Python, Natural Language Processing (NLP), and Machine Learning.

The application allows users to enter customer reviews and automatically classifies them into:

- Positive
- Negative
- Neutral

The review and predicted sentiment are stored in a MySQL database and can be viewed through the feedback history page.

## Technologies Used

- Python
- Django
- Natural Language Processing (NLP)
- TF-IDF
- Logistic Regression
- MySQL
- HTML
- CSS

## Main Features

- Customer review input
- Sentiment prediction
- Positive, Negative, and Neutral classification
- MySQL database storage
- Feedback history
- Input validation
- Simple and user-friendly interface

## Machine Learning Workflow

Dataset → Text Cleaning → Train/Test Split → TF-IDF → Logistic Regression → Prediction

## Application Workflow

User enters review → Django processes the review → TF-IDF converts the text → Machine Learning model predicts sentiment → Result is displayed → Feedback is stored in MySQL

## Dataset

The project uses a dataset containing 500 customer review records with sentiment labels.

## Model Performance

The Logistic Regression model achieved 99% accuracy on the held-out test dataset.

## Project Structure

```text
sentiment_analysis/
├── dataset/
├── ml_model/
├── training/
├── sentiment/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

## Future Enhancements

- User authentication
- Dashboard and analytics
- Data visualization
- Larger real-world datasets
- Deployment to a cloud platform
- Advanced Machine Learning models

## Author

Nakka Srinivasulu