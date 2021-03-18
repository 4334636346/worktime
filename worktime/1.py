import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, dialog
import os
import csv
import time
import math
import sys
'''
import pandas as pda
ex=pda.read_excel("1.xls")
ex.to_csv("1.csv")
'''

with open(file='1.csv',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    your_list = list(reader)

'''
for i in range(3):
    print(your_list[3][10+i*15])
    '''



def main():
    for j in range(3):
        print(your_list[3][10+j*15])
        ff.write(your_list[3][10+j*15]+'\n')



        timelist=[]
        timelist2=[]
        for i in range(31):
            #print(your_list[12+i][2+j*15])
            if  your_list[12+i][2+j*15] in ':':
                #print(your_list[12+i][2+j*15])

                print('None morning in')
                ff.write('上午沒有打卡入\n')
                continue
            if  your_list[12+i][4+j*15] in ':':
                #print(your_list[12+i][2+j*15])
                print('None morning out')
                ff.write(your_list[12+i][1][:2]+'日,星期'+your_list[12+i][1][-1])
                ff.write('上午\n')
                ff.write(your_list[12+i][2+j*15])
                ff.write('打卡入\n')
                ff.write('上午沒有打卡出\n')
                continue
            x=float(your_list[12+i][4+j*15][:2])*60*60
            xx=float(your_list[12+i][4+j*15][3:5])*60
            xxx=float(your_list[12+i][4+j*15][6:])
            y=float(your_list[12+i][2+j*15][:2])*60*60
            yy=float(your_list[12+i][2+j*15][3:5])*60
            yyy=float(your_list[12+i][2+j*15][6:])
            xxxx=x+xx+xxx
            yyyy=y+yy+yyy


            timelist.append(xxxx-yyyy)
            '''
            z=(xxxx-yyyy)/3600
            zz=(z-int(z))*3600/60
            zzz=(zz-int(zz))*60
            '''
            #print(your_list[12+i][1],int(z),'小時',int(zz),'分',float(zzz),'秒')
        for i in range(31):
            #print(your_list[12+i][7+j*15])
            if  your_list[12+i][7+j*15] in ':':
                #print(your_list[12+i][2+j*15])
                #print('下午沒有打卡入')
                ff.write('下午沒有打卡入\n')
                continue
            if  your_list[12+i][9+j*15] in ':':
                #print(your_list[12+i][2+j*15])
                print('None afternoon out')
                ff.write(your_list[12+i][1][:2]+'日,星期'+your_list[12+i][1][-1])
                ff.write('下午')
                ff.write(your_list[12+i][7+j*15])
                ff.write('打卡入\n')
                ff.write('下午沒有打卡出\n')
                continue
            a=float(your_list[12+i][9+j*15][:2])*60*60
            aa=float(your_list[12+i][9+j*15][3:5])*60
            aaa=float(your_list[12+i][9+j*15][6:])
            b=float(your_list[12+i][7+j*15][:2])*60*60
            bb=float(your_list[12+i][7+j*15][3:5])*60
            bbb=float(your_list[12+i][7+j*15][6:])

            aaaa=a+aa+aaa
            bbbb=b+bb+bbb

            timelist2.append(aaaa-bbbb)
            '''
            c=(aaaa-bbbb)/3600
            cc=(c-int(c))*3600/60
            ccc=(cc-int(cc))*60
            '''
            
        ii=0
        for i in timelist:
            ii=ii+i
        for i in timelist2:
            ii=ii+i
        i=ii/3600
        #print(i)
        ii=(i-int(i))*3600/60
        #print(ii)
        iii=(ii-int(ii))*60
        #print(iii)
        print('總工時',int(i),'小時',int(ii),'分',float(iii),'秒')
        www='總工時'+str(int(i))+'小時'+str(int(ii))+'分'+str(float(iii))+'秒'
        ff.write(str(www))
        ff.write('\n')
        ff.write('\n')

e=1
if os.path.exists('result.txt') is True:
    if not os.path.exists('result-%s.txt' % e):
        with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
            main()
    else:
        while os.path.exists('result-%s.txt' % e):
            e=e+1
        with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
            main()
else:
    with open(file='result.txt',mode='w',newline='',encoding='gbk') as ff:
        main()
main()





'''
x=float(your_list[29][4][:2])*60*60
xx=float(your_list[29][4][3:5])*60
xxx=float(your_list[29][4][6:])
y=float(your_list[29][2][:2])*60*60
yy=float(your_list[29][2][3:5])*60
yyy=float(your_list[29][2][6:])
xxxx=x+xx+xxx
yyyy=y+yy+yyy
z=(xxxx-yyyy)/3600
zz=(z-int(z))*3600/60
zzz=(zz-int(zz))*60

print(int(z),'小時',int(zz),'分',float(zzz),'秒')

'''
