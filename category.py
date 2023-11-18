from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By SangJin")
        self.root.config(bg="white")
        self.root.focus_force()

        #===Variable=======================================================================
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        #===Title============================================================================
        lbl_title=Label(self.root, text="Manage Product Category", font=("TkDefaultFont", 30), bg='#184a45', fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=2)

        lbl_name=Label(self.root, text="Enter Category Name", font=("TkDefaultFont", 30), bg="white")
        lbl_name.place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("TkDefaultFont", 30), bg="lightyellow")
        txt_name.place(x=50, y=170, width=300)

        # ===Button===========================================================================
        btn_add = Button(self.root, text="Add", command=self.add, font=("TkDefaultFont", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_add.place(x=360, y=175, width=150, height=30)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("TkDefaultFont", 15), bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=520, y=175, width=150, height=30)

        # ===Category Details==================================================================
        cat_frame=Frame(self.root,bd=3, relief=RIDGE)
        cat_frame.place(x=680, y=90, width=380, height=115)

        scrolly=Scrollbar(cat_frame, orient=VERTICAL)
        scrollx=Scrollbar(cat_frame, orient=HORIZONTAL)


        self.CategoryTable=ttk.Treeview(cat_frame, columns=("cid", "name"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="C ID")
        self.CategoryTable.heading("name", text="Name")
        self.CategoryTable["show"]="headings" #heading 부분이 정렬되어서 보여짐
        self.CategoryTable.column("cid",width=90) #width=는 컬럼 가로 사이즈
        self.CategoryTable.column("name", width=100)

        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        #===images============================================================ wr r r r
        self.im1=Image.open("images/cat.jpg")
        self.im1 = self.im1.resize((490,250), Image.ANTIALIAS)
        self.im1 =ImageTk.PhotoImage(self.im1)

        self.lb1_im1 = Label(self.root, image=self.im1)
        self.lb1_im1.place(x=50, y=220)

        self.im2 = Image.open("images/category.jpg")
        self.im2 = self.im2.resize((490, 250), Image.ANTIALIAS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lb1_im1 = Label(self.root, image=self.im1)
        self.lb1_im1.place(x=50, y=220)

        self.lb1_im2 = Label(self.root, image=self.im2)
        self.lb1_im2.place(x=564, y=220)

        self.show()

    # ====Function====================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category name should be required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?", (self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Category already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        print(content)
        row=content['values']
        print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select category name from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()