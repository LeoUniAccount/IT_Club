import tkinter as tk

expression =  ""

# press function
def press(num):
    global expression

    #add the word to the expression
    expression  = expression + str(num)

    equation.set(expression)


# clear function
def clear():
    global expression

    expression = ""

    equation.set(expression)

def backspace():
    global expression

    expression = expression[:-1]

    equation.set(expression)

def calculate():

    try :
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression= ""
    except:
        
        equation.set('error')
        expression=""
        
        

if __name__ == "__main__":
    root = tk.Tk() #making instance of tkinter tk class

    root.configure(background="black") #setting the background
    root.geometry("265x150") # setting the gui window size
    root.title("Calculator using Tkinter") # set title
    
    #equation
    equation = tk.StringVar()

    expression_field = tk.Entry(root,textvariable=equation)

    expression_field.grid(columnspan=4,ipadx=70)

    # ( ) Clear back space
    button_left_bracket = tk.Button(root,text="(",fg='black',bg='white',command=lambda: press('('),height=1,width=7)
    button_right_bracket = tk.Button(root,text=")",fg='black',bg='white',command=lambda: press(')'),height=1,width=7)
    button_clear = tk.Button(root,text="Clear",fg='black',bg='white',command=lambda: clear(),height=1,width=7)
    button_backspace= tk.Button(root,text="CE",fg='black',bg='white',command=lambda: backspace(),height=1,width=7)

    # 7 8 9 /
    button7 = tk.Button(root,text="7",command=lambda: press(7),fg='black',bg='white', height=1,width=7)
    button8 = tk.Button(root,text="8",command=lambda: press(8),fg='black',bg='white', height=1,width=7)
    button9 = tk.Button(root,text="9",command=lambda: press(9),fg='black',bg='white', height=1,width=7)
    button_divide = tk.Button(root,text="/",command=lambda: press('/'),fg='black',bg='white', height=1,width=7)

    # 4 5 6 *
    button4 = tk.Button(root,text="4",command=lambda: press(4),fg='black',bg='white', height=1,width=7)
    button5 = tk.Button(root,text="5",command=lambda: press(5),fg='black',bg='white', height=1,width=7)
    button6 = tk.Button(root,text="6",command=lambda: press(6),fg='black',bg='white', height=1,width=7)
    button_multiply = tk.Button(root,text="*",command=lambda: press('*'),fg='black',bg='white', height=1,width=7)

    # 1 2 3 -
    button1 = tk.Button(root,text="1",command=lambda: press(1),fg='black',bg='white', height=1,width=7)
    button2 = tk.Button(root,text="2",command=lambda: press(2),fg='black',bg='white', height=1,width=7)
    button3 = tk.Button(root,text="3",command=lambda: press(3),fg='black',bg='white', height=1,width=7)
    button_subtract = tk.Button(root,text="-",command=lambda: press('-'),fg='black',bg='white', height=1,width=7)

    # 0 . = +   
    button0 = tk.Button(root,text="0",command=lambda: press(0),fg='black',bg='white', height=1,width=7)
    button_decimal = tk.Button(root,text=".",command=lambda: press("."),fg='black',bg='white', height=1,width=7)
    button_equals = tk.Button(root,text="=",command=lambda: calculate(),fg='black',bg='white', height=1,width=7)
    button_add = tk.Button(root,text="+",command=lambda: press('+'),fg='black',bg='white', height=1,width=7)


    # placing the buttons
    button_left_bracket.grid(row=2,column=0)
    button_right_bracket.grid(row = 2, column=1)
    button_clear.grid(row=2,column=2)
    button_backspace.grid(row = 2, column=3)

    button7.grid(row=3,column=0)
    button8.grid(row=3,column=1)
    button9.grid(row=3,column=2)
    button_divide.grid(row=3,column=3)

    button4.grid(row=4,column=0)
    button5.grid(row=4,column=1)
    button6.grid(row=4,column=2)
    button_multiply.grid(row=4,column=3)

    button1.grid(row=5,column=0)
    button2.grid(row=5,column=1)
    button3.grid(row=5,column=2)
    button_subtract.grid(row=5,column=3)

    button0.grid(row=6,column=0)
    button_decimal.grid(row=6,column=1)
    button_equals.grid(row=6,column=2)
    button_add.grid(row=6,column=3)

    root.mainloop() # run this to keep the code up