from tkinter import *

def login():
    def start():
            #calculator
        def calculator():
            window5=Tk()
            window5.title("calculator")
            window5.geometry("600x600")
        
            #def 1
            def calculatorbuttondef1():
                try:
                    value1 = int(calculatorentry1.get()) + int(calculatorentry2.get())
                    calculatorlabel1 = Label(window5, text=value1)
                    calculatorlabel1.pack()
                except ValueError:
                    calculatormessagebox1 = messagebox.showerror("value error","you enterd value is not an integer")
                    calculatormessagebox1.pack()

            #def2
            def calculatorbuttondef2():
                try:
                    value2 = int(calculatorentry1.get()) - int(calculatorentry2.get())
                    calculatorlabel2 = Label(window5, text=value2)
                    calculatorlabel2.pack()
                except ValueError:
                    errorlabel2 = Label(window5 , text="value error")
                    errorlabel2.pack()

            #def3       
            def calculatorbuttondef3():
                try:
                    value3 = int(calculatorentry1.get()) * int(calculatorentry2.get())
                    calculatorlabel3 = Label(window5, text=value3)
                    calculatorlabel3.pack()
                except ValueError:
                    errorlabel3 = Label(window5 , text="value error")
                    errorlabel3.pack()

            #def4      
            def calculatorbuttondef4():
                try:
                    value4 = int(calculatorentry1.get()) / int(calculatorentry2.get())
                    calculatorlabel4 = Label(window5, text=value4)
                    calculatorlabel4.pack()
                except ValueError:
                    errorlabel4 = Label(window5 , text="value error")
                    errorlabel4.pack()        
            #entry box
            calculatorentry1 = Entry(window5)
            calculatorentry2 = Entry(window5)

            #button
            calculatorbutton1 = Button(window5 , text="+" ,command=calculatorbuttondef1)
            calculatorbutton2 = Button(window5 , text="-" ,command=calculatorbuttondef2)
            calculatorbutton3 = Button(window5 , text="*" ,command=calculatorbuttondef3)
            calculatorbutton4 = Button(window5 , text="/" ,command=calculatorbuttondef4)
        
            #position
            calculatorentry1.place(x=10,y=50)
            calculatorentry2.place(x=10,y=50)
            
            #packing
            calculatorentry1.pack()
            calculatorentry2.pack()
            calculatorbutton1.pack()
            calculatorbutton2.pack()
            calculatorbutton3.pack()
            calculatorbutton4.pack()

            window5.mainloop()
        #turtle tool
        def turtle_program():
            window3 = Tk()
            window3.title("turtle program")
            window3.geometry("600x600")
            
            #turtle selection
            buttonturtle1 = Button(window3,text="love",width=50)#command not added
            turtlelabel = Label(window3, text="select a turtle program")

            #packing section
            turtlelabel.pack()
            buttonturtle1.pack()
            
            window3.mainloop()#window3 main loop
        #odd or even program
        def odd_or_even():
            #finding_def
            def find_even_or_odd():
                try:
                    num = int(entry.get())
                    if num % 2 == 0:
                        result_label.config(text=f"{num} is even")
                    else:
                        result_label.config(text=f"{num} is odd")
                except ValueError:
                    result_label.config(text="invalid input ,enter a valid number")
                
            window4 = Tk()
            window4.title("odd or even cheker")
            window4.geometry("600x600")
    
            #create a label and entry widget for user input
            input_label=Label(window4, text = "enter a number")
            input_label.pack()
            entry = Entry(window4)
            entry.pack()

            #create button to check odd or even
            check_button = Button(window4, text="check" ,command=find_even_or_odd)
            check_button.pack()

            #create a label to dis play the result
            result_label=Label(window4, text="")
            result_label.pack()

            #start the tkinter odd or even finder main loop
            window4.mainloop()
        
        window2 = Tk()
        window2.title("main screen")
        window2.geometry("600x600")
        label1 = Label(window2, text="what tool are you want" ,fg="blue")
        buttonturtle = Button(window2, text="turtle" ,width=50 ,command=turtle_program)
        buttonoddoreven = Button(window2, text="find odd or even ",width=50, command=odd_or_even)
        buttoncalculator = Button(window2, text="calculator" , width=50 ,command=calculator)
        #packing section
        label1.pack()
        buttonoddoreven.pack()
        buttonturtle.pack()
        buttoncalculator.pack()
        
        #mainloop starting    
        window2.mainloop()
    
    username = loginentry1.get()   
    password = loginentry2.get()        
        
    if username == "rhithik" and password == "2006":
        logbutton =Button(window1,text="start" ,command=start)
        logbutton.pack()
    else:
        print("wrong user name or password")
                
                  
                        
window1 = Tk()
window1.title("login")
window1.geometry("600x600")

#user name
loginentry1 = Entry()
#password
loginentry2 = Entry()

loginbutton = Button(window1, text="login" , command=login)

loginentry1.pack()
loginentry2.pack()
loginbutton.pack()


window1.mainloop()
