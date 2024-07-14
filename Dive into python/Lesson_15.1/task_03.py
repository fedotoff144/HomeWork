"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
MAX_WEIGHT = 1.0
result_lst = []
copy_items = items.copy()

for item in items:
    check_weight = MAX_WEIGHT
    temp_dict = {}

    for key, value in copy_items.items():
        if check_weight - value >= 0:
            temp_dict[key] = value
            check_weight -= copy_items[key]
    copy_items.pop(item)
    result_lst.append(temp_dict)

for i in result_lst:
    print(i)
