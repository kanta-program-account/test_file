#function
import string
import secrets
import pyperclip

def select_secure_level():
    secure_level = int(input('生成するパスワードのセキュリティレベルを入力してください\n（0:弱, 1:中, 2:強）：'))
    if secure_level < 0 or 2 < secure_level:
        print('入力に誤りがあります。')
        return False
    return secure_level

def select_Password_length():
    Password_length = int(input('パスワードの長さを指定してください：'))
    return Password_length

def get_Password_string(secure_level, Password_length):
    if secure_level == 0:
        pass_chars = string.ascii_letters
        password = ''.join(secrets.choice(pass_chars) for x in range(Password_length))#forはjoin関数の中
        return password
    
    elif secure_level == 1:
        pass_chars = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(pass_chars) for x in range(Password_length))#forはjoin関数の中
        return password
    
    elif secure_level == 2:
        pass_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(pass_chars) for x in range(Password_length))#forはjoin関数の中
        return password
    
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print('パスワードがクリップボードにコピーされました！')
        