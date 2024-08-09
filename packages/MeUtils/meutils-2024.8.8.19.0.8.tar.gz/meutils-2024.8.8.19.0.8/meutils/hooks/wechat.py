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


# handler_group_msg
def chat_group_hook(msg, debug: bool = False, send_fn: Callable = None):
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

    if any(flag.lower() in group_name for flag in ['TEST']):
        print(Path('.').resolve())

        # itchat.send(f"FromUserName: {msg.FromUserName}", toUserName=msg.chatroom_id)  # msg.FromUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.chatroom_id)  # ToUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.ToUserName)  # ToUserName
        # itchat.send('@fil@test.ipynb', toUserName=msg.chatroom_id)  # ToUserName

        send_fn('@vid@vidu.mp4', toUserName=msg.chatroom_id)  # ToUserName itchat.send
        # send_fn('@img@vidu.mp4', toUserName=msg.chatroom_id)  # ToUserName
        return None

    # try:
    #     cmsg = WechatMessage(msg, True)
    # except NotImplementedError as e:
    #     logger.debug("[WX]group message {} skipped: {}".format(msg["MsgId"], e))
    #     return None
    # WechatChannel().handle_group(cmsg)
    # return None
