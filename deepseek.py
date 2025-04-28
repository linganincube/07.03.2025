# Please install OpenAI SDK first: ``

from openai import OpenAI

client = OpenAI(api_key="<sk-feee0c24ebc64e0e81961a190d65ee1a>", base_url="https://api.deepseek.com/v1/summarize")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)