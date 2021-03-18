import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, dialog
import os
import csv
import time
import math
import sys

lang=[['報告','选择csv文件','打开文件','打开csv档','搜寻','选取 储存txt','全选 储存txt','另存为...','清空','关闭','档案'],\
    ['Report','Choose csv File','Open file','Open csv file','Search','Save txt (Selected record)','Save txt (All records)','Save as...','Clean','Shut down','File'],\
        ['Reporte','Elija el archivo csv','Abrir Documento','Abrir archivo csv','Buscar','Guardar txt (Registro seleccionado)',\
            'Guardar txt (Todos los registros)','Guardar como...','Limpio','Apagar','El expediente']]

confirmlang=[]

with open(file='lang.txt',mode='r',encoding='utf-8')as lff:
    ook= lff.read()
    ook=ook[0]
print(ook)

if str(ook) in str(1):
    for i in lang[0]:
        confirmlang.append(i)
elif str(ook) in str(2):
    for i in lang[1]:
        confirmlang.append(i)
elif str(ook) in str(3):
    for i in lang[2]:
        confirmlang.append(i)


'''
import requests
response = requests.get("https://www.flaticon.com/svg/vstatic/svg/4336/4336621.svg?token=exp=1615867492~hmac=08288e4c795d93f2bc5932751b6d9b14")
with open("runico.ico","wb") as f:
    f.write(response.content)
    f.close()
    '''



default_dir=os.path.abspath(os.path.dirname(__file__))
print(default_dir)


win = tkinter.Tk()
scn_w, scn_h = win.maxsize()



win.title(confirmlang[0])  #報告
def set_win_center(win, curWidth='', curHight=''):

    if not curWidth:
        '''获取窗口宽度，默认200'''
        curWidth = win.winfo_width()
    if not curHight:
        '''获取窗口高度，默认200'''
        curHight = win.winfo_height()
    # print(curWidth, curHight)

    # 获取屏幕宽度和高度
    scn_w, scn_h = win.maxsize()
    # print(scn_w, scn_h)

    # 计算中心坐标
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    # print(cen_x, cen_y)

    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
    win.geometry(size_xy)
#set_win_center(win,1340,627)
#win.geometry("1340x627")   


print(math.floor(scn_h/21))
tree = ttk.Treeview(win,show="headings",height=math.floor(scn_h/21))
vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
#vsb.place(x=1324,height=627)
vsb.place(x=scn_w-17,height=scn_h-17)






placelist=[]
def clean():
    x=tree.get_children()
    for item in x:
        tree.delete(item)

def open_file():
    
    def printt():
        x=tree.get_children()
        for item in x:
            tree.delete(item)

        def heading():
            tree["columns"] = (your_list[0][0],your_list[0][1],your_list[0][2],your_list[0][3],your_list[0][4],\
                your_list[0][5],your_list[0][6],your_list[0][7],your_list[0][8],your_list[0][9],your_list[0][10])   
            for i in range(11):
                tree.column(your_list[0][i], width=120)
            for i in range(11):
                tree.heading(your_list[0][i], text=your_list[0][i]) 
            '''
            tree["columns"] = ("序号","设备编号","测试时间","警察姓名","警察编号","所属部门","驾驶员姓名","驾驶证号码","车牌号码","测试模式","测试结果")     # #定义列
            tree.column("序号", width=120)          # #设置列
            tree.column("设备编号", width=120)
            tree.column("测试时间", width=120)
            tree.column("警察姓名", width=120)
            tree.column("警察编号", width=120)
            tree.column("所属部门", width=120)
            tree.column("驾驶员姓名", width=120)
            tree.column("驾驶证号码", width=120)
            tree.column("车牌号码", width=120)
            tree.column("测试模式", width=120)
            tree.column("测试结果", width=120)

            tree.heading("序号", text="序号")      
            tree.heading("设备编号", text="设备编号")
            tree.heading("测试时间", text="测试时间")
            tree.heading("警察姓名", text="警察姓名")
            tree.heading("警察编号", text="警察编号")
            tree.heading("所属部门", text="所属部门")
            tree.heading("驾驶员姓名", text="驾驶员姓名")
            tree.heading("驾驶证号码", text="驾驶证号码")
            tree.heading("车牌号码", text="车牌号码")
            tree.heading("测试模式", text="测试模式")
            tree.heading("测试结果", text="测试结果")
            '''
        heading()

    
        rangg=len(your_list)-1
        for i in range(rangg):
            oooo=your_list[rangg-i][0],your_list[rangg-i][1],your_list[rangg-i][2],your_list[rangg-i][3],\
            your_list[rangg-i][4],your_list[rangg-i][5],your_list[rangg-i][6],your_list[rangg-i][7],your_list[rangg-i][8],your_list[rangg-i][9],your_list[rangg-i][10]

            tree.insert("", 0, text="",values=(oooo))
    global file_path
    global file_text
    file_path = filedialog.askopenfilename(title=confirmlang[1], initialdir=(os.path.isdir('')))#选择csv文件
    print('打开文件：', file_path)#confirmlang[2]
    if file_path is not None:
        with open(file=file_path,newline='') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            printt()
            tree.place(x=(scn_w-120*11)/2, y=0)
