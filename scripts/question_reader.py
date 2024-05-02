import json
from datetime import date
time_stamp = date.today()

relative_location_name = '../data/sample.json'

def read(relative_location_name):
    with open(relative_location_name, 'r') as f:
        out = json.load(f)
        return out

# reading in data
analysis_data = read(relative_location_name)



def extract_questions(analysis_data):
    out = []
    for dicti in analysis_data:
        out.append(dicti["Question"])
    return out

def extract_answers(analysis_data):
    out = []
    for dicti in analysis_data:
        out.append(dicti["Aswer"])
    return out


    
# Extracting questions and answers
questions = extract_questions(analysis_data)
answers_h = extract_answers(analysis_data)

#Getting the lenght of question and answer
answer_lenght = [i['answer_len'] for i in analysis_data]
question_lenght = [i['question_len'] for i in analysis_data]

# Calculating max token lenght
token = [sum(x) for x in zip(answer_lenght * 2, question_lenght)]
