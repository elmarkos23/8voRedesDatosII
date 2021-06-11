switches=[]
routers=[]
devices=["R1","R2","R3","S1","S2"]
for item in devices:
        if "S" in item:
            switches.append(item)
        elif "R" in item:
            routers.append(item)
            
print('Switches:')
for item in switches:
    print(item)
print('Routers:')
for item in routers:
    print(item)
