# -*- coding: utf-8 -*-

"""Модуль для работы с API разных соц. сетей (VK, Discord)"""
import vk_api, discord, pypresence, time, telebot

import vk_api.longpoll

class Discord():
    """Класс для работы с Discord."""
    def presence(id: str, title: str, title2: str, btns: dict, is_time_shared: bool = False):
        """Создайте кастомную активность с кнопками с помощью данной функции.\nid: ID приложения на портале разрабов.\ntitle: первый заголовок.\ntitle2: заголовок ниже первого.\nbtns: кнопки. Пример: {'VK':'https://vk.com', 'YouTube':'https://youtube.com/'}\nis_time_shared: распостранять ли время запуска активности? По умолчанию, False."""
        if is_time_shared:
            profile = pypresence.Presence(id)
            profile.connect()
            profile.update(details=title, state=title2, buttons=btns, start=time.time())
        else:
            profile = pypresence.Presence(id)
            profile.connect()
            profile.update(details=title, state=title2, buttons=btns)
    class WebhookSender:
        """Класс, руководящий вебхуками.\nurl: URL вебхука."""
        def __init__(self, url: str):
            self.webhook = discord.SyncWebhook.from_url(url)
        def send(self, message: str):
            """Отправьте текст с помощью вебхука.\nmessage: текст сообщения."""
            self.webhook.send(message)
        def send_embed(self, embed: discord.Embed):
            """Отправьте эмбед с помощью вебхука.\nembed: ваш эмбед."""
            self.webhook.send(embed=embed)
        def send_picture(self, directory: str, spoiler: bool = False, title: str = None):
            """Отправьте картинку с помощью вебхука.\ndirectory: директория твоей картинки.\nspoiler: нужно-ли поместить картинку в спойлер? По умолчанию, False.\ntitle: надпись, которая будет выше твоей картинки. По умолчанию, None."""
            self.webhook.send(title, file=discord.File(directory, spoiler=spoiler))
class VK:
    """Класс для работы с VK API.\ntoken: токен твоего приложение, которое привязано к сообществу.\nid: id твоего сообщества, которое привязано к сообществу. Пригодится в большинстве случаев."""
    def __init__(self, token: str, id: int):
        self.vk_session = vk_api.VkApi(token=token)
        self.id = id
    def inspect_messages(self):
        """Отслеживайте все сообщения из сообщества."""
        for event in vk_api.longpoll.VkLongPoll(self.vk_session).listen():
            if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW:
                if event.to_me == True:
                    user = self.vk_session.method("users.get", {"user_ids": event.user_id})
                    fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
                    print(f'{fullname} написал(а) сообщение: {event.message}')
    def get_subs(self):
        """Узнать количество подписчиков на сообществе на данный момент."""
        members = self.vk_session.method('groups.getMembers', {'group_id': self.id})
        return len(members['items'])
    def inspect_new_subs(self, text: str, time1: float = 5):
        """Приветствовать новых участников.\ntext: текст, который мы будем отправлять новым подписчикам.\ntime: время, раз в которое начинается следующая проверка. По умолчанию, раз в 5 секунд."""
        previous_followers = self.vk_session.method('groups.getMembers', {'group_id': self.id})['items']
        while True:
        # Проверяем наличие новых подписчиков
            current_followers = self.vk_session.method('groups.getMembers', {'group_id': self.id})['items']
            new_followers = list(set(current_followers) - set(previous_followers))
    
            # Если есть новые подписчики, отправляем им сообщение
            for follower_id in new_followers:
                self.vk_session.method('messages.send', {"user_id":follower_id, "message":text, "random_id":0})

            # Обновляем список подписчиков
            previous_followers = current_followers
    
            # Пауза перед следующей проверкой
            time.sleep(time1)
class Telegram:
    """Класс для работы с Telegram API.\ntoken: токен бота. Его можно получить в [BotFather](https://t.me/BotFather)."""
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)
    def echo_bot(self):
        """Бот, который будет повторять все, что Вы напишите. Как попугай!"""
        @self.bot.message_handler(content_types=['text'])
        def text(message: telebot.types.Message):
            self.bot.reply_to(message, message.text)
        self.bot.infinity_polling()
        return text
    def inspect_new_messages(self):
        """Бот, который будет выводить все сообщения, которому ему напишут."""
        @self.bot.message_handler(content_types=['text'])
        def message_Inpect(message: telebot.types.Message):
            print(f'Новое сообщение от {message.from_user.first_name}: {message.text}')
        self.bot.infinity_polling()
        return message_Inpect
    def inspect_new_group_members(self, group_id: str):
        @self.bot.message_handler(content_types=['new_member_join'], chat_types=['groups'])
        def new_members(message: telebot.types.Message):
            print(f'Новый участник! {message.from_user.first_name}')
        self.bot.infinity_polling()
        return new_members