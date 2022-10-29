# Naive Bayes Classifier for intent classification in python

You can built a simple classifier for your chatbot using `NaiveBayesClassier` from [textblob](https://textblob.readthedocs.io/en/dev/classifiers.html)

The dataset I've used is taken from [Kaggle](https://www.kaggle.com/datasets/himanshu01dadhich/chat-bot-dataset)

---

## Steps to build your own model

1. Create a dataset which has data in from of `(Training Phrase, Intent Name)`.
2. You can make list of such phrases with the name of the intent.
3. I've process the dataset and generated a json file which has data in the form

    ```
    [
        ...,
        "GreetingResponse": {
            "text": [
                "My user is Adam",
                "This is Adam",
                "I am Adam",
                "It is Adam",
                "My user is Bella",
                "This is Bella",
                "I am Bella",
                "It is Bella"
            ],
            "responses": [
                "Great! Hi <HUMAN>! How can I help?",
                "Good! Hi <HUMAN>, how can I help you?",
                "Cool! Hello <HUMAN>, what can I do for you?",
                "OK! Hola <HUMAN>, how can I help you?",
                "OK! hi <HUMAN>, what can I do for you?"
            ]
        },
        ...
    ]
    ```

4. Here the key name **"GreetingResponse"** is the name of the intent and in that **text** contains list of phrases with the list of **responses** below.

---

### Steps to run the code

`pip install -r requirements.txt`

1. Create a Naive Bayes classifier using `create_naive_bayes_classifier.py`

Execute > `python create_naive_bayes_classifier.py`

2. Run the next script to test the classifier which you've created.

Execute > `python classify_intent.py`
