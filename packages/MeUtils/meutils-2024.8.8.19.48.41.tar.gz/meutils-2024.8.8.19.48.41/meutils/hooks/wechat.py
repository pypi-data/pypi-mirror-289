#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : wechat
# @Time         : 2024/8/8 18:45
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.schemas.wechat_types import Message

os.system("pip install meutils -U --user")


# import importlib
#
# importlib.reload()

# handler_group_msg

# rm -rf wechat_channel.py && python -m wget https://oss.ffire.cc/files/wechat_channel.py
def chat_group_hook(msg, debug: bool = False, send_fn: Callable = None):
    # pip install meutils
    #     os.system("pip install meutils -U --user") 第一次的时候 加缓存 定期更新 并且重载
    logger.debug(msg)
    msg = obj_to_dict(msg)
    msg = Message(**msg)  # filter

    group_name = msg.chatroom_name  # msg.User.NickName
    # msg.ToUserName 加密的群名

    if debug:
        logger.debug(f"群名: {group_name}")
        # logger.debug(msg.model_dump_json(indent=4))
        logger.debug(f"[{type(msg)} => {msg.Type}]")

    # msg.ToUserName， msg.ActualNickName群里机器人的name
    # msg.FromUserName 群id【除非机器人本身发信息，就是他自己的id】

    # 时间内容
    prompt = msg.Content.split(maxsplit=1)[-1]
    if any(flag.lower() in group_name for flag in ['TEST']) or prompt.startswith('视频'):
        # itchat.send(f"FromUserName: {msg.FromUserName}", toUserName=msg.chatroom_id)  # msg.FromUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.chatroom_id)  # ToUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.ToUserName)  # ToUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.chatroom_id)  # ToUserName

        # send_fn('@vid@vidu.mp4', toUserName=msg.chatroom_id)  # ToUserName itchat.send
        # send_fn('@img@vidu.mp4', toUserName=msg.chatroom_id)  # ToUserName

        filename = wget.download('https://oss.ffire.cc/files/vidu.mp4')
        send_fn(f'@vid@{filename}', toUserName=msg.chatroom_id)  # ToUserName itchat.send

        return None

    # try:
    #     cmsg = WechatMessage(msg, True)
    # except NotImplementedError as e:
    #     logger.debug("[WX]group message {} skipped: {}".format(msg["MsgId"], e))
    #     return None
    # WechatChannel().handle_group(cmsg)
    # return None
