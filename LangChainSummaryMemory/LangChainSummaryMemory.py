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
from callMemBuffer import callMemoryBuffer
import PySimpleGUI as sg

import warnings
warnings.filterwarnings("ignore")

sg, window, userInput = createGUI()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Default':
        window['-USRI-'].update(userInput)  
    if event == 'Submit':
        userInput = values['-USRI-']
       
        responseVal75 = callMemoryBuffer(userInput, 75)
        window['-T75-'].update(responseVal75)  
        
        responseVal500 = callMemoryBuffer(userInput,500)
        window['-T500-'].update(responseVal500)

window.close()
