import individual_score as inds

from openpyxl import Workbook, load_workbook

wb = load_workbook('score_card.xlsx')

ws = wb.active

for row in range(2,ws.max_row+1):
    s = str(ws['G'+str(row)].value)
    new_score = inds.get_score(s)
    ws["H"+str(row)].value = int(new_score)
    
wb.save('score_card.xlsx')
