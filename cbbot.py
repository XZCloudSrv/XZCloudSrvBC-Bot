# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

import requests  # 导入requests库，用于发送HTTP请求  # Copyright (c) 散小战开发
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton  # 导入Telegram相关模块，用于处理更新和按钮  # 作者频道@SAN869CN
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext  # 导入处理Telegram消息和命令的工具  # 作者高级版机器人@Sanxiaozhan886
from telegram.constants import ParseMode  # 导入Telegram常量ParseMode，用于设置消息格式  # 版权所有，请勿二改

# 机器人 Token（替换为你的实际 Token）  # 保留所有权利。
TOKEN = "Token"  # 你需要在此处输入你自己的Telegram Bot Token  # Copyright (c) 散小战开发

# QQ 查询 API  # 作者频道@SAN869CN
API_URL = "https://api.xywlapi.cc/qqapi?qq={}"  # 这是QQ查询的API接口  # 作者高级版机器人@Sanxiaozhan886

# 人工查询 Telegram 链接  # 版权所有，请勿二改
MANUAL_QUERY_URL = "https://t.me/Sanxiaozhan886"  # 如果自动查询失败，用户可以通过此链接进行人工查询  # 保留所有权利。

# /qq 命令处理函数  # Copyright (c) 散小战开发
async def qq_query(update: Update, context: CallbackContext) -> None:  # 当用户输入 /qq 命令时，会触发此函数  # 作者频道@SAN869CN
    if len(context.args) == 0:  # 如果没有提供QQ号  # 作者高级版机器人@Sanxiaozhan886
        await update.message.reply_text(  # 回复给用户提示信息  # 版权所有，请勿二改
            "❌ *请输入 QQ 号，例如：*\n` /qq 336699`",  # 如果没有输入QQ号，提醒用户输入  # 保留所有权利。
            parse_mode=ParseMode.MARKDOWN_V2  # 设置消息格式为Markdown  # Copyright (c) 散小战开发
        )  # 作者频道@SAN869CN
        return  # 作者高级版机器人@Sanxiaozhan886

    qq_number = context.args[0]  # 获取用户输入的QQ号  # 版权所有，请勿二改
    response = requests.get(API_URL.format(qq_number)).json()  # 向API发送请求，获取查询结果  # 保留所有权利。

    # 查询成功  # Copyright (c) 散小战开发
    if response["status"] == 200:  # 如果API返回的状态码是200，表示查询成功  # 作者频道@SAN869CN
        # 处理 Telegram Markdown V2 转义字符  # 作者高级版机器人@Sanxiaozhan886
        qq = response['qq'].replace("-", "\\-")  # 将QQ号中的“-”替换为转义字符  # 版权所有，请勿二改
        phone = response['phone'].replace("-", "\\-")  # 将绑定手机号码中的“-”替换为转义字符  # 保留所有权利。
        phonediqu = response['phonediqu'].replace("-", "\\-")  # 将归属地中的“-”替换为转义字符  # Copyright (c) 散小战开发

        # 回复消息，显示查询结果  # 作者频道@SAN869CN
        reply_text = (  # 作者高级版机器人@Sanxiaozhan886
            f"✅ *查询成功！*\n"  # 查询成功的消息  # 版权所有，请勿二改
            f"🔹 *QQ号：* [`{qq}`](tg://copy?copy={qq})\n"  # 显示QQ号，并允许用户点击复制  # 保留所有权利。
            f"📱 *绑定手机：* [`{phone}`](tg://copy?copy={phone})\n"  # 显示绑定手机号码  # Copyright (c) 散小战开发
            f"📍 *归属地：* [`{phonediqu}`](tg://copy?copy={phonediqu})\n\n"  # 显示号码归属地  # 作者频道@SAN869CN
            f"🔎 *如果查询结果不准确，可以人工查询：*"  # 提供人工查询链接  # 作者高级版机器人@Sanxiaozhan886
        )  # 版权所有，请勿二改
    else:  # 查询失败  # 保留所有权利。
        # 查询失败，返回失败信息  # Copyright (c) 散小战开发
        reply_text = f"❌ *查询失败：* `{response['message']}`\n\n"  # 如果查询失败，显示失败信息  # 作者频道@SAN869CN
                     f"🔎 *查询不到，可以人工查询：*"  # 提供人工查询链接  # 作者高级版机器人@Sanxiaozhan886

    # 添加“人工查询”按钮  # 版权所有，请勿二改
    keyboard = [[InlineKeyboardButton("🔍 人工查询", url=MANUAL_QUERY_URL)]]  # 创建一个按钮，指向人工查询链接  # 保留所有权利。
    reply_markup = InlineKeyboardMarkup(keyboard)  # 创建按钮的键盘布局  # Copyright (c) 散小战开发
    
    # 发送消息给用户，包含查询结果和人工查询按钮  # 作者频道@SAN869CN
    await update.message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=reply_markup)  # 作者高级版机器人@Sanxiaozhan886

# 处理普通文本消息（回显功能）  # 版权所有，请勿二改
async def echo(update: Update, context: CallbackContext) -> None:  # Copyright (c) 散小战开发
    text = update.message.text.replace("-", "\\-")  # 处理 Markdown V2 特殊字符  # 作者频道@SAN869CN
    await update.message.reply_text(f"*你说的是：*\n`{text}`", parse_mode=ParseMode.MARKDOWN_V2)  # 回复用户输入的文本  # 作者高级版机器人@Sanxiaozhan886

# 运行 Bot  # 版权所有，请勿二改
def main():  # 保留所有权利。
    application = Application.builder().token(TOKEN).build()  # 创建 Telegram 应用实例并使用 Token 进行身份验证  # Copyright (c) 散小战开发

    application.add_handler(CommandHandler("qq", qq_query))  # 处理 /qq 命令  # 作者频道@SAN869CN
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # 处理普通文本消息  # 作者高级版机器人@Sanxiaozhan886

    application.run_polling()  # 启动 Bot，开始轮询消息  # 版权所有，请勿二改

if __name__ == "__main__":  # 保留所有权利。
    main()  # 启动 main 函数  # Copyright (c) 散小战开发