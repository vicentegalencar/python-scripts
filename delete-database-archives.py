import os
import pandas as pd

path = "output"
pastas = os.listdir(path)

for i in pastas:
    pasta2 = os.listdir("output/" + i)
    for x in pasta2:
        print(x)
        if(x == "0_L-CC.png" or "0_R-CC.png" or "0_L-MLO.png" or "0_C-MLO.png"):
            print("output/" + i + "/" + x)
            #os.remove("output/" + i + "/" + x)
