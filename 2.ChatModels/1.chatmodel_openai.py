from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4' , temperature = 0)

#result = model.invoke("what is the capital of india?")
result = model.invoke("suggest me name of 5 males of india?")

print(result)