#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: laiunce
"""

import requests

directorio=''
lista_imagenes=['https://www.madisoundspeakerstore.com/images/H2606_9200-mech.jpg','https://www.madisoundspeakerstore.com/images/H2606_9200-mech.jpg']

nom=0
for i in lista_imagenes:
    nom+=1
    f = open(directorio+str(nom)+'.jpg','wb')
    f.write(requests.get(i).content)
    f.close()


