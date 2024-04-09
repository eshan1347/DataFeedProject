# Sentiment Analysis

This project performs sentiment analysis on Reddit posts scraped from the "politics" subreddit using natural language processing techniques. It utilizes a Multinomial Naive Bayes classifier trained on a 
labeled dataset to classify the sentiment of the posts into different categories.

## Table of Contents
- Introduction
- Setup
- Front-End
- Results

## Introduction
The goal of this project is to analyze the sentiment of Reddit posts on political topics. It involves scraping posts from the "politics" subreddit, preprocessing the text data, training a Multinomial 
Naive Bayes classifier, and predicting the sentiment of new posts. It provides a front-end for users to utilize it and an authentication facility.

## Setup

1. Install Python dependencies:
   `pip install numpy pandas praw scikit-learn nltk`
   
3. Install NLTK data:
   `python -m nltk.downloader stopwords`
   
5. Clone the repository:
   `git clone https://github.com/eshan1347/DataFeedProject && cd DataFeedProject`
   
7. Run the Python script:
   `python sentiment_analysis.py`

## Front-End
A complete frontend for this project has been developed using React.js and Flask. It includes login and home pages for interacting with the sentiment analysis model.

## Results
The trained model will predict the sentiment of Reddit posts based on the provided dataset and new scraped posts. The results will be displayed in a multi-class format, where each sentiment category 
is assigned a numerical value.
