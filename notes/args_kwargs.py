#LV 2nd *args and **kwargs

"""def hello(name = "Sam", age = 17):
    return f"Hello{name}! You are {age}!"

print(hello())
print(hello("Tom"))
print(hello(age = 19,name = "Rod"))"""


# position arguments, *args, keyword arguments, ** kwargs
def hello(*names,**last):
    print(type(names))
    for name in names:
        if name == "Tom":
            print(f"Hello {name} {last['alast']} {last['vlast']}")
        else:
            print(f"Hello {name} {last['alast']}")

hello("Tom","Angi","Rod",alast="Mostaceli",vlast ="Venancio")