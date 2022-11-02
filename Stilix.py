from dataclasses import dataclass


          
class stilix_list:
          def add_styles(self,reciever_list: list,sender_list: list):
                    for item in sender_list:
                              reciever_list.append(item)
                              
          def remove_styles(self,remove_list: list,items_to_remove: list):
                    for item in items_to_remove:
                              if item in remove_list:
                                        remove_list.remove(item) 
          
          def reveal_item_position(self,items_to_reveal: list,list_containing_item: list,list_name: str):
                    for item in items_to_reveal:
                              print(f"position (item:{item}) (list:{list_name}):{list_containing_item.index(item)}")
                              
          def display_all(self,list_to_display_all: list):
                    for item in list_to_display_all:
                              print(item)
          
          def display_all_horizontal(self,list_to_display_all: list):
                    for item in list_to_display_all:
                              print(item,end="")

class stilix_list_count:
          def list_length(self,list_: list):
                    return len(list_)
          def list_count(self,list_: list,desired_count: str):
                    return list_.count(list_)
          
STILIX_LIST = stilix_list()    

STILIX_LIST_COUNT = stilix_list_count()

@dataclass
class stilix:
          style: str = " * "
          def split_(self,storage: list,storage_to: list):
                    STILIX_LIST.add_styles(storage_to,storage)
                    
          def insert_style(self,storage: list):
                    value = 1
                    while value < STILIX_LIST_COUNT.list_length(storage):
                              storage.insert(value,self.style)
                              value += 2
                               
          def change_style(self,desired_style: str):
                    self.style = f" {desired_style} "

STILIX = stilix([])

 