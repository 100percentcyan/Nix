from abc import ABC , abstractmethod

class array_change(ABC):
          @abstractmethod
          def display_tuple(self):
                    pass
          
          @abstractmethod
          def display_set(self):
                    pass
          
          @abstractmethod
          def change_array(self):
                    pass

'''
The array change abstract class can be used to create classes with methods that can change an array.
You just have to inheret this class when you want to create a class with methods like this.
-
class my_way_of_change(array_change):
          def display_tuple():
                    some of your code here
          def display_set():
                    some of your code here
          def change_array():
                    some of your code here

'''