
import wikipedia


def getSummary(term):
    try:    
        result = wikipedia.summary("'"+term+"'",sentences = 3)
    
    except Exception as e: 
       result=e
    return result


 
