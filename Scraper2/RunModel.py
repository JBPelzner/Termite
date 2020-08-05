### Main logic
import warnings
warnings.filterwarnings("ignore")

#from sklearn.svm import LinearSVC
import random
from random import randrange
import pickle
#from sklearn.model_selection import train_test_split
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.linear_model import LogisticRegression
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.svm import LinearSVC
import numpy as np
import re
from readability import Readability

## other loads 
topic_model = pickle.load(open('topicmodel.sav', 'rb'))
topic_vectorizer = pickle.load(open('topicvectorizer.sav', 'rb'))

all_subclasses= [["sub1_1", "sub1_2", "sub1_3", "sub1_4", "sub1_5", "sub1_6", "sub1_7"],
["sub2_1", "sub2_2", "sub2_3", "sub2_4", "sub2_5", "sub2_6", "sub2_7", "sub2_8","sub2_9"],
["sub3_1", "sub3_2", "sub3_3", "sub3_4", "sub3_5", "sub3_6", "sub3_7", "sub3_8", "sub3_9","sub3_10"],
["sub4_1", "sub4_2", "sub4_3", "sub4_4", "sub4_5", "sub4_6"],
["sub5_1", "sub5_2", "sub5_3", "sub5_4", "sub5_5"],
["sub6_1", "sub6_2", "sub6_3", "sub6_4"]
]

# preprocess data 

def get_lines(body):
    output_lines = []
    prelines = body.replace('\n', '. ')
    lines = prelines.split('. ')
    for line in lines:
        if len(line) > 20:
            output_lines.append(line)
        
    return output_lines

def super_topic_classifier(line):
    
    vectorized = topic_vectorizer.transform([line])
    topic = topic_model.predict(vectorized)
    conf = topic_model.predict_proba(vectorized)
    
    return topic, conf



def subtopic_classification(topic_lines, topic_num, subclass):
    
    foldername = "./topic" + str(topic_num) + "models"
    model_filename = foldername + '/' + subclass + "model.sav"
    vectorizer_filename = foldername + '/' + subclass + "vectorizer.sav"
    
    ## what kind of model logic
    
    subtopic_model = pickle.load(open(model_filename, 'rb'))
    subtopic_vectorizer = pickle.load(open(vectorizer_filename, 'rb'))
    
    vectorized = subtopic_vectorizer.transform(topic_lines)
    

    #labels = subtopic_model.predict(vectorized)
    confs = subtopic_model.predict_proba(vectorized)
    
    
    confs_in_pos_class = confs[:,1]
    
    return confs_in_pos_class

    

def topic_classifier(topic_lines, topic_num, scores):


    subclasses = all_subclasses[topic_num-1]
    
    
    for subclass in subclasses: 

        if len(topic_lines) > 0:
            max_conf = 0
            extract = ""

            items = [x[2] for x in topic_lines]


            confs = subtopic_classification(items, topic_num, subclass)

            max_index = np.argmax(confs)
            max_conf = confs[max_index]
            extract = items[max_index]

            scores[subclass + "_score"] = max_conf
            scores[subclass + "_extract"] = extract.replace('\n',' ')
        else:
            scores[subclass + "_score"] = 0
            scores[subclass + "_extract"] = "No information found."


def get_lexicon_score(body):
    r = Readability(body)
    

    d = r.flesch()

    
    return(d.score)

    

def getModelScores(body):
    

    
    scores = {}
    
    lines = get_lines(body)

    lexicon_score = get_lexicon_score(body)
    scores['lexicon_score'] = lexicon_score
    topic1 = []
    topic2 = []
    topic3 = []
    topic4 = []
    topic5 = []
    topic6 = []
    irr = []
    
    
    
    for line in lines: 
        
        raw_topic, raw_conf = super_topic_classifier(line)
        topic, conf = raw_topic[0]+1, raw_conf[0][int(raw_topic[0])]
        
        if conf > .3:
            if str(topic) == '1':
                topic1.append([topic, conf, line])

            if str(topic) == '2':
                topic2.append([topic, conf, line])

            if str(topic) == '3':
                topic3.append([topic, conf, line])

            if str(topic) == '4':
                topic4.append([topic, conf, line])

            if str(topic) == '5':
                topic5.append([topic, conf, line])

            if str(topic) == '6':
                topic6.append([topic, conf, line])
        else:
            irr.append(line)
            
    
    topics = [topic1,topic2,topic3,topic4,topic5,topic6]

    counter = 1
    for topic in topics:
        topic_classifier(topic, counter, scores)
        counter += 1
        
    return scores