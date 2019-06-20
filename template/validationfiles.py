"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""


def validate(dataf, findfile: str, cuenta ='', path_to_move=''):
    global permit
    import pandas as pd
    import re
    from datetime import datetime
    from template.capture_of_event import event_error, send_the_event
    import os
    import sys
    from template.html import html_one, html_two

    """ Count files and columns """
    rows_num = len(dataf)
    columns_num = len(dataf.columns)
    date_log = datetime.now()

    """ Validate date of the name of file with the date of the content."""
    date_of_file = re.sub("\D", "", findfile)
    try:
        date_of_file = datetime.strptime(
            (str(date_of_file[:4]) + '-' + str(date_of_file[4:6]) + '-' + str(date_of_file[6:])),
            '%Y-%m-%d').date()
        get_only_date = dataf['Fecha'].astype('datetime64[D]').unique()
        for d in get_only_date:
            date_content_file = datetime.strptime(str(d)[:10], '%Y-%m-%d').date()
            if date_content_file == date_of_file:
                print("Th dates are equals.")
                permit = 1
            else:
                a = html_one().format(findfile, date_content_file, path_to_move)
                send_the_event(6, body_html=a, cuenta=cuenta)
                print("La fecha del nombre del archivo no corresponde a la fecha que contiene el archivo.")
                permit = 0
        if os.path.exists(r'logs\info_base_log.csv'):
            info_base_log = {'date': [], 'file_name': [], 'rows_num': [], 'columns_num': []}
            info_base_log['date'].append(date_log)
            info_base_log['file_name'].append(findfile)
            info_base_log['rows_num'].append(rows_num)
            info_base_log['columns_num'].append(columns_num)
            info_base_log = pd.DataFrame(data=info_base_log)
            info_base_log.to_csv(r'logs\info_base_log.csv', index=False, sep=';', mode='a', header=False,
                                 encoding='Latin-1')
        else:
            info_base_log = {'date': [], 'file_name': [], 'rows_num': [], 'columns_num': []}
            info_base_log['date'].append(date_log)
            info_base_log['file_name'].append(findfile)
            info_base_log['rows_num'].append(rows_num)
            info_base_log['columns_num'].append(columns_num)
            info_base_log = pd.DataFrame(data=info_base_log)
            info_base_log.to_csv(r'logs\info_base_log.csv', index=False, sep=';', encoding='Latin-1')

        return permit

    except Exception:

        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = findfile

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)
        permit = 0
        return permit
