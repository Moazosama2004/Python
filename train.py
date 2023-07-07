"""
_summary_
"""

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello (some_peoples) -> list:
    """_summary_
    Args:
        some_peoples (_type_): _description_

    Returns:
        list: _description_
    """
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)
