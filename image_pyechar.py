import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
from datetime import datetime

# 连接数据库并获取数据
def get_data_from_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='217727bhj',
        database='my_database'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT time, weight, bmi FROM users")
    results = cursor.fetchall()

    connection.close()
    return results

# 绘制折线图
def draw_line_chart(data):
    x_data = [datetime.strptime(str(item[0]), '%Y-%m-%d') if item[0] is not None else datetime.min for item in data]
    weight_data = [item[1] for item in data]
    bmi_data = [item[2] for item in data]

    line = (
        Line()
      .add_xaxis(x_data)
      .add_yaxis("Weight", weight_data)
      .add_yaxis("BMI", bmi_data)
      .set_global_opts(
            title_opts=opts.TitleOpts(title="Weight and BMI 随时间变化"),
            xaxis_opts=opts.AxisOpts(name="时间"),
            yaxis_opts=opts.AxisOpts(name="值")
        )
    )
    line.render("weight_bmi_line_chart.html")


if __name__ == '__main__':
    datas = get_data_from_database()
    draw_line_chart(datas)