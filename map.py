import random

#map
'START BLOCK'
#house
houses = (
    {'id':0,'position':(-200,400),'doorposition':(-200+110,400+50),'entered':False,'contents':[{'position':(-160,460),'weapon':'bow'},{'position':(-20,455),'weapon':'arrows'}]},
    {'id':1,'position':(600,400),'doorposition':(600+110,400+50),'entered':False,'contents':[]},
    {'id':2,'position':(1400,400),'doorposition':(1400+110,400+50),'entered':False,'contents':[]}
)
'END BLOCK'

#grass
'START BLOCK'
grassdata = list()

for i in range(-50,50):
    #generate grass in patches
    for j in range(random.randint(1,4)):
        grass = dict()
    
        grass['X'] = random.randint(-50,50)+i*random.randint(500,700)
        grass['type'] = random.randint(0,1)

        grassdata.append(grass)
'END BLOCK'
