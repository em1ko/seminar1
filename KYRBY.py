def read(path):
    try:
        file = open(path,"r")
       
    except FileNotFoundError:
        print("Soubor nenalezen :c")
        return[]
    obsah = file.read()
    file.close()
    return obsah
    
print (read("nacteni.txt"))

def look_for(key,worth,dictionary):
    try:
        value=dictionary[key]
        
    except KeyError:
        print("skoda")
    if worth==value:
        print("shoda")
    else:
        print("neshoda")
look_for("rohlik","chleba",{"rohlik":"chleba"})