#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
from argparse import ArgumentParser
import sqlite3

from base.func_report_reminder import ReportReminder
from configuration import Config
from constants import ChatType
from robot import Robot, __version__
from wcferry import Wcf


def main(chat_type: int):
    config = Config()
    wcf = Wcf(debug=True)
    print(wcf.get_msg_types())
    def handler(sig, frame):
        wcf.cleanup()  # 退出前清理环境
        exit(0)

    signal.signal(signal.SIGINT, handler)
    user_database=sqlite3.connect("Contact.db")
    cor=user_database.cursor()
    robot = Robot(config, wcf, chat_type)
    robot.LOG.info(f"WeChatRobot【{__version__}】成功启动···")
    for key,value in robot.getAllContacts().items():
        if (cor.execute("SELECT * FROM Contacts WHERE wxid=?",(key,)).fetchall())==[]:
            cor.execute("INSERT INTO Contacts VALUES (?,?)",(key,value))

    # 机器人启动发送测试消息
    user_database.commit()
    user_database.close()
    robot.sendTextMsg("机器人启动成功！", "filehelper")

    # 接收消息
    # robot.enableRecvMsg()     # 可能会丢消息？
    robot.enableReceivingMsg()  # 加队列

    # 每天 7 点发送天气预报

    # 让机器人一直跑
    robot.keepRunningAndBlockProcess()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-c', type=int, default=0, help=f'选择模型参数序号: {ChatType.help_hint()}')
    args = parser.parse_args().c
    main(args)
