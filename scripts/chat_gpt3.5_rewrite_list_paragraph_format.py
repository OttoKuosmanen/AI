import openai
from key_ring import key
import json
import time
openai.api_key = key

output_file = '../data/AI/gpt_3.5_nolists.json'
json_file_path = "../data/AI/chat_gpt_answers_new.json"

#read in jsonfile
def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

#Sett the contents to data
data = read_json_file(json_file_path)


# Specify the indices you want to include in the new list
indices_to_include = [1, 6, 9,15,21,25,31,34,35,36,38,41,42,47,48]

# List comprehension to create the new list
new_data = [data[index] for index in indices_to_include]



chat_gpt_answers = []

def save_file(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)
        
def GPT(new_data):
    for answer in new_data:
        success = False
        while not success:
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You will transform text into paragraph structure"},
                        {"role": "user", "content": "numbered list format: " + answer},
                        {"role": "assistant", "content": "paragraph structured: "},
                        
                        ]
                )

                chat_response = completion.choices[0].message.content
                chat_gpt_answers.append(chat_response)
                success = True
            except Exception as e:
                print(f"Error generating answer for question: {answer}")
                print(f"Error message: {str(e)}")
                time.sleep(30)
                continue


GPT(new_data)

save_file(chat_gpt_answers)




