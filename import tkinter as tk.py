import tkinter as tk

def is_valid_input(char):
    return char.isdigit() or char == ""
#檢查是否為數字或空字串，數字或空字串為ture，其餘為false

def validate_input(new_text):
    return all(char.isdigit() for char in new_text)
#使新文本也能使用此功能

def clear_input():
    systemVar.set("")
#清除空白框

system = tk.Tk()
system.geometry("700x600") #視窗大小
system.title("統一發票兌獎系統") #視窗標題

labell = tk.Label(system, text="112年9-10月發票兌獎", fg="black", font=("新細明體", 19, "bold"))#在視窗中設定標籤
labell.place(x=10, y=0) #位置

systemVar = tk.StringVar() #創建空白框
systemLab = tk.Label(system, text="請輸入發票號碼:", font=("新細明體", 17, "bold"), pady=40)
systemLab.pack()

# 使用 validate 和 validatecommand 來限制只能輸入數字
validate_cmd = system.register(validate_input)
systemEntry = tk.Entry(system, textvariable=systemVar, validate="key", validatecommand=(validate_cmd, "%P"))
systemEntry.pack()

clearBut = tk.Button(system, text="清除", command=clear_input) #清除按鈕
clearBut.place(x=420, y=160)

errorlab = tk.Label(system, text="", font=("新細明體", 12), fg="red") #錯誤訊息提示
errorlab.pack()

def systemNum():
    num1 = '72054514'
    num2 = '92488868'
    num3 = ['98111935', '57355279', '74926745']
    input_text = systemVar.get()
    
    if not input_text.isdigit() or len(input_text) != 8: #如果不是數字或8位數的格式就報錯
        errorlab.config(text="格式錯誤，請輸入8位數字的發票號碼")
        result.config(text="")
        tax.config(text="")
    elif systemVar.get() == num1:
        result.config(text="恭喜對中1000萬元")
        tax.config(text="印花稅為4萬元")
        errorlab.config(text="")
    elif systemVar.get() == num2:
        result.config(text="恭喜對中4萬元")
        tax.config(text="印花稅為8000元") 
        errorlab.config(text="")
    elif systemVar.get() in num3:  
        result.config(text="恭喜對中20萬元")
        tax.config(text="印花稅為800元")
        errorlab.config(text="")
    elif systemVar.get()[-7:] == num3[-7:]:
        result.config(text="恭喜對中4萬元")
        tax.config(text="印花稅為160元")
        errorlab.config(text="")
    elif systemVar.get()[-6:] == num3[-6:]:
        result.config(text="恭喜對中1萬元")
        tax.config(text="印花稅為40元")
        errorlab.config(text="")
    elif systemVar.get()[-5:] == num3[-5:]:
        result.config(text="恭喜對中4000元")
        tax.config(text="印花稅為16元")
        errorlab.config(text="")
    elif systemVar.get()[-4:] == num3[-4:]:
        result.config(text="恭喜對中1000元")
        tax.config(text="印花稅為4元")
        errorlab.config(text="")
    elif systemVar.get()[-3:] == num3[-3:]:
        result.config(text="恭喜對中200元")
    elif systemVar.get() != num1 and num2 and num3:
        result.config(text="沒中獎")
        tax.config(text="")
        errorlab.config(text="")
systemBut = tk.Button(system, text="查詢", command=systemNum) #創建按鍵and引入data
systemBut.place(x=330, y=160) #位置
result = tk.Label(system, text="", fg="black", font=("新細明體", 20, "bold"))#對中金額
result.place(x=210, y=250) #位置
tax = tk.Label(system, text="", font=("新細明體", 17))#印花稅
tax.place(x=210, y=290) #位置
system.mainloop()