from aiogram import types

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