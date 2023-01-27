# 1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
# за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re

text_x = "Rbbbr RRbbrr,b,odfbk Rrbbb., , ' ' gjkerjgeokr rbbbbbr\n guigi. Rbbbbbbbbbbrr Rr"

pattern = r"Rb+r"

result = re.findall(pattern, text_x)

if result:
    print(result)
else:
    print("pattern not found")

# 2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

card = "7878 0239 8695 4768"


def card_validation(card: str):
    pattern = r"^(\d{4})( |-)?(\d{4})( |-)?(\d{4})( |-)?(\d{4})( |-)?$"
    result = re.search(pattern, card)
    return result


if card_validation(card):
    print("card number is validated")
else:
    print("card number is not validated")

# 3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

str_text = "09hdgj-_dbh04@gmail.com"


def match_email(str_text: str):
    pattern = r"^[A-Za-z0-9]+(\w|(-{1}))\w*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$"
    result = re.search(pattern, str_text)
    return result


if match_email(str_text):
    print(True)
else:
    print(False)


# 4. Напишіть функцію, яка перевіряє правильність логіну.
# Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.

login = "55gky9fo59"


def check_login(login):
    pattern = r"^(\w|\d){2,10}$"
    result = re.search(pattern, login)
    return result


if check_login(login):
    print(True)
else:
    print(False)

#