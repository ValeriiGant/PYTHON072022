from csv_writer import csv_writer as csv


def add_contact() -> None:
    surname = input('\n Фамилия: ')
    csv(field=surname + ';', path="phonebook", filename="phonebook.csv")
    name = input('\nИмя: ')
    csv(field=name + ';', path="phonebook", filename="phonebook.csv")
    middlename = input('\n Отчество: ')
    csv(field=middlename + ';', path="phonebook", filename="phonebook.csv")
    phone = input('\n Телефон: ')
    csv(field=phone + ';', path="phonebook", filename="phonebook.csv")
    description = input('\n Описание: ')
    csv(field=description + ';', path="phonebook", filename="phonebook.csv")
    csv(field='\n', path="phonebook", filename="phonebook.csv")
