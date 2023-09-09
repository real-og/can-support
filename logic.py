from aiogram import types
import redis

def add_header(form, id, username=None):
    header = str(id)
    if username:
        header += f' {username}'
    return header + ' \n' + form

def add_header_to_mes(mes: types.Message) -> types.Message:
    username = 'юзернейма нет'
    if mes.from_user.username:
        username = mes.from_user.username
    header = f"{mes.from_id} {username}\n"
    if mes.caption:
        mes.caption = header + mes.caption
    elif mes.text:
        mes.text = header + mes.text
    else:
        mes.caption = header
    return mes

def get_all_redis_keys():
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=6)  # Замените параметры на свои, если они отличаются

# Получите все ключи из базы данных
    keys = redis_client.keys('*')
    formatted_keys = []
    for key in keys:
        text_string = key.decode('utf-8')
        parts = text_string.split(':')
        formatted_keys.append(int(parts[2]))

    return formatted_keys