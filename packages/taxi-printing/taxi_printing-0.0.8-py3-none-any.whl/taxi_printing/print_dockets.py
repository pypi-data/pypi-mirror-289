#!/usr/bin/env python
from taxi_printing import classes as schema

spreadsheetId = "148J47DO_RZe-bbCbN_1yyqHB6MWS9JNKjvjPsg_5wlA"
spreadsheetRange = "Dockets!A2:W"
apicredentials = "/home/wayne/sheets-api-credentials.json"
docketstatuses = ["Completed","Lodged"]
dockettemplate = "/home/wayne/Documents/print dockets.docx"
pdfdir = "/tmp/taxi_printing"

def get_dockets() -> list[schema.docket]:
    from taxi_printing import google_sheets as sheets
    from taxi_printing import data_processor as dp

    values: list[list] = sheets.get_range(spreadsheetId,range=spreadsheetRange,credentials=apicredentials)

    return dp.filter_dockets(values,statuses=docketstatuses)

def generate_pdfs(pdfdir: str, dockets: list[schema.docket]) -> None:
    for docket in dockets:
        import aspose.words as aw

        fields = [
            "Dollar_words",
            "Docket_Type",
            "Amount_Owing",
            "Paid_by_PassengerTSS",
            "Extras",
            "Meter_Total",
            "Cents_words",
            "Destination_Area",
            "Pickup_Area",
            "Passenger_Name",
            "Order_Number",
            "Job_Number",
            "Date",
            "Finish_Time",
            "Start_Time",
            "Car_Number",
            "DA",
            "ABN",
            "Driver",
            "Account_Number"
            ]
        values = [
            docket.dollarswords,
            docket.type,
            docket.owing,
            docket.tss,
            docket.extras,
            docket.meter,
            docket.centswords,
            docket.destination,
            docket.pickup,
            docket.name,
            docket.order,
            docket.job,
            docket.date,
            docket.finish,
            docket.start,
            docket.car,
            docket.da,
            docket.abn,
            docket.driver,
            docket.account
            ]

        doc = aw.Document(dockettemplate)
        doc.mail_merge.execute(fields, values)
        doc.save(f"{pdfdir}/{docket.job}.pdf")

if __name__ == "__main__":
    import os

    dockets: list[schema.docket] = get_dockets()

    # Make pdfdir
    if not os.path.exists(pdfdir):
        os.makedirs(pdfdir)

    generate_pdfs(pdfdir, dockets)

    # delete pdfdir
    os.removedirs(pdfdir)

    