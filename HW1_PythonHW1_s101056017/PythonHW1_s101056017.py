#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import random

Proj_name = "PythonHW1_s101056017 ID generator"
random.seed()

root = Tk(Proj_name)

sex = 0

sexOption = [1,2]
sexOptionBtn = []

locationOption = [
    # [ID,Location_name],
    ['F',"新北市"],
    ['A','臺北市'],
    ['B','臺中市'],
    ['C','基隆市'],
    ['D','臺南市'],
    ['E','高雄市'],
    ['G','宜蘭市'],
    ['H','桃園市'],
    ['I','嘉義市'],
    ['J','新竹縣'],
    ['K','苗栗縣'],
    ['M','南投縣'],
    ['N','彰化縣'],
    ['O','新竹市'],
    ['P','雲林縣'],
    ['Q','嘉義縣'],
    ['T','屏東縣'],
    ['U','花蓮縣'],
    ['V','臺東縣'],
    ['W','金門縣'],
    ['X','澎湖縣'],
    ['Z','連江縣'],
    ['L','臺中縣'],
    ['R','臺南縣'],
    ['S','高雄縣'],
    ['Y','陽明山管理局'],
]

locationLabel = Label(root,text="Location:")
hintLabel = Label(root,text="Generate ID randomly:")
locationList = Listbox(root,selectmode=SINGLE)
resultLabel = Label(root,text="")

for l in locationOption:
    locationList.insert(END,l[1])

sexFrame = Frame(root)

def clearSex():
    global sex
    sex = 0
    for b in sexOptionBtn:
        b['text'] = b['text'].replace("*","")

def setSexOpt(i):
    global sex
    clearSex()
    sex = sexOption[i]
    sexOptionBtn[i]['text'] = "%s*" % sexOptionBtn[i]['text']

maleBtn = Button(sexFrame,text="Man",command=lambda:setSexOpt(0))
sexOptionBtn.append(maleBtn)
femaleBtn = Button(sexFrame,text="Woman",command=lambda:setSexOpt(1))
sexOptionBtn.append(femaleBtn)

def clear():
    selected = locationList.curselection()
    if selected:
        locationList.selection_clear(selected[0])
    clearSex()

clearBtn = Button(root,height=1,text="Clear",command=clear)

def chk(alpha,sex_val):
    id=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num=[10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
    a2n=dict(zip(id, num))
    # alpha = random.choice(id)
    r = [sex_val]+random.sample(range(0, 10), 7)
    k = [ v*(8-i) for i,v in enumerate(r) ]
    chk = (a2n[alpha]/10)+(a2n[alpha]%10*9) + sum(k)
    chk = (10 - (chk % 10)) % 10
    return alpha+''.join(map(str, r))+str(chk)

def gen_digi():
    return random.randint(0,9)

def gen():
    selected = locationList.curselection()
    if selected:
        selected = selected[0]
    else:
        selected = random.randint(0,len(locationOption) - 1)
    locationChar = locationOption[selected][0]
    
    if sex:
        sex_val = sex
    else:
        sex_val = sexOption[random.randint(0,len(sexOption) - 1)]

    result = chk(locationChar,sex_val)

    # print(result,sex)
    resultLabel['text'] = result

genBtn = Button(root,text="Generate!",command=gen)

locationLabel.pack(side='top',fill=BOTH)
locationList.pack(side='top',fill=BOTH,expand=1)
sexFrame.pack(side='top',fill=BOTH)
maleBtn.pack(side='left',fill=BOTH,expand=1)
femaleBtn.pack(side='left',fill=BOTH,expand=1)
clearBtn.pack(side='top',fill=BOTH)
genBtn.pack(side='top',fill=BOTH)
hintLabel.pack(side='top',fill=BOTH)
resultLabel.pack(side='top',fill=BOTH)

root.minsize(200, 400)

root.mainloop()
