import matplotlib.pyplot as plt
from pylab import mpl  # 解决中文方块乱码

from src.tsp import x, y

mpl.rcParams['font.sans-serif'] = ['SimHei']


def fun(result, title, d):
    lujing: str = ""
    for i in range(len(x)):  # 坐标点
        plt.scatter(int(x[i]), int(y[i]), s=10, c='c')
    for i in range(len(result) - 1):  # 连线
        lujing = lujing + str(result[i]) + ","
        plt.plot([x[result[i]], x[result[i + 1]]], [y[result[i]], y[result[i + 1]]], c='b')
    plt.plot([x[result[0]], x[result[len(result) - 1]]], [y[result[0]], y[result[len(result) - 1]]], c='b')
    # plt.show()
    p = "第" + str(d) + "代" + lujing + "长度：" + str(title)
    plt.title(p)
    plt.savefig("temp.png")
    plt.close('all')
