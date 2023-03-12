
import glob
import os
import shutil

import pandas as pd

path = "output"
files = glob.glob(path + '/*.png')
df = pd.read_excel('output/balanced_mass_nof.xlsx')
pastas = os.listdir(path)


for i in pastas:
    folder_name = df["folder_name"] #for nas pastas, escolhe uma


    for p in folder_name: #for no excel, se não achar, repete
        if(i == p): # se os valores forem iguais
            print(i)
            pasta2 = os.listdir("output/" + i)
            for x in pasta2:
                print(x)
                img_pd = df.loc[(df["folder_name"] == i) & (df["img_old_name"] == x) ]
                for y in img_pd:
                    img_new = img_pd["img_new_name"]
                    try:
                        for l in img_new:
                            print(l)
                            os.rename("output/"+ i + "/" + x,"output/"+ i + "/" + l)
                    except:
                        pass
                    img_old = df["img_old_name"] == x
                    for y in img_old:
                        if(y == True):
                            img_new = df.loc[df["folder_name"] == i,"img_new_name"]
                            for l in img_new:
                                print(l)
                                os.rename("output/"+ i + "/" + x,"output/"+ i + "/" + l)
            break
                            
                    
        
                    
          
    

                     
  



# for p in pastas:
#     new_path = path + "/" + p
#     print(new_path)
