#Create GUI window
import PySimpleGUI as sg

def createGUI():
    layout = [
            #Create header, and render side images with text boxes and submit buttion
            [sg.Image(source='./graphics/RAGHeader2.png')],
            [sg.Image(source='./graphics/AIQuestion.png'),sg.Multiline(size=(60,2), key='-QUR-',font='Courier 14')],
            [sg.Image(source='./graphics/AISubmit.png'),sg.Image(source='./graphics/spscerBlue.png'),sg.Button('Submit', image_filename = './graphics/RAGButton1.PNG',image_size=(200,50 ),font=("Calibri 20 bold")) ],    
            [sg.Image(source='./graphics/AIResponse.png'),sg.Multiline(size=(60,18), key='-AIR-',font='Courier 14')]
    ]
    sg.theme('DarkPurple2')
    window = sg.Window('Advanced RAG techniques', layout)
    return(sg, window)

