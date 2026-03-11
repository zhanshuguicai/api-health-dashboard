\# API 健康检查工具



这是一个使用 Python 编写的 API 健康检查小项目。

目前这个项目可以读取一个接口列表，并依次检测每个接口是否可以正常访问，记录它们的状态码、响应时间以及错误信息。



---



\## 目前已实现的功能



\- 从 `targets.json` 中读取待检测接口

\- 依次对多个接口发送请求

\- 记录每个接口的状态码

\- 记录每个接口的响应时间

\- 当请求失败时记录错误信息

\- 将检测结果保存到 `results.json`



---



\## 项目结构



```text

api-health-dashboard/

├─ main.py              主程序

├─ targets.json        待检测接口列表

├─ results.json         检测结果输出文件（运行后自动生成）

├─ requirements.txt 项目依赖

├─ README.md       项目说明文档

