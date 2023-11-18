from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By SangJin")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===All Variables===
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        #===SearchFrame===
        # SearchFrame=LabelFrame(self.root,text="Search Supplier", font=("System", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        # SearchFrame.place(x=250, y=20, width=520, height=70)

        #===Options===
        lbl_search=Label(self.root,text="Invoice No.", bg="white", font=("TkDefaultFont",12))
        lbl_search.place(x=590, y=80)

        txt_search=Entry(self.root, textvariable=self.var_searchtxt, font=("TkDefaultFont",13), bg="lightyellow")
        txt_search.place(x=680, y=80,width=150)

        btn_search=Button(self.root, text="Search", command=self.search, font=("TkDefaultFont",13), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=840, y=77, width=100, height=25)

        #===Title===
        title=Label(self.root, text="Supplier Details", font=("TkDefaultFont", 20), bg="#0f4d7d", fg="white")
        title.place(x=50, y=10, width=1000, height=40)

        #===Content===
        #===Row1===
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("TkDefaultFont", 13), bg="white")
        lbl_supplier_invoice.place(x=50, y=80)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_supplier_invoice.place(x=140, y=80, width=180)

        # ===Row2===
        lbl_name = Label(self.root, text="Name", font=("TkDefaultFont", 13), bg="white")
        lbl_name.place(x=50, y=120)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_name.place(x=140, y=120, width=180)

        # ===Row3===
        lbl_contact = Label(self.root, text="Contact", font=("TkDefaultFont", 13), bg="white")
        lbl_contact.place(x=50, y=160)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_contact.place(x=140, y=160, width=180)

        # ===Row4===
        lbl_desc = Label(self.root, text="Description", font=("TkDefaultFont", 13), bg="white")
        lbl_desc.place(x=50, y=200)

        self.txt_desc = Text(self.root, font=("TkDefaultFont", 13), bg="lightyellow")
        self.txt_desc.place(x=140, y=200, width=430, height=90)

        # ===Buttons===
        btn_add = Button(self.root, text="Save", command=self.add, font=("TkDefaultFont", 13), bg="#2196f3", fg="white",cursor="hand2")
        btn_add.place(x=140, y=310, width=100, height=35)

        btn_update = Button(self.root, text="Update", command=self.update, font=("TkDefaultFont", 13), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=250, y=310, width=100, height=35)

        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("TkDefaultFont", 13), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=360, y=310, width=100, height=35)

        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("TkDefaultFont", 13), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=470, y=310, width=100, height=35)

        # ===Supplier Details===
        emp_frame=Frame(self.root,bd=3, relief=RIDGE)
        emp_frame.place(x=590, y=110, width=450, height=370)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)


        self.SupplierTable=ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Desc")

        self.SupplierTable["show"]="headings" #heading 부분이 정렬되어서 보여짐

        self.SupplierTable.column("invoice",width=90) #width=는 컬럼 가로 사이즈
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc", width=100)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ====Function===
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Invoice no already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no. Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no. Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice no", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()