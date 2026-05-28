import sys
from PyQt5 import QtWidgets
from datetime import datetime,timedelta
from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMessageBox,QMainWindow
import pymysql
import numpy as np
from sklearn.linear_model import LinearRegression
import subprocess
import webbrowser
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


# -----------------------------------------------------------------------------------------------------
global_username = None

#self.fore_window = None

#  从ui转换的.py文件中导入Ui_MainWindow类
from BMI_jisuan_1 import Ui_MainWindow as BMI
from more_func_2 import Ui_MainWindow as MORE
from BMI_plan_3 import Ui_MainWindow as PLAN
from diary_2_1 import Ui_MainWindow as DIARY
from begin_0 import Ui_MainWindow as BEGIN
from message_0_0 import Ui_MainWindow as MESSAGE


# -----------------------------------------------------------------------------------------------------
class Main_Window(QtWidgets.QMainWindow, MESSAGE):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.zc_Button.clicked.connect(self.register)
        self.dl_Button.clicked.connect(self.login)
    def gologin_next(self):
        self.ui_login = message_Window()
        self.ui_login.show()
        self.close()

    def register(self):
        password = self.zc_mmEdit.text()
        password_confirm = self.zc_mmqrEdit.text()
        username = self.zc_nameEdit.text()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM message WHERE name=%s", (username,))
        #如果参数是一个值，应该将其包装在元组中，即 (username,)，而不是 (username)。如果写成 (username)，在某些情况下可能不会被正确识别为单个参数的元组，而可能被解释为其他类型的数据，导致参数绑定错误。
        existing_user = cursor.fetchone()
        if existing_user:
            QMessageBox.warning(self, "错误", "名字已存在，请重新注册。")
            self.zc_mmEdit.clear()
            self.zc_mmqrEdit.clear()
            self.zc_nameEdit.clear()
            return
        if password == password_confirm:
            try:
                cursor = db.cursor()
                cursor.execute("INSERT INTO message (name, password) VALUES (%s, %s)", (username, password))
                db.commit()
                QMessageBox.information(self, "注册成功", "注册成功！\n开始使用！")
                global global_username
                global_username = username  # 设置全局变量
                self.gologin_next()

            except pymysql.connector.Error as err:
                QMessageBox.warning(self, "错误", f"注册失败：{err}")
        else:
            QMessageBox.warning(self, "错误", "两次输入的密码不一致！请重新输入")
            self.zc_mmEdit.clear()
            self.zc_mmqrEdit.clear()

    def login(self):
        username = self.dl_nameEdit.text()
        password = self.dl_mmEdit.text()
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM message WHERE name=%s", (username,))
            user = cursor.fetchone()
            if user and user[2] == password:
                QMessageBox.information(self, "登录成功", "登录成功！欢迎使用☺")
                global global_username
                global_username = username  # 设置全局变量
                self.gologin_next()
            else:
                if not user:
                    QMessageBox.warning(self, "错误", "用户不存在，请注册♥")
                else:
                    QMessageBox.warning(self, "错误", "密码错误，请重新输入☺")
                self.dl_mmEdit.clear()
        except pymysql.connector.Error as err:
            QMessageBox.warning(self, "错误", f"登录失败：{err}")

# -----------------------------------------------------------------------------------------------------
class message_Window(QtWidgets.QMainWindow, BEGIN):
    def __init__(self):
        super(message_Window, self).__init__()
        self.setupUi(self)
        self.begin_button.clicked.connect(self.gologin_next)

    def gologin_next(self):
        self.ui_login = begin_Window()
        self.ui_login.show()
        self.close()

# -----------------------------------------------------------------------------------------------------

