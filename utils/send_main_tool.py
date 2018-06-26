from users.models import EmailVerify
from random import randint
from django.core.mail import send_mail
from ShangOnline.settings import EMAIL_FROM


def get_random_code(code_length=8):
    code_sources = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += code_sources[randint(0, len(code_sources) - 1)]
    return code


def send_email_verify(email, send_type):
    code = get_random_code()
    if send_type == 'change_email':
        code = get_random_code(4)
    email_ver = EmailVerify()
    email_ver.email = email
    email_ver.send_type = send_type
    email_ver.code = code
    email_ver.save()
    if send_type == 'register':
        send_title = '欢迎注册尚在线'
        send_body = '请点击链接完成激活\nhttp://127.0.0.1:8000/users/active/' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])
    elif send_type == 'forget':
        send_title = '尚在线重置密码功能'
        send_body = '请点击下面链接进行重置密码\nhttp://127.0.0.1:8000/users/user_reset/'+code
        send_mail(send_title, send_body, EMAIL_FROM, [email])
    elif send_type == 'change_email':
        send_title = '尚在线修改邮箱功能'
        send_body = '您的验证码是：' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])