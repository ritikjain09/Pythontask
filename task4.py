class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        txt = open(self.filename)
        for line in txt:
            print(line)

    def write(self):
        with open(self.filename, "w") as mile:
            mile.write("Hello world\n")
            mile.write("How r uh")
        txt = open(self.filename)
        for line in txt:
            print(line)


class Role:
    def per(self):
        self.read()
        self.write()

    def __init__(self):
        self.c = []

    def ad(self, a):
        return self.c.append(a)


class User(Role):
    def __init__(self):
        self.n = {}

    try:
        def add(self, **kwargs):
            for key, value in kwargs.items():
                self.n[key] = value
    except ValueError:
        print("Oops!  That was not valid option.  Try again...")

    try:
        def update(self, key, value):
            self.n[key] = value
    except ValueError:
        print("Oops!  That was not valid option.  Try again...")

    try:
        def delete(self, key):
            del self.n[key]
    except ValueError:
        print("Oops!  That was not valid option.  Try again...")


obj1 = User()
obj1.add(Firstname='Ritik', Lastname='Jain', Department='IT')
obj1.update("Firstname", "Rit")
obj1.delete("Lastname")
print(obj1.n)

obj2 = User()
obj2.add(Firstname='Harshvardhan', Lastname='Gupta', Department='IT')
obj2.update("Firstname", "Harsh")
obj2.delete("Lastname")
print(obj2.n)

filename = File('/home/daffodil-42/PycharmProjects/python task/task.py')
filename.read()

filename = File('/home/daffodil-42/PycharmProjects/python task/hello.txt')
filename.write()

obj1 = Role()
obj1.ad("employee")
print(obj1.c)

obj2 = Role()
obj2.ad("manager")
print(obj2.c)


