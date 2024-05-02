
import openai
from key_ring import key
from question_reader import questions
import time
import json

output_file = '../data/AI/gpt_3_answers.json'
gpt_3_answers = []

def GPT(questions):
    for question in questions:
        success = False
        while not success:
            try:
                prompt = "Question: " + question + "\nAnswer: "
                openai.api_key = key
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=1400
                )
                answer = response.choices[0].text
                gpt_3_answers.append(answer)
                success = True
            except Exception as e:
                print(f"Error generating answer for question: {question}")
                print(f"Error message: {str(e)}")
                time.sleep(30)
                continue

    
def save(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)

GPT(questions)
save(gpt_3_answers)

#Sett the right settings
# Implement loop
# Generate data
# ;)