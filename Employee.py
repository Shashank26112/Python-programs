class Employee:
    def get_data(self):
        self.emp_no=int(input("Enter employee number: "))
        self.name=input("Enter Employee name: ")
        self.desig=input("Enter designation of Employee: ")
        self.dept=input("Enter Department: ")
        self.age=int(input("Enter the age: "))
        self.basic=int(input("Enter the basic salary: "))
    def display(self):
        print(self.emp_no,"\t",self.name,"\t",self.desig,"\t",self.dept,"\t",self.age,"\t",self.basic)
    def search(self,id):
        if id==self.emp_no:
            return True
        else:
            return False; 
n=int(input("Enter the number of employee: "))
Lst=[]
for i in range(n):
    E1=Employee()
    E1.get_data()
    Lst.append(E1)
while True:
    print("1.To Display Employee information \n 2.Search for an employee")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print('------------------------------------------------------\n')
        print("Emp No \t  Name \t\t Desig \t Dept \t Age \t Salary")
        for e in Lst:
            e.display()
        print('-----------------------------------------------------\n')
    elif ch==2:
        id=int(input("Enter the employee number to be searched"))
        for i in Lst:
            found=i.search(id)
            if found:
                print("Employee Details found.They are")
                i.display()
                break
        else:
            print("Employee details not found")
    else:
        break
    
            

    