def readxlsx(path: str, type_file: int, sheet: str, index: str):
    import pandas as pd
    import os, sys
    from template.capture_of_event import event_error, send_the_event
    from template.html import html_two
    import logging

    df = globals()
    try:
        logging.info("Paso de lectura")

        if type_file == 0:
            """ Read excel file """
            print("Haciendo Lectura de {0}".format(os.path.basename(path)))
            df = pd.read_excel(path, sheet_name=sheet)
    except:
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = path

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

    return df
