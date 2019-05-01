class user():
    def __init__(self):
        self.n={}
    def add(self,user_id,**kwargs):
        return self.n.update({user_id:{'first_name': kwargs.get('first_name'),
                 'last_name': kwargs.get('last_name')}})
    def delete(self,user_id):
        self.n.pop(user_id)
    def dis(self):
        return (self.n)

object_selected = ''
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    print("4. Select Object")
    try:
        choice=int(input("Enter choice: "))
        if choice==1:
            if isinstance(object_selected, str):
                print ('Please select an object to proceed')
            else:    
                user_id = str(input("Enter User ID: "))
                first_name=str(input("Enter First name: "))
                last_name = str(input("Enter Last name: "))
                data = {'first_name':first_name, 'last_name': last_name}
                object_selected.add(user_id, **data)
                print("Data: ",object_selected.dis())
                
     
        elif choice==2:
            user_id=str(input("Enter user_id to remove: "))
            object_selected.delete(user_id)
            print("Data: ",object_selected.dis())
     
        elif choice==3:
            print("Data: ",object_selected.dis())
        elif choice==4:
            object_selected = str(input('Please select either obj1 or obj2 to add details: '))
            if object_selected not in ['obj1','obj2']:
                print ('Invalid object selected')
            else:
                object_selected = user()
        elif choice==0:
            print("Exiting!")
        else:
            print("Invalid choice!!")
    except ValueError:
        print ("Invalid Choice!!")


