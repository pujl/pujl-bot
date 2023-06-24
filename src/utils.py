import yaml
import os
from .logger import Logger
import json

# 实例化类
logger = Logger(name='words',show=True)

class Utils:
    '''该类用于设置一些辅助的方法'''

    def __init__(self) -> None:
        logger.info('实例化Utils')
        pass

    def read_config(self,config_name: str) -> dict:
        '''读取配置'''
        config_path = os.path.abspath(os.path.join(os.getcwd(), config_name))
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        logger.info(f'已载入配置{config_name}')
        return config

    def load_words(self, words: str):
        '''读取并加载词库'''
        words_path = os.path.join(
            os.getcwd(), 'data', 'words', f'{words}.json')
        try:
            with open(words_path, 'r',encoding='utf-8') as f:
                the_words_json = json.load(f)
            logger.info(f'已载入词库：{words_path}')
            return the_words_json
        except Exception as e:
            logger.error(f'载入词库出错：{words_path}, {e}')
            return {'Exception': 'except'}
