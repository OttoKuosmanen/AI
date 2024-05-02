import openai
from key_ring import key
import json


output_file = '../data/AI/gpt_3_nolists.json'
json_file_path = "../data/AI/gpt_3_answers.json"

#read in jsonfile
def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

#Sett the contents to data
data = read_json_file(json_file_path)

gpt_3_answers = []


def GPT(data):
## Call the API key under your account (in a secure way)
        openai.api_key = key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt =  "Rewrite this into paragraph structure: " + data[34],
            max_tokens = 3000
            )
        answer = response.choices[0].text
        gpt_3_answers.append(answer)
        
    


GPT(data)
print(gpt_3_answers)



