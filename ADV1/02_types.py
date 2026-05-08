# type definations
age : int = 5
name : str = "Fenil"
cgpa : float = 9.8


# its just type hints not rules
def sum(a:int, b:int) -> int:
    return a+b

print(sum(1,3))
# print(sum(1,"awc")) # error




#advance type hints
from typing import List, Dict, Union, Tuple
nums : List[int] = [1,2,3,4]
persons : Tuple[str,int] = ("rahul",20)
subjects : Tuple[str] = ("phy", "chem", "math")
scores : Dict[str,int] = {"phy" : 90, "chem" : 80, "math" : 70}
identifier : Union[str,int] = "ID123"
identifier = 123 # also valid