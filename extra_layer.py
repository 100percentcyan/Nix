from Stilix import STILIX_LIST
from dataclasses import dataclass
from Stilix_data_change import data_change
from array_change import array_change
import cProfile
@dataclass
class extra_layer:
          extra_layer_storage: list[list]
          def add_layers(self,layers_amount: int):
                    while layers_amount > 0:
                              STILIX_LIST.add_styles(self.extra_layer_storage,[[]])
                              layers_amount -= 1
          
          def remove_layers(self,layers_to_remove_amount: int):
                    while layers_to_remove_amount > 0:
                              STILIX_LIST.remove_styles(self.extra_layer_storage,[[]])
                              layers_to_remove_amount -= 1
                              
          def display_layers(self):
                    STILIX_LIST.display_all(self.extra_layer_storage)
          
          def display_layers_horizontal(self):
                    STILIX_LIST.display_all_horizontal(self.extra_layer_storage)
                    
EXTRA_LAYER = extra_layer([])

def function():
          EXTRA_LAYER.add_layers(2)

cProfile.run("EXTRA_LAYER.add_layers(2)",sort="tottime")
'''
The EXTRA_LAYER object can be used to make multiple empty lists.Each empty list can be assigned to manage one task.The add_layers method can be used to add a desired amount of empty lists to EXTRA_LAYER.extra_layer_storage.
The remove layers method can be used to remove a desired amount of empty lists from EXTRA_LAYER.extra_layer_storage.The display_layers method can be used to display the empty lists vertically.The display_layers_horizontal
method can be used to display the empty lists horizontally.

EXTRA_LAYER.add_layers(3)

print(EXTRA_LAYER.extra_layer_storage)

[[],[],[]]

EXTRA_LAYER.remove_layers(1)

print(EXTRA_LAYER.extra_layer_storage)

[[],[]]

EXTRA_LAYER.display_layers()

[]
[]

EXTRA_LAYER.display_layers_horizontal()

[][]

'''

class extra_layer_change(array_change):
          def display_tuple(self,array_position_tuple: int):
                    return tuple(EXTRA_LAYER.extra_layer_storage(array_position_tuple))
          
          def display_set(self,array_position_set: int):
                    return set(EXTRA_LAYER.extra_layer_storage[array_position_set])
          
          def change_array(self,array_position: int,wanted_array: any):
                    EXTRA_LAYER.extra_layer_storage[array_position] = wanted_array          

EXTRA_LAYER_CHANGE = extra_layer_change()

'''
The EXTRA_LAYER_CHANGE object can be used to change an array in the EXTRA_LAYER.extra_layer_storage array to something else.
Note that your array should belong in the EXTRA_LAYER.extra_layer_storage array.
The display_tuple method returns a tuple version of the desired array.
The display_set method return a set version of the desired array.
The change_array method changes the desired array to anything you desire.

-
Lets say I have two arrays in EXTRA_LAYER.extra_layer_storage.
EXTRA_LAYER.add_layers(2)
note:I recommend you first read the documentation on how the EXTRA_LAYER object works.
-
Lets say you want to return a tuple version of the second array.

print(EXTRA_LAYER_CHANGE.display_tuple(1))
note:The index of the second array is 1.

output:
()

-
Now lets say you want to return a set version of the first array.

print(EXTRA_LAYER_CHANGE.display_set(0))
note:The index of the first array is 0.

output:
{}

-
So now lets say I want to change the first array to a set.

EXTRA_LAYER_CHANGE.change_array(0,EXTRA_LAYER_CHANGE.display_set(0))
print(EXTRA_LAYER.extra_layer_storage[0])

output:
{}

'''