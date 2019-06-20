""" Connections to databases """
import sys
import os
from template.capture_of_event import send_the_event, event_error
from template.html import html_two


def accessdatabases(server: str, database: str, user: str, password: str, cuenta: str):
    import pyodbc

    """ Personal connection string """
    try:
        connection_string = "DRIVER={ODBC Driver 13 for SQL Server};" \
                        "SERVER=" + server + ";DATABASE=" + database + ";UID=" + user + ";PWD=" + password

        con = pyodbc.connect(connection_string)

        return con

    except Exception:
        print("--" * 5, ">", " ¡Warning!. Please you review the file info_event_log.csv.", "\n")
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = database

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, server)
        send_the_event(7, body_html=a, cuenta=cuenta)
