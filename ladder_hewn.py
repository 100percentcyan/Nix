from dataclasses import dataclass
from d_tool import d_management_display
from Stilix_data_change import empty_list
@dataclass
class ladder_:
          ladder_design_storage: list[str]
          new_design: list[str]
          def set_amount(self,amount: int,list_: list):
                    list_.append(amount)
          
LADDER_ = ladder_(["-"],[])

class ladder_hewn_:
                    
          def design_ladder(self,amount: int):
                    while amount > 0:
                              print(LADDER_.ladder_design_storage[0])
                              amount -= 1

          def ladder_amount(self,amount_of_ladder: list[int]):
                    d_management_display.store_(True,amount_of_ladder[0])

LADDER_HEWN_ = ladder_hewn_()

