from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi

example_template = PromptTemplate.from_template("单词：{word},反义词：{antonym}")           # 示例模板

example_data = [                                                # 示例数据
    {"word": "大", "antonym": "小"},
    {"word": "长", "antonym": "短"},
    {"word": "上", "antonym": "下"},
]









fewshot_template = FewShotPromptTemplate(
    example_prompt=example_template,                               # 示例模板
    examples=example_data,                                         # 示例数据 list内嵌字典
    prefix="根据我提供一个单词，并给出它的反义词,以下是我提供的示例。", # 前缀
    suffix="基于我前面的示例告知我：{1word},{2word}的反义词。",               # 后缀
    input_variables=["1word","2word"]                                       # 输入变量

)

prompt = fewshot_template.invoke(input={"1word": "前","2word":"左"}).to_string()


model = Tongyi(model="qwen-max")


print(model.invoke(prompt))
