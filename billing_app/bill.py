from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x792+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gel=IntVar()
        self.body_lotion=IntVar()

        self.rice=IntVar()
        self.oil=IntVar()
        self.dal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        self.thumsup=IntVar()
        self.cocacola=IntVar()
        self.mazza=IntVar()
        self.frooti=IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_tax=StringVar()

        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=20,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bathsoap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bathsoap_txt=Entry(F2,width=10,textvariable=self.bath_soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        facecream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        facecream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        facewash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        facewash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hairspray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hairspray_txt=Entry(F2,width=10,textvariable=self.hair_spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hairgel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hairgel_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        bodylotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        bodylotion_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=10)

        oil_lbl=Label(F3,text="Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=10)

        dal_lbl=Label(F3,text="Dal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        dal_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=4,padx=10,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=3,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=3,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=4,padx=10,pady=10)

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=380)

        thumsup_lbl=Label(F4,text="Thums Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=6,padx=10,pady=10,sticky="w")
        thumsup_txt=Entry(F4,width=10,textvariable=self.thumsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=7,padx=10,pady=10)

        cocacola_lbl=Label(F4,text="Coca-Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=6,padx=10,pady=10,sticky="w")
        cocacola_txt=Entry(F4,width=10,textvariable=self.cocacola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=7,padx=10,pady=10)

        mazza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=6,padx=10,pady=10,sticky="w")
        mazza_txt=Entry(F4,width=10,textvariable=self.mazza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=7,padx=10,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=6,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=7,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=6,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=7,padx=10,pady=10)

        limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=6,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=7,padx=10,pady=10)

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 16 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=230)

        total_cosmetic_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=15,sticky="w")
        total_cosmetic_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=15)

        total_grocery_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=15,sticky="w")
        total_grocery_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=15)

        total_cold_drinks_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=15,sticky="w")
        total_cold_drinks_txt=Entry(F6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=15)

        cosmetic_tax_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=15,sticky="w")
        cosmetic_tax_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=15)

        grocery_tax_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=15,sticky="w")
        grocery_tax_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=15)

        cold_drinks_tax_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=15,sticky="w")
        cold_drinks_tax_txt=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=15)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=782,y=42,width=680,height=102)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=8,pady=5)
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=9,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=2,padx=9,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=9,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_bs_p=self.bath_soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.hair_spray.get()*180
        self.c_hg_p=self.hair_gel.get()*140
        self.c_bl_p=self.body_lotion.get()*180

        self.total_cosmetic_price=float(
                            self.c_bs_p+
                            self.c_fc_p+
                            self.c_fw_p+
                            self.c_hs_p+
                            self.c_hg_p+
                            self.c_bl_p
                            )
        self.cosmetic_price.set("Rs "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set("Rs "+str(self.c_tax))

        self.g_r_p=self.rice.get()*80
        self.g_o_p=self.oil.get()*180
        self.g_d_p=self.dal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150

        self.total_grocery_price=float(
                            self.g_r_p+
                            self.g_o_p+
                            self.g_d_p+
                            self.g_w_p+
                            self.g_s_p+
                            self.g_t_p
                            )
        self.grocery_price.set("Rs "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.20),2)
        self.grocery_tax.set("Rs "+str(self.g_tax))

        self.cd_t_p=self.thumsup.get()*85
        self.cd_c_p=self.cocacola.get()*80
        self.cd_m_p=self.mazza.get()*90
        self.cd_f_p=self.frooti.get()*95
        self.cd_s_p=self.sprite.get()*75
        self.cd_l_p=self.limca.get()*70

        self.total_cold_drinks_price=float(
                            self.cd_t_p+
                            self.cd_c_p+
                            self.cd_m_p+
                            self.cd_f_p+
                            self.cd_s_p+
                            self.cd_l_p
                            )
        self.cold_drinks_price.set("Rs "+str(self.total_cold_drinks_price))
        self.cd_tax=round((self.total_cold_drinks_price*0.15),2)
        self.cold_drinks_tax.set("Rs "+str(self.cd_tax))

        self.total_bill=float(
                            self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_cold_drinks_price+
                            self.c_tax+
                            self.g_tax+
                            self.cd_tax
                            )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t      Shreya Retail Shop\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n ==========================================================")
        self.txtarea.insert(END,f"\n Products\t\t\tQuantity\t\t\tPrice")
        self.txtarea.insert(END,f"\n ==========================================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs 0.0" and self.grocery_price.get()=="Rs 0.0" and self.cold_drinks_price.get()=="Rs 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()
            if self.bath_soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.bath_soap.get()}\t\t\tRs {self.c_bs_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t\tRs {self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t\tRs {self.c_fw_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t\t{self.hair_spray.get()}\t\t\tRs {self.c_hs_p}")
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t\t{self.hair_gel.get()}\t\t\tRs {self.c_hg_p}")
            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t\t{self.body_lotion.get()}\t\t\tRs {self.c_bl_p}")

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t\t{self.rice.get()}\t\t\tRs {self.g_r_p}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Oil\t\t\t{self.oil.get()}\t\t\tRs {self.g_o_p}")
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\n Dal\t\t\t{self.dal.get()}\t\t\tRs {self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t\tRs {self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t\tRs {self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t\tRs {self.g_t_p}")

            if self.thumsup.get()!=0:
                self.txtarea.insert(END,f"\n Thums Up\t\t\t{self.thumsup.get()}\t\t\tRs {self.cd_t_p}")
            if self.cocacola.get()!=0:
                self.txtarea.insert(END,f"\n Coca-Cola\t\t\t{self.cocacola.get()}\t\t\tRs {self.cd_c_p}")
            if self.mazza.get()!=0:
                self.txtarea.insert(END,f"\n Mazza\t\t\t{self.mazza.get()}\t\t\tRs {self.cd_m_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t\tRs {self.cd_f_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t\t{self.sprite.get()}\t\t\tRs {self.cd_s_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t\tRs {self.cd_l_p}")

            self.txtarea.insert(END,f"\n ==========================================================")
            if self.cosmetic_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax : {self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax : {self.grocery_tax.get()}")

            if self.cold_drinks_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Cold Drinks Tax : {self.cold_drinks_tax.get()}")

            self.txtarea.insert(END,f"\n ==========================================================")

            self.txtarea.insert(END,f"\n Total : Rs {self.total_bill}")
            self.txtarea.insert(END,f"\n ==========================================================")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. {self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            self.bath_soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.body_lotion.set(0)

            self.rice.set(0)
            self.oil.set(0)
            self.dal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            self.thumsup.set(0)
            self.cocacola.set(0)
            self.mazza.set(0)
            self.frooti.set(0)
            self.sprite.set(0)
            self.limca.set(0)

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()