# LV 2nd Dictionaries Notes

avatar = {
    "earth":{
        "Toph": "My name is Toph"
    },
    "water": {
        "Katara":"It's not like I am a preachy crybaby who can't help but make speaches about hope all the time",
        "Sokka": "used to be boomerang guy"
    },
    "fire": {
        "Zuko": "like everything always does!",
        "Uncle Iroh": "It's nothing but boiled leaf juice!"
    },
    "air":{
        "Aang":"something"
    }
}

print(avatar["earth"]["Toph"])
print(avatar["water"]["Sokka"])

person = {
    #key : value,
    "name": "Rod",
    "age": 11,
    "job": "engineer",
    "siblings": ["Ana","Tomas"]
}

print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
        else:
            print(f"{key} are {person[key]}")

print(person.values())
person["age"]+=1
print(person["age"])
person["birthday"] = "May 13"
print(person.items())
person["birthday"] = "March 24"
print(person.items())

