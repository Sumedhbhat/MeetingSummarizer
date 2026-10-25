from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, BartTokenizerFast, EncoderDecoderModel
import torch
from nltk import tokenize
import os
import openai

# Set the OPENAI_API_KEY environment variable before running the app

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Function to split the paragraph into sentences


def split_sentences(text):
    return tokenize.sent_tokenize(text)

# Function to merge the two texts extracted


def merge_text(text_1, text_2):
    print("In merger data")
    index=0
    res = ''
    while index < len(text_1) or index <len(text_2):
        if index<len(text_1):
            res+=text_1[index]
        if index<len(text_2):
            res+=text_2[index]
        index+=1
    return res

# Function to generate the summary of the text


def generate_summary_pipeline(text, model_name="knkarthick/MEETING_SUMMARY"):
    # transformers 5 removed the "summarization" pipeline, so call the model directly
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    output_ids = model.generate(**inputs, max_length=500, min_length=200, do_sample=False)
    # print(tokenizer.decode(output_ids[0], skip_special_tokens=True))

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def generate_summary_generative(text):
    summary = ""
    prompt = f"Summarize this : {text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2000,
    )
    summary = response["choices"][0]["text"]
    return summary


def generate_summary_gpt(text):
    print("have entered gpt")
    summary = ""
    prompt = f"Summarize this : {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    summary = response["choices"][0]["message"]["content"]
    return summary


def generate_title(text):
    title = ""
    prompt = f"Generate a title for this text : {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    title = response["choices"][0]["message"]["content"]
    return title


