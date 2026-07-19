import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的小助手,不以话多为特点,但尽可能地回答问题"},
        {"role": "user", "content": "你好啊 你能做什么"},
    ],
    stream=True,
    reasoning_effort="low",
    extra_body={"thinking": {"type": "disabled"}}
)

for chunk in response:
    print(chunk.choices[0].delta.content,end=" ",flush=True)
