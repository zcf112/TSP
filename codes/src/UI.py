from tkinter import *
from tkinter import ttk

from src.fun import fun
from src.tsp import TSP


class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        lf = ttk.Labelframe(self.master,
                            text='请选择参数：群体规模(0-500)，交叉概率(0.2-0.4)，变异概率(0.01-0.08)，遗传代数(0-300)',
                            padding=20)
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 四个entry
        self.entry = []
        default = ["200", "0.7", "0.1", "500"]
        for i in range(4):
            self.entry.append(ttk.Entry(lf, width=4))
            self.entry[i].insert(0, default[i])
            self.entry[i].pack(side=LEFT)

        ttk.Button(lf, text='开始', command=self.start).pack(side=LEFT)

    def start(self):
        # 调用遗传算法
        tspResult = TSP(self.entry[0].get(), self.entry[1].get(), self.entry[2].get())
        tspResult.set()
        result, title = tspResult.evolution(self.entry[3].get())
        i = 0
        for bestresult in result:
            fun(bestresult, title[i], i)
            i += 1
            w = Label(self)
            bm = PhotoImage(file='temp.png')
            w.x = bm
            w['image'] = bm
            w.grid(row=0, column=2)
            self.update()
        # P.Print();
