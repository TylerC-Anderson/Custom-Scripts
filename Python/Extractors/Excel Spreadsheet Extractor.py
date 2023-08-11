# Excel Spreadsheet Extractor
"""
PURPOSE: This script will be able to take in column names as input, and group the
columns by similar data. For example if emails are given as data for column
"Contact Info", the sheet will group all rows that have the same contact in them.
Script will group all rows with arbitrary amounts of columns with repeat data
together.

Script will output list data which was grouped by those column names to a .txt
file for future processing.

FUTURE GOAL: to use this script as a module to then
output the data directly to the Microsoft Teams app: Tasks by Planner To Do for
automated scheduling.
"""

#TODO Take in excel pages, will need openpyxl module: see URL:
#       https://realpython.com/openpyxl-excel-spreadsheets-python/

#TODO Take in user input for an arbitrary number of column names

#TODO Grouping function: have python recognize the column names, search through them
#       looking for data that is the same and go through the row for each that is
#       the same and group all data for all named columns that is the same. Should
#       perform this recursively so that it will recognize if data it encounters while
#       performing the grouping is repeated, and create a new group for that

#TODO Output to .txt file for now.