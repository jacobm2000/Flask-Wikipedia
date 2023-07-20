
import wikipedia


def getSummary(term,sent):
    
    if(term==""):
        return "No term inputed. Please enter a term."
    elif (sent.isnumeric()==False):
        return "The number of sentances needs to be an even integer. Please try again"
    try:    
        result = wikipedia.summary("'"+term+"'",sentences = sent)
    
    except Exception as e: 
       result=e
    return result


 
