from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    

class Name(Field):
    def __init__(self, name = None):
        if name is None:
            raise ValueError
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        
    def add_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
         for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
         raise ValueError
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError
    
    def __str__(self):
        return f"Record(Name: {self.name} Phones {self.phones})"
    
    def __str__(self):
        return f"Record(Name: {self.name} Phones {self.phones})"
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        self.data.update({name: record})
    
    def find(self, name):
        return self.get(name)
    
    def delete(self, name):
        del self[name]

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
        