class begin_Window(QtWidgets.QMainWindow, BMI):
    def __init__(self):
        super(begin_Window, self).__init__()
        self.setupUi(self)
        self.morefunc_button.clicked.connect(self.gologin_next)
        self.jisuan_BMI_button.clicked.connect(self.BMI_result_hanshu)


    # ♥♥BMI计算
    def BMI_result_hanshu(self):
        height_edit_text = self.height_edit.text()
        weight_edit_text = self.weight_edit.text()

        if not height_edit_text:
            QtWidgets.QMessageBox.warning(self, "输入提示", "请输入身高。")
            return
        if not weight_edit_text:
            QtWidgets.QMessageBox.warning(self, "输入提示", "请输入体重。")
            return
        if not self.gender_man_button.isChecked() and not self.gender_woman_button.isChecked():
            QtWidgets.QMessageBox.warning(self, "输入提示", "请选择性别。")
            return

        height = float(height_edit_text)
        weight = float(weight_edit_text)
        bmi = weight / ((height / 100) ** 2)
        self.BMI_result_line_edit_2.setText(str(round(bmi, 2)))

        if self.gender_man_button.isChecked():
            gender = "男"
        if self.gender_woman_button.isChecked():
            gender = "女"

        current_time = datetime.now().strftime('%Y-%m-%d')

        self.save_to_database(height, weight, bmi, gender, current_time,global_username)

    def save_to_database(self, height, weight, bmi, gender, current_time,global_username):
        cursor = db.cursor()
        sql = "INSERT INTO users (height, weight, BMI, gender, time,name) VALUES (%s, %s, %s, %s, %s,%s)"
        values = (height, weight, bmi, gender, current_time,global_username)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("数据成功存储到数据库")
        except pymysql.Error as e:
            print(f"存储数据时出错: {e}")
            db.rollback()

    # ♥♥进入第二菜单
    def gologin_next(self):
        self.ui_login = more_Window()
        self.ui_login.show()
        self.close()

# -----------------------------------------------------------------------------------------------------
# 更多界面的类
class more_Window(QtWidgets.QMainWindow, MORE):
    def __init__(self):
        super(more_Window, self).__init__()
        self.setupUi(self)
        self.next_plan_button.clicked.connect(self.gologin_next)
        self.back_jisuan_BMI_2.clicked.connect(self.gologin_last)
        self.diary_button.clicked.connect(self.gologin_next_diary)
        self.look_change_line_button.clicked.connect(self.generate_chart_and_open)

        self.web_window  = None

        self.last_predit_button.clicked.connect(self.predict_BMI)

    # ♥♥进入第三菜单
    def gologin_next(self):
        self.ui_login2 = change_Window()
        self.ui_login2.show()
        self.close()

    def gologin_next_diary(self):
        self.ui_login3 = diary_Window()
        self.ui_login3.show()
        self.close()

    # ♥♥返回第一菜单
    def gologin_last(self):
        self.ui_login = begin_Window()
        self.ui_login.show()
        self.close()

    def generate_chart_and_open(self):

        try:
            # 运行生成图像的文件
            subprocess.run(["python", "image_pyechar.py"], check=True)

            # 获取生成图像的文件路径
            file_path = os.path.abspath("weight_bmi_line_chart.html")

            cursor = db.cursor()
            sql = "SELECT time, weight,BMI FROM users WHERE name=%s"
            cursor.execute(sql, (global_username,))
            results = cursor.fetchall()

            # 处理数据
            x_data = [result[0] for result in results]
            y_data_weight = [result[1] for result in results]
            y_data_bmi = [result[2] for result in results]
            # 绘制折线图
            line = (
                Line()
                .add_xaxis(x_data)
                .add_yaxis("BMI", y_data_bmi)
                .add_yaxis("Weight", y_data_weight)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title=global_username+"的BMI & weight change over Time"),
                    yaxis_opts=opts.AxisOpts(
                    min_=10,  # y 轴最小值
                    max_=90,  # y 轴最大值
                    interval=0.01,  #y 轴刻度间隔
                    ),
                    legend_opts=opts.LegendOpts(is_show=True),  # 显示图例
                    toolbox_opts=opts.ToolboxOpts(is_show=True),  # 显示工具箱
                    visualmap_opts=opts.VisualMapOpts(is_show=True),
                )
            )

            # 保存图表为 HTML 文件  file:///C:/Users/a/PycharmProjects/pythonProject7/new_weight_bmi_line_chart.html
            html_path = os.path.join(os.path.dirname(file_path), "new_weight_bmi_line_chart.html")
            line.render(html_path)

            # 在浏览器中打开新生成的图表
            webbrowser.open('file://' + html_path)

        except subprocess.CalledProcessError as e:
            print(f"运行生成图像的文件时出错: {e}")

        except pymysql.Error as e:
            print(f"数据库操作出错: {e}")


    def predict_BMI(self):  # 预测 BMI 变化
        cursor = db.cursor()
        sql = "SELECT time, BMI FROM users WHERE name=%s"
        cursor.execute(sql, (global_username,))
        results = cursor.fetchall()

        # 使用 pandas 进行数据清洗
        df = pd.DataFrame(results, columns=['time', 'BMI'])
        df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')

        # 处理异常值,用平均值来代替
        df['BMI'].fillna(df['BMI'].mean(), inplace=True)
        #df[col].method(value, inplace=True)
        #df.method({'BMI': df['BMI'].mean(),}, inplace=True)

        # 提取时间和 BMI 数据
        times = np.array(df['time'])
        bmis = np.array(df['BMI'])

        # 创建线性回归模型
        model = LinearRegression()

        # 准备数据
        X = np.array(range(len(times))).reshape(-1, 1)
        y = bmis

        # 训练模型
        model.fit(X, y)

        # 预测未来一个月的 BMI
        future_dates = np.array(range(len(times), len(times) + 30))
        future_X = future_dates.reshape(-1, 1)
        predicted_bmis = model.predict(future_X)

        # 使用 pyecharts 绘制未来一个月每天的 BMI 变化
        line = Line()
        line.add_xaxis([times[i] for i in range(len(times))] + [datetime.strftime(datetime.now() + timedelta(days=i), '%Y-%m-%d') for i in range(30)])
        line.add_yaxis("Predicted BMI", list(bmis) + list(predicted_bmis))
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=global_username+"基于历史BMI数据的未来一个月 BMI 变化预测"),
            legend_opts = opts.LegendOpts(is_show=True),  # 显示图例
            toolbox_opts = opts.ToolboxOpts(is_show=True),  # 显示工具箱
            visualmap_opts = opts.VisualMapOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(
                min_=10,  # y 轴最小值
                max_=30,  # y 轴最大值
                interval=0.01,  # y 轴刻度间隔
            ),
    )


        print("正常")
        # 保存图表为 HTML 文件
        chart_path = "predicted_BMI_chart.html"
        line.render(chart_path)

        #ui_login3 = Fore_MainWindow()
        # ui_login3.show()
        #self.close()
        #fore_window = Fore_MainWindow()
        #fore_window.show()
        # 在浏览器中打开图表
        #web_window = Fore_MainWindow()
        #web_window.show()
        chart__path = os.path.abspath("predicted_BMI_chart.html")
        webbrowser.open('file://' + chart__path)





