class PhoneBook:
    def __init__(self):
        self.phonebook = {}

#Jeżeli osoba już jest w naszej ksiażce, to po prostu dopisujemy do niej kolejny numer.
#Jeżeli osoby nie ma w naszej książce, tworzymy nowy record 
    def insert(self, name, number):
        if name in self.phonebook:
            self.phonebook[name].append(number)
        else:
            self.phonebook[name] = [number]

#Zwracamy numery danej osoby
    def retrieve(self, name):
        if name in self.phonebook:
            return self.phonebook[name]
        else:
            return None

#Usuwamy numer danej osoby, jezeli nie ma jej w ksiazce to zwracamy False
    def delete(self, name, number):
        if number in self.phonebook[name]:
            self.phonebook[name].remove(number)
        else:
            return False
    

    def print_phonebook(self):
        for name, numbers in self.phonebook.items():
            print(f"{name}: {', '.join(numbers)}")

#Testing
pb = PhoneBook()

pb.insert("Ala Wesołowska", "+048 513 056 121")
pb.insert("Ala Wesołowska", "22-848-34-21")
pb.insert("John Smith", "469-452-199")
pb.insert("John Smith", "0800 241 6331")
pb.insert("Susan Brown", "315-728-3639")    

pb.print_phonebook()


print("\nNumery Johna Smitha:", pb.retrieve("John Smith"))


pb.delete("John Smith", "0800 241 6331")

print("\nKsiązka Telefoniczna po usunięciu numeru")
pb.print_phonebook()

