
from typing import AbstractSet, Any
from abc import ABC , abstractmethod
from Stilix import STILIX ,STILIX_LIST_COUNT
from dataclasses import dataclass
class d_display:
          def store_(self,should_store_: bool,item_to_store: Any):
                    store_dict = {
                              True:item_to_store
                    }
                    return store_dict.get(should_store_)

class my_class(ABC):
          @abstractmethod
          def save(self):
                    pass
          
          @abstractmethod
          def process(self):
                    pass
          
          @abstractmethod
          def display(self):
                    pass
          
d_management_display = d_display()

'''
The d_management_display object displays an item depending on the boolean entered.
The my_class abstract class can be used to make custom classes based on the methods save_ , process and display.
my_class indicates that it is your class that you coded.

def do_(my_class):
          def save(self,something):
                    #some code
                    
          def process(self,something):
                    #some code
          
          def display(self,something):
                    #some code

value = 1
t = False

if value == 1:
          t = True
          d_management_display.store_(t,value)

'''

@dataclass
class d_mapper:
          dict_style: str
          def view_dict(self,dict_to_view: dict):
                    for k in dict_to_view:
                              print(f"{k}{self.dict_style}{dict_to_view.get(k)}")
          def independent_change(self):
                    self.dict_style=STILIX.style
          def view_multiple_dicts(self,things_to_view: list[dict],styles: list[str]):
                    VALUE = 0
                    STYLES_VALUE = STILIX_LIST_COUNT.list_lengths([styles]) - 1
                    
                    while VALUE < STILIX_LIST_COUNT.list_lengths([things_to_view]):
                              try:
                                        STILIX.change_style(styles[VALUE])
                              except:
                                        STILIX.change_style(styles[STYLES_VALUE])
                              self.independent_change()
                              self.view_dict(things_to_view[VALUE])
                              
                              VALUE += 1
                    
D_MAPPER = d_mapper("-" * 3)
'''
The D_MAPPER object can be used to visualize your dictionary.
The view_dict method is the method in this object that is used to visualize the dictionary.
Theres a default style which is used to visualize your dictionary.
The independent_change method is used to change the default style in this object to the default style which is implemented in the STILIX object from Stilix.py.
Independent_change does this so you can make use of the change_style method from the STILIX object.
The view_multiple_dicts method can be used to visualize multiple dictionaries.
-
Lets say that I have dictionaries 'a' and 'b'.
a={"data 1":1,"data 2":2}
b={"data 3":3,"data 4":4}

-
Now lets say I want to visualize 'a'.

from d_tool import D_MAPPER
D_MAPPER.view_dict(a)

output:
data 1---1
data 2---2

-
Now lets say I want to visualize 'b' but with a different style.

from Stilix import STILIX
STILIX.change_style("*" * 3)
D_MAPPER.independent_change()
D_MAPPER.view_dict(b)
note:STILIX.change_style() should always be above D_MAPPER.independent_change().

output:
data 3***3
data 4***4

note:If you have no idea how STILIX works , you should go and read the documentation of STILIX from Stilix.py.
-
Now lets say I want to visualize 'a' and 'b' , both in different styles.

D_MAPPER.view_multiple_dicts([a,b],[".",":"])

output:
data 1 . 1
data 2 . 2
data 3 : 3
data 4 : 4
-
Now lets say I want to visualize 'a' and 'b' all in same style.

D_MAPPER.view_multiple_dicts([a,b],[":"])

output:
data 1 : 1
data 2 : 2
data 3 : 3
data 4 : 4

'''