# -----------------------------------------------------------------------------------------------------
import time



# -----------------------------------------------------------------------------------------------------
class change_Window(QtWidgets.QMainWindow, PLAN):
    def __init__(self):
        super(change_Window, self).__init__()
        self.setupUi(self)
        self.back_lastmenu.clicked.connect(self.gologin_last)
        self.cacluta_kcal_button.clicked.connect(self.open_webpage_calcut)
        self.look_kcalin_buttton.clicked.connect(self.open_webpage_in)
        self.save_button.clicked.connect(self.save_to_database)
        self.predit_button.clicked.connect(self.predict_weight)
        # 判断 height_edit 不为空时允许点击predit_button 按钮
        self.height_edit.textChanged.connect(self.enable_predit_button)

    def enable_predit_button(self):
        if self.height_edit.text():
            self.predit_button.setEnabled(True)
        else:
            self.predit_button.setEnabled(False)

    def save_to_database(self):
        data = []
        all_filled = True  # 标记是否所有输入框都已填写
        for i in range(1, 8):
            wei = self.__get_attribute(f"day{i}_wei_edit").text()
            in_ = self.__get_attribute(f"day{i}_in_edit").text()
            out = self.__get_attribute(f"day{i}_out_edit").text()
            if not wei or not in_ or not out:
                all_filled = False
                break
            data.append((wei, in_, out))

        if all_filled:  # 当所有输入框都有值时才执行保存操作
            try:
                with db.cursor() as cursor:
                    # 执行 SQL 语句清空表内容
                    sql = "TRUNCATE TABLE future;"
                    cursor.execute(sql)
                    # 提交更改
                    db.commit()
                    print("数据表内容已清空。")
            except Exception as e:
                # 如果出现错误，回滚操作
                db.rollback()
                print(f"发生错误：{e}")
            cursor = db.cursor()
            sql = "INSERT INTO future (weightt, kcal_in, kcal_out) VALUES (%s, %s, %s)"
            try:
                cursor.executemany(sql, data)
                db.commit()
                print("数据成功存储到数据库")
            except pymysql.Error as e:
                print(f"存储数据时出错: {e}")
                db.rollback()
        else:
            QtWidgets.QMessageBox.warning(self, "输入提示", "请填写所有输入框。")

    def __get_attribute(self, name):
        return getattr(self, name)

    def predict_weight(self):
        # 检查 height_edit 是否为空
        if not self.height_edit.text():
            QtWidgets.QMessageBox.warning(self, "输入提示", "请输入身高。")
            return

        # 从数据库中获取数据
        cursor = db.cursor()
        sql = "SELECT day, weightt, kcal_in, kcal_out FROM future"
        cursor.execute(sql)
        results = cursor.fetchall()

        # 使用 pandas 进行数据清洗
        df = pd.DataFrame(results, columns=['day', 'weightt', 'kcal_in', 'kcal_out'])
        df['weightt'] = pd.to_numeric(df['weightt'], errors='coerce')
        df['kcal_in'] = pd.to_numeric(df['kcal_in'], errors='coerce')
        df['kcal_out'] = pd.to_numeric(df['kcal_out'], errors='coerce')

        # 处理异常值,对异常值敏感
        # 线性回归模型对异常值比较敏感。一个或几个异常值可能会对模型的参数估计产生较大的影响，从而降低模型的准确性。
        weightt_mean = df['weightt'].mean()
        df['weightt'] = df['weightt'].apply(lambda x: weightt_mean if pd.isna(x) or x > weightt_mean + 100 else x)
        df['weightt'].fillna(df['weightt'].mean(), inplace=True)
        df['kcal_in'].fillna(df['kcal_in'].mean(), inplace=True)
        df['kcal_out'].fillna(df['kcal_out'].mean(), inplace=True)

        # 提取数据
        weights = np.array(df['weightt'])
        cal_in = np.array(df['kcal_in'])
        cal_out = np.array(df['kcal_out'])

        # 创建线性回归模型
        model = LinearRegression()

        # 准备数据
        X = np.column_stack((cal_in, cal_out))
        y = weights

        # 训练模型
        model.fit(X, y)

        # 预测未来一个月的体重
        future_cal_in = np.mean(cal_in)  # 使用平均值作为未来的卡路里摄入
        future_cal_out = np.mean(cal_out)  # 使用平均值作为未来的卡路里消耗
        future_X = np.array([[future_cal_in, future_cal_out]] * 30)
        predicted_weights = model.predict(future_X)

        # 预测未来一个月的 BMI
        height = float(self.height_edit.text())  # 在界面中获取的身高
        predicted_bmis = [w / ((height / 100) ** 2) for w in predicted_weights]

        # 使用 pyecharts 绘制未来一个月每天的体重和 BMI 变化折线图
        line = Line()
        line.add_xaxis([f"Day {i}" for i in range(1, 31)])
        line.add_yaxis("Predicted Weight", predicted_weights, is_connect_nones=True)  # 使用 is_connect_nones=True 连接空值
        line.add_yaxis("Predicted BMI", predicted_bmis, is_connect_nones=True)
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=global_username+"的未来一个月体重和 BMI 变化预测"),
            legend_opts=opts.LegendOpts(is_show=True),  # 显示图例
            toolbox_opts=opts.ToolboxOpts(is_show=True),  # 显示工具栏
            xaxis_opts=opts.AxisOpts(name="Day"),  # X 轴名称
            yaxis_opts=opts.AxisOpts(name="Value"),  # Y 轴名称

        )

        # 保存图表为 HTML 文件
        chart_path = "predicted_weight_bmi_chart.html"
        line.render(chart_path)
        chart__path = os.path.abspath("predicted_weight_bmi_chart.html")
        # 在浏览器中打开图表  file:///C:/Users/a/PycharmProjects/pythonProject7/predicted_weight_bmi_chart.html
        webbrowser.open('file://' + chart__path)

    def gologin_last(self):
        self.ui_login = more_Window()
        self.ui_login.show()
        self.close()

    def open_webpage_calcut(self):  # 网页跳转
        from PyQt5.QtGui import QDesktopServices
        url = "https://dailycalculators.com/cn/daily-calorie-calculator"
        QDesktopServices.openUrl(QUrl(url))

    def open_webpage_in(self):  # 新增：网页跳转
        from PyQt5.QtGui import QDesktopServices
        url = "https://wenku.so.com/d/3dbb52f5bf3f58a6841299c5b7af7c55?src=baiduss1&ocpc_id=125406&plan_id=577706901&group_id=10142384836&keyword=%CA%B3%CE%EF%BF%A8%C2%B7%C0%EF%B1%ED%B4%F3%C8%AB%CD%EA%D5%FB%B0%E6&bd_vid=6849921537351635132"
        QDesktopServices.openUrl(QUrl(url))



