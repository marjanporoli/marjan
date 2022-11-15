thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
    
}

for x in thisdict:
    print(x)
for x,y in thisdict.items():
    print(x,y)
for x in thisdict.values():
    print(x)
for x in thisdict:
    print (thisdict[x])
    
thisdict.pop("model")
print(thisdict)

