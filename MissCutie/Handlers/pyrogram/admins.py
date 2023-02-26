from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from MissCutie import OWNER_ID, DEV_USERS, pbot


def can_change_info(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in DEV_USERS:
            return await func(_, message)

        check = await pbot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "KITNI BAAR BOLU TUM admin NAHI HO"
            )

        admin = (
            await pbot.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_change_info:
            return await func(_, message)
        else:
            return await message.reply_text(
                "`TUMHARE PASS  permissions NAHI HAI change group info KA PAHLE LEKAR AOO."
            )

    return non_admin


def can_restrict(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in OWNER_ID:
            return await func(_, message)

        check = await pbot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "KITNI BAAR BOLU TUM ADMIN NAHI HO ."
            )

        admin = (
            await pbot.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_restrict_members:
            return await func(_, message)
        else:
            return await message.reply_text(
                " TUMAHRE PASS permissions NAHI KI TUM KISE  users KO BAN KAR SAKO in this chat."
            )

    return non_admin
