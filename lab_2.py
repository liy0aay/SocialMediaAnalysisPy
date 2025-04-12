# Парсинг сообщений с Telegram-каналов о Франции, очистка от эмодзи для дальнейшего анализа

from telethon import TelegramClient
import pandas as pd
from dotenv import load_dotenv
import os
import asyncio
import re


load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
channel_list = ['marie_paris', 'notesdedenis', 'tanya_in_france', 'bonjourcroissant', 'french_irene']


def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # смайлики
        u"\U0001F300-\U0001F5FF"  # символы
        u"\U0001F680-\U0001F6FF"  # транспорт
        u"\U0001F1E0-\U0001F1FF"  # флаги
        u"\U00002700-\U000027BF"  # доп. символы
        u"\U0001F900-\U0001F9FF"  # расширенные
        u"\U00002600-\U000026FF"  # прочее
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)



all_data = pd.DataFrame(columns=['id_post', 'date', 'text', 'views', 'reactions', 'comments', 'channel'])


async def main(name_chanel, API_ID, API_HASH):
    #авторизация клиента
    async with TelegramClient('session', API_ID, API_HASH) as client:
      #получение сообщений из канала
      messages = await client.get_messages(name_chanel, limit=None)  # limit=None для получения всех сообщений
      return messages
    
# проходимся по каждому каналу
for channel in channel_list:
    messages = asyncio.run(main(channel, API_ID, API_HASH))
    # проходимся по каждому посту
    for i, message in enumerate(messages):
        if message.text:
            # получаем суммарное кол-во всех реакций
            count_reactions = sum([r.count for r in message.reactions.results]) if message.reactions else 0
            # получаем кол-во комментов
            count_replies = message.replies.replies if message.replies else 0

            # записываем все в DataFrame
            all_data.loc[len(all_data)] = [
                message.id,
                message.date,
                message.text,
                message.views,
                count_reactions,
                count_replies,
                channel
            ]

# удаляем смайлики
all_data['text'] = all_data['text'].apply(remove_emoji)

#выводим 5 первых записей
print(all_data.tail(5))
all_data.to_csv("messages.csv", index=False, encoding='utf-8-sig')
