import PySimpleGUI as sg

def createGUI():
    layout = [ 
            [sg.Image(source='./graphics/PrmHeader2.png')],
            [sg.Image(source='./graphics/custReviewW - Gift.png'),sg.Multiline(size=(60,8), key='-CUST-',font='Courier 14')],
            [sg.Image(source='./graphics/instructionTemplateW.png'),  sg.Multiline(size=(60,14), key='-INS-',font='Courier 14')],
            [sg.Image(source='./graphics/AIResponseW.png'),sg.Multiline(size=(60,6), key='-RESP-',font='Courier 14')],
       
          
            [sg.Image(source='./graphics/AISubmit1.png'),sg.Image(source='./graphics/spscerBlue.png'), 
             sg.Button('Default', image_filename = './graphics/prmButton1.PNG',image_size=(200,50 ),font=("Calibri 20 bold") ),
             sg.Button('Submit', image_filename = './graphics/prmButton1.PNG',image_size=(200,50 ),font=("Calibri 20 bold")) ]
        ]
    sg.theme('Tan')
    

    
    window = sg.Window('Complex prompt', layout)
    return(sg, window)
