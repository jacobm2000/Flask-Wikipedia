
import wikipedia


def getSummary(term,sent):
    if (sent.isnumeric()==False):
        return "The number of sentances needs to be an even integer. Please try again"
    try:    
        result = wikipedia.summary("'"+term+"'",sentences = sent)
    
    except Exception as e: 
       result=e
    return result


 
