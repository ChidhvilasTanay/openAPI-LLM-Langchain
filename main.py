from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

prompt_template_name = PromptTemplate(
    input_variables=['animal_type', 'pet_color'],
    template = "I have a pet {animal_type}, it is {pet_color} in color, and I need a cool name for it, suggest me five good ones."
)


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)
    
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain.invoke({'animal_type':animal_type, 'pet_color':pet_color})

    return response

if (__name__ == "__main__"):
    print(generate_pet_name("cat", "pink"))
