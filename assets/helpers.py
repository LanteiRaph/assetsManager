from django.db import connection


#returns an sql for retriving request detail report.
def get_report_sql():
    #Compile a comprihensive sql to return the report data:
    #reoprt data should produce the hard copy version almost 89%
    #get the maximun date for each return date this equites to the current condition dates.
    max_date = ("SELECT Max(returndetail.date_in) AS date_in, requestdetail.request_detail "
    "FROM returndetail INNER JOIN requestdetail ON returndetail.return_detail = requestdetail.return_detail "
    "GROUP BY requestdetail.request_detail")

    #Compile the condition on the max date: the current condition
    conditionOnMaxDate = ("SELECT situation.description, situation.equipment "
    "FROM situation INNER JOIN (" + max_date + " )as max_date ON situation.date = max_date.date_in")

    #Compile the reports sql
    reportsSql = ("SELECT "
    "make.name, "
    "requestdetail.qty, "
    "situation_.description, "
    "returndetail.date_in "
    "FROM requestdetail LEFT JOIN "
    "returndetail on requestdetail.request_detail = returndetail.return_detail INNER JOIN "
    "equipment on requestdetail.equipment=equipment.equipment INNER JOIN "
    "make on equipment.make=make.make LEFT JOIN (" + conditionOnMaxDate
    + ") as situation_ on equipment.equipment= situation_.equipment"
    " where requestdetail.request = %s ")

    return reportsSql


#Helper function to run Raw sql aganist the current database.
def raw_query_sql(sql, params):
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        row = cursor.fetchall()
    return row