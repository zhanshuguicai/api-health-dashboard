# API 健康检查小工具

这是一个使用 Python 编写的 API 健康检查项目。
目前这个项目可以读取一个接口列表，并依次检测每个接口是否可以正常访问，记录它们的状态码、响应时间以及错误信息，并输出简单的检测统计结果。

---

## 项目功能

目前已经实现的功能包括：

- 从 `targets.json` 中读取待检测接口
- 依次对多个接口发送 GET 请求
- 记录每个接口的状态码
- 记录每个接口的响应时间
- 当请求失败时记录错误信息
- 根据状态码判断接口是否健康
- 当前将 `200~399` 视为成功，`404` 等状态码视为失败
- 输出检测总数、成功数量、失败数量
- 输出失败接口明细
- 将检测结果保存到 `results.json`

---

## 项目结构

```text
api-health-dashboard/
├─ main.py          主程序
├─ targets.json     待检测接口列表
├─ results.json     检测结果输出文件（运行后生成）
├─ requirements.txt 项目依赖
├─ README.md        项目说明文档

运行环境

Python 3.9 及以上版本

依赖库：

requests

安装依赖:

先在项目目录下运行

-pip install -r requirements.txt

如果你还没有 requirements.txt，可以写成：

-requests

配置检测目标

项目通过 targets.json 文件读取待检测接口信息。

一个简单的配置示例如下：

[
  {
    "name": "微软官网",
    "url": "https://www.microsoft.com",
    "method": "GET",
    "timeout": 5
  },
  {
    "name": "HTTPBin 状态码 200",
    "url": "https://httpbin.org/status/200",
    "method": "GET",
    "timeout": 5
  },
  {
    "name": "HTTPBin 状态码 404",
    "url": "https://httpbin.org/status/404",
    "method": "GET",
    "timeout": 5
  },
  {
    "name": "Python官网",
    "url": "https://www.python.org",
    "method": "GET",
    "timeout": 5
  }
]
字段说明

-name：检测目标名称，便于终端输出和结果识别

-url：要访问的目标地址

-method：请求方式，目前第一版只支持 GET

-timeout：超时时间，单位为秒

使用方法

在项目目录下运行：

python main.py

运行后程序会：

-读取 targets.json

-依次检测每个接口

-在终端打印检测结果

-将结果保存到 results.json

示例输出
开始进行 API 健康检查...

[成功] 微软官网 | 状态码: 200 | 耗时: 0.212 秒
[成功] HTTPBin 状态码 200 | 状态码: 200 | 耗时: 1.570 秒
[失败] HTTPBin 状态码 404 | 状态码: 404 | 耗时: 1.083 秒
[失败] Python官网 | 错误信息: HTTPSConnectionPool(host='www.python.org', port=443): Read timed out. (read timeout=5) | 耗时: 5.011 秒

检测完成，结果已保存到 results.json 文件中。
========== 检测统计 ==========
接口总数：4
成功数量：2
失败数量：2

失败接口如下：
- HTTPBin 状态码 404（状态码：404）
- Python官网（错误：请求超时）
检测逻辑说明

当前的判断规则是：

-200 ~ 399：视为成功

-其他状态码（如 404、500）：视为失败

-如果请求过程中发生异常（例如超时、SSL 问题、连接失败），也视为失败

输出文件说明

程序运行后会生成 results.json 文件，用来保存检测结果。

每条结果中一般包括：

-检测目标名称

-URL

-请求方式

-是否成功

-状态码

-响应时间

-错误信息

-这样后续可以方便查看，也便于继续扩展历史记录功能。


当前项目的不足

这个项目目前还是第一版，功能比较基础，还存在一些可以继续完善的地方，例如：

-目前只支持 GET 请求，不支持 POST、PUT 等方式

-还没有图形化界面

-还没有保存多次检测历史

-对错误分类还比较简单

-结果展示方式还可以进一步优化

后续准备继续完善的方向

-支持更多请求方式，例如 POST

-增加历史检测结果统计

-增加表格化输出

-尝试增加简单图形界面

-尝试使用 SQLite 保存历史结果

-对超时、SSL 错误、状态码错误进行更细致的分类

项目定位说明

在学习 Python、HTTP 请求、异常处理和项目组织过程中的一个练习型项目。

作者

本人
