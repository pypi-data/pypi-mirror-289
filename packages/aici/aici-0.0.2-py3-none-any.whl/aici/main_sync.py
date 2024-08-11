from openai import OpenAI
import os
import argparse

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 環境変数からAPIキーを取得


def query_chatgpt(prompt, system="You are a helpful assistant."):
    response = client.chat.completions.create(model="gpt-4-0613",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Query OpenAI's ChatGPT")
    parser.add_argument('prompt', type=str, help='The prompt to send to ChatGPT')

    args = parser.parse_args()

    prompt = args.prompt
    answer = query_chatgpt(prompt)
    print(answer)

if __name__ == "__main__":
    main()
