from tkinter import Tk,Radiobutton, Button,Label,StringVar,IntVar,Entry
class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="Sky blue")
        window.geometry("375x250")
        window.resizable(width=False,height=False)


        self.meal_cost = StringVar()
        self.tip_percent = StringVar()
        self.tip = StringVar()
        self.total_cost = StringVar()


        tip_percents = Label(window,text ="Tip Percentages",bg="purple",fg="white")
        tip_percents.grid(column=0,row=0,padx=15)

        bill_amount = Label(window,text ="Bill Amount",bg="black",fg="white")
        bill_amount.grid(column=1,row=0,padx=15)

        bill_amount_entry = Entry(window,textvariable =self.meal_cost,width =14)
        bill_amount_entry.grid(column=2,row=0)

        five_percent_tip = Radiobutton(window,text="5%",variable = self.tip_percent,value = 5,tristatevalue=0)
        five_percent_tip.grid(column=0,row=1)
        ten_percent_tip = Radiobutton(window,text="10%",variable = self.tip_percent,value = 10,tristatevalue=0)
        ten_percent_tip.grid(column=0,row=2)
        fifteen_percent_tip = Radiobutton(window,text="15%",variable = self.tip_percent,value = 15,tristatevalue=0)
        fifteen_percent_tip.grid(column=0,row=3)

        tip_amount_lb1 = Label(window,text ="Tip Amount",bg="brown" ,fg="white")
        tip_amount_lb1.grid(column=1,row=3,padx=15)
        tip_amount_entry = Entry(window,textvariable =self.tip,width =14)
        tip_amount_entry.grid(column=2,row=3)

        total_cost_lb1 = Label(window,text ="Total cost",bg="blue",fg="white")
        total_cost_lb1.grid(column=1,row=5,padx=15)
        bill_amount_value = Entry(window,textvariable=self.total_cost,width =14)
        bill_amount_value.grid(column=2,row=5)

        calculate_btn = Button(window,text="Calculate",bg="green",fg="white",command=self.Calculate_Tip)
        calculate_btn.grid(column=1,row=8,padx=15)

        clear_btn = Button(window,text="Clear",bg="black",fg="white",command=self.Clear)
        clear_btn.grid(column=2,row=8)


        window.mainloop()

    def Calculate_Tip(self):
        value1 = float(self.meal_cost.get())
        value2 = float(self.tip_percent.get()) / 100
        value3 = value1 * value2
        self.tip.set(value3)

        finalbill = value1 + value3
        self.total_cost.set(finalbill)

    def Clear(self):
        self.tip.set("")
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip_percent.set("")

TipCalculator()
                #self.arg = arg
