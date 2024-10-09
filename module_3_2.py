def send_email(message='', recipient='', *, sender="university.help@gmail.com"):
    doman = ('.com', '.ru', '.net')
    if message=='' and recipient=='':
        print(f"Невозможно отправить письмо без сообщения или получателя.")
        exit()
    if (recipient.find('@') != -1 and sender.find('@') != -1) \
            and not (sender.endswith(doman) and recipient.endswith(doman)):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса<{sender}> на адрес <{recipient}>')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
