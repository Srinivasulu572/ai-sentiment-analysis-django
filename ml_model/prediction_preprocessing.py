def clean_text(text):
    text=text.lower()
    text=text.replace("!","")
    text=text.replace(".","")
    text=text.replace(",","")
    text=text.strip()
    
    return text