

from d_tool import d_management_display
class stilix:
          def position_item(self,position: int,item: str,display_checker: bool,custom_style: str,custom: str):
                    
                    _dict_custom_={
                              f"-dont":"*",
                              f"-never":"",
                              f"{custom_style}-agree":custom_style
                    }
                    
                    
                    print(f"{' ' * position} {_dict_custom_.get(custom_style)} {item} {_dict_custom_.get(custom_style)}")
                              
                    d_management_display.store_(display_checker,position)
    

          
class stilix_list:
          def add_styles(self,reciever_list: list,sender_list: list):
                    reciever_list.append("*" * 2)   
                    for item in sender_list:
                              reciever_list.append(item)
                    reciever_list.append("*" * 2)
                              
          def remove_styles(self,remove_list: list,items_to_remove: list):
                    for item in items_to_remove:
                              if item in remove_list:
                                        remove_list.remove(item) 
          
          def reveal_item_position(self,items_to_reveal: list,list_containing_item: list,list_name: str):
                    for item in items_to_reveal:
                              print(f"position (item:{item}) (list:{list_name}):{list_containing_item.index(item)}")

class stilix_list_count:
          def list_length(self,list_length: list):
                    print(len(list_length))
                    
          def count_list(self,list_count: list,clone: str):
                    print(list_count.count(clone))
                    
          def no_style_show(self,list_no_style: list):
                    for i in list_no_style.count("**"):
                              list_no_style.remove("**")
                              
                              if list_no_style.count("**") > 2:
                                        list_no_style.remove(list_no_style[0])
                                        list_no_style.remove(list_no_style[len(list_no_style)])
                     
STILIX=stilix()

STILIX_LIST=stilix_list()    

STILIX_LIST_COUNT = stilix_list_count()

                