from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llms = OpenAI(model='gpt-3.5-turbo-instruct')

result = llms.invoke("what is the capital of india")

print(result)