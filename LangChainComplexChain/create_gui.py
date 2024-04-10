#initialize GUI window
def createGUI():
    import PySimpleGUI as sg
    
    questionForLLM = "Following is input fed to three chains: \n     1. I want to open a restaurant with my choice of cuisine. Suggest a fancy name for this. \n \
    2. Check if the city of my choice has restaurant with this same name. \n \
    3. Suggest some menu items for this cuisine. Return it as a comma separated list."
    
    layout = [
            [sg.Image('./graphics/restaurantheader.PNG')],
            [sg.Image(source='./graphics/cuisine.png'),sg.Combo(values=('Chinese', 'Italian', 'Japanese', 'French', 'Mediterranean', 'American', 'Indian'), default_value='Indian', readonly=False, k='-CUSIN-',font='Courier 14')],
            [sg.Image(source='./graphics/city.png'), sg.Combo(values=('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'), default_value='Dallas', readonly=False, k='-CITY-',font='Courier 14')],

            [sg.Image(source='./graphics/AISubmit.png'),sg.Text(questionForLLM,font='Courier 14')],

            #Display the output from LLM
            #[sg.Image(source='./graphics/selectedCus.png'), sg.Multiline(size=(60,1), key='-MCUIS-',font='Courier 14')],
            [sg.Image(source='./graphics/namesuggest.png'), sg.Multiline(size=(60,3), key='-MSUG-',font='Courier 14')],
            [sg.Image(source='./graphics/restpresent.png'), sg.Multiline(size=(60,3), key='-MRSTP-',font='Courier 14')],
            [sg.Image(source='./graphics/menuitems.png'), sg.Multiline(size=(60,5), key='-MUN-',font='Courier 14')],
           
            #Submit button
            [sg.Image(source='./graphics/AISubmit.png'),sg.Image(source='./graphics/spscerBlue.png'),sg.Button('Submit',image_filename = './graphics/prmButton1.PNG',image_size=(200,50 ),font=("Calibri 20 bold")) ] 
        ]

    sg.theme('LightBrown7')
    window = sg.Window('Complex chain demo', layout)
    
    return(sg, window)
