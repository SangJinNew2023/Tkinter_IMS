from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By SangJin")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===Variable=======================================================================
        self.bill_list=[]
        self.var_invoice = StringVar()

        # ===Title============================================================================
        lbl_title = Label(self.root, text="View Customer Bills", font=("TkDefaultFont", 30), bg='#184a45',
                          fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=2)

        # ===Invoice No.============================================================================
        lbl_invoice = Label(self.root, text="Invoice No.", font=("TkDefaultFont", 13), bg='white')
        lbl_invoice.place(x=50, y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("TkDefaultFont", 13), bg='lightyellow')
        txt_invoice.place(x=160, y=100, width=180, height=28)

        btn_search=Button(self.root,text="Search", command=self.search, font=("TkDefaultFont", 13, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=360, y=98, width=120, height=28)

        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("TkDefaultFont", 13, "bold"), bg="lightgray", fg="white", cursor="hand2")
        btn_clear.place(x=490, y=98, width=120, height=28)

        # ===Bill List============================================================================
        salesFrame=Frame(self.root, bd=3, relief=RIDGE)
        salesFrame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(salesFrame, orient=VERTICAL)

        self.Sales_List=Listbox(salesFrame, font=("TkDefaultFont", 13, "bold"), bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        # ===Bill Area============================================================================
        billFrame = Frame(self.root, bd=3, relief=RIDGE)
        billFrame.place(x=280, y=140, width=370, height=330)

        lbl_title2 = Label(billFrame, text="Customer Bills Area", font=("TkDefaultFont", 20), bg='orange')
        lbl_title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(billFrame, orient=VERTICAL)
        self.bill_area=Text(billFrame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.Sales_List.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # === Image ============================================================================
        self.bill_photo = Image.open("images/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((370, 300), Image.ANTIALIAS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=140)

        self.show()
    #
    # #=========================================================================================
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        for i in os.listdir('bill'):

            if i.split('.')[-1]=='txt': #output is "txt"
                print("i1:",i)
                i= i.split('.')[0]
                print("i2:", i)
                self.Sales_List.insert(END, i)
                print("*",i)
                self.bill_list.append(i)
                print("self.bill_list_1",self.bill_list)

    def get_data(self, ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        # print("file_name",file_name)
        self.bill_area.delete('1.0', END)
        fp=open(f'bill/{file_name}.txt', 'r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            print(type(self.var_invoice.get()))
            print("var_invoice",self.var_invoice.get())
            print("bil_list",self.bill_list)
            if self.var_invoice.get() in self.bill_list:
                print("yes find the invoice")
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()