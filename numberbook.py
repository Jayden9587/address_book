import ast
import os

class Person:
    def __init__(self,name,age,address,category):
        self.name = name
        self.age = age
        self.address = address
        self.category = category


def book_print(dir):
    try:
        category_set = set()
        with open(dir,'r') as f:
            idx = 0
            full_content = f.readlines()
            for readline in full_content:
                idx += 1
                read = ast.literal_eval(readline)
                category_set.add(read['category'])
            for category in category_set :
                print('category : {}'.format(category))
                for readline in full_content:
                    read = ast.literal_eval(readline)
                    if read['category'] == category :
                        print('name : {} age : {} address : {} category : {}'.format(read['name'],read['age'],read['address'],read['category']))
                print('')
    except FileNotFoundError :
        print('File not exist!!')


def save_person(dir,p):
    with open(dir,'a') as f:
        f.write(str(p)+'\n')


def delete_person(dir,n):
    try :
        content = ''
        with open(dir,'r') as f:
            for readline in f.readlines():
                read = ast.literal_eval(readline)
                if read['name']!= n:
                    content += readline
        with open(dir,'w') as f:
            f.write(content)
    except FileNotFoundError :
        print('File not exist!!')


def search_person(dir,n):
    try :
        with open(dir,'r') as f:
            for readline in f.readlines():
                read = ast.literal_eval(readline)
                if read['name'] == n:
                    print('find person --> name : {} age : {} address : {} category : {}'.format(read['name'],read['age'],read['address'],read['category']))
                    break
    except:
        print('File not exist !!')


dir = 'address_list.txt'

while True :
    print('1. print address_book ')
    print('2. save Person')
    print('3. delete Person')
    print('4. Search Person')
    print('5. exit')
    a = input()
    if a == '1':
        book_print(dir)
    elif a == '2':
         person ={}
         print('input name : ')
         person['name']=input()
         print('input age : ')
         person['age']=input()
         print('input address : ')
         person['address']=input()
         print('input category : ')
         person['category']=input()
         save_person(dir,person)
    elif a == '3':
        print('Fine person name :')
        name = input()
        delete_person(dir,name)
    elif a == '4':
        print('Fine person name :')
        name = input()
        search_person(dir,name)
    elif a == '5':
        print('address book Exit')
        break