#!/usr/bin/env python
from taxi_printing import google_sheets as sheets
from taxi_printing import dollars_to_words as convert
import datetime

# class docketcolumns:
#     date: int = 0
#     type: int = 1
#     job: int = 2
#     account: int = 3
#     order: int = 4
#     reference: int = 5
#     start: int = 6
#     finish: int = 7
#     name: int = 8
#     pickup: int = 9
#     destination: int = 10
#     meter: int = 11
#     surcharge: int = 12
#     extras: int = 13
#     tss: int = 14
#     owing: int = 15
#     car: int = 16
#     status: int = 17

# class docket:
#     date: datetime
#     type: str
#     job: int
#     account: str
#     order: str
#     reference: str
#     start: datetime
#     finish: datetime
#     name: str
#     pickup: str
#     destination: str
#     meter: float
#     surcharge: float
#     extras: float
#     tss: float
#     owing: float
#     car: int
#     status: str
#     dollarswords: str
#     centswords: str

values: list[docket] = sheets.get_range(spreadsheetId="148J47DO_RZe-bbCbN_1yyqHB6MWS9JNKjvjPsg_5wlA",range="Dockets!A2:R",credentials="/home/wayne/sheets-api-credentials.json")

#def get_dockets():
filteredlist: list[docket] = []

for row in values:
#    print(row[docketcolumns.status])
    if row[docketcolumns.status] == "Completed":
#        print(f"{row[docketcolumns.date]} {row[docketcolumns.name]} {row[docketcolumns.owing]} {row[docketcolumns.status]}")
        
        # newrow = docket()
        # newrow.account = row[docketcolumns.account]
        # newrow.date = row[docketcolumns.date]
        # newrow.type = row[docketcolumns.type]
        # newrow.job = row[docketcolumns.job]
        # newrow.account = row[docketcolumns.account]
        # newrow.order = row[docketcolumns.order]
        # newrow.reference = row[docketcolumns.reference]
        # newrow.start  = row[docketcolumns.start]
        # newrow.finish  = row[docketcolumns.finish]
        # newrow.name = row[docketcolumns.name]
        # newrow.pickup = row[docketcolumns.pickup]
        # newrow.destination = row[docketcolumns.destination]
        # newrow.meter = row[docketcolumns.meter]
        # newrow.surcharge = row[docketcolumns.surcharge]
        # newrow.extras = row[docketcolumns.extras]
        # newrow.tss = row[docketcolumns.tss]
        # newrow.owing = row[docketcolumns.owing]
        # newrow.car = row[docketcolumns.car]
        # newrow.status = row[docketcolumns.status]
        # newrow.dollarswords, newrow.centswords = convert.dollars2words(float(str(row[docketcolumns.owing]).lstrip("$")))
        

    
        


        filteredlist += [newrow]
for _ in filteredlist:
    print(_.date)