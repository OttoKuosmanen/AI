import openai
from key_ring import key
from docx import Document
import time
import json

openai.api_key = key
output_file = '../data/AI/gpt_3_short.json'

# Open the .docx file
document = Document('../texts/GPT3_censored_nolist.docx')

# Read in the text
text = [paragraph.text for paragraph in document.paragraphs]

# Join all paragraphs into a single string
text_str = ' '.join(text)

# Split the string into chunks based on the "##" character
list_answers = text_str.split('##')

# Now text_chunks is a list of chunks separated by "##"




#read in jsonfile
def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


gpt_3_answers = []

def GPT(list_answers):
    for answer in list_answers:
        success = False
        while not success:
            try:
                prompt = "Slightly shorten the following text: " + answer + "\n The slightly shorter text: "
                openai.api_key = key
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=2400
                )
                answerr = response.choices[0].text
                gpt_3_answers.append(answerr)
                print(prompt)
                print(answerr)
                success = True
            except Exception as e:
                print(f"Error generating answer: {answer}")
                print(f"Error message: {str(e)}")
                time.sleep(30)
                continue

    
def save(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)

GPT(list_answers)
save(gpt_3_answers)



