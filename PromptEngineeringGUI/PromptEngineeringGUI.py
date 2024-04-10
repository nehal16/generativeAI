#Prompt for something and get reply
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import PySimpleGUI as sg
from create_gui import createGUI
from getInitTemp import getInitTemplates

#get LLM endpoint
new_varnew_var = llm_model = "gpt-3.5-turbo"
chat = ChatOpenAI(temperature=0.0, model=llm_model)

#call GUI creating function and Render window
sg, window = createGUI()

#initialize the template string
instruction_template, customer_review = getInitTemplates()
prompt_template = ChatPromptTemplate.from_template(instruction_template)
messages = prompt_template.format_messages(text=customer_review)

# Call the LLM to translate to the style of the customer message
response = chat(messages)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Default':
        window['-CUST-'].update(customer_review)
        window['-INS-'].update(instruction_template)
        
    if event == 'Submit':
        prompt_template = ChatPromptTemplate.from_template(str(values['-INS-']))
        messages = prompt_template.format_messages(text=str(values['-CUST-']))
        
        response = chat(messages)
        
        window['-RESP-'].update(response.content)
window.close()