# -----------------------------------------------------------------------------------------------------

class diary_Window(QtWidgets.QMainWindow, DIARY):
    def __init__(self):
        super(diary_Window, self).__init__()
        self.setupUi(self)
        self.back_to_2_button.clicked.connect(self.gologin_last)
        self.save_diary_button.clicked.connect(self.save_diary)
        self.look_diary_button.clicked.connect(self.show_diary)
    def save_diary(self):
        diary_content = self.new_diary_edit.toPlainText() # 获取编辑框中的内容
        current_time = datetime.now().strftime('%Y-%m-%d ')  # 获取当前时间
        # 连接数据库并保存数据
        cursor = db.cursor()
        sql = "INSERT INTO diary (time, diary,name) VALUES (%s, %s,%s)"
        values = (current_time, diary_content,global_username)
        print("lianjie")
        try:
            cursor.execute(sql, values)
            db.commit()
            print("保存日记")
            QtWidgets.QMessageBox.information(self, "保存成功", "日记已成功保存！")
        except pymysql.Error as e:
            print(f"保存数据时出错: {e}")
            db.rollback()

    def show_diary(self):
        # 连接数据库并获取日记数据
        print("查看")
        cursor = db.cursor()
        sql = "SELECT * FROM diary WHERE name=%s"
        cursor.execute(sql, (global_username,))
        results = cursor.fetchall()
        # 创建并显示表格
        self.tableWidget = QTableWidget()
        self.tableWidget.setWindowTitle("My Diary")
        #self.tableWidget.setColumnWidth(1, 800)
        self.tableWidget.setStyleSheet(" background-image: url(C:/Users/a/PycharmProjects/pythonProject7/images/pic5.png);")
        self.tableWidget.setColumnCount(2)  # 三列：id, time, diary
        self.tableWidget.setHorizontalHeaderLabels(["时间", "日记内容"])
        # 设置窗口大小
      #  self.tableWidget.setColumnWidth(3, 500)
        self.tableWidget.setFixedSize(2000, 1000)
        row = 0
        for result in results:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(result[1].strftime('%Y-%m-%d')))  # 将日期转换为字符串
            self.tableWidget.setItem(row, 1, QTableWidgetItem(result[2]))  # diary

            row += 1

        self.tableWidget.setColumnWidth(1,1770)
        self.tableWidget.show()
    def gologin_last(self):
        self.ui_login = more_Window()
        self.ui_login.show()
        self.close()



# -----------------------------------------------------------------------------------------------------
# 主要运行程序入口
if __name__ == '__main__':
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='your_mysql_password',
        # 数据库名，如变动请按变动后修改
        database='my_database')

    app = QApplication(sys.argv)
    window = Main_Window()
    window.widget_3.hide()
    def change_widget3():
        window.widget_2.hide()
        window.widget_3.show()
    def change_widget2():
        window.widget_3.hide()
        window.widget_2.show()

    window.chuose_dl_Button.clicked.connect(change_widget2)
    window.chose_zc_Button.clicked.connect(change_widget3)
    window.show()
    sys.exit(app.exec_())
    db.close()
