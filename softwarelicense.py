#!/usr/bin/env python3

input1 = input("SoftwareLicense: ")

input2 = input("LicenseNumber: ")

file = open("license.txt", "a")

file.write(input1)
file.write(":")
file.write(input2)
file.write("\n")
file.write("---" + "\n")
file.close()
