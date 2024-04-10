import PySimpleGUI as sg
from create_gui import createGUI
from callChain import setupChain
import json
import pandas as pd

sg, window = createGUI()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        new_varnew_var = cuisine = values['-CUSIN-']
        new_varnew_var = lcity = values['-CITY-']
        
        #Set up chain and invoke with with user input of Cuisine and City
        responseVal = setupChain(cuisine,lcity)
        
        #convert unformatted string output to Indivdual fields for display
        modResponse = json.dumps(responseVal)
        myjsonvar =  json.loads(modResponse)
        
        #Display output
        #window['-MCUIS-'].update(myjsonvar['cuisine'])
        window['-MSUG-'].update(myjsonvar['restaurant_name'])
        window['-MRSTP-'].update(myjsonvar['restaurant_present'])
        window['-MUN-'].update(myjsonvar['menu_items'])

window.close()
        
    
    




