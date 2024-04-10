from tkinter.font import BOLD
import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from create_gui import createGUI


def callMemoryBuffer(userInput,noOfTokens):
    llm_model = "gpt-3.5-turbo"
    llm = ChatOpenAI(temperature=0.0, model=llm_model)
    
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=int(noOfTokens))
    memory.save_context({"input": "Hello"}, {"output": "What's up"})
    memory.save_context({"input": "Not much, just hanging"},
                        {"output": "Cool"})
    memory.save_context({"input": "What is on the schedule today?"}, 
                        {"output": f"{userInput}"})
    conversation = ConversationChain(
        llm=llm, 
        memory = memory
    )
    #ask the question and publish the answer
    
    conversation.predict(input="What would be a good demo to show?")
    responseVal = memory.load_memory_variables({})
    return(responseVal)
