from taxi_printing import google_sheets as sheets

values: list[list] = sheets.get_range(spreadsheetId="148J47DO_RZe-bbCbN_1yyqHB6MWS9JNKjvjPsg_5wlA",range="Dockets!A:Q",credentials="/home/wayne/sheets-api-credentials.json")