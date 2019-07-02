

def insertsqlserver(data, server, database, user, password, driver, table, scheme, msg_error_avoid_inserting=None,
                    cuenta=' ', path_to_move=' '):
    import sqlalchemy
    import os
    import sys
    from template.capture_of_event import event_error, send_the_event
    from template.html import html_two
    import logging

    print("#" * 5, " ¡Preparing the sql server connection string! ")
    engine = sqlalchemy.create_engine("mssql+pyodbc://" + user + ":" + password + "@" + server
                                      + ":1433/" + database + "?driver=" + driver, pool_size=0,
                                      max_overflow=-1, )
    try:

        logging.info('Start "def insertsqlserver".')
        if msg_error_avoid_inserting is None or msg_error_avoid_inserting == 1:
            print("#" * 5, " ¡Inserting data in {0}! ".format(table))
            data.to_sql(table, engine, schema=scheme, if_exists='append', chunksize=50, index=False)
            print("#" * 5, " ¡Insert successful! ", "\n")

        else:

            print("--" * 5, ">", " ¡There were problems deleting rows. The insertion will be avoided. {0}! ".format(table))

    except Exception:

        print("--" * 5, ">", " ¡Warning!. Please you review the file info_event_log.csv.", "\n")
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")
        logging.exception(f'Watch out. Exist a exception in this process "def insertsqlserver" {type_class}')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = table

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)
