from dataclasses import dataclass
from Stilix import STILIX_LIST_COUNT
from abc import ABC , abstractmethod
from Stilix_data_change import CHANGE
class simple_reader:
          def read_files(self,files: list[str]):
                    value = 0
                    while value < STILIX_LIST_COUNT.list_lengths([files]):
                              with open (files[value],"r") as file_:
                                        print(file_.read())
                              value += 1

SIMPLE_READER = simple_reader()

'''
The SIMPLE_READER object can be used to read from multiple files.For example if I have two text files called a and b , and if a contains 'a' and b contains 'b' , I can read 'a' and 'b' from a and b with the SIMPLE_READER object.
SIMPLE_READER.read_files(["a.txt","b.txt"])

a
b
'''

@dataclass
class array_text:
          item: any = None
          horizontal_or_vertical: str = None
          def text_data(self,data: any,text_file: str):
                    with open (text_file,"w") as file:
                              file.write(str(data))      
                                        
          def text_data_display(self,data: any,text_file: str,horizontal_or_vertical: str):
                    with open (text_file,"w") as file:
                              for stuff in data:
                                        if horizontal_or_vertical == "horizontal":
                                                  file.write(str(stuff))
                                        if horizontal_or_vertical == "vertical":
                                                  file.write(f"{stuff}\n") 

          def multi_text(self,data: any,text_file: str,modes: list):
                    for item in modes:
                              with open (text_file,item) as file:
                                        if item == "r":
                                                  print(file.read())
                                        if item == "w":
                                                  if self.item is not None and self.item == "" and self.horizontal_or_vertical == "horizontal" or self.horizontal_or_vertical == "vertical":
                                                            self.text_data_display(data,text_file,self.horizontal_or_vertical)
                                                  if self.item is None and self.item != "":
                                                            self.text_data(data,text_file)
ARRAY_TEXT = array_text()
'''
The ARRAY_TEXT object can be used to text arrays to files and to read arrays from files.The text_array method can be used to text an array to a file.The text_array_display can be used to text all of the stuff in the
array to the file vertically or horizontally.The multi_text method can be used to text and read the array or, it can be used to text and read the arrays stuff horizontally or vertically.

i=["hey","hello"]
-
ARRAY_TEXT.text_array(i,"greetings.txt")

greetings.txt:
["hey","hello"]

-

ARRAY_TEXT.text_array_display(i,"greetings.txt","vertical")

greetings.txt:
hey
hello

-

ARRAY_TEXT.multi_text(i,"greetings.txt",["w","r"])

greetings.txt:
["hey","hello"]

output:
["hey","hello"]

-
ARRAY_TEXT.item , ARRAY_TEXT.horizontal_or_vertical = "" , "vertical"
ARRAY_TEXT.multi_text(i,"greetings.txt",["w","r"])

greetings.txt:
hey
hello

output:
hey
hello

-
'''

class multi_text:
          def text_datas(self,datas: list[any],file: str,modes: list[str]):
                    ARRAY_TEXT.item ,ARRAY_TEXT.horizontal_or_vertical = "" , "vertical"
                    ARRAY_TEXT.multi_text(datas,file,modes)
          
          def text_multiple_files(self,datas: list[any],files: list[str],modes: list[str]):
                    value = 0
                    while value < STILIX_LIST_COUNT.list_lengths([datas]):
                              for file in files:
                                        ARRAY_TEXT.multi_text(datas[value],file,modes)
                                        value += 1
                              else:
                                        break

 

MULTI_TEXT = multi_text()
'''
Data structures this module can process with:
1.Tuple
2.List
3.Set
note:Not sure if this module can process with data structures like linked lists , trees , etc.

'''
'''
The MULTI_TEXT object is an advanced version of the ARRAY_TEXT object.It is more complex and advanced than the ARRAY_TEXT object.It can text and read multiple data structures.It can even text data structures to multiple files and
even read multiple arrays from multiple files.
-
a , b = ["a"] , ["b"]
-

MULTI_TEXT.text_arrays([a,b],"a and b.txt",["w","r"])

a and b.txt:
["a"]
["b"]

output:
["a"]
["b"]

-

MULTI_TEXT.text_multiple_files([a,b],["a.txt","b.txt"],["w","r"])

a.txt:
["a"]

b.txt:
["b"]

output:
["a"]
["b"]

-
Lets say I have many items and I want to write and read the items of the arrays to and from multiple files.
a , b = ["a","another a"] , ["b","another b"]


ARRAY_TEXT.item , ARRAY_TEXT.horizontal_or_vertical = "" , "vertical"
MULTI_TEXT.text_multiple_files([a,b],["a.txt","b.txt"],["w","r"])

a.txt:
a
another a

b.txt:
b
another b

output:
a
another a
b
another b
'''
class write_read(ABC):
          @abstractmethod
          def write(self):
                    pass
          
          @abstractmethod
          def read(self):
                    pass
'''
With the write_read abstract class you can make your own way of reading and writing files.Just import the class and make your own class inhereting from this class.Create the write and read method and inside them create
your own code.
-
my_own_class(write_read):
def write(self,some parameters: some type hints):
my own way of writing files
def read(self,some parameters: some type hints):
my own way of reading files
'''

