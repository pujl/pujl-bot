import random
from .utils import Utils
from .logger import Logger

# 实例化类
logger = Logger(name='words',show=True)
utils = Utils()

# 读取 ohayo.json 这个词库
ohayo_words = utils.load_words('ohayo')

class GetWords():
    def __init__(self):
        """
        该类用于提取消息特定文本，或是返回特定文本
        """
        logger.debug('实例化GetWords')
        self.ohayo = ohayo_words

    def get_ohayo(self) -> str:
        '''返回早安问候句子'''
        word =  random.choice(self.ohayo)
        logger.debug(f'获取到早安:{word}')
        return word
