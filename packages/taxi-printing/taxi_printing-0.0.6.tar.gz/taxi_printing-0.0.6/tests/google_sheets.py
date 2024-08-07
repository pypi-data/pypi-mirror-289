#!/usr/bin/env python
from taxi_printing import google_sheets as sheets
#from taxi_printing import classes as schema
from taxi_printing import data_processor as dp


values: list[list] = sheets.get_range(spreadsheetId="148J47DO_RZe-bbCbN_1yyqHB6MWS9JNKjvjPsg_5wlA",range="Dockets!A2:R",credentials="/home/wayne/sheets-api-credentials.json")

#def get_dockets():






#for _ in filteredlist:

filteredlist = dp.filter_dockets(values,statuses=["Completed","Lodged"])


print(filteredlist[-1].id)