from dataclasses import dataclass
@dataclass
class builtin:
          _1: any
          _2: any
          _3: any


'''
With the builtin class you can implement your own builtin styles.You can fetch your builtin styles with the variables _1 , _2 and _3.
-
my_builtin_style=builtin("style_1","style_2","style_3")
-
print(my_builtin_style._1)

output:
style_1
-
print(my_builtin_style._2)

output:
style_2
-
print(my_builtin_style._3)

output:
style_3

'''
