#main
import function

secure_level = function.select_secure_level()
if secure_level:
    password_length = function.select_Password_length()
    password = function.get_Password_string(secure_level, password_length)
    print(password)
    function.copy_to_clipboard(password)