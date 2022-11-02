from Stilix import STILIX_LIST
from dataclasses import dataclass

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
          def display_layers(self):
                    STILIX_LIST.display_all(self.extra_layer_storage)
          
          def display_layers_horizontal(self):
                    STILIX_LIST.display_all_horizontal(self.extra_layer_storage)
                    
EXTRA_LAYER = extra_layer([])

