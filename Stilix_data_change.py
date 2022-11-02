from dataclasses import dataclass
from Stilix import STILIX_LIST
@dataclass
class empty_space:
          list_: list
          def check_reset(self,list_to_check_reset: list):
                    dict_check = {
                              0:True
                    }
                    print(dict_check.get(len(list_to_check_reset)))
                    
empty_list=empty_space([])

class change_data:
          def normal_save(self,thing_to_save: list,save_on: empty_list.list_):
                    save_on.append(thing_to_save)
                    
          def tuple_save(self,thing_too_tup: list,save_tup_on_thing: empty_list.list_):
                    thing_too_tup=tuple(thing_too_tup)
                    save_tup_on_thing.append(thing_too_tup)
                    thing_too_tup=list(thing_too_tup)
                    
          def set_save(self,thing_to_list: list,save_list_on: empty_list.list_):
                    thing_to_list=set(thing_to_list)
                    save_list_on.append(thing_to_list)
                    thing_to_list=list(thing_to_list)

data_change=change_data()

class change_add:
          def add_and_tuple(self,thing_to_tuple: list,things_to_add: list):
                    STILIX_LIST.add_styles(thing_to_tuple,things_to_add)
                    data_change.tuple_save(thing_to_tuple,empty_list.list_)
                    
          def add_and_set(self,thing_to_set: list,things_to_add_set: list):
                    STILIX_LIST.add_styles(thing_to_set,things_to_add_set)
                    data_change.set_save(thing_to_set,empty_list.list_)

add_change=change_add()

