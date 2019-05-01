class file:
    def userfile(self,obj):
        self.obj=obj

print("1.employee")
print("2.manager")
n = int(input("select the user:"))


if n==1:
    a=str(input("Enter the name of the file with extension:"))
    file1=open(a,'r')
    line=file1.readline()
    while(line!=""):
        print(line)
        line=file1.readline()
    file1.close()


elif n==2:
    fname = input("Enter file name: ")
    file2=open(fname,"a")
    c=input("Enter string to append: \n");
    file2.write("\n")
    file2.write(c)
    file2.close()
    print("Contents of appended file:");
    file3=open(fname,'r')
    line1=file3.readline()
    while(line1!=""):
        print(line1)
        line1=file3.readline()
    file3.close()
else:
    print ("Invalid selection")





