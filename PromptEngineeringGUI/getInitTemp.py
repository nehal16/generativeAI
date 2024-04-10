def getInitTemplates():
    
    instruction_template = """For the following text, extract the following information:
    Gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.
    
    Delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.
    
    Price_value: Extract any sentences about the value or price, and output them as a comma separated Python list.
    
    Format the output as JSON with the following keys:
    Gift
    Delivery_days
    Price_value

    text: {text}
    """
        
    customer_review = """This leaf blower is pretty amazing. It has four settings: candle blower, gentle breeze, windy city, and tornado. It arrived in two days, just in time for my wife's anniversary present.
    I think my wife liked it so much she was speechless. So far I've been the only one using it, and I've been using it every other morning to clear the leaves on our lawn. It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features."""
        
    return (instruction_template, customer_review)
