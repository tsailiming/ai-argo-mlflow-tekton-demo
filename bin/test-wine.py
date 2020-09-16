#!/usr/bin/env python

import os
import warnings
import sys

import argparse
from pprint import pprint

from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="predict url")
    args = parser.parse_args()

    if not args.url:
        print("Prediction URL not provided")
        sys.exit(-1)

    url = "{}/api/v1.0/predictions".format(args.url)

    warnings.filterwarnings("ignore")
    # Read the wine-quality csv file from the URL
    csv_url = (
        "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    )
    try:
        data = pd.read_csv(csv_url, sep=";")
    except Exception as e:
        logger.exception(
            "Unable to download training & test CSV, check your internet connection. Error: %s", e
        )

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    print("Predict URL: {}".format(url))
    
    payload = {'data': {'ndarray': train_x.sample(1).values.tolist()}}
    print("Payload: {}".format(payload))
    
    response = requests.post(url, json = payload).json()
    print("Response: {}".format(response))    
                            