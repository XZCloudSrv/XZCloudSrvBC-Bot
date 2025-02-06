# Telegram QQ 查询机器人
[![GitHub license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/yourusername/yourrepository/blob/main/LICENSE)![Python Version](https://img.shields.io/badge/Python-3.9.20-blue)
这个开源项目是一个使用 `python-telegram-bot` 库编写的 Telegram 机器人，它提供了一个 `/qq` 命令用于查询 QQ 号的相关信息。通过与一个公共的 QQ 查询 API 接口交互，用户可以获得绑定的手机号码、归属地等信息。同时，机器人还提供了一个回显功能，能够自动回复用户发送的文本消息。

## 功能

- **/qq 查询命令**：用户可以使用 `/qq <QQ号>` 命令查询某个 QQ 号的绑定手机和归属地等信息。
- **回显功能**：机器人会回显用户发送的文本消息，并处理 Markdown V2 特殊字符。
- **人工查询按钮**：当查询结果不准确时，用户可以通过点击按钮访问人工查询链接。

## 安装与使用

[安装python教程](https://doc.78san.top/python.html)

### 1. 安装依赖

首先，确保你已经安装了 Python 3.9 以上版本。然后，你可以使用 `pip3.9` 安装依赖：

```bash
pip3.9 install -r requirements.txt
