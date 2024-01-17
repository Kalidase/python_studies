def read_contact_from_console():
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    return name+"#"+email+"#"+mobile+"\n"
def create_contact():
    data=read_contact_from_console()
    fp=open("contact_data","w")
    fp.write(data)
    fp.close()
    print("Contact Created Successfully")
def list_all_contacts():
    fp=open("contact_data","r")
    data=fp.read()
    fp.close()
    return data 
def search_contact_data():
    fp=open("contact_data","r")
    data=fp.read()
    fp.close()
