#!/usr/bin/env python
import datetime

class columns:
    date: int = 0
    type: int = 1
    job: int = 2
    account: int = 3
    order: int = 4
    reference: int = 5
    start: int = 6
    finish: int = 7
    name: int = 8
    pickup: int = 9
    destination: int = 10
    meter: int = 11
    surcharge: int = 12
    extras: int = 13
    tss: int = 14
    owing: int = 15
    car: int = 16
    status: int = 17
    lodgement: int = 18
    statement: int = 19
    driver: int = 20
    da: int = 21
    abn: int = 22

class docket:
    date: datetime
    type: str
    job: int
    account: str
    order: str
    reference: str
    start: datetime
    finish: datetime
    name: str
    pickup: str
    destination: str
    meter: float
    surcharge: float
    extras: float
    tss: float
    owing: float
    car: int
    status: str
    lodgement: datetime
    statement: datetime
    driver: str
    da: int
    abn: int
    dollarswords: str
    centswords: str