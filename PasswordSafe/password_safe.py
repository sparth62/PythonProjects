from tkinter import *
import tkinter.messagebox as tmsg


def encrypt():
    plain_text =text.get()
    key1 = int(key1_entry.get())
    key2 = key2_entry.get()

    def ceaser(plain_text,key1):
        encrypt_text = ''
        for i in plain_text:
            if i in small:
                index = small.index(i)
                encrypt_text += small[index-key1]
            elif i in caps:
                index = caps.index(i)
                encrypt_text += caps[index-key1]
            elif i in digit:
                index = digit.index(i)
                encrypt_text += digit[index-key1]
            elif i in symbol:
                index = symbol.index(i)
                encrypt_text += symbol[index-key1]
            else:
                return 'Error'
        return encrypt_text

    def trans(plain_text, key2):
        matrix = []
        cnt = 0
        for i in range(6):
            matrix.append([])
            for j in range(5):
                matrix[i].append(plain_text[cnt])
                cnt+=1

        encrypt_text = ''
        for i in key2:
            k = int(i) - 1
            for j in range(6):
                encrypt_text += matrix[j][k]
        return encrypt_text

    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/']

    while len(plain_text) != 30:
        plain_text += 'x'

    for i in range(1001):
        plain_text = ceaser(plain_text,key1)
        plain_text = trans(plain_text,key2)

    a = tmsg.showinfo('Cipher text',plain_text)

def decrypt():
    plain_text =text.get()
    key1 = int(key1_entry.get())
    key2 = key2_entry.get()

    def ceaser(plain_text,key1):
        encrypt_text = ''
        for i in plain_text:
            if i in small:
                index = small.index(i)
                encrypt_text += small[(index+key1)%len(small)]
            elif i in caps:
                index = caps.index(i)
                encrypt_text += caps[(index+key1)%len(caps)]
            elif i in digit:
                index = digit.index(i)
                encrypt_text += digit[(index+key1)%len(digit)]
            elif i in symbol:
                index = symbol.index(i)
                encrypt_text += symbol[(index+key1)%len(symbol)]
            else:
                return 'Error'
        return encrypt_text

    def trans(plain_text, key2):
        matrix = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
        cnt = 0
        for i in key2:
            k = int(i) - 1
            for j in range(6):
                matrix[j][k] = plain_text[cnt]
                cnt+=1
			
        encrypt_text = ''
        for i in range(6):
            for j in range(5):
                encrypt_text += matrix[i][j]
        return encrypt_text

    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/']

    while len(plain_text) != 30:
        plain_text += 'x'

    for i in range(1001):
        plain_text = trans(plain_text,key2)
        plain_text = ceaser(plain_text,key1)
    
    a = tmsg.showinfo('Plain text',plain_text)

root = Tk()
root.geometry('300x100')
text_var=StringVar() 
key1_var=StringVar() 
key2_var=StringVar() 
textLabel = Label(root,text='TEXT')
textLabel.grid(row=0,column=0)
text = Entry(root, textvariable = text_var, width=30)
text.grid(row=0,column=1)
key1Label = Label(root,text='KEY1')
key1Label.grid(row=1,column=0)
key1_entry = Entry(root, textvariable = key1_var)
key1_entry.grid(row=1,column=1)
key2Label = Label(root,text='KEY2')
key2Label.grid(row=2,column=0)
key2_entry = Entry(root, textvariable = key2_var)
key2_entry.grid(row=2,column=1)
encrypt = Button(root,text = 'ENCRYPT',command = encrypt)
encrypt.grid(row=3,column=0)
decrypt = Button(root,text = 'DECRYPT',command = decrypt)
decrypt.grid(row=3,column=1)
root.mainloop()