class file():

    def read(fname):
        txt = open(fname)
        print(txt.read())

    def write(fname):
        with open(fname, "w") as myfile:
            myfile.write("Hello world\n")
            myfile.write("How r uh")
        txt = open(fname)
        print(txt.read())


class role(file):
    def __init__(self):
        self.c=[]

    def add(self,a):
        return self.c.append(a)

class user(role):
    def __init__(self):
        self.n = {}

    def add(self, **kwargs):
        for key, value in kwargs.items():
            self.n[key] = value

    def update(self, key,value):
        self.n[key] = value

    def delete(self,key):
        del self.n[key]



obj1=user()
obj1.add(**{"Firstname":"Ritik" , "Lastname":"Jain", "Department":"IT"})
obj1.update("Firstname","Rit")
obj1.delete("Lastname")
print(obj1.n)

obj2=user()
obj2.add(**{"Firstname":"Harshvardhan" , "Lastname":"Gupta", "Department":"IT"})
obj2.update("Firstname","Harsh")
obj2.delete("Lastname")
print(obj2.n)

file.read('/home/daffodil-42/PycharmProjects/python task/task.py')

file.write('/home/daffodil-42/PycharmProjects/python task/hello.txt')

obj1 = role()
obj1.add("employee")
print (obj1.c)
