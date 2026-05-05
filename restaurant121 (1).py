from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1000x700+600+400")
        self.root.configure(bg="#EEE9DA")

        # Variables
        self.username = StringVar()
        self.password = StringVar()

        # Title
        title = Label(self.root, text="Restaurant Billing System", padx=600, font=("Arial Black", 25), bg="sky blue", fg="black")
        title.pack(pady=20)

        # Username label and entry
        username_label = Label(self.root, text="Username", font=("Arial Black", 25), bg="white")
        username_label.pack(pady=20)
        username_entry = Entry(self.root, textvariable=self.username, font=("Arial Black", 25), bd=5)
        username_entry.pack(pady=20)

        # Password label and entry
        password_label = Label(self.root, text="Password", font=("Arial Black", 25), bg="white")
        password_label.pack(pady=20)
        password_entry = Entry(self.root, textvariable=self.password, font=("Arial Black", 25), show="*", bd=5)
        password_entry.pack(pady=20)

        # Login button
        login_button = Button(self.root, text="Login", font=("Arial Black", 25), bg="sky blue", fg="black", command=self.login)
        login_button.pack(pady=40)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        # Hardcoded username and password for simplicity
        if user == "harsh" and pwd == "8957":
            self.root.destroy()  # Close the login window
            self.open_billing_app()  # Open the billing system
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    def open_billing_app(self):
        root = Tk()  # Create a new Tkinter window
        app = Bill_App(root)  # Open the billing system
        root.mainloop()

