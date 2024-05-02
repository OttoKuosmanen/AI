import openai
from key_ring import key
from docx import Document
import time
import json

# Open the .docx file
document = Document('../texts/GPT3.5_answers_censored_nolist.docx')

# Read in the text
text = [paragraph.text for paragraph in document.paragraphs]

# Join all paragraphs into a single string
text_str = ' '.join(text)

# Split the string into chunks based on the "##" character
list_answers = text_str.split('##')

# Now text_chunks is a list of chunks separated by "##"

output_file = '../data/AI/GPT35_shorter.json'
openai.api_key = key


gpt35_answers = []

def GPT(questions):
    for question in questions:
        success = False
        while not success:
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "slightly shorten the text"},
                        {"role": "user", "content": question},
                        {"role": "assistant", "content": "The same text but slightly shorter: "},
                        
                        ]
                )

                chat_response = completion.choices[0].message.content
                gpt35_answers.append(chat_response)
                print(chat_response)
                success = True
            except Exception as e:
                print(f"Error generating answer for question: {question}")
                print(f"Error message: {str(e)}")
                time.sleep(30)
                continue

def save_file(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)


GPT(list_answers)

save_file(gpt35_answers)

