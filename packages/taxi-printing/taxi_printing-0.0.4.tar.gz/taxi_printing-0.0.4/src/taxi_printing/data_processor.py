#!/usr/bin/env python

def dockets_from_range(record):
    import datetime
    from taxi_printing import dollars_to_words as convert
    from taxi_printing import classes as schema
    # class columns:
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
    columns = schema.columns()
    newdocket = schema.docket()
    newdocket.account = record[columns.account]
    newdocket.date = record[columns.date]
    newdocket.type = record[columns.type]
    newdocket.job = record[columns.job]
    newdocket.account = record[columns.account]
    newdocket.order = record[columns.order]
    newdocket.reference = record[columns.reference]
    newdocket.start  = record[columns.start]
    newdocket.finish  = record[columns.finish]
    newdocket.name = record[columns.name]
    newdocket.pickup = record[columns.pickup]
    newdocket.destination = record[columns.destination]
    newdocket.meter = record[columns.meter]
    newdocket.surcharge = record[columns.surcharge]
    newdocket.extras = record[columns.extras]
    newdocket.tss = record[columns.tss]
    newdocket.owing = record[columns.owing]
    newdocket.car = record[columns.car]
    newdocket.status = record[columns.status]
    newdocket.dollarswords, newdocket.centswords = convert.dollars2words(float(str(record[columns.owing]).lstrip("$")))

    return newdocket

