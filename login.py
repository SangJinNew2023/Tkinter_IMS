from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import smtplib
import time
import email_pass

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed By Teddy")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #=== Variable ===
        self.otp=''
        self.employee_id = StringVar()
        self.password = StringVar()

        #=== images ===
        # self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        # self.lbl_Phone_image=Label(self.root, image=self.phone_image, bd=0)
        # self.lbl_Phone_image.place(x=200, y=50)

        #===Login Frame ===
        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title=Label(login_frame, text="Login System", font=("TkDefaultFont", 30, "bold"), bg="white")
        title.place(x=45, y=20)

        lbl_user=Label(login_frame, text="Employee ID", font=("TkDefaultFont", 13), bg="white", fg="#767171")
        lbl_user.place(x=60, y=100)
        txt_username=Entry(login_frame, textvariable=self.employee_id, font=("TkDefaultFont", 15), bg="white")
        txt_username.place(x=60, y=130)

        lbl_pass = Label(login_frame, text="Password", font=("TkDefaultFont", 13), bg="white")
        lbl_pass.place(x=60, y=190)
        txt_pass = Entry(login_frame, textvariable= self.password, font=("TkDefaultFont", 15), bg="white")
        txt_pass.place(x=60, y=220)

        btn_login=Button(login_frame, command=self.login, text="Login",font=("TkDefaultFont", 13))
        btn_login.place(x=60, y=290, width=225, height=30)

        hr=Label(login_frame, bg="lightgray")
        hr.place(x=50, y=370, width=250, height=2)

        or_ = Label(login_frame, text="OR", font=("TkDefaultFont", 13), bg="white", fg="lightgray")
        or_.place(x=160, y=357)

        btn_forget=Button(login_frame, text="Forget Password?",command=self.forget_window, font=("TkDefaultFont", 10), bd=0, bg="white", fg="blue", activebackground="white")
        btn_forget.place(x=110, y=400)

        #=== Frame2 ===
        register_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        lbl_reg=Label(register_frame, text="SUBCRIBE | LIKE | SHARE", font=("TkDefaultFont", 13, 'bold'), bg="white")
        lbl_reg.place(x=65, y=17)
        #
        #=== Animation Images ===
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root, bg="white")
        self.lbl_change_image.place(x=150, y=153, width=450, height=428)

        self.animate()

#=============All Functions ===================
    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                print(user)
                if user == None:
                    messagebox.showerror('Error', "Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    if user[0] ==  "Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forget_window(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror('Error', "Employee Id must be required", parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email = cur.fetchone()
                # print(email[0])
                if email == None:
                    messagebox.showerror('Error', "Invalid Employee ID, try again", parent=self.root)
                else:
                    #==== Forget Window ====
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    # call send_emial_function()
                    chk=self.send_email(email[0]) #send_email() 함수 호출 인자는 DB로 부터 얻은 메일 주소
                    if chk != 's':
                        messagebox.showerror("Error", "Connection Error, try again", parent=self.root)
                    else:
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win, text='Reset Password', font=("TkDefaultFont", 13, 'bold'), bg="#3f51b5", fg="white")
                        title.pack(side=TOP, fill=X)
                        lbl_reset=Label(self.forget_win, text="Enter OTP Sent on Registered Email",font=("TkDefaultFont", 13, 'bold'))
                        lbl_reset.place(x=20, y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("TkDefaultFont", 13, 'bold'),bg='lightyellow')
                        txt_reset.place(x=20, y=100, width=250, height=30)
                        self.btn_reset = Button(self.forget_win, text="SUBMIT", command=self.validate_otp, state=NORMAL, font=("TkDefaultFont", 13, 'bold'),bg='lightblue')
                        self.btn_reset.place(x=280, y=100, width=100, height=30)

                        lbl_new_pass = Label(self.forget_win, text='New Password', font=("TkDefaultFont", 13, 'bold'))
                        lbl_new_pass.place(x=20, y=160)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=("TkDefaultFont", 13, 'bold'), bg='lightyellow')
                        txt_new_pass.place(x=20, y=190, width=250, height=30)

                        lbl_c_pass = Label(self.forget_win, text="Confirm Password",font=("TkDefaultFont", 13, 'bold'))
                        lbl_c_pass.place(x=20, y=225)
                        txt_c_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, font=("TkDefaultFont", 13, 'bold'),bg='lightyellow')
                        txt_c_pass.place(x=20, y=255, width=250, height=30)

                        self.btn_update = Button(self.forget_win, text="Update", command=self.update_password, state=DISABLED ,font=("TkDefaultFont", 13, 'bold'),
                                                bg='lightblue')
                        self.btn_update.place(x=150, y=300, width=100, height=30)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to1 : {str(ex)}", parent=self.root)

    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_conf_pass.get() == "":
            messagebox.showerror("Error", "Password is required", parent=self.forget_win)
        elif self.var_new_pass.get() != self.var_conf_pass.get():
            messagebox.showerror("Error", "New Password & confirm password  should be same", parent=self.forget_win)
        else:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            print(len(self.employee_id.get()))
            try:
                cur.execute("Update employee set pass=? where eid=?", (self.var_new_pass.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success", "Password updated sucessfully", parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def validate_otp(self):
        if int(self.otp) == int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)

    def send_email(self, send_to):
        email_ =email_pass.email_
        pass_ = email_pass.pass_
        server = "smtp.naver.com"
        port= 587

        s=smtplib.SMTP(server, port)
        s.starttls() #tls를 사용해 모든 내용이 암호화 되도록 설정
        s.login(email_, pass_)

        self.otp = str(time.strftime("%H%M%S")+str(time.strftime("%S")))

        subject = 'IMS-Reset password OTP'
        message = f'<div>Dear Sir/Madam,</div>' \
                  f'<div>Your Reset OTP is {str(self.otp)}.</div>' \
                  f'<div>With Regards,</div><div>IMS Team</div>'
        mtype= 'html'

        msg = MIMEMultipart()
        msg['From'] = email_
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject # msg = MIMEMultipart()
        msg.attach(MIMEText(message, mtype))

        s.sendmail(email_, send_to, msg.as_string())

        chk=s.ehlo() #연결이 수립되는지 확인 연결이 수립되면 250을 반환#연결이 수립되는지 확인 연결이 수립되면 250을 반환
        if chk[0] == 250:
            return 's'
        else:
            return 'f'
        s.quit()

root=Tk()
obj = Login_System(root)
root.mainloop()

