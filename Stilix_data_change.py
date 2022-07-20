from dataclasses import dataclass
from Stilix import STILIX_LIST
@dataclass
class empty_space:
          list_: list
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

class change_add:
          def add_and_tuple(self,thing_to_tuple: list,things_to_add: list):
                    STILIX_LIST.add_styles(thing_to_tuple,things_to_add)
                    thing_to_tuple=tuple()
                    
          def add_and_set(self,thing_to_set: list,things_to_add_set: list):
                    STILIX_LIST.add_styles(thing_to_set,things_to_add_set)
                    thing_to_set=set()
                    
          def data_and_add(self,things_to_add: list,data_type: str,adder):
                    _dict_data_type_={"tuple":tuple(),"set":set(),"list":list()}
                    adder=list()
                    STILIX_LIST.add_styles(adder,things_to_add)
                    adder=_dict_data_type_.get(data_type)


data_change=change_data()

add_change=change_add()