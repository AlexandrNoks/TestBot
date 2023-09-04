from aiogram import Dispatcher
from .chat_subscriber import IsSubscriber
from .filter_group import IsAdminGroup,IsUserGroup,IsUserBanned
from .filter_private_chat import IsPrivateChat,IsNewUser,IsUserLeftChat




def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdminGroup)
    dp.filters_factory.bind(IsUserGroup)
    dp.filters_factory.bind(IsUserBanned)

    dp.filters_factory.bind(IsPrivateChat)
    dp.filters_factory.bind(IsNewUser)
    dp.filters_factory.bind(IsUserLeftChat)


