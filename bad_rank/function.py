#function
import openpyxl

def get_match_result(column):
    x = [cell.value for cell in column[1:]]
    return x

def reshape_ranking(sheet, winners, challengers, defenders):
    for winner, defender, challenger in zip(winners, defenders, challengers):
        if winner == challenger:
            for row_number1, row_challenger in enumerate(sheet['B'], start = 2):
                if row_challenger.value == challenger:
                    sheet.delete_rows(row_number1 - 1)
                    break
            
            for row_number2, row_defender in enumerate(sheet['B'], start = 2):
                if row_defender.value == defender:
                    sheet.insert_rows(row_number2 - 1)
                    sheet.cell(row_number2 - 1, column = 2, value = challenger)
                    break

def allocate_rank_number(sheet):
    i = 1
    for cell in sheet['A'][1:]:
        cell.value = i
        i += 1

def update_ranking(file_name):
    wb = openpyxl.load_workbook(file_name)
    sheet1 = wb['rank']
    sheet2 = wb['matches']
    
    winners = get_match_result(sheet2['D'])
    challengers = get_match_result(sheet2['C'])
    defenders = get_match_result(sheet2['A'])
    
    reshape_ranking(sheet1, winners, challengers, defenders)
    allocate_rank_number(sheet1)
    
    wb.save(file_name)