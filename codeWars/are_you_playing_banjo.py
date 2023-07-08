import re

def are_you_playing_banjo(name):
    """
    Here i using Exception Handling and Regular Expression to 
    Do this problem
    """
    
    try :
        src = re.search(r"^[Rr]", name)
        return f"{src.string} plays banjo"
    except AttributeError :
        return f"{name} does not play banjo"


