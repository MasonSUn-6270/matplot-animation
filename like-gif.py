import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn
plt.fig, ax = plt.subplots()
plt.fig.set_tight_layout(True)  # tight:紧的；layout：布局
# DPI：每英寸的点数
# 获取图片的分辨率和尺寸
# 在保存图片时，还需要另外指明图片的DPI
print('图片的分辨率尺寸是{0}DPI，size in inches is {1}'.format(plt.fig.get_dpi(), plt.fig.get_size_inches()))  # inches:英寸

# 画出一个维持不变的散点图和一开始的那条直线
# 困难的问题从约定俗成的方法去解决，不如先不管多么复杂的图像，第一步就是创建点的集合
X = np.arange(0, 20, 0.1)
ax.scatter(X, X + np.random.normal(0, 3.0, len(X)))  # 这种方法很好啊
line, = plt.plot(X, X - 0.5, 'r-', linewidth=2)
plt.title('Interesting Graph', fontsize='large', fontweight='bold', verticalalignment='center')  # 设置标题位置不起作用


def update(i):
    label = 'timestep{0}'.format(i)
    print(label)
    # 更新直线和X轴，使用一个新的X轴的标签
    # 以元组的形式返回在这一帧需要被更新的物体
    line.set_ydata(X - 5 + i)
    ax.set_label(label)
    return ax, line


if __name__ == '__main__':
    # FuncAnimation会在每一帧都调用update函数
    # 在这里设置一个10帧的动画，每帧之间间隔200ms
    anim = animation.FuncAnimation(plt.fig, update, frames=np.arange(0, 10), interval=200)  # frame:帧
    # 我知道问什么这里提示figundefine了，因为前面的fig在函数中声明的
    plt.show()