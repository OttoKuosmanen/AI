import openai
from key_ring import key
from question_reader import questions
import json
import time
output_file = '../data/AI/chat_gpt_answers_new.json'
openai.api_key = key


chat_gpt_answers = []

def save_file(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)
        
def GPT(questions):
    for question in questions:
        success = False
        while not success:
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are answering an advice question"},
                        {"role": "user", "content": "Question: " + question},
                        {"role": "assistant", "content": "Answer: "},
                        
                        ]
                )

                chat_response = completion.choices[0].message.content
                chat_gpt_answers.append(chat_response)
                success = True
            except Exception as e:
                print(f"Error generating answer for question: {question}")
                print(f"Error message: {str(e)}")
                time.sleep(30)
                continue

GPT(questions)

save_file(chat_gpt_answers)




# The limiting of responses is not working as well as i would like to. 
# Seems like either the responses are cut out mid sentences or the lenght is not presice.

# Should i prompt with question: txt. Answer:
