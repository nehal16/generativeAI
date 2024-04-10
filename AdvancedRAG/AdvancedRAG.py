#import all needed libraries
import warnings
warnings.filterwarnings('ignore')
from create_index import create_index_with_doc
from run_query import run_the_query
from create_GUIFile import createGUI
import PySimpleGUI as sg

#call GUI creating function and Render window
sg, window = createGUI()

#Ingestion - Call the Index creating routine
retVal = create_index_with_doc()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        new_varnew_var = lquery = values['-QUR-']
        
        #Retrival and Synthesis: user clicked submit. Now run the call to LLM 
        retVal = run_the_query(lquery)
        window['-AIR-'].update(retVal)
        
#we are dpme! let us close window
window.close()