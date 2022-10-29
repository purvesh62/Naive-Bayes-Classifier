import joblib
from textblob.classifiers import NaiveBayesClassifier
import json

process_data = []

with open('data.json') as fp:
    data = json.loads(fp.read())
    for key in data.keys():
        for text in data.get(key).get('text'):
            process_data.append((text, key))
            
clf = NaiveBayesClassifier(process_data)

joblib.dump(clf, 'classifier.pkl')
