import logging
import os
from logging import handlers

class Logger:
    def __init__(self, name: str, show: bool, save: bool = True, debug: bool = False) -> None:
        """
        日志系统

        :param name: 日志系统实例名
        :param show: 是否显示在控制台
        :param save: 是否保存到文件, defaults to True
        :param debug: debug模式, defaults to False
        """
        # 日志文件路径
        normal_log_path = f'logs/normal.log'
        debug_log_path = f'logs/debug.log'
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
        #初始化日志模块，name可以不填，也可填当前日志类别，比如聊天模块、数据库模块等
        self.logger = logging.getLogger(name)
        # 设置日志等级和格式，一旦设置了日志等级，则调用比等级低的日志记录函数则不会输出，当seLevel设置为DEBUG时，可以截获取所有等级的输出
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        # 判断条件，如果存在handlers则不创建，解决日志重复输出问题
        if not self.logger.handlers:
            if show:
                # 控制台 handler
                sh = logging.StreamHandler()
                if debug:
                    sh.setLevel(logging.DEBUG)
                else:
                    sh.setLevel(logging.INFO)
                sh.setFormatter(self.formatter)
                self.logger.addHandler(sh)
            if save:
                # 保存到文件的 handler
                fh_debug = handlers.TimedRotatingFileHandler(
                    filename=debug_log_path,
                    when="D",
                    interval=1,
                    backupCount=3,
                    encoding='utf-8'
                ) # 自动日志切割
                fh_debug.setLevel(logging.DEBUG)
                fh_debug.setFormatter(self.formatter)
                fh = handlers.TimedRotatingFileHandler(
                    filename=normal_log_path,
                    when="D",
                    interval=1,
                    backupCount=3,
                    encoding='utf-8'
                )
                fh.setLevel(logging.INFO)
                fh.setFormatter(self.formatter)
                self.logger.addHandler(fh)
                self.logger.addHandler(fh_debug)

    #
    # 日志接口，用户只需调用这里的接口即可
    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
