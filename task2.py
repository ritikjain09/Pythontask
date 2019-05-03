class file():
    def read(self):
        self.filename = "hello.txt"
        file = open(self.filename, "+r")
        for line in file:
            print(line)
        print('you have read permission only')
    def write(self):
        self.filename = open("hello.txt", "+a")
        lines_of_text = ["a line of text", "another line of text", "a third line"]
        self.filename.writelines(lines_of_text)
        self.filename.close()
        print("File updated")
        print ('you have write and read permissions')


class role(file):

    def employee(self):
        self.read()

    def manager(self):
        self.write()

class user(role):
    n = {}
    def add(self, dictionary):
        for item in dictionary.keys():
            self.n[item] = dictionary[item]
    def update(self, key,value):
        self.n[key] = value
    def delete(self,key):
        del self.n[key]





obj1=user()
obj1.add({"Firstname":"Ritik" , "Lastname":"Jain", "Department":"IT"})
obj1.update("Firstname","Rit")
obj1.delete("Lastname")
print(obj1.n)
obj1.manager()
# obj1.write()

obj2=user()
obj2.add({"Firstname":"Harshvardhan" , "Lastname":"Gupta", "Department":"IT"})
obj2.update("Firstname","Harsh")
obj2.delete("Lastname")
print(obj2.n)
obj2.employee()

