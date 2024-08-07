#!/usr/bin/env python
from taxi_printing import classes as schema

def docket_from_record(record) -> schema.docket:
    from taxi_printing import dollars_to_words as convert


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
    newdocket.lodgement = record[columns.lodgement]
    newdocket.statement = record[columns.statement]
    newdocket.driver = record[columns.driver]
    newdocket.da = record[columns.da]
    newdocket.abn = record[columns.abn]
    newdocket.dollarswords, newdocket.centswords = convert.dollars2words(float(str(record[columns.owing]).lstrip("$")))

    return newdocket

def filter_dockets(values: list[list],statuses: tuple) -> list[schema.docket]:
    from taxi_printing import data_processor as dp

    filteredlist: list[schema.docket] = []
    
    for row in values:
        for status in statuses:
            if row[schema.columns.status] == status:    
                filteredlist += [dp.docket_from_record(row)]
    return filteredlist