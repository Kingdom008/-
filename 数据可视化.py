import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

#设置绘图风格
plt.style.use('ggplot')
#处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#坐标轴负号的处理
plt.rcParams['axes.unicode_minus']=False
# 读入数据
iris = pd.read_csv(r'C:\Users\26371\Desktop\图书推荐系统\data\train_dataset.csv')
# 绘制散点图
plt.scatter(x = iris.user_id, # 指定散点图的x轴数据
            y = iris.item_id, # 指定散点图的y轴数据
            color = 'steelblue' # 指定散点图中点的颜色
           )
# 添加x轴和y轴标签
plt.xlabel('用户')
plt.ylabel('相关图书')
# 添加标题
plt.title('用户与相关图书的关系')
plt.savefig('./data/scatter.jpg')#保存图片
x_major_locator=MultipleLocator(1000)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(200)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(-500,60000)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(-100,10000)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
plt.show()