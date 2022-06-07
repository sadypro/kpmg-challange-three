
#Example input
d={'a':{'b':{'c':1, 'd':2},'e':{'f':3, 'g':4}}, 'h':{'i':5, 'j':6}}

#Travesal function
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)
# Match the Key
def retrive(d,key):
    for k, value in recursive_items(d):
        if k == key:
            print(key, value)
        
retrive(d,'j')


