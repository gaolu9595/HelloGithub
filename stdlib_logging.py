#日志模块：如果你想将一些调试（Debugging） 信息或一些重要的信息储存在某个地方
# 以便你可以检查你的程序是否如你所期望那般运行

import os    #os模块用以和操作系统交互
import platform   #Platform模块用以获取操作系统平台信息
import logging  #logging模块用来记录日志信息

if platform.platform().startswith("Windows"):
    logging_file = os.path.join(os.getenv("HOMEDRIVE"),os.getenv('HOMEPATH'),'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.log')

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s : %(levelname)s : %(message)s',
filename=logging_file,
filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
