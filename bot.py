# Update:从Telegram获取更新
from telegram import Update
#ApplicationBuilder:简单立即为构建 bot 对象
#ContextTypes:上下文类型
#CommandHandler:命令处理器
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,filters,MessageHandler
from src.logger import Logger
from src.utils import Utils
from src.words import GetWords

#实例化
getWords = GetWords()
logger = Logger(name='bot', show=True)
utils = Utils()
config = utils.read_config('config.yml')

#响应start命令的函数
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''
    logger.info(f'收到来自{update.effective_chat.username}的/start指令')
    text = '你好~我是pujl编写的bot，目前还在测试阶段'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

async def set_right(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''设置成员权限和头衔，目前该功能不好用，或者不会用'''
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    bot_username_len = len(update._bot.name)
    custom_title = update.effective_message.text[3+bot_username_len:]
    if not custom_title:
        custom_title = update.effective_user.username
    try:
        await context.bot.promote_chat_member(chat_id=chat_id, user_id=user_id, can_manage_chat=True)
        await context.bot.set_chat_administrator_custom_title(chat_id=chat_id, user_id=user_id, custom_title=custom_title)
        text = f'好,你现在是{custom_title}啦'
        await context.bot.send_message(chat_id=chat_id, reply_to_message_id=update.effective_message.id, text=text)
    except:
        await context.bot.send_message(chat_id=chat_id, text='不行!!')

async def ohayo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = getWords.get_ohayo()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应未知命令'''
    logger.debug('调用:unknown')
    text = "我不会这个哦~"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def run():
    logger.info('代码开始运行！')
    start_handler = CommandHandler('start', start)
    set_right_handler = CommandHandler('p', set_right)
    #过滤命令 /早上好等等
    filter_ohayo = filters.Regex('早安|早上好|哦哈哟|ohayo')
    ohayo_handler = MessageHandler(filter_ohayo, ohayo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    # 构建 bot
    TOKEN=config['token']
    application = ApplicationBuilder().token(TOKEN).build()
    # 注册 handler
    application.add_handler(start_handler)
    application.add_handler(set_right_handler)
    application.add_handler(ohayo_handler)
    application.add_handler(unknown_handler)
    # run!
    application.run_polling()


if __name__ == "__main__":
    run()