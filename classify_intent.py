import pickle
import json
import random

with open('data.json') as fp:
    data = json.loads(fp.read())

def detect_intent(text):
    with open('classifier.pkl', 'rb') as file:
        clf = pickle.load(file)
        prob_dist = clf.prob_classify(text)
        response = {
            "text": text,
            "intent": prob_dist.max(),
            "accuracy": prob_dist.prob(prob_dist.max())
        }
        if response.get('accuracy') > 0.60:
            return (response, True)
        else:
            return (response, False)
        

inp = input("User text: ")
while inp:
    if inp:
        detected_intent = detect_intent(inp)
        responses = data.get(detected_intent[0].get('intent')).get('responses')
        print(detected_intent[0])
        print(f"Response: {random.choice(responses)}")
    else:
        break
    inp = input("Input: ")




