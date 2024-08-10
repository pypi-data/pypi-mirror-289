from textblob import TextBlob
from transformers import AutoTokenizer
import requests
import json


def xx_response_xx(text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = "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"

    YOUR_SITE_URL = "https://your-site-url.com"
    YOUR_APP_NAME = "YourAppName"

    payload = {
        "model": "openai/gpt-4o-mini-2024-07-18",  # Optional
        "messages": [
            {"role": "user", "content": f"Paraphrase this Urdu sentence in simple English: {text}"}
        ],
        "top_p": 0.99,
        "temperature": 0.9,
        "frequency_penalty": 1.53,
        "presence_penalty": 1.7,
        "repetition_penalty": 1,
        "top_k": 50,
    }

    response = requests.post(
        url=url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": f"{YOUR_SITE_URL}",  # Optional
            "X-Title": f"{YOUR_APP_NAME}",  # Optional
        },
        data=json.dumps(payload)
    )

    content_str = ""

    if response.status_code == 200:
        response_json = response.json()
        content = response_json['choices'][0]['message']['content']

        try:
            parsed_content = json.loads(content)
            content_str += json.dumps(parsed_content, indent=4)
        except json.JSONDecodeError:
            content_str += content

        return content_str
    else:
        return "Max_tokens limit exceeded"


def tokenized_inputs(text, secondary_tokenizer):
    try:
        urdu_text = TextBlob(xx_response_xx(text)).translate(from_lang='en', to='ur')
        inputs = secondary_tokenizer.encode(str(urdu_text), return_tensors="pt")
        return [inputs, secondary_tokenizer]

    except Exception as e:
        print("Error:", e)
        return None


def process_input_file(input_file_path, output_file_path, secondary_tokenizer_):
    secondary_tokenizer = None
    if secondary_tokenizer is None:
        secondary_tokenizer = AutoTokenizer.from_pretrained(secondary_tokenizer_)
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w',
                                                                      encoding='utf-8') as outfile:
        for line in infile:
            text = line.strip()
            if text:
                inputs = tokenized_inputs(text, secondary_tokenizer)
                if inputs is not None:
                    # outfile.write(f"Original: {text}\n")
                    outfile.write(str(inputs.tolist()))
                else:
                    outfile.write(f"Original: {text}\n")
                    outfile.write(f"Error processing this input.\n\n")


print(process_input_file("inputdata", "outputdata", 'bigscience/mt0-base'))
