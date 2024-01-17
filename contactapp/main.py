from library import *
i=0
while i==0:
    print("-----Welcome to Contact App------ ")
    print("1-> For Creating a new contact\n")
    print("2-> For Listing all  contacts \n")
    print("3-> For Searching a  contact \n")
    opt=int(input("Select an option from list"))
    if opt==1:
        create_contact()
    if opt==2:
        s=list_all_contacts()
        contact_details=s.split('#')
        for item in contact_details:
            print(item)
    if opt==3:
        print("Enter code for searching contacts")
    i=int(input("Do you want to continue? Press 0 for Yes"))