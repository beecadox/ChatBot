import re
from word2number import w2n

prices_en = {
    "kabsad": 4, "avot": 3, "torc": 5, "chick": 7, "avol": 8, "taco": 5, "toast": 3, "eggu": 4, "scram": 5, "caku": 4,
    "cupcake": 2, "cm": 5, "green": 4, "red": 4, "purple": 4, "sauce": 1, "bread": 1
}


def check_if_food_item(user_input):
    checked_price = 0
    food_flag = 0
    # cleaning user input
    user_input.replace(",", " ")
    user_input = re.sub(r"[^\w\s]", '', user_input)
    user_input = re.sub(r"\s+", ' ', user_input)
    tokens = user_input.split()
    length = len(tokens)
    if length >= 2:
        for i in range(0, length):
            food_code = tokens[i]
            if food_code in prices_en:
                tmp_price = prices_en.get(food_code)
                food_flag = 1
                if i + 1 < len(tokens):
                    if tokens[i + 1].isnumeric():
                        number_of_items = int(tokens[i + 1])
                    elif tokens[i + 1] in prices_en:
                        number_of_items = 1
                    else:
                        try:
                            number_of_items = w2n.word_to_num(tokens[i + 1])
                        except ValueError:
                            number_of_items = 1
                else:
                    number_of_items = 1
                if food_flag == 1:
                    checked_price = checked_price + number_of_items * tmp_price
    else:
        food_code = tokens[0]
        if food_code in prices_en:
            tmp_price = prices_en.get(food_code)
            checked_price = checked_price + tmp_price
    return food_flag, checked_price


def check_if_name(user_input):
    flag = 0
    if user_input.split()[0] == "name":
        flag = 1
    return flag