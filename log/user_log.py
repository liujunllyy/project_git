#coding=utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        # 文件的命名
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d"+".log")
        self.logname = log_dir+"/"+log_file
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志的输出格式
        self.formatter=logging.Formatter('%(asctime)s %(filename)s---> %(lineno)d: %(levelname)s------> %(message)s')
        
    def console(self,level,message):
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()


    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)
