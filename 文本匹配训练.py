from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")



fewshot = [
    {"role": "system", "content": "你作为一名专业的文本匹配分析师，请根据我给的示例对我新发的问题进行文本匹配，只需要给出：是或者不是"},
    {"role": "user", "content": ("新能源汽车销量持续攀升，市场前景看好。电动车市场增长迅速，未来发展可期。")},
    {"role": "assistant", "content": "是"},
    {"role": "user", "content": ("人工智能技术突破，医疗诊断更精准。全球粮食价格上涨，农民收入增加。")},
    {"role": "assistant", "content": "不是"},
]

question = [('股票市场今日大涨，投资者乐观。','持续上涨的市场让投资者感到满意。'),
('油价大幅下跌，能源公司面临挑战。','未来智能城市的建设趋势愈发明显。'),
('利率上升，影响房地产市场。','持续上涨的市场让投资者感到满意。')]


for q in question:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=fewshot+[{"role": "user", "content":f'请根据示例，判断：{q[0]},{q[1]}'}])

    print(response.choices[0].message.content)