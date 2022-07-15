
from d_tool import d_management_display
import nix_data_change 
class nix:
          def position_item(self,position: int,item: str,display_checker: bool,custom_style: str):
                    
                    _dict_custom_={
                              f"-dont":"*",
                              f"-never":"",
                              f"{custom_style}-agree":custom_style
                    }
                    
                    print(f"{' ' * position} {_dict_custom_.get(custom_style)} {item} {_dict_custom_.get(custom_style)}")
                              
                    d_management_display.store_(display_checker,position)
          
class nix_list:
          def add_styles(self,reciever_list: set,sender_list: set):
                    reciever_list.append("*" * 2)   
                    for item in sender_list:
                              reciever_list.append(item)
                    reciever_list.append("*" * 2)
                              
          def remove_styles(self,remove_list: set,items_to_remove: set):
                    for item in items_to_remove:
                              if item in remove_list:
                                        remove_list.remove(item) 
          
          def reveal_item_position(self,items_to_reveal: set,list_containing_item: set,list_name: str):
                    for item in items_to_reveal:
                              print(f"position (item:{item}) (list:{list_name}):{list_containing_item.index(item)}")
                              
NIX=nix()

NIX_LIST=nix_list()                    
