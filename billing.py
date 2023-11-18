from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0") #창 사이즈 및 위치
        self.root.title("Inventory Management System | Developed By Teddy")
        self.root.config(bg="white")
        self.chk_print=0

        #===title===
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,
                    font=("TkDefaultFont", 40, "bold"), bg="black", fg="white", anchor="w",padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",command=self.logout, font=("TkDefaultFont", 15, "bold"), bg="yellow",cursor="hand2")
        btn_logout.place(x=1100, y=10, height=50, width=150)
        #
        #===clock===
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                             font=("TkDefaultFont", 15, "bold"), bg="grey", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        #
        # ===Variable=======================================================================
        self.var_search = StringVar()

        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        self.var_cal_input = StringVar()
        self.cart_list=[]
        # ===Product_Frame==================================================================
        # ===ProductFrame1==================================================================
        ProductFrame1 = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        ProductFrame1.place(x=10, y=110, width=410, height=550)

        pTitle = Label(ProductFrame1, text="All products",font=("TkDefaultFont", 15, "bold"), bg="#262626", fg="white")
        pTitle.pack(side=TOP, fill=X)

        # ===ProductFrame2==================================================================
        ProductFrame2 = Frame(ProductFrame1, bd=1, relief=RIDGE, bg="white")
        ProductFrame2.place(x=4, y=42, width=400, height=90)

        lbl_search = Label(ProductFrame2, text="Search Product | By Name",font=("TkDefaultFont", 13, "bold"), bg="white", fg="green")
        lbl_search.place(x=2, y=5)

        lbl_name = Label(ProductFrame2, text="Product Name", font=("TkDefaultFont", 13, "bold"),bg="white")
        lbl_name.place(x=5, y=45)

        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_search.place(x=125, y=47, width=150, height=22)

        btn_search=Button(ProductFrame2, text="Search", command= self.search, font=("TkDefaultFont", 13),bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=284, y=45, width=100, height=25)
        btn_show_all = Button(ProductFrame2, command=self.show, text="Show All", font=("TkDefaultFont", 13), bg="#083531", fg="white", cursor="hand2")
        btn_show_all.place(x=284, y=10, width=100, height=25)
        #
        # ===ProductFrame3==================================================================
        ProductFrame3=Frame(ProductFrame1,bd=2, relief=RIDGE)
        ProductFrame3.place(x=4, y=140, width=400, height=385)

        scrolly=Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3, orient=HORIZONTAL)


        self.ProductTable=ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty","status"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="PID")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="QTY")
        self.ProductTable.heading("status", text="Status")
        self.ProductTable["show"]="headings" #heading 부분이 정렬되어서 보여짐

        self.ProductTable.column("pid",width=50) #width=는 컬럼 가로 사이즈
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=40)
        self.ProductTable.column("status", width=80)

        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data) #ProductTable에 마우스 버튼이릴리즈 됐을떼 get_data함수 호출

        lbl_note = Label(ProductFrame1, text="Note:'Enter 0 Qunatity to remove product from the Cart'", font=("TkDefaultFont", 10), anchor='w', bg="white",fg="red")
        lbl_note.pack(side=BOTTOM, fill=X)
        #
        # ===CustomerFrame==================================================================
        CustomerFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        CustomerFrame.place(x=430, y=110, width=530, height=70)

        cTitle = Label(CustomerFrame, text="Customer Details", font=("TkDefaultFont", 13),bg="lightgray")
        cTitle.pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Name", font=("TkDefaultFont", 13), bg="white")
        lbl_name.place(x=5, y=35)

        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_name.place(x=60, y=35, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact", font=("TkDefaultFont", 13), bg="white")
        lbl_contact.place(x=250, y=35)

        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("TkDefaultFont", 13), bg="lightyellow")
        txt_contact.place(x=330, y=35, width=180)
        #
        # ===Cal_Cart_Frame==================================================================
        Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=430, y=190, width=530, height=360)

        # ===Cal_Frame==================================================================
        Cal_Frame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)

        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("arial", 23, 'bold'),
                                   width=15, bd=5, relief=GROOVE, state='readonly')
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7=Button(Cal_Frame, text='7', font=("arial", 15, 'bold'),command=lambda:self.get_input(7), bd=5, width=4, pady=10, cursor="hand2")
        btn_7.grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', font=("arial", 15, 'bold'),command=lambda:self.get_input(8), bd=5, width=4, pady=10, cursor="hand2")
        btn_8.grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=("arial", 15, 'bold'),command=lambda:self.get_input(9), bd=5, width=4, pady=10, cursor="hand2")
        btn_9.grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text="+", font=("arial", 15, 'bold'),command=lambda:self.get_input('+'), bd=5, width=4, pady=10, cursor="hand2")
        btn_sum.grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=("arial", 15, 'bold'),command=lambda:self.get_input(4), bd=5, width=4, pady=10, cursor="hand2")
        btn_4.grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=("arial", 15, 'bold'),command=lambda:self.get_input(5), bd=5, width=4, pady=10, cursor="hand2")
        btn_5.grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=("arial", 15, 'bold'),command=lambda:self.get_input(6), bd=5, width=4, pady=10, cursor="hand2")
        btn_6.grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text="-", font=("arial", 15, 'bold'),command=lambda:self.get_input('-'), bd=5, width=4, pady=10, cursor="hand2")
        btn_sub.grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=("arial", 15, 'bold'),command=lambda:self.get_input(1), bd=5, width=4, pady=10, cursor="hand2")
        btn_1.grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=("arial", 15, 'bold'),command=lambda:self.get_input(2), bd=5, width=4, pady=10, cursor="hand2")
        btn_2.grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=("arial", 15, 'bold'),command=lambda:self.get_input(3), bd=5, width=4, pady=10, cursor="hand2")
        btn_3.grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text="*", font=("arial", 15, 'bold'),command=lambda:self.get_input('*'), bd=5, width=4, pady=10, cursor="hand2")
        btn_mul.grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=("arial", 15, 'bold'),command=lambda:self.get_input(7), bd=5, width=4, pady=21, cursor="hand2")
        btn_0.grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text='C', font=("arial", 15, 'bold'), command=self.clear_cal, bd=5, width=4, pady=21, cursor="hand2")
        btn_c.grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=', font=("arial", 15, 'bold'), command=self.perform_cal, bd=5, width=4, pady=21, cursor="hand2")
        btn_eq.grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text="/", font=("arial", 15, 'bold'),command=lambda:self.get_input('/'), bd=5, width=4, pady=21, cursor="hand2")
        btn_div.grid(row=4, column=3)

        # ===Cart_Frame==================================================================
        Cart_Frame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE)
        Cart_Frame.place(x=280, y=8, width=245, height=342)
        self.cartTitle = Label(Cart_Frame, text="Cart \t Total Product: [0]", font=("TkDefaultFont", 13), bg="lightgray")
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(Cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(Cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(Cart_Frame, columns=("pid", "name", "price", "qty"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="PID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="QTY")
        self.CartTable["show"] = "headings"  # heading 부분이 정렬되어서 보여짐

        self.CartTable.column("pid", width=40)  # width=는 컬럼 가로 사이즈
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=60)
        self.CartTable.column("qty", width=40)

        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>", self.get_data_cart)

        # ===Add Cart Widgets Frame==================================================================
        Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=430, y=550, width=530, height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame, text="Product Name",font=("TkDefaultFont", 13), bg="white")
        lbl_p_name.place(x=5, y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("TkDefaultFont", 13), bg="lightgray", state='readonly')
        txt_p_name.place(x=5, y=35, width=190, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price Per QTY", font=("TkDefaultFont", 13), bg="white")
        lbl_p_price.place(x=220, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("TksefaultFont", 13),bg="lightgray", state='readonly')
        txt_p_price.place(x=220, y=35, width=150, height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("TkDefaultFont", 13), bg="white")
        lbl_p_qty.place(x=395, y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("TksefaultFont", 13), bg="lightyellow")
        txt_p_qty.place(x=395, y=35, width=80, height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame, text="In Stock", font=("TkDefaultFont", 13), bg="white")
        self.lbl_inStock.place(x=5, y=70)

        btn_clear_cart = Button(Add_CartWidgetsFrame, text="Clear", command=self.clear_cart, font=("TkDefaultFont", 13), bg="lightgray",cursor="hand2")
        btn_clear_cart.place(x=160, y=65, width=150, height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame, text="Add|Update Cart", command=self.add_update_cart, font=("TkDefaultFont", 13), bg="lightgray",
                                cursor="hand2")
        btn_add_cart.place(x=325, y=65, width=150, height=30)

        #===billing Area================================================================================
        billFrame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billFrame.place(x=970, y=110, width=370, height=410 )

        BTitle = Label(billFrame, text="Customer Bill Area", font=("TkDefaultFont", 15, 'bold'), bg="#262626", fg='white')
        BTitle.pack(side=TOP, fill=X)

        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(expand=1, fill=BOTH)

        scrolly.config(command=self.txt_bill_area.yview)

        #===billing buttons=================================================================================
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billMenuFrame.place(x=970, y=520, width=370, height=140)

        self.lbl_amnt = Label(billMenuFrame, text="Bill Amount\n[0]", font=("TkDefaultFont", 13, "bold"), bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=5, y=5, width=110, height=70)

        self.lbl_discount = Label(billMenuFrame, text="Discount\n[5%]", font=("TkDefaultFont", 13, "bold"), bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=122, y=5, width=110, height=70)

        self.lbl_net_pay = Label(billMenuFrame, text="Net Pay\n[0]", font=("TkDefaultFont", 13, "bold"), bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=239, y=5, width=126, height=70)

        btn_print = Button(billMenuFrame, text="Print", command=self.print_bill, font=("TkDefaultFont", 13), bg="#3f51b5",fg="white",cursor='hand2')
        btn_print.place(x=5, y=80, width=110, height=50)

        btn_clear = Button(billMenuFrame, text="Clear All", command=self.clear_all, font=("TkDefaultFont", 13),bg="#8bc34a", fg="white",cursor='hand2')
        btn_clear.place(x=122, y=80, width=110, height=50)

        btn_generate = Button(billMenuFrame, text="Generate/Save Bill", command=self.generate_bill, font=("TkDefaultFont", 10), bg="#607d8b",fg="white",cursor='hand2')
        btn_generate.place(x=239, y=80, width=126, height=50)

        # ===Footer=================================================================================
        footer = Label(self.root, text="IMS-Inventory Management System | Developed By Teddy\n For any Technical Issue contact: 111-1111",
                   font=("TkDefaultFont", 11), bg="#4d636d",fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.show()
        # # self.bill_top()
        self.update_date_time()

    #===All Functions===================================================================================
    #===Functions for Cal=======================================
    def get_input(self, num):
        xnum=self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        print(type(result))
        print(result)
        self.var_cal_input.set(eval(result))
        # self.show()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select pid, name, price, qty, status from product where status='Active'")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search  input should be required", parent=self.root)
            else:
                cur.execute(
                    "select pid, name, price, qty, status from product where name LIKE '%" + self.var_search.get() + "%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        print(type(content))
        print(content)
        row = content['values']
        # print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3]) #ProductTable의 QTY 값을 var_stock에 대입 후 CartTable에서 사용
        self.var_qty.set('1') #cart의 기본 qty를 1로 설정



    def get_data_cart(self, ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4]) #add_update_cart()에서 var_stock을 추가하여 index[4]에 저장

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror("Error", "Please select product from the list", parent=self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror("Error", "Quantity is required", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()): #max stock과 cart qty 비교 후 cart qty가 크면 에러
            messagebox.showerror("Error", "Invalid Quiantity", parent=self.root)
        else:
            # price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            # price_cal=self.var_price.get()
            cart_data = [self.var_pid.get(), self.var_pname.get(), self.var_price.get(), self.var_qty.get(),self.var_stock.get()]
            print(self.cart_list)
            #===update_cart=============================================
            present = 'no'
            index_ = -1
            # 중복된 product가 cart에 들어왔을 때 기존 product를 삭제하고 업데이트실행 여부를 물어봄
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_ += 1
            if present=='yes':
                op = messagebox.askyesno('Confirm', "Product already present\nDo you want to Update | Remove from the Cart List", parent=self.root)
                if op == True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #pid, name, price, qty, status
                        # self.cart_list[index_][2] = price_cal #price
                        print("self.cart_list",self.cart_list)
                        self.cart_list[index_][3] = self.var_qty.get() #qty
            else:
                self.cart_list.append(cart_data) #중복된것이 아니면 cart_list에 추가

            print(present, index_)
            self.show_cart() # quantity 수정 후 data를 CartTable에 보여주기위해 실행
            self.bill_update()

    def bill_update(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            # pid, name, price, qty, stock
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3])) #row[2]는 price,row[3]는 qty

        self.discount = (self.bill_amnt * 5) / 100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get() == '':
             messagebox.showerror("Error", f"Customer Details are required", parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error", f"Please Add product to the Cart!!!", parent=self.root)
        else:
            # ====Bill Top====
            self.bill_top()
            # ====Bill Top====
            self.bill_middle()
            # ====Bill Top====
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt', 'w' )
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved', "Bill has been generated/Save in Backend", parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
        #bill top에 보여질 영역
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 98725*****, Delhi-125001
{str("="*49)}
 Customer Name: {self.var_cname.get()}
 Ph No. {self.var_contact.get()}
 Bill No.{str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("="*49)}
 Product Name\t\t\tQTY\tPrice
{str("="*49)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*49)}
Bill Amount\t\t\t\tRs.{self.bill_amnt}
Discount\t\t\t\tRs. {self.discount}
Net Pay\t\t\t\tRs. {self.net_pay}
{str("="*49)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                # pid, name, price, qty, stock
                print(type(row))
                pid=row[0]
                name=row[1]
                qty=int(row[4]) - int(row[3])
                print(type(qty))
                #=== stock과 주문량 비교===
                if int(row[3]) == int(row[4]):
                    status="InActive"
                if int(row[3]) != int(row[4]):
                    status="Active"

                price=float(row[2])*int(row[3])
                price=str(price)
                ##qty 변수 적용시 에러 발생 qty는 int row[3]은 list 추가 확인 필요
                self.txt_bill_area.insert(END, "\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #=== update qty in product table =======================================
                cur.execute('Update product set qty=?,status=? where pid=?', (
                    qty, status, pid
                ))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print', "Please wait while printing", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror('Print', "Please generate bill, to print the receipt", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()