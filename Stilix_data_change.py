from dataclasses import dataclass
from Stilix import STILIX_LIST , STILIX_LIST_COUNT
from array_change import array_change
@dataclass
class empty_space:
          list_: list
          def check_reset(self,list_to_check_reset: list):
                    dict_check = {
                              0:True
                    }
                    print(dict_check.get(STILIX_LIST_COUNT.list_length(list_to_check_reset)))
                    
empty_list=empty_space([])

'''
The empty_list object contains an empty list which can be used on anything.
The check_reset mehod of the empty list object checks if the desired list is empty.

empty_list.list_ = ["a"]

empty_list.check_reset(empty_list.list_)

False

w = []

empty_list.check_reset(w)

True
'''

class change_data:
          def normal_save(self,thing_to_save: list,save_on: list):
                    save_on.append(thing_to_save)
                    
          def tuple_save(self,thing_too_tup: list,save_tup_on_thing: list):
                    thing_too_tup=tuple(thing_too_tup)
                    save_tup_on_thing.append(thing_too_tup)
                    thing_too_tup=list(thing_too_tup)
                    
          def set_save(self,thing_to_list: list,save_list_on: list):
                    thing_to_list=set(thing_to_list)
                    save_list_on.append(thing_to_list)
                    thing_to_list=list(thing_to_list)

data_change=change_data()

'''
The data_change object saves a list as a different data structure like tuples or sets in a list.
The data_change.normal_save method can be used to just save a list in another list without changing it.
The data_change.tuple_save method can be used to save a list as a tuple in another list.
The data_change.set_save method can be used to save a list as a set in another list.

b = []
a = []
data_change.normal_save(a,b)
print(b)

[[]]

data_change.tuple_save(a,b)
print(b)

[()]

data_change.set_save(a,b)
print(b)

[{}]

'''
@dataclass
class array_to_change(array_change):
          def display_tuple(self,array_to_tuple: list):
                    array_to_tuple=tuple(array_to_tuple)
           
          def display_set(self,array_to_set: list):
                    array_to_set=set(array_to_set)
           
          def change_array(self,array,modified_array: any):
                    STILIX_LIST.remove_styles(array,array)
                    STILIX_LIST.add_styles(array,list(modified_array))
class change:
          def change_in_array(self,things: list,things_modified: list,storage: list):
                    for item in things:
                              storage.insert(storage.index(item),things_modified[things.index(item)])
                              STILIX_LIST.remove_styles(storage,[item])
CHANGE = change()
ARRAY_TO_CHANGE = array_to_change()

'''
The ARRAY_TO_CHANGE object can be used to directly change your array.It does not save a changed version of your array like the data_change object.
The display_tuple method can be used to change your array to a tuple.
The display_set method can be used to change your array to a set.
The change_array method can be used to change your array to some other array.
-
Lets say I have some arrays called 'a' , 'b' and 'c'.

a , b , c = ["a"] , ["b"] , ["c"]

-
Now lets say I want to change 'a' to a tuple.

ARRAY_TO_CHANGE.display_tuple(a)
print(a)

output:
("a",)
-
Now lets say I want to change 'b' to a set.

ARRAY_TO_CHANGE.display_set(b)
print(b)

output:
{"b"}
-
Finally lets say I want to change my array 'c' to ["d"]

ARRAY_TO_CHANGE.change_array(c,["d"])
print(c)

output:
["d"]
'''
'''
The CHANGE object changes the stuff in your array with the change_in_array method.
-
Lets say I have an array named 'a'.

a=[4,5]
-
Lets say I want to change these numbers in the array to a product of 6 x number.

CHANGE.change_in_array(a,[a[0] * 6,a[1] * 6],a)
-
Now Lets check my array 'a'.

print(a)

output:
[24,30]
'''
