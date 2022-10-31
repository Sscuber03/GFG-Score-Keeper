# this program gets the list of user profile link from an excel sheet, and add their updated marks to the excel sheet itself.
# it is assumed that only one row is used for the heading, and is always present in the excel file.
# close the excel file if it is open in your machine, otherwise, it will not run.

import individual_score as inds

from openpyxl import Workbook, load_workbook

wb = load_workbook('Scorecard_october_end.xlsx') # replace 'Scorecard_october_end.xlsx' with the path including the file name of the excel file of the student info

ws = wb.active

for row in range(2,ws.max_row+1):
    s = str(ws['H'+str(row)].value) # replace 'H' with the column name containing the gfg profile links. Full links should be added in the excel file for this to work.
    new_score = inds.get_score(s)
    if new_score == '_ _':
        ws["J"+str(row)].value = 0 # replace 'J' with the column where you have to write the current total score obtained by the student
    else:
        ws["J"+str(row)].value = int(new_score) # replace 'J' with the column where you have to write the current total score obtained by the student
    wb.save('Scorecard_october_end.xlsx') # replace 'Scorecard_october_end.xlsx' with the path including the file name of the excel file of the student info
    
wb.save('Scorecard_october_end.xlsx') # replace 'Scorecard_october_end.xlsx' with the path including the file name of the excel file of the student info