# Existing Bill_App class
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.configure(bg="#f2f4f3")
        self.root.title("Restaurant Billing System")
        title = Label(self.root, text="Restaurant Billing System", bd=10, relief=RIDGE, font=("Sitka Small Semibold", 26), bg="#BEAEE2", fg="black").pack(fill=X)

        # =====================variables=========================
        self.samosa = IntVar()
        self.paneertikka = IntVar()
        self.butterroti = IntVar()
        self.manchurian = IntVar()
        self.papdichaat = IntVar()
        self.tomatosoup = IntVar()
        self.masalapapad = IntVar()

        self.vegburger = IntVar()
        self.pasta = IntVar()
        self.basmathirice = IntVar()
        self.paneermasala = IntVar()
        self.sahipaneer = IntVar()
        self.pizza = IntVar()
        self.daalmakhani = IntVar()

        self.noodles = IntVar()
        self.aalutikki = IntVar()
        self.dahivada = IntVar()
        self.pavbhaji = IntVar()
        self.bhelpuri = IntVar()
        self.soup = IntVar()
        self.pakora = IntVar()

        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()

        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()

        # Payment Option Variables
        self.payment_method = StringVar()
        self.cash_amount = StringVar()
        self.card_number = StringVar()

        # =====================Customer details section===================
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#eee2df", fg="#6C3483", relief=GROOVE, bd=10)
        details.place(x=0, y=60, relwidth=1)
        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#eee2df", fg="#6C3483").grid(row=0, column=0, padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=9)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#eee2df", fg="#6C3483").grid(row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=9)

        bill_name = Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#eee2df", fg="#6C3483").grid(row=0, column=4, padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=9)

        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#eee2df",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=0,y=125,height=390,width=290)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.samosa).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.paneertikka).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Butter Roti",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.butterroti).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Manchurian",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.manchurian).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.papdichaat).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.tomatosoup).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.masalapapad).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#eee2df",fg="#6C3483")
        grocery.place(x=300,y=125,height=390,width=290)

        item8=Label(grocery,text="Veg Burger",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.vegburger).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Basmathi Rice",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.basmathirice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Paneer Masala",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.paneermasala).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Sahi Paneer",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sahipaneer).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Pizza",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pizza).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Daal Makhani",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.daalmakhani).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#eee2df",fg="#6C3483")
        hygine.place(x=600,y=125,height=390,width=290)

        item15=Label(hygine,text="Noodles",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.noodles).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Aalu Tikki ",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.aalutikki).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.dahivada).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.pavbhaji).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.bhelpuri).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Soup",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soup).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Pokara",font=("Arial Black",11),bg="#eee2df",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.pakora).grid(row=6,column=1,padx=10)

        # =====================Bill Area======================================================
        bill_area = Frame(self.root, bd=10, relief=GROOVE, bg="#eee2df")
        bill_area.place(x=900, y=125, width=290, height=535)

        bill_title = Label(bill_area, text="Bill Area", font=("Arial Black", 15), bd=7, relief=GROOVE, bg="#eee2df", fg="#6C3483").pack(fill=X)
        scroll_y = Scrollbar(bill_area, orient=VERTICAL)
        self.txtarea = Text(bill_area, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================================= Menu Card =======================================
        self.menu_card = LabelFrame(self.root, text="Menu Card", font=("Arial Black", 9), 
                                    bg="#eee2df", fg="#6C3483", relief=GROOVE, bd=9)
        self.menu_card.place(x=1200, y=125, width=330, height=535)

        menu_title = Label(self.menu_card, text="Item Name\t\tPrice", font=("Arial Black", 9), 
                           bg="#eee2df", fg="#6C3483").grid(row=0, column=0, padx=0, pady=0)

        # List of items and prices
        menu_items = [("Samosa","\t10"), ("Paneer Tikka", "40"), ("Butter Roti", "10"),
                      ("Manchurian", "40"), ("Papdi Chaat", "30"), ("Tomato Soup", "60"),
                      ("Masala Papad", "15"), ("Veg Burger", "42"), ("Pasta","\t120"),
                      ("Basmathi Rice", "160"),("Paneer Masala", "113"), ("Sahi Paneer", "55"),
                      ("Pizza","\t76"), ("Daal Makhani", "480"), ("Noodles","\t30"),
                      ("Aalu Tikki", "180"), ("Dahi Vada", "130"), ("Pav Bhaji","\t500"),
                      ("Bhel Puri", "\t85"), ("Soup", "\t100"), ("Pakora", "\t20")
        ]

        # Dynamically adding the menu items and prices to the menu card
        for i, (item, price) in enumerate(menu_items, start=1):
            Label(self.menu_card, text=f"{item}\t\t{price} Rs", font=("Arial Black", 9), 
                  bg="#eee2df", fg="#6C3483").grid(row=i, column=0, padx=8, pady=0)

 # Billing menu frame
        billing_menu = LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#BE9FE1", fg="white")
        billing_menu.place(x=0, y=660, relwidth=1, height=135)
        
        total_snacks=Label(billing_menu,text="Total Starter Price",font=("Arial Black",11),bg="#BE9FE1",fg="black").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=1.5,textvariable=self.total_sna).grid(row=0,column=1,padx=7,pady=7)

        total_grocery=Label(billing_menu,text="Total Main Course Price",font=("Arial Black",11),bg="#BE9FE1",fg="black").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=1.5,textvariable=self.total_gro).grid(row=1,column=1,padx=7,pady=7)


        total_hygine=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#BE9FE1",fg="black").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=1.5,textvariable=self.total_hyg).grid(row=2,column=1,padx=7,pady=7)

        tax_snacks=Label(billing_menu,text="Total Amount",font=("Arial Black",11),bg="#BE9FE1",fg="black").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=1.5,textvariable=self.a).grid(row=0,column=3,padx=7,pady=7)

        tax_grocery=Label(billing_menu,text="Service Tax",font=("Arial Black",11),bg="#BE9FE1",fg="black").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=1.5,textvariable=self.b).grid(row=1,column=3,padx=7,pady=7)


        # =====================Payment Section=========================
        payment_frame = LabelFrame(self.root, text="Payment Details", font=("Arial Black", 12), bg="#eee2df", fg="#6C3483", relief=GROOVE, bd=10)
        payment_frame.place(x=0, y=515, height=147, width=890)

        # Payment Method Selection
        pay_label = Label(payment_frame, text="Select Payment Method", font=("Arial Black", 14), bg="#eee2df", fg="#6C3483").grid(row=0, column=0, padx=20, pady=10)
        pay_method_cash = Radiobutton(payment_frame, text="Cash", variable=self.payment_method, value="Cash", font=("Arial Black", 12), bg="#eee2df", fg="#6C3483", command=self.show_payment_field).grid(row=0, column=1, padx=20, pady=10)
        pay_method_card = Radiobutton(payment_frame, text="Debit Card", variable=self.payment_method, value="Debit Card", font=("Arial Black", 12), bg="#eee2df", fg="#6C3483", command=self.show_payment_field).grid(row=0, column=2, padx=20, pady=10)

        # Cash Amount or Debit Card Number Input Fields                                 
        self.pay_label_dynamic = Label(payment_frame, text="Enter Cash Amount", font=("Arial Black", 14), bg="#eee2df", fg="#6C3483")
        self.pay_label_dynamic.grid(row=1, column=0, padx=20, pady=10)
        self.pay_entry_dynamic = Entry(payment_frame, borderwidth=2, width=30, textvariable=self.cash_amount)
        self.pay_entry_dynamic.grid(row=1, column=1, padx=20, pady=10)

        button_frame = Frame(self.root, bd=7, relief=GROOVE,bg="#BE9FE1")
        button_frame.place(x=875, y=685, width=605, height=95)

        total_button = Button(button_frame, text="Total", font=("Arial Black", 16), bg="#eee2df", fg="black", command=self.total).grid(row=0, column=0, padx=12)
        generate_bill_button = Button(button_frame, text="Generate Bill", font=("Arial Black", 16), bg="#eee2df", fg="black", command=self.bill_area).grid(row=0, column=1, padx=10, pady=15)
        pay_button = Button(button_frame, text="Pay", font=("Arial Black", 16), bg="#eee2df", fg="black", command=self.pay).grid(row=0, column=2, padx=10,pady=15)
        clear_button = Button(button_frame, text="Clear", font=("Arial Black", 16), bg="#eee2df", fg="black", command=self.clear_data).grid(row=0, column=3, padx=10,pady=15)
        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 16), bg="#eee2df", fg="black", command=self.exit1).grid(row=0, column=4, padx=10,pady=15)
        self.intro()
        

    # Function to show payment field based on payment method selected
    def show_payment_field(self):
        if self.payment_method.get() == "Cash":
            self.pay_label_dynamic.config(text="Enter Cash Amount")
            self.pay_entry_dynamic.config(textvariable=self.cash_amount)
        else:
            self.pay_label_dynamic.config(text="Enter Debit Card Number")
            self.pay_entry_dynamic.config(textvariable=self.card_number)
       
    # Function to calculate totals
    def total(self):
        if (self.c_name.get=="" or self.phone.get()==""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
        self.sm=self.samosa.get()*10
        self.no=self.paneertikka.get()*40
        self.la=self.butterroti.get()*10
        self.ore=self.manchurian.get()*40
        self.mu=self.papdichaat.get()*30
        self.si=self.tomatosoup.get()*60
        self.na=self.masalapapad.get()*15
        total_starter_price=(self.sm+ self.no+ self.la+ self.ore+ self.mu+ self.si+ self.na)
        self.total_sna.set(total_starter_price)

        self.at=self.vegburger.get()*42
        self.pa=self.pasta.get()*120
        self.oi=self.basmathirice.get()*113
        self.ri=self.paneermasala.get()*160
        self.su=self.sahipaneer.get()*55
        self.te=self.pizza.get()*480
        self.da=self.daalmakhani.get()*76
        total_maincourse_price=(self.at+ self.pa+ self.oi+ self.ri+ self.su+ self.te+ self.da)
    
        self.total_gro.set(total_maincourse_price)

        self.so=self.noodles.get()*30
        self.sh=self.aalutikki.get()*180
        self.cr=self.dahivada.get()*500
        self.lo=self.pavbhaji.get()*130
        self.fo=self.bhelpuri.get()*85
        self.ma=self.soup.get()*100
        self.sa=self.pakora.get()*20

        total_snacks_price=(self.so+ self.sh+ self.cr+ self.lo+ self.fo+ self.ma+ self.sa)

        self.total_hyg.set(total_snacks_price)
        self.a.set(total_starter_price+ total_maincourse_price+ total_snacks_price)
        self.b.set(round(total_starter_price+ total_maincourse_price+ total_snacks_price)*0.05)
        self.total_all_bill=(total_starter_price+ total_maincourse_price+ total_snacks_price+(round(total_starter_price+ total_maincourse_price+ total_snacks_price)*0.05))
        self.total_all_bil=(self.total_all_bill)
        


    # Function to generate bill area content
    def intro(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Restaurant\n")
        self.txtarea.insert(END, f"Bill No: {self.bill_no.get()}\n")
        self.txtarea.insert(END, f"Customer Name: {self.c_name.get()}\n")
        self.txtarea.insert(END, f"Phone No: {self.phone.get()}\n")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "Items\t\tQty\tPrice\n")
        self.txtarea.insert(END, "====================================\n")
    def bill_area(self):
        if self.samosa.get()!=0:
            self.txtarea.insert(END,f"Samosa\t\t {self.samosa.get()}\t{self.sm}\n")
        if self.paneertikka.get()!=0:
            self.txtarea.insert(END,f"Paneer Tikka\t\t {self.paneertikka.get()}\t{self.no}\n")
        if self.butterroti.get()!=0:
            self.txtarea.insert(END,f"Butter Roti\t\t {self.butterroti.get()}\t{self.la}\n")
        if self.manchurian.get()!=0:
            self.txtarea.insert(END,f"Manchurian\t\t {self.manchurian.get()}\t{self.ore}\n")
        if self.papdichaat.get()!=0:
            self.txtarea.insert(END,f"Papdi Chat\t\t {self.papdichaat.get()}\t{self.mu}\n")
        if self.tomatosoup.get()!=0:
            self.txtarea.insert(END,f"Tomato Soup\t\t {self.tomatosoup.get()}\t{self.si}\n")
        if self.masalapapad.get()!=0:
            self.txtarea.insert(END,f"Masala Papad\t\t {self.masalapapad.get()}\t{self.na}\n")
        if self.vegburger.get()!=0:
            self.txtarea.insert(END,f"Veg Burger\t\t {self.vegburger.get()}\t{self.at}\n")
        if self.pasta.get()!=0:
            self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
        if self.basmathirice.get()!=0:
            self.txtarea.insert(END,f"Basmati Rice\t\t {self.basmathirice.get()}\t{self.ri}\n")
        if self.paneermasala.get()!=0:
            self.txtarea.insert(END,f"Paneer Masala\t\t {self.paneermasala.get()}\t{self.oi}\n")
        if self.sahipaneer.get()!=0:
            self.txtarea.insert(END,f"Sahi Paneer\t\t {self.sahipaneer.get()}\t{self.su}\n")
        if self.pizza.get()!=0:
            self.txtarea.insert(END,f"Pizza\t\t {self.pizza.get()}\t{self.da}\n")
        if self.daalmakhani.get()!=0:
            self.txtarea.insert(END,f"Daal Makhani\t\t {self.daalmakhani.get()}\t{self.te}\n")
        if self.noodles.get()!=0:
            self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.so}\n")
        if self.aalutikki.get()!=0:
            self.txtarea.insert(END,f"Aalu Tikki\t\t {self.aalutikki.get()}\t{self.sh}\n")
        if self.dahivada.get()!=0:
            self.txtarea.insert(END,f"Dahi Vada\t\t {self.dahivada.get()}\t{self.lo}\n")
        if self.pavbhaji.get()!=0:
            self.txtarea.insert(END,f"Pav Bhaji\t\t {self.pavbhaji.get()}\t{self.cr}\n")
        if self.bhelpuri.get()!=0:
            self.txtarea.insert(END,f"Bhel Puri\t\t {self.bhelpuri.get()}\t{self.fo}\n")
        if self.soup.get()!=0:
            self.txtarea.insert(END,f"Soup\t\t {self.soup.get()}\t{self.ma}\n")
        if self.pakora.get()!=0:
            self.txtarea.insert(END,f"Pakora\t\t {self.pakora.get()}\t{self.sa}\n")
        self.txtarea.insert(END,f"--------------------------------------\n")
        if self.a.get()!="0.0 Rs":
            self.txtarea.insert(END,f"Total Amount : {self.a.get()}\n")
        if self.b.get()!="0.0 Rs":
            self.txtarea.insert(END,f"service Tax : {self.b.get()}\n")
            self.txtarea.insert(END,f"------------------------------------\n")
            self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")

    # Function to validate payment and display success message
    def pay(self):
        if self.payment_method.get() == "Cash":
            try:
                cash = int(self.cash_amount.get())
                if cash >= self.total_all_bil:
                    change = cash - self.total_all_bil
                    messagebox.showinfo("Payment Successful", f"Payment of Rs {cash} received.\nChange: Rs {change}")
                else:
                    messagebox.showerror("Error", "Insufficient Cash!")
            except ValueError:
                messagebox.showerror("Error", "Invalid Cash Amount!")
        elif self.payment_method.get() == "Debit Card":
            card_num = self.card_number.get()
            if len(card_num) == 16 and card_num.isdigit():
                messagebox.showinfo("Payment Successful", "Payment made successfully with Debit Card.")
            else:
                messagebox.showerror("Error", "Invalid Card Number!")
        else:
            messagebox.showerror("Error", "Please select a payment method!")

    # Function to clear data
    def clear_data(self):
        self.txtarea.delete("1.0", END)
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.samosa.set("")
        self.paneertikka.set("")
        self.butterroti.set("")
        self.manchurian.set("")
        self.papdichaat.set("")
        self.tomatosoup.set("")
        self.masalapapad.set("")
        self.vegburger.set("")
        self.pasta.set("")
        self.basmathirice.set("")
        self.paneermasala.set("")
        self.sahipaneer.set("")
        self.pizza.set("")
        self.daalmakhani.set("")
        self.noodles.set("")
        self.aalutikki.set("")
        self.dahivada.set("")
        self.pavbhaji.set("")
        self.bhelpuri.set("")
        self.soup.set("")
        self.pakora.set("")
        self.total_sna.set("")
        self.total_gro.set("")
        self.total_hyg.set("")
        self.a.set("")
        self.b.set("")
        self.c.set("")
        self.c_name.set("")
        self.bill_no.set("")
        self.bill_no.set("")
        self.phone.set("")
        self.payment_method.set("")
        self.cash_amount.set("")
        self.card_number.set("")

    def exit1(self):
        self.root.destroy()
        

# Main Code to run the application
if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
