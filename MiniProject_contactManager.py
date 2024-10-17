# Create a simple contact manager that:
# - Stores name and phone number
# - Allows adding new contacts
# - Shows all contacts
# - Use lists or dictionary (your choice)
import json


def add_person():
    name=input("enter the name: ")
    phonenumber=int(input("enter the number: "))
    person={ "name":name,
              "mobilenumber":phonenumber
             }
    return person
def get_people(people):
    for i,person in enumerate(people):
        print(i+1 , '-',person['name'],"|",person['mobilenumber'])

def delete(people):
    get_people(people)
    while True:
        number=input("enter number: ").lower()
        try:
            number=int(number)
            if number <= 0 or number > len(people):
                print("Number is out of range ")
            elif number > 0 or number <= len(people):
                break
        except:
            print("invalid number")


    people.pop(number-1)
    print("person deleted")
    return people
def Search_person(people):
    search_name=input(" enter the search name: ").lower()
    result=[]
    for person in people:
        name=person["name"]
        if search_name in name.lower():
            result.append(person)
    get_people(people)
def list(people):
    for i,person in enumerate(people):
        print(i+1,person["name"],person["mobilenumber"])



print("Hi Welcome to Contact Management System.")
with open("contacts.json","r") as f:
    people=json.load(f)["contacts"]


while True:
    print("contact size: ",len(people))
    operation=input(" you can add/delete/search/show and 'Q' for quit :").lower()
    if operation=="add":
        person=add_person()
        people.append(person)
        print("person added ! ")
    elif operation=="delete":
        delete(people)
    elif operation == "search":
        Search_person(people)
    elif operation=="show":
        list(people)
    elif operation=="q":
        break
    else:
        print("invalid command")
with open("contacts.json","w") as f:
    people=json.dump({"contacts": people},f)