def open_file_gpk():
    def printt():
        x=tree.get_children()
        for item in x:
            tree.delete(item)


        rangg=len(your_list)-1
        for i in range(rangg):
            oooo=your_list[rangg-i][0],your_list[rangg-i][1],your_list[rangg-i][2],your_list[rangg-i][3],\
            your_list[rangg-i][4],your_list[rangg-i][5],your_list[rangg-i][6],your_list[rangg-i][7],your_list[rangg-i][8],your_list[rangg-i][9],your_list[rangg-i][10]

            tree.insert("", 0, text="",values=(oooo))
    global file_path
    global file_text
    
    file_path = filedialog.askopenfilename(title=confirmlang[1], initialdir=(os.path.expanduser(default_dir)))#u'选择csv文件'

    print('打开文件：', file_path)
    if file_path is not None:
        with open(file=file_path,newline='',encoding='gpk') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            printt()



def searchItem():
    def set_win2_center(win2, curWidth='', curHight=''):
        if not curWidth:
            '''获取窗口宽度，默认200'''
            curWidth = win2.winfo_width()
        if not curHight:
            '''获取窗口高度，默认200'''
            curHight = win2.winfo_height()
        # print(curWidth, curHight)

        # 获取屏幕宽度和高度
        scn_w, scn_h = win2.maxsize()
        # print(scn_w, scn_h)

        # 计算中心坐标
        cen_x = (scn_w - curWidth) / 2
        cen_y = (scn_h - curHight) / 2
        # print(cen_x, cen_y)

        # 设置窗口初始大小和位置
        size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
        win2.geometry(size_xy)
    
    def search():
        query = search_entry.get()
        selections = []
        for child in tree.get_children():
            for i in tree.item(child)['values']:
                if str(query) in str(i):
                    print(tree.item(child)['values'])
                    selections.append(child)
        print('search completed')
        tree.selection_set(selections)
        tree.see(selections[0])
    win2 = tkinter.Tk()
    set_win2_center(win2,300,100)
    #win2.geometry("300x100")   
    win2.attributes("-toolwindow", 2)
    
    search_entry = tkinter.Entry(win2, width=39)
    search_entry.place(x=10)
    btn = tkinter.Button(win2, text="search", width=10, height=1,command=search)
    btn.place(x=100,y=40)
    win2.title('Search')
    win2.mainloop()



'''
    child_id = tree.get_children()[-1]
    print(child_id)
    tree.focus(child_id)
    tree.selection_set(child_id)
    tree.see(child_id)'''

def selectItem():
    def ffw():

        c=1
        for item in tree.selection():
            if c==1:
                c=1
            else:
                ff.write('\n')
            c=c+1
            item_text = tree.item(item,"values")
            ff.write(str(item_text))
    e=1
    if os.path.exists('result.txt') is True:
        if not os.path.exists('result-%s.txt' % e):
            with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                ffw()
        else:
            while os.path.exists('result-%s.txt' % e):
                e=e+1
            with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                ffw()
    else:
        with open(file='result.txt',mode='w',newline='',encoding='gbk') as ff:
            ffw()


def selectallItem():
    def ffw():
        c=1
        for item in tree.selection():
            if c==1:
                c=1
            else:
                ff.write('\n')
            c=c+1
            item_text = tree.item(item,"values")
            ff.write(str(item_text))
    children = tree.get_children() 
    tree.selection_set(children)


    e=1
    if os.path.exists('result.txt') is True:
        if not os.path.exists('result-%s.txt' % e):
            with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                ffw()
        else:
            while os.path.exists('result-%s.txt' % e):
                e=e+1
            with open(file='result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                ffw()
    else:
        with open(file='result.txt',mode='w',newline='',encoding='gbk') as ff:
            ffw()


    

menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="打開(简体中文)csv檔", command=open_file_gpk)
filemenu.add_command(label=confirmlang[3], command=open_file)#"打開csv檔"
filemenu.add_separator()



filemenu.add_command(label=confirmlang[4], command=searchItem)#"搜寻"
filemenu.add_command(label=confirmlang[5], command=selectItem)#"選取 储存txt"
filemenu.add_separator()
filemenu.add_command(label=confirmlang[6], command=selectallItem)#"全選 储存txt"
filemenu.add_separator()
#filemenu.add_command(label=confirmlang[7], command=donothing)#"另存为..."
filemenu.add_command(label=confirmlang[8], command=clean)#"清空"
filemenu.add_separator()
filemenu.add_command(label=confirmlang[9], command=sys.exit)#"關閉"
menubar.add_cascade(label=confirmlang[10], menu=filemenu)#"檔案"
win.config(menu=menubar)


win.resizable(0,0)
win.attributes("-fullscreen", True)  #设置全屏窗口，没有Windows屏幕了
win.iconbitmap('runico.ico')
win.mainloop()