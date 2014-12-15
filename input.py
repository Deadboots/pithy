#!/usr/bin/env python3

name = input("Enter your name:")

age = input("Enter your age:")

sex = input("Enter your sex (male or female):")

lang = input("Enter your native language:")

print(name.capitalize())
print(age)
print(sex.upper())
print(lang.upper())

print("7 years from now, you will be:")

age7 = int(age) + 7

print(age7)
