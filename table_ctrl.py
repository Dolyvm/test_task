from datetime import datetime

import gspread
from gspread import worksheet
from config import table_link, table_id

table = table_link
id_table = table_id

#Открываем таблицу, и нужный лист
gc = gspread.service_account(filename="doltest.json")

sh = gc.open("doltestt")

worksheet = sh.get_worksheet(0)

#Получаем значения ячейки А2
def get_a2():
    cell_value = worksheet.acell('A2').value
    return cell_value

#Проверяем дату на корректность
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False

#Обновляем в таблице столбец B
def update_table(date_str):
    next_row = len(worksheet.col_values(2)) + 1
    worksheet.update_cell(next_row, 2, date_str)

