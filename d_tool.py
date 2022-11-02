
from typing import AbstractSet, Any
from abc import ABC , abstractmethod

class d_display:
          def store_(self,should_store_: bool,item_to_store: Any):
                    store_dict = {
                              True:item_to_store
                    }
                    return store_dict.get(should_store_)

class my_class(ABC):
          @abstractmethod
          def save_(self):
                    pass
          
          @abstractmethod
          def process(self):
                    pass
          
          @abstractmethod
          def display(self):
                    pass
          
d_management_display = d_display()
