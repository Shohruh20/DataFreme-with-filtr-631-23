# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mxk3Yu91E_N6mAa25SIOFvtoyBn4DEcE
"""

import pandas as pd

malumot = {
    "FISH": [
        "Aliyev Azamat",
        "Murodov Doston",
        "Rahmonova Dilnoza",
        "Karimov Sherzod",
        "Qodirov Shoxjahon",
        "Abdurahmonova Malika",
        "Ismoilov Farrux",
        "Tursunova Gulrukh",
        "Asqarov Jamshid",
        "Nurmatova Sabina"
    ],
    "Yoshi": [
        12, 14, 15, 13, 17, 16, 11, 10, 18, 13
    ],
    "Maktabi": [
        "123-sonli maktab",
        "45-sonli maktab",
        "12-sonli maktab",
        "8-sonli maktab",
        "34-sonli maktab",
        "56-sonli maktab",
        "78-sonli maktab",
        "90-sonli maktab",
        "100-sonli maktab",
        "67-sonli maktab"
    ],
    "jinsi": [
        "Erkak", "Erkak", "Qiz", "Erkak", "Erkak",
        "Qiz", "Erkak", "Qiz", "Erkak", "Qiz"
    ],
    "Manzili": [
        "Toshkent", "Samarqand", "Buxoro", "Navoiy", "Farg'ona",
        "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo", "Jizzax"
    ]
}

df = pd.DataFrame(malumot)
print(df)

filtr=df[df['jinsi']=="Qiz"]
print(filtr)

filtr=df[df['jinsi']=="Erkak"]
print(filtr)

filtr = df[(df['jinsi'] == "Erkak") & (df['Yoshi'] < 15)]

# Natijani tartiblash (agar kerak bo'lsa)
filtr_sorted = filtr.sort_values(by='Yoshi')

print(filtr_sorted)

filtr = df[(df['jinsi'] == "Erkak") & (df['Yoshi'] > 15)]

# Natijani tartiblash (agar kerak bo'lsa)
filtr_sorted = filtr.sort_values(by='Yoshi')

print(filtr_sorted)