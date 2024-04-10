#import streamlit as st
import pandas as pd
import os 
import json

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from create_gui import createGUI



def setupChain(cuisine,lcity):

    os.environ['OPENAI_API_KEY'] = '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'
    llm = ChatOpenAI(model="gpt-4")

    #First chain - Input: Cuisine                     Output: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

   #Second chain - Input : city , restaurant name     Output: if this restarant is present in the city
    prompt_template_city = PromptTemplate(
        input_variables = ['lcity','restaurant_name'],
        template = "Check if this [lcity] has restaurant with this name {restaurant_name}. Answer as Yes present or No not present "
    )

    city_rest_present_chain = LLMChain(llm=llm, prompt=prompt_template_city, output_key="restaurant_present")

    #Third chain - Input : restaurant name            Output: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list. "
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    
    #intantiate the chain
    overall_simple_chain = SequentialChain(
        chains=[name_chain, food_items_chain, city_rest_present_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items","restaurant_present"])
    
    responseVal = overall_simple_chain.invoke(cuisine)
    
    return(responseVal)
