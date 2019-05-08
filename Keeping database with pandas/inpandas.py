import pandas as pd
import random
a = ["Steve Peterman"]
b = ["Canada"]
c = ["30"]
d = ["Queen"]

id1 = (random.randint(0,10000000)) * 2 +1

name = input("Name: ")
a.append(name)
country = input("Country: ")
b.append(country)
age = input("Age: ")
c.append(age)
music = input("Music: ")
d.append(music)
print("Name: ", name)
print("Age: ", age)
print("ID: ", id1) 

w = {"Name": a,
       "Country": b,
             "Age": c,
               "Music": d}

data = pd.DataFrame(w)

data.to_save('C:/Users/Галым/Desktop/Pandas/pandas3.csv')
