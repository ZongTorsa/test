from openai import OpenAI
import os


client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

fewshot = [
    {"role": "system", "content": "你是一名专业的数据分析师，请根据我给的实例提示，对我后续的数据进行：期数，中奖号码，几等奖。以以上三类进行分类"},
    {"role": "user", "content": "2021年第313期号码为01 03 05 06 01 特码 12,一等奖中奖为10注"},
    {"role": "assistant", "content": '{"期数":"2021313","中奖号码":[01,03,05,06,01,12],"一等奖":"10注"}'},
    {"role": "user", "content": "2025314期号码为09 03 15 26 11 特码 22,二等奖中奖为3注"},
    {"role": "assistant", "content": '{"期数":"2025314","中奖号码":[09,03,15,26,11,22],"二等奖":"3注"}'},
]
print(fewshot)
question = [
    "2025第100期的中奖号码是22 21 06 03 11特码 80,一等奖中奖为2注",       
    "2025第251期的中奖号码是24 12 06 14 04特码 72,二等奖中奖为5注",
    "2025第117期的中奖号码是66 25 13 82 89特码 36,二等奖中奖为7注",
    "2025第802期的中奖号码是15 28 19 17 31特码 54,五等奖中奖为1注",

]



for q in question:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages= fewshot + [{"role": "user", "content": f"按照示例，回答这段文本的分类类别：{q}"}],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print(response.choices[0].message.content)