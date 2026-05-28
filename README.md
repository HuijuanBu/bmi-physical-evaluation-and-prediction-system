# bmi-physical-evaluation-and-prediction-system
A BMI physical evaluation and prediction system based on Python, PyQt5, MySQL, Pandas and Pyecharts.
<div align="center">

# 🧮 BMI Physical Evaluation and Prediction System

## BMI 体质评估与预测系统

基于 **Python + PyQt5 + MySQL + Pandas + Numpy + Pyecharts** 实现的个人 BMI 体质评估、健康数据记录、趋势可视化与未来变化预测系统。

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-41CD52?style=for-the-badge\&logo=qt\&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Numpy](https://img.shields.io/badge/Compute-Numpy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Pyecharts](https://img.shields.io/badge/Charts-Pyecharts-FF6F00?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge\&logo=windows\&logoColor=white)

<br>

**A personal BMI evaluation, visualization and prediction system.**

</div>

---

## 📑 目录

* [📌 项目简介](#-项目简介)
* [🌟 项目背景](#-项目背景)
* [✨ 核心功能](#-核心功能)
* [🧩 系统模块](#-系统模块)
* [🛠 技术栈](#-技术栈)
* [📁 项目结构](#-项目结构)
* [💻 运行环境](#-运行环境)
* [🚀 快速开始](#-快速开始)
* [🗄 数据库配置](#-数据库配置)
* [▶️ 启动项目](#️-启动项目)
* [📊 功能说明](#-功能说明)
* [📦 Release 下载说明](#-release-下载说明)
* [❓ 常见问题](#-常见问题)
* [⚠️ 注意事项](#️-注意事项)
* [✅ 项目总结](#-项目总结)

---

## 📌 项目简介

**BMI 体质评估与预测系统** 是一个面向个人健康管理场景的桌面端应用系统。系统围绕 BMI 计算、体重记录、健康趋势分析和未来变化预测展开，帮助用户更直观地了解自己的身体状态变化，并辅助用户进行健康管理。

用户可以通过注册和登录进入属于自己的健康档案，输入身高、体重、性别等基础信息后，系统会自动计算 BMI 数值并判断当前身体状态。同时，系统会将用户的体重与 BMI 数据保存到数据库中，便于后续进行趋势分析和可视化展示。

此外，系统还提供了基于历史数据和七天饮食运动数据的预测功能，可以对未来一段时间内的体重与 BMI 变化趋势进行预测。系统还内置日记模块，用户可以记录自己的健康计划、生活感受和阶段性总结。

---

## 🌟 项目背景

BMI，即 **Body Mass Index**，中文通常称为身体质量指数，是衡量人体胖瘦程度和健康状态的常用指标。其计算公式为：

```text
BMI = 体重(kg) / 身高²(m²)
```

BMI 可以帮助用户快速判断自己当前是否处于体重过轻、正常、超重或肥胖状态。对于个人健康管理而言，单次 BMI 计算只能反映当前状态，而连续记录和趋势分析才能帮助用户更好地认识身体变化。

因此，本项目尝试将 **BMI 计算、数据存储、趋势可视化、线性回归预测和个人日记记录** 结合起来，构建一个完整的个人 BMI 健康管理系统。

---

## ✨ 核心功能

| 功能          | 说明                              |
| ----------- | ------------------------------- |
| 🔐 用户登录与注册  | 用户可以创建账号并进入个人专属健康档案             |
| 🧮 BMI 自动计算 | 根据用户输入的身高、体重和性别计算 BMI 数值        |
| 💾 健康数据存储   | 将用户 BMI、体重、日期等信息保存到 MySQL 数据库   |
| 📈 数据可视化    | 使用图表展示用户 BMI 与体重变化趋势            |
| 🔮 未来趋势预测   | 基于历史数据或七天饮食运动数据预测未来体重和 BMI      |
| 📓 健康日记     | 用户可以记录计划、想法、感受和阶段性变化            |
| 🖥 图形化界面    | 使用 PyQt5 和 QtDesigner 构建桌面端交互界面 |

---

## 🧩 系统模块

本系统主要由五个核心模块组成：

### 1. 🔐 登录与注册模块

用户初次使用系统时，可以通过注册功能创建账号和密码。注册成功后，系统会为用户建立个人健康档案。之后用户可以通过用户名和密码登录，进入自己的 BMI 管理页面。

主要功能包括：

* 用户注册；
* 用户登录；
* 密码校验；
* 用户名重复检测；
* 登录错误提示；
* 个人健康档案管理。

---

### 2. 🧮 BMI 计算模块

用户输入自己的身高、体重和性别后，系统会自动计算 BMI 数值，并将结果展示在界面中。

主要功能包括：

* 身高输入；
* 体重输入；
* 性别选择；
* BMI 自动计算；
* BMI 数据保存；
* 输入为空时进行提示。

---

### 3. 📈 查看记录模块

用户可以查看自己使用程序以来的 BMI 和体重变化记录。系统会将数据库中的历史数据进行处理，并通过图表方式展示变化趋势。

主要功能包括：

* 查询历史 BMI 数据；
* 查询历史体重数据；
* 生成折线图；
* 生成柱状图；
* 展示 BMI 与体重变化趋势。

---

### 4. 🔮 预测模块

系统提供两种预测方式：

#### 方式一：基于七天饮食与运动数据预测

用户输入过去七天的体重、饮食摄入卡路里和运动消耗卡路里，系统通过数据分析和线性回归方法，预测未来一个月的体重与 BMI 变化趋势。

#### 方式二：基于历史 BMI 与体重记录预测

系统根据用户使用程序以来保存的所有 BMI 和体重数据，分析已有变化趋势，并预测未来一个月的 BMI 和体重变化情况。

主要功能包括：

* 七天体重数据输入；
* 卡路里摄入记录；
* 卡路里消耗记录；
* 历史 BMI 数据预测；
* 历史体重数据预测；
* 未来趋势图表展示。

---

### 5. 📓 日记模块

用户可以在系统中记录自己的健康计划、生活感受、运动安排或阶段性总结。系统会自动记录日记时间，并支持用户查看历史日记。

主要功能包括：

* 新增日记；
* 保存日记；
* 查看历史日记；
* 记录健康计划；
* 记录个人感受。

---

## 🛠 技术栈

| 类型       | 技术         |
| -------- | ---------- |
| 🐍 编程语言  | Python     |
| 🖥 图形界面  | PyQt5      |
| 🎨 界面设计  | QtDesigner |
| 🗄 数据库   | MySQL      |
| 🔗 数据库连接 | PyMySQL    |
| 📊 数据处理  | Pandas     |
| 🔢 数值计算  | Numpy      |
| 📈 图表可视化 | Pyecharts  |
| 🔮 预测算法  | 线性回归       |
| 💻 开发工具  | PyCharm    |
| 🪟 运行平台  | Windows    |

---

## 📁 项目结构

```text
bmi-physical-evaluation-and-prediction-system/
│
├── BMI_tool.py                  # 项目主入口文件
├── BMI_jisuan_1.py              # BMI 计算界面逻辑
├── BMI_jisuan_1.ui              # BMI 计算界面 UI 文件
├── BMI_change.py                # BMI 与体重变化记录模块
├── BMI_plan_3.py                # 七天数据预测模块
├── BMI_plan_3.ui                # 七天预测界面 UI 文件
├── begin_0.py                   # 欢迎界面
├── begin_0.ui                   # 欢迎界面 UI 文件
├── diary_2_1.py                 # 日记模块
├── diary_2_1.ui                 # 日记模块 UI 文件
├── future.py                    # 预测相关逻辑
├── image_pyechar.py             # 图表生成逻辑
├── message_0_0.py               # 登录注册模块
├── message_0_0.ui               # 登录注册界面 UI 文件
├── more_func_2.py               # 更多功能界面
├── more_func_2.ui               # 更多功能界面 UI 文件
│
├── icons/                       # 图标资源文件夹
├── images/                      # 图片资源文件夹
│
├── frame.qrc                    # Qt 资源文件
├── res.qrc                      # Qt 资源文件
├── res.py                       # 资源编译文件
├── res_rc.py                    # 资源编译文件
│
├── requirements.txt             # Python 依赖列表
├── database_schema.sql          # 数据库建表脚本
├── .gitignore                   # Git 忽略文件配置
└── README.md                    # 项目说明文档
```

---

## 💻 运行环境

建议使用以下环境运行本项目：

| 环境           | 推荐配置                         |
| ------------ | ---------------------------- |
| 操作系统         | Windows 10 / Windows 11      |
| Python       | Python 3.x                   |
| 开发工具         | PyCharm / Visual Studio Code |
| 数据库          | MySQL                        |
| 数据库管理工具      | MySQL Workbench              |
| Python 包管理工具 | pip / Anaconda               |

---

## 🚀 快速开始

如果已经配置好 Python 和 MySQL，可以按以下步骤快速启动项目：

```bash
pip install -r requirements.txt
```

然后在 MySQL 中创建数据库和数据表，修改项目中的数据库连接密码，最后运行：

```bash
python BMI_tool.py
```

---

## 📦 安装依赖

项目运行前需要安装相关 Python 依赖。

如果项目中还没有 `requirements.txt`，可以新建该文件，并写入以下内容：

```txt
PyQt5
PyQtWebEngine
pymysql
pandas
numpy
pyecharts
scikit-learn
```

然后执行：

```bash
pip install -r requirements.txt
```

如果 `pip` 命令不可用，可以尝试：

```bash
python -m pip install -r requirements.txt
```

---

## 🗄 数据库配置

本项目使用 MySQL 存储用户信息、BMI 记录、预测数据和日记内容。

### 1. 创建数据库

可以在 MySQL Workbench 中执行以下 SQL：

```sql
CREATE DATABASE IF NOT EXISTS my_database
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE my_database;
```

---

### 2. 创建用户信息表

```sql
CREATE TABLE IF NOT EXISTS message (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
```

---

### 3. 创建 BMI 记录表

```sql
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    height FLOAT,
    weight FLOAT,
    BMI FLOAT,
    gender VARCHAR(10),
    time DATE,
    name VARCHAR(50)
);
```

---

### 4. 创建预测数据表

```sql
CREATE TABLE IF NOT EXISTS future (
    day INT AUTO_INCREMENT PRIMARY KEY,
    weightt FLOAT,
    kcal_in FLOAT,
    kcal_out FLOAT
);
```

---

### 5. 创建日记表

```sql
CREATE TABLE IF NOT EXISTS diary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time VARCHAR(50),
    diary TEXT,
    name VARCHAR(50)
);
```

---

### 6. 修改数据库连接信息

请在项目源码中找到 MySQL 连接配置，并将其中的用户名和密码改成自己电脑上的 MySQL 配置。

示例：

```python
db = pymysql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="my_database"
)
```

> 注意：不要把自己的真实数据库密码直接上传到 GitHub。建议使用 `your_mysql_password` 作为占位符，并在 README 中说明需要自行修改。

---

## ▶️ 启动项目

### 方式一：使用 PyCharm 启动

1. 打开 PyCharm；
2. 点击 `Open`；
3. 选择项目文件夹；
4. 等待项目加载完成；
5. 安装项目依赖；
6. 配置 MySQL 数据库；
7. 打开 `BMI_tool.py`；
8. 点击右上角 `Run` 按钮运行项目。

---

### 方式二：使用命令行启动

进入项目根目录，执行：

```bash
python BMI_tool.py
```

如果使用的是 Windows 系统，也可以尝试：

```bash
py BMI_tool.py
```

---

## 📊 功能说明

### 🔐 用户注册

用户第一次使用系统时，需要先创建账号。注册时需要输入用户名、密码和确认密码。

系统会进行以下检查：

* 用户名是否为空；
* 密码是否为空；
* 两次输入密码是否一致；
* 用户名是否已经存在。

注册成功后，用户即可使用该账号登录系统。

---

### 🔑 用户登录

用户输入已经注册的用户名和密码后，系统会进行密码校验。如果密码正确，则进入个人 BMI 健康档案；如果密码错误，系统会弹出提示信息，并要求重新输入。

---

### 🧮 BMI 计算

用户输入身高、体重和性别后，系统自动计算 BMI。

BMI 计算公式如下：

```text
BMI = 体重(kg) / 身高²(m²)
```

常见 BMI 判断标准如下：

| BMI 范围          | 判断结果 |
| --------------- | ---- |
| BMI < 18.5      | 体重过轻 |
| 18.5 ≤ BMI < 24 | 正常范围 |
| 24 ≤ BMI < 27   | 超重   |
| 27 ≤ BMI < 30   | 轻度肥胖 |
| 30 ≤ BMI < 35   | 中度肥胖 |
| BMI ≥ 35        | 重度肥胖 |

---

### 📈 BMI 与体重记录查看

用户可以查看自己使用程序以来保存的 BMI 和体重记录。系统会调用数据库中的历史数据，并通过图表方式展示变化趋势。

支持展示内容包括：

* 历史 BMI 数据；
* 历史体重数据；
* BMI 变化趋势；
* 体重变化趋势；
* 折线图；
* 柱状图。

---

### 🔮 未来趋势预测

系统提供两类预测功能：

| 预测类型   | 数据来源           | 预测内容         |
| ------ | -------------- | ------------ |
| 七天数据预测 | 七天体重、饮食摄入、运动消耗 | 未来一个月体重与 BMI |
| 历史数据预测 | 用户历史 BMI 与体重记录 | 未来一个月体重与 BMI |

系统会结合用户输入或历史记录进行数据分析，并生成对应的预测图表。

---

### 📓 日记记录

日记模块用于记录用户的健康计划、生活感受和阶段性变化。

用户可以：

* 新增日记；
* 保存日记；
* 查看历史日记；
* 记录健康计划；
* 记录个人总结。

该模块可以帮助用户更主观、更连续地观察自己在健康管理过程中的变化。

---

## 🔁 基本使用流程

```text
启动系统
  ↓
用户注册 / 登录
  ↓
进入个人健康档案
  ↓
输入身高、体重、性别
  ↓
计算 BMI 并保存记录
  ↓
查看 BMI 与体重变化趋势
  ↓
选择预测方式
  ↓
查看未来一个月预测结果
  ↓
记录或查看健康日记
```

---

## 📦 Release 下载说明

本项目的大文件、项目说明材料和原始压缩包建议放在 GitHub Release 中，而不是直接放在 Code 页面。

推荐 Release 中包含：

| 文件                      | 说明        |
| ----------------------- | --------- |
| 📄 `项目介绍PPT.pptx`       | 项目展示与汇报材料 |
| 📘 `用户手册.docx`          | 系统使用说明文档  |
| 🗂 `pythonProject7.zip` | 原始项目源码压缩包 |

如果只想查看源码，可以浏览仓库 Code 页面；如果需要下载完整项目材料，可以进入 Release 页面下载。

---

## 🧹 建议的 .gitignore 配置

建议在项目根目录添加 `.gitignore` 文件，避免上传缓存文件、IDE 配置文件和临时文件：

```gitignore
# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environment
.venv/
venv/
env/

# PyCharm / VS Code
.idea/
.vscode/

# System files
.DS_Store
Thumbs.db

# Temporary files
*.log
*.tmp

# Build output
build/
dist/
*.spec
*.exe

# Local database or backup files
*.db
*.sql.bak
```

---

## ❓ 常见问题

### 1. 运行时报错：缺少 PyQt5

请执行：

```bash
pip install PyQt5
```

或者直接安装全部依赖：

```bash
pip install -r requirements.txt
```

---

### 2. 运行时报错：无法连接 MySQL

请检查以下内容：

* MySQL 服务是否已经启动；
* 数据库名称是否正确；
* 用户名是否正确；
* 密码是否正确；
* 项目中的数据库连接配置是否已经修改。

---

### 3. 登录或注册失败怎么办？

可能原因包括：

* 数据库没有创建；
* 用户信息表没有创建；
* MySQL 密码配置错误；
* 用户名已经存在；
* 两次输入密码不一致。

---

### 4. 为什么图表打不开？

可能原因包括：

* 没有安装 `pyecharts`；
* 没有安装 `PyQtWebEngine`；
* 图表 HTML 文件路径不正确；
* 数据库中暂无可用于展示的数据。

可以尝试安装：

```bash
pip install pyecharts PyQtWebEngine
```

---

### 5. 为什么不建议上传 `.idea` 和 `__pycache__`？

`.idea` 是 PyCharm 的本地配置文件，`__pycache__` 是 Python 运行时生成的缓存文件。这些文件与项目核心功能无关，不建议上传到 GitHub。

---

### 6. 数据库密码可以上传到 GitHub 吗？

不建议。

如果源码中包含真实密码，建议改成：

```python
password="your_mysql_password"
```

然后在 README 中说明用户需要自行修改为本机 MySQL 密码。

---

## ⚠️ 注意事项

1. 本项目建议在 Windows 环境下运行。
2. 运行前需要安装 Python 和 MySQL。
3. 首次运行前需要创建数据库和数据表。
4. 需要根据本机环境修改 MySQL 用户名和密码。
5. 不建议将个人数据库密码上传到 GitHub。
6. 不建议上传 `.idea`、`__pycache__`、`.pyc` 等本地缓存文件。
7. 项目介绍 PPT、用户手册和源码压缩包建议放在 GitHub Release 中。

---

## 🎓 项目应用场景

本项目适用于：

* Python 课程设计；
* 数据库课程设计；
* 软件工程综合实践；
* 数据分析与可视化实验；
* 个人健康管理工具开发；
* PyQt5 桌面应用开发学习；
* MySQL 数据库应用实践。

---

## ✅ 项目总结

本项目围绕个人 BMI 健康管理需求，设计并实现了一个集 **用户管理、BMI 计算、健康数据存储、趋势可视化、未来预测和日记记录** 于一体的桌面端应用系统。

系统通过 PyQt5 提供图形化交互界面，通过 MySQL 存储用户健康数据，通过 Pandas 和 Numpy 对数据进行处理，并使用 Pyecharts 生成可视化图表。同时，系统结合线性回归思想，对未来一个月的体重和 BMI 变化趋势进行预测。

整体来看，本项目功能结构较为完整，既体现了 Python GUI 编程能力，也体现了数据库操作、数据分析、可视化展示和简单预测建模能力，可作为课程设计、项目展示和后续扩展的基础。

---

<div align="center">

<br>

🧮 **BMI Physical Evaluation and Prediction System**
💙 **让健康数据更直观，让身体变化可记录、可分析、可预测**

</div>
