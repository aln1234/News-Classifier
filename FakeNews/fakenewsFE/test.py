
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.cm as cmap
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score


def predict(filename):
    df = pd.read_csv('fakenewsFE/train.csv')
    print(df)

    y = df.label

    df.drop("label", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], y, test_size=0.5, random_state=53)

    count_vectorizer = CountVectorizer(stop_words='english')

    count_train = count_vectorizer.fit_transform(X_train)

    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    tfidf_train = tfidf_vectorizer.fit_transform(X_train)

    print(tfidf_vectorizer.get_feature_names()[-10:])

    print(count_vectorizer.get_feature_names()[:10])

    count_df = pd.DataFrame(
        count_train.A, columns=count_vectorizer.get_feature_names())
    tfidf_df = pd.DataFrame(
        tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())
    difference = set(count_df.columns) - set(tfidf_df.columns)
    set()
    print(count_df.equals(tfidf_df))
    count_df.head()

    tfidf_df.head()

    linear_clf = PassiveAggressiveClassifier(
        n_iter_no_change=5)
    linear_clf.fit(tfidf_train, y_train)

    linear_clf.fit(tfidf_train, y_train)

    a = pd.read_csv(filename, encoding='latin1')
    X_test = a['text']

    count_test = count_vectorizer.transform(X_test)

    tfidf_test = tfidf_vectorizer.transform(X_test)
    pred = linear_clf.predict(tfidf_test)
    probs = linear_clf.decision_function(tfidf_test)
    probs = (probs+1.0)/2.0
    print(probs)
    flag = True
    for i in probs:
        if(i > (0.25)):
            flag = True
        else:
            flag = False

    print(flag)
    return (probs[0]*100)
