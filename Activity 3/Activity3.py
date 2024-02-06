import csv

class Person:
    def __init__(self, id, first_name, middle_name, last_name, birthday, gender, address):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.address = address
    
def load_csv(file_path):
    persons = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # next(reader)
        for row in reader:
            id, first_name, middle_name, last_name, birthday, gender, address = row
            persons.append(Person(id, first_name, middle_name, last_name, birthday, gender, address))
    return persons

def search(keyword):
    keyword_upper = keyword.upper()
    counter = 0
    for person in person_list:
        if(keyword_upper in person.first_name.upper() or
           keyword_upper in person.middle_name.upper() or
           keyword_upper in person.last_name.upper()):
            counter += 1
            print(f"ID: {person.id}\nFirst Name: {person.first_name}\nMiddle Name: {person.middle_name}\nLast Name: {person.last_name}\nBirthday: {person.birthday}\nGender: {person.gender}\nAddress: {person.address}\n")
    print(f"Successfully found {counter} results for \"{keyword}\" keyword.")
    
def main():
    while True:
        user_search = input("Search: ")
        search(user_search)
    
person_list = load_csv("algorit/Activity 3/persons.csv")
if __name__ == "__main__":
    main()