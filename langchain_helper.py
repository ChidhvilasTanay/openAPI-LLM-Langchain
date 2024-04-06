from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, create_react_agent, AgentExecutor
from langchain.agents import load_tools
from langchain import hub
prompt = hub.pull("hwchase17/react")


load_dotenv()

prompt_template_name = PromptTemplate(
    input_variables=['animal_type', 'pet_color'],
    template = "I have a pet {animal_type}, it is {pet_color} in color, and I need a cool name for it, suggest me five good ones."
)

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)
    
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='pet_name')

    response = name_chain.invoke({'animal_type':animal_type, 'pet_color':pet_color})

    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = create_react_agent(
        llm, tools, prompt
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({
        "input":"calculate the average age of a dog and multiply it with 2"
    })

    print (result)

if(__name__ == "__main__"):
    langchain_agent()