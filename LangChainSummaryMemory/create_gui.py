from tkinter.font import BOLD
import PySimpleGUI as sg

#initialize GUI window
def createGUI():
    
    # create a long string
    userInput = """There is a meeting at 8am with your product team.\
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."""
    
    layout = [
       
        [sg.Image(source='./graphics/MemoryHeader.png')],
        [sg.Image(source='./graphics/AIQuestion.png'),sg.Multiline(size=(60,7),  key='-USRI-',font='Courier 14')],
               
        [sg.Image(source='./graphics/AIResponse75.png'),sg.Multiline(size=(60,7), key='-T75-',font='Courier 14')],       
       
        [sg.Image(source='./graphics/AIResponse500.png'),sg.Multiline(size=(60,13), key='-T500-',font='Courier 14')],
             
        [sg.Image(source='./graphics/AISubmit.png'),sg.Image(source='./graphics/spscerBlue.png'),
        sg.Button('Default',font=("Calibri", 24,BOLD)),sg.Button('Submit',font=("Calibri", 24,BOLD)) ]

        ]
    
    sg.theme("DarkGreen")

    window = sg.Window('Summary Memory buffer', layout)
    return(sg, window,userInput)

