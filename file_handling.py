#file handling
f = open("sample.txt","w")
f.write("hello")
f.close()
print("Written successfully")

name = input("Enter a file name : ")
f = open(f"{name}.txt","w")
f.write("hello")
f.close()
print("Written successfully")

f = open("sample.txt","a")
f.write("\nhi")
f.close()
print("Written successfully")

f = open("sample.txt","a")
data = input("Enter the data to store :")
f.write(f"\n{data}")
f.close()
print("Written successfully")

f = open("sample.txt","a")
print("Name :",f.name)
print("File Status :",f.closed)
print("File mode :",f.mode)
f.close()
print("File Status :",f.closed)
f = open("sample.txt","r")
print(f.read())
f.close()

x ="""
TamilNadu Foods Are : 

1. Breakfast (Tiffin)
Idli: Steamed rice and lentil cakes.
Dosa: Fermented rice crepes (Plain, Masala, or Ghee Roast).
Vadai: Savory fried lentil doughnuts (Medhu Vadai) or flat spicy patties (Paruppu Vadai).
Pongal: A soft mash of rice and moong dal seasoned with pepper, cumin, and ghee.
Idiyappam: Steamed rice noodles served with coconut milk or spicy curry.
Appam: Thin, bowl-shaped rice pancakes with a soft center and crispy edges.

2. Lunch (The Full Meal)
Sambar: A lentil-based vegetable stew with tamarind.
Rasam: A thin, spicy, and peppery soup used as a digestive aid.
Kuzhambu: Thick gravies like Kara Kuzhambu (spicy) or Vatha Kuzhambu (dried berries in tangy sauce).
Poriyal: Sautéed vegetables with mustard seeds and grated coconut.
Kootu: A semi-solid blend of vegetables and lentils.
Curd Rice: Plain rice mixed with yogurt, tempered with ginger and green chilies.

3. Regional Specialties
Chettinad Cuisine: Intense, spicy dishes like Pepper Chicken and Mutton Sukka.
Madurai Street Food: Kari Dosa (meat-topped dosa) and Parotta (flaky layered bread).
Kongu Nadu: Features dishes like Arisimparuppu Sadam (rice and lentils cooked together).
Nanjil Nadu: Known for seafood and heavy use of coconut oil.

4. Snacks & Sweets
Murukku: Crunchy, spiral-shaped savory snacks.
Filter Coffee: Strong brew made with chicory and frothed milk.
Payasam: A sweet milk pudding with vermicelli or lentils.
Mysore Pak: A rich sweet made of chickpea flour, ghee, and sugar.
"""
f = open("food.txt","r")

f.write(x)
print(f.read())
print(f.read(200))
print(f.readline())
o = f.readlines()
for i in o:
    print(i)
f.close()

import os
print(os.getcwd())
print(os.listdir())
os.rename('file1.txt','new name.txt')
os.remove('new name.txt')

