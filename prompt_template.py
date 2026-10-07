from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)

template2= PromptTemplate(
    template= 'Greet this person in 5 languages. The name of the person is {name}',
    input_variables= ['name']
)

prompt= template2.invoke({'name': 'John'})

result= model.invoke(prompt)

print(result.content)