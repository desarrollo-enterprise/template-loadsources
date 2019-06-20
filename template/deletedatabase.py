"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""
def deletetable(typedelte: int, namefile: str, server: str, database: str, user: str, password: str,
                nametable: str, scheme: str, columncriteriondelete: str, cuenta = '', path_to_move= ''):

    from model.setting_access_database import accessdatabases
    from template.capture_of_event import event_error
    import os, sys
    import re
    from template.html import html_two
    from template.capture_of_event import send_the_event

    print("#" * 5, "Step: Delete!")
    try:
        if typedelte == 0:
            c = accessdatabases(server, database, user, password)

            date_of_file = re.sub("\D", "", namefile)

            cursor = c.cursor()
            query_delete = "DELETE " + scheme + "." + nametable + " WHERE " + columncriteriondelete + " = ?" + \
                           " AND Fecha >= DATEADD(DAY, -15, " + "'" + date_of_file + "'" + ")" + \
                           " AND Fecha < DATEADD(DAY, 15, " + "'" + date_of_file + "'" + ")"

            with cursor.execute(query_delete, namefile):
                print("#" * 5, "Data deletes {0} with filter {1}!".format(nametable, namefile))
            c.close()

        if typedelte == 1:
            c = accessdatabases(server, database, user, password)

            date_of_file = re.sub("\D", "", namefile)

            cursor = c.cursor()
            query_delete = "DELETE " + scheme + "." + nametable + " WHERE " + columncriteriondelete + " = ?" + \
                           " AND Fecha >= DATEADD(DAY, -15, " + "'" + date_of_file + "'" + ")" + \
                           " AND Fecha < DATEADD(DAY, 15, " + "'" + date_of_file + "'" + ")"

            with cursor.execute(query_delete, namefile):
                print("#" * 5, "Data deletes {0} with filter {1}!".format(nametable, namefile), "\n")
            c.close()
        msg_error_avoid_inserting = 1
        return msg_error_avoid_inserting

    except Exception:
        print("ALERT!!!! It doesn't could to process. Please you review the file info_event_log.csv")
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = nametable
        msg_error_avoid_inserting = 0

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)

        return msg_error_avoid_inserting
