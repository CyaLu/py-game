#!/usr/bin/env python
#auth:cyalu

import os,logging
base_dir=os.path.dirname(os.path.dirname(__file__))


#操作和错误日志全局配置
logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)


#打印日志
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)

#输出日志文件
fh = logging.FileHandler(base_dir + "/log/game_play.log",encoding='utf-8')
fh.setLevel(logging.INFO)



#配置日志格式
formatter = logging.Formatter('%(asctime)s ：%(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)

#
logger.addHandler(sh)
logger.addHandler(fh)


