class user(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value, **kwargs):
        self[key] = value
obj1 = user()
obj1.add("firstname","ritik")
obj1.update({'Department':'IT'})
obj1.popitem()
print(obj1)
obj2=user()
obj2.add('firstname', 'rahul')
obj2.update({'Department':'IT'})
obj2.popitem()
print(obj2)
class role():
    def __init__(self):
        self.write = False
    def file(self):
        self.read = True
employee = role()
employee.write
employee.file()


