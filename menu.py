#!/usr/bin/python3
import os
import crypt
from googlesearch import search 
print("-------Menu---------")
print("1, Create Directory: ")
print("2, File Create: ")
print("3, Check and install given software: ")
print("4, To add/create user and password: ")
print("5, Reboot your machine: ")
print("6, Check current date and time: ")
print("7, to search some thing on google: ")
print("8, Play a song in current OS player: ")
print("9, To search on goole to get 5 URl: ")
print("10, Login your fb abd update a status '\"Hello Adhoc'\": ")
print("11, To send msg '\"HELLO'\" from adhoc to whatsapp ")
choice = int(input("Enter your choice: "))
if(choice == 1):
   dir_name = input("Enter directory name: ")
   os.system("mkdir " +dir_name)
     
elif(choice == 2):
  dir_name = input("Enter your file name: ")
  os.system("touch " +dir_name)

elif(choice == 3):
  dir_name = input("Enter software name: ")
  os.system("yum install -y " +dir_name)

elif(choice == 4):
  uname = input("Enter user_name : ")
  password = input("Enter password : ")
  ucrypt=crypt.crypt(password,"123")
  os.system("useradd -m -p "+password+" "+uname)

elif (choice == 5):
  answer = str(input('reboot_system? (y/n): '))
  if answer == 'n':
    print ('Goodbye')
    
  elif answer == 'y':
    os.system("reboot")
  else:
    print ('Invalid Input.')

elif (choice == 6):
  os.system('date')

elif (choice == 7):
  query = input("Enter keyword which you want to search: ")
  
  for j in search(query, tld="com", num=10, stop=1, pause=2): 
    print(j) 

