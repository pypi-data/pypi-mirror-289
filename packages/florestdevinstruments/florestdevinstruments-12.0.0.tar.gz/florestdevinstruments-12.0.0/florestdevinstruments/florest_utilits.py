# -*- coding: utf-8 -*-

"""Всякие утилиты для работы с ИИ и RCON!"""
import g4f.client
from rcon.source import Client
from g4f.Provider import Bing
from MukeshAPI import api
import g4f
import requests
from typing import Union
import time, pyautogui
import googletrans
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ai_text(prompt: str) -> str:
    """Попросите ИИ написать Вам любой текст на Ваш вкус по запросу."""
    response = g4f.client.Client().chat.completions.create(model='gpt-4o', messages=[{"role": "user", "content": prompt}], provider=Bing)
    return response.choices[0].message.content

def ai_image(prompt: str) -> bytes:
    """Попросите ИИ нарисовать картинку по Вашему запросу.\n\nВНИМАНИЕ! МОГУТ БЫТЬ НЕТОЧНОСТИ, ЖЕЛАТЕЛЬНО ВВОДИТЬ СВОЙ ЗАПРОС НА АНГЛИЙСКОМ ЯЗЫКЕ.\nФункция возвращает тип `bytes`.\nВот примерчик использования: ```with open('file.png', 'rb') as file:\nfile.write(ai_image('Draw a car.'))\nfile.close()```"""
    return api.ai_image(prompt)

def rcon_connect(host: str, passwd: str, port: int, command: str, arg1: str = None, arg2: str = None):
    """Взаимодействуйте с RCON с помощью данной функции.\nhost: IP/Домен сервера.\npasswd: RCON пароль сервера.\ncommand: Команда, которую надо прописать.\narg1, arg2 - необязательные аргументы."""
    with Client(host, port, passwd=passwd) as server:
        server.run(command, arg1, arg2)

def ip_deanon(ip: str) -> Union[list, str]:
    """Пробейте IP с помощью данной функции.\nВозвращает `list` при удачной завершении операции."""
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        return f'Произошла ошибка 404. Возможно, это проблема с сайтом, которую мы используем для пробива.'
    results = response.json()
    if results['status'] == 'fail':
        return f'Не удалось пробить IP адрес, который был введен в аргумент `ip`.'
    record = []
    for key, value in results.items():
        record.append(f"[{key.title()}]: {value}")
    return record

def spamer(text: Union[str, list], time1: float = 5):
    """Спамер на Python, которого можно юзать в различных мессенджерах.\ntext: текст, которым будет спамить спамер. Или даже список.\ntime: время, через которое начинается исполнение программы после запуска в секундах. По умолчанию, 5 секунд."""
    if isinstance(text, str):
        time.sleep(time1)
        while True:
            pyautogui.write(text)
            pyautogui.press('enter')
    if isinstance(text, list):
        time.sleep(time1)
        while True:
            for _ in text:
                pyautogui.write(_)
                pyautogui.press('enter')
            print(f'Мы перебрали {str(len(text))} элементов из списка. Повторяем...')

def translate(text: Union[str, list], lang: str) -> Union[str, list]:
    """Перевести текст, или список текстов на какой-либо язык.\ntext: текст, или список текстов, который пренадлежит к переводу.\nlang: язык, на который надо перевести текст, или список текстов."""
    if isinstance(text, str):
        trans_result = googletrans.Translator().translate(text, lang).text
        return trans_result
    if isinstance(text, list):
        results = []
        for _ in text:
            trans_result_one = googletrans.Translator().translate(_, lang).text
            results.append(trans_result_one)
        return results
    
def send_email(login: str, passwd: str, title: str, text: str, to_addr: str) -> bool:
    """Отправьте письмо, используя MAIL.RU API.\nlogin: адрес вашей электронной электронной почты на MAIL.RU (это ваш логин).\npasswd: токен от MAIL.RU API. [Подробнее...](https://api.mail.ru/docs/)\ntitle: заголовок письма.\ntext: остальная часть письма.\nto_addr: адрес электронной почты получателя."""
    msg = MIMEMultipart()
 
    msg["From"] = login
    msg["To"] = to_addr
    msg["Subject"] = title
 
    msg.attach(MIMEText(text, "plain"))
    with smtplib.SMTP('smtp.mail.ru', 465) as server:
        server.login(login, passwd)
        server.sendmail(login, to_addr, msg.as_string())
        server.quit()
        return True
