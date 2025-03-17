import logging,os  # 引入logging模块
from logging import handlers

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射
    def __init__(self,filename,level='info',when='MIDNIGHT',backCount=10,fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往控制台输出
        sh.setFormatter(format_str) #设置控制台上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,interval=1,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.suffix = "%Y-%m-%d.log" #设置文件后缀
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
    
    def info(self, msg,*args,**kwargs):
        self.logger.info(msg,*args,**kwargs)
    def debug(self, msg,*args,**kwargs):
        self.logger.debug(msg,*args,**kwargs)
    def warning(self, msg,*args,**kwargs):
        self.logger.warning(msg,*args,**kwargs)
    def error(self, msg,*args,**kwargs):
        self.logger.error(msg,*args,**kwargs)
    def critical(self, msg,*args,**kwargs):
        self.logger.critical(msg,*args,**kwargs)
    def exception(self, msg,*args,**kwargs):
        self.logger.exception(msg,*args,**kwargs)
