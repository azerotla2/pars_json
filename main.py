import json
import re

date_operations_dict = {}


def date_formatter(date):
    return re.sub(r'(\d{4})-(\d\d)-(\d\d)(.*)', r'\3.\2.\1', date)


def card_from_formatter(card):
    card_number = re.search(r'\d{16,20}', card)
    length_card = len(card_number[0])
    if length_card == 20:
        return re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})(\d{4})', r'\1 \2** **** **** \6', card)
    elif length_card == 16:
        return re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})', r'\1 \2** **** \5', card)
    else:
        return "unrecognized card format"


def card_to_formatter(card):
    return re.sub(r'(\d{12,16})(\d{4})', r'**\2', card)


def print_formatter_opertions(count_operation):
    list_dates = list(date_operations_dict)

    for i in range(count_operation):
        oldest_date = min(list_dates)

        print(
            f"{date_formatter(date_operations_dict[oldest_date]['date'])} {date_operations_dict[oldest_date]['description']} \n"
            f"{card_from_formatter(date_operations_dict[oldest_date]['from'])} -> {card_to_formatter(date_operations_dict[oldest_date]['to'])} \n"
            f"{date_operations_dict[oldest_date]['operationAmount']['amount']} {date_operations_dict[oldest_date]['operationAmount']['currency']['name']} \n")
        list_dates.remove(oldest_date)


with open('data/operations.json', 'r', encoding='utf-8') as f:
    operations = json.load(f)

for operation in operations:
    if 'state' in operation and operation['state'] == 'EXECUTED' and 'from' in operation:
        date_operations_dict[operation['date']] = operation
else:
    count_executed_operation = 5
    print_formatter_opertions(count_executed_operation)
