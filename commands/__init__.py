__all__ = ['bot_commands']

from aiogram import  filters
from aiogram import  Router
from use_commands import cmd_start, answer, questions, cat, cmd_help, add, quest


def register_user_commands(router: Router) -> None:
    router.message.register(cmd_start, filters.Command(commands=['start']))
    router.message.register(cmd_help, filters.Command(commands=['help']))
    router.message.register(cat, filters.Command(commands=['cat']))
    router.message.register(quest, filters.Command(commands=['quest']))
    router.message.register(add, filters.Command(commands=['add']))
