import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from pyecharts.charts import Line
from pyecharts import options as opts

# 假设我们有以下数据，第一列是卡路里消耗，第二列是体重变化
data = {'Calorie_Consumption': [1500, 1800, 2000, 1600, 1900, 2100, 1700],
        'Weight_Change': [0.5, 0.8, 1.0, 0.6, 0.9, 1.2, 0.7]}

df = pd.DataFrame(data)

# 划分训练集和测试集
X = pd.DataFrame(df['Calorie_Consumption'], columns=['Calorie_Consumption'])
X = df[['Calorie_Consumption']]
y = df['Weight_Change']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 假设未来三十天每天的卡路里消耗
future_calorie_consumptions = np.array([[1800], [2000], [1700], [2200], [1900], [1600], [2100], [1850], [1950], [2050], [1750], [1650], [2300], [2150], [1900], [1700], [2000], [1800], [2200], [1950], [1750], [2100], [1850], [2050], [1650], [2350], [2250], [1800], [1900]])

# 进行预测
predicted_weight_changes = model.predict(future_calorie_consumptions)

# 准备绘图数据
days = list(range(1, 31))
weight_changes = predicted_weight_changes

# 创建折线图
line = (
    Line()
  .add_xaxis(days)
  .add_yaxis("体重变化预测", weight_changes)
  .set_global_opts(
        title_opts=opts.TitleOpts(title="未来三十天体重变化预测"),
        xaxis_opts=opts.AxisOpts(name="天数"),
        yaxis_opts=opts.AxisOpts(name="体重变化")
    )
)

# 渲染图表
line.render("weight_change_prediction.html")