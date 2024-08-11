import os
import argparse
import openai

# 環境変数からAPIキーを取得
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def query_chatgpt(prompt, system="You are a helpful assistant."):
    # Streaming response from OpenAI's API
    response = client.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        stream=True  # Enable streaming mode
    )

    # Collecting the streamed response
    collected_response = ""
    for chunk in response:
        # Each chunk has a structure with a 'choices' list containing the streamed content
        chunk_message = chunk['choices'][0]['delta'].get('content', '')
        print(chunk_message, end='', flush=True)  # Print incrementally
        collected_response += chunk_message

    return collected_response

def main():
    parser = argparse.ArgumentParser(description="Query OpenAI's ChatGPT")
    parser.add_argument('prompt', type=str, help='The prompt to send to ChatGPT')

    args = parser.parse_args()

    prompt = args.prompt
    answer = query_chatgpt(prompt)
    # If you want to print the final full response after streaming
    # print("\nFinal answer:", answer)

if __name__ == "__main__":
    main()
