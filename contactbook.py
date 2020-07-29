from tkinter import *
from tkinter import Tk
#creation of main dialogue box
root=Tk()
root.title("Contacts book")
root.geometry("400x400+50+50")
readablecontacts=StringVar()
def Addcontact():
        #new contacts dialogue box entries and buttons
        root1=Tk()
        root1.title("new contacts")
        root1.geometry("200x200+20+20")
        def save():
                #saving in a file
                file1=open("contactlist.txt","a")
                file1.write("\n")
                file1.writelines(new_name.get())
                file1.write("\n")
                file1.writelines(new_number.get())
                file1.write("\n")

                file1.close()
                Label2=Label(root1,text="Contact saved")
                Label2.pack()
                        
       #taking entries for new contact
        new_name=Entry(root1)
        new_name.pack()
        new_number=Entry(root1)
        new_number.pack()
        btn3=Button(root1,text="save contact",command=save)
        btn3.pack()
        root1.mainloop()
#check contacts dialogue box buttons and entries
def checkcontact():

        
                 file1=open("contactlist.txt","r")
                 readablecontacts=file1.readlines()
                 file1.close()
                 for i in range(0,len(readablecontacts)):
                         if(str(query.get()+"\n")==readablecontacts[i]):
                                 label4=Label(root,text=str(readablecontacts[i])+str(readablecontacts[i+1]))
                                 label4.pack()
                    
#main dialogue box buttons
btn1=Button(root,text="Add contact",command=Addcontact)
btn1.pack()
query=Entry(root)
query.pack()
btn4=Button(root,text="Show",command=checkcontact)
btn4.pack()
root.mainloop()