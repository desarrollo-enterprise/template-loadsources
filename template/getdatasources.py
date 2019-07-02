"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""


def get_sec(time_str):
    if len(time_str) > 0:
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        return time_str


def get_positive(num_positive):
    if float(num_positive) > 0:
        return num_positive
    else:
        return "0"


def htmltrafico(dafra, file=None, cuenta='', path_to_move=''):
    import pandas as pd
    import numpy as np
    from datetime import datetime
    import os, sys
    from template.capture_of_event import event_error
    from template.capture_of_event import send_the_event
    from template.html import html_two

    try:
        print("#" * 5, " ¡Obteniendo ruta del archivo! ", file)

        html = pd.read_html(dafra, keep_default_na=False)  # requiere instalar lxml.

        df = pd.DataFrame(html[0])

        """ Using "melt" for to pass columns to rows.  """
        print("#" * 5, " ¡Pasando Fecha de registro a columna! ")

        df2 = df.melt(id_vars=['Object', 'Group', 'Statistic'], var_name='Fecha', value_name='Value')

        df2 = pd.DataFrame(df2)

        """ Using "pivot_table" for to group values. """
        print("#" * 5, " ¡Agrupando por object y fecha! ")

        df3 = pd.pivot_table(df2, values='Value', index=['Object', 'Fecha'], columns=['Statistic'], aggfunc=np.sum)

        """ Pass df3 to Dataframe """
        df4 = pd.DataFrame(df3)

        # print(df4)
        """ Create dictionary to store Dataframe """

        dic = {'object': [], 'Fecha': [], 'Abandonadas': [], 'Abandonadas010': [], 'Abandonadas015': [],
               'Abandonadas020': [],
               'Abandonadas05': [], 'Contestadas': [], 'Contestadas010': [], 'Contestadas015': [], 'Contestadas020': [],
               'Contestadas05': [], 'Distribuidas': [], 'Entrantes': [], 'NA': [], 'NS_05S': [], 'NS_10S': [],
               'NS_15S': [],
               'NS_20S': []}
        # df4.fillna(0, inplace=True)
        """ Save data on dictionary """
        for inderow, row in enumerate(df4.itertuples()):
            dic['object'].append(row[0][0])
            dic['Fecha'].append(row[0][1].replace('.1', '').replace('.2', ''))
            dic['Abandonadas'].append(str(row[1]).replace("n/a", "0").split(".")[0])
            dic['Abandonadas010'].append(str(row[2]).replace("n/a", "0").split(".")[0])
            dic['Abandonadas015'].append(str(row[3]).replace("n/a", "0").split(".")[0])
            dic['Abandonadas020'].append(str(row[4]).replace("n/a", "0").split(".")[0])
            dic['Abandonadas05'].append(str(row[5]).replace("n/a", "0").split(".")[0])
            dic['Contestadas'].append(str(row[6]).replace("n/a", "0").split(".")[0])
            dic['Contestadas010'].append(str(row[7]).replace("n/a", "0").split(".")[0])
            dic['Contestadas015'].append(str(row[8]).replace("n/a", "0").split(".")[0])
            dic['Contestadas020'].append(str(row[9]).replace("n/a", "0").split(".")[0])
            dic['Contestadas05'].append(str(row[10]).replace("n/a", "0").split(".")[0])
            dic['Distribuidas'].append(str(row[11]).replace("n/a", "0").split(".")[0])
            dic['Entrantes'].append(str(row[12]).replace("n/a", "0").split(".")[0])
            dic['NA'].append(row[13])
            dic['NS_05S'].append(row[14])
            dic['NS_10S'].append(row[15])
            dic['NS_15S'].append(row[16])
            dic['NS_20S'].append(row[17])

        df5 = pd.DataFrame(data=dic)
        df5.fillna(0, inplace=True)

        df5['Fecha'] = pd.to_datetime(df5['Fecha'], dayfirst=True)
        df5['NA'] = df5['NA'].astype(float)
        df5['NS_05S'] = df5['NS_05S'].astype(float)
        df5['NS_10S'] = df5['NS_10S'].astype(float)
        df5['NS_15S'] = df5['NS_15S'].astype(float)
        df5['NS_20S'] = df5['NS_20S'].astype(float)
        df5['FileName'] = os.path.basename(dafra)
        df5['LoadDate'] = datetime.now()

        print("#" * 5, " ¡Finally process! ", '\n')

        return df5
    except:
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = file

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)


def htmltiempos(dafra, file= None, cuenta = ' ', path_to_move= ' '):
    import pandas as pd
    import numpy as np
    from datetime import datetime
    import os, sys
    from template.capture_of_event import event_error, send_the_event
    from template.html import html_two

    try:
        print("#" * 5, " ¡Obteniendo ruta del archivo! ", file)

        html = pd.read_html(dafra, keep_default_na=False)  # requiere instalar lxml.
        print("#" * 5, " ¡Pasando datos a Dataframe! ")

        df = pd.DataFrame(html[0])

        """ Using "melt" for to pass columns to rows.  """
        print("#" * 5, " ¡Pasando Fecha de registro a columna! ")

        df2 = df.melt(id_vars=['Object', 'Group', 'Statistic'], var_name='Fecha', value_name='Value')

        df2 = pd.DataFrame(df2)

        df2['GroupStatistic'] = df2['Group'] + df2['Statistic']

        """ Using "pivot_table" for to group values. """
        print("#" * 5, " ¡Agrupando por object y fecha! ")

        df3 = pd.pivot_table(df2, values='Value', index=['Object', 'Fecha'], columns=['GroupStatistic'], aggfunc=np.sum)

        """ Pass df3 to Dataframe """
        df4 = pd.DataFrame(df3)

        """ Create dictionary to store Dataframe """
        print("#" * 5, " ¡Almacenando datos agrupados a un diccionario! ")

        dic = {'object': [], 'Fecha': [], 'DetallePrLogin': [], 'DetalleTMO': [], 'LlamadosAbandonedRinging': [],
               'LlamadosInbound': [],
               'LlamadosLlamadosMenos10segTMO': [], 'LlamadosOutbound': [], 'TiempoPromedioInbound': [],
               'TiempoPromedioOutbound': [], 'TiempoACW': [],
               'TiempoHold': [], 'TiempoInbound': [], 'TiempoLogin': [], 'TiempoNotReady': [], 'TiempoOutbound': [],
               'TiempoReady': [], 'TiemposNotReadyTiempoNotReady': []}

        """ Save data on dictionary """
        for inderow, row in enumerate(df4.itertuples()):
            dic['object'].append(row[0][0])
            dic['Fecha'].append(row[0][1].replace('.1', '').replace('.2', ''))
            dic['DetallePrLogin'].append(row[1])
            dic['DetalleTMO'].append(row[2])
            dic['LlamadosAbandonedRinging'].append(row[3].replace('n/a', '0'))
            dic['LlamadosInbound'].append(row[4].replace('n/a', '0'))
            dic['LlamadosLlamadosMenos10segTMO'].append(row[5].replace('n/a', '0'))
            dic['LlamadosOutbound'].append(row[6].replace('n/a', '0'))
            dic['TiempoPromedioInbound'].append(row[7].replace('n/a', '00:00:00'))
            dic['TiempoPromedioOutbound'].append(row[8].replace('n/a', '00:00:00'))
            dic['TiempoACW'].append(row[9].replace('n/a', '00:00:00'))
            dic['TiempoHold'].append(row[10].replace('n/a', '00:00:00'))
            dic['TiempoInbound'].append(row[11].replace('n/a', '00:00:00'))
            dic['TiempoLogin'].append(row[12].replace('n/a', '00:00:00'))
            dic['TiempoNotReady'].append(row[13].replace('n/a', '00:00:00'))
            dic['TiempoOutbound'].append(row[14].replace('n/a', '00:00:00'))
            dic['TiempoReady'].append(row[15].replace('n/a', '00:00:00'))
            dic['TiemposNotReadyTiempoNotReady'].append(row[16].replace('n/a', '00:00:00'))

        print("#" * 5, " ¡Diccionario a Dataframe! ", '\n')
        df5 = pd.DataFrame(data=dic)
        df5.fillna(0)

        df5['Fecha'] = pd.to_datetime(df5['Fecha'], dayfirst=True)
        df5['FileName'] = os.path.basename(dafra)
        df5['LoadDate'] = datetime.now()

        for index, row in enumerate(df5.itertuples()):
            df5.loc[index, 'TiempoPromedioInbound'] = get_sec(df5.loc[index, 'TiempoPromedioInbound'])
            df5.loc[index, 'TiempoPromedioOutbound'] = get_sec(df5.loc[index, 'TiempoPromedioOutbound'])
            df5.loc[index, 'TiempoACW'] = get_sec(df5.loc[index, 'TiempoACW'])
            df5.loc[index, 'TiempoHold'] = get_sec(df5.loc[index, 'TiempoHold'])
            df5.loc[index, 'TiempoInbound'] = get_sec(df5.loc[index, 'TiempoInbound'])
            df5.loc[index, 'TiempoLogin'] = get_sec(df5.loc[index, 'TiempoLogin'])
            df5.loc[index, 'TiempoNotReady'] = get_sec(df5.loc[index, 'TiempoNotReady'])
            df5.loc[index, 'TiempoOutbound'] = get_sec(df5.loc[index, 'TiempoOutbound'])
            df5.loc[index, 'TiempoReady'] = get_sec(df5.loc[index, 'TiempoReady'])
            df5.loc[index, 'TiemposNotReadyTiempoNotReady'] = get_sec(df5.loc[index, 'TiemposNotReadyTiempoNotReady'])

        return df5

    except Exception:
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = file

        event_error(e_class=type_class,
                    e_desc=type_desc,
                    e_file=fname,
                    e_line=e_line,
                    file_or_reason=file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)


def htmlagent(dafra, file: str, cuenta=' ', path_to_move=' '):
    import pandas as pd
    import numpy as np
    from datetime import datetime
    import os, sys
    from template.capture_of_event import event_error, send_the_event
    from template.html import html_two

    cont = globals()
    try:
        print("#" * 5, " ¡Obteniendo ruta del archivo! ",file)

        html = pd.read_html(dafra, keep_default_na=False)  # requiere instalar lxml.
        print("#" * 5, " ¡Pasando datos a Dataframe! ")

        df = pd.DataFrame(html[0])

        """ Using "melt" for to pass columns to rows.  """
        print("#" * 5, " ¡Pasando Fecha de registro a columna! ")

        df2 = df.melt(id_vars=['Object', 'Group', 'Statistic'], var_name='Fecha', value_name='Value')

        df2 = pd.DataFrame(df2)

        df2['GroupStatistic'] = df2['Group'] + df2['Statistic']

        """ Using "pivot_table" for to group values. """
        print("#" * 5, " ¡Group by object y fecha! ")

        df3 = pd.pivot_table(df2, values='Value', index=['Object', 'Fecha'], columns=['GroupStatistic'], aggfunc=np.sum)

        """ Pass df3 to Dataframe """
        df4 = pd.DataFrame(df3)

        """ Create dictionary to store Dataframe """
        print("#" * 5, " ¡Almacenando datos agrupados a un diccionario and Change Values! ")

        dic = {'object': [], 'Fecha': [], 'DetalleProdLogin': [], 'DetalleTMO': [], 'LlamadosInbound': [],
               'LlamadosOutbound': [], 'LlamadosTotal': [], 'NotReadyNotReadyActExtra': [], 'NotReadyNotReadyBano': [],
               'NotReadyNotReadyBreak': [], 'NotReadyNotReadyCapacitacion': [], 'NotReadyNotReadyCoaching': [],
               'NotReadyNotReadyEscuchallamadas': [], 'PorcentajeACW': [], 'PorcentajeInbound': [],
               'PorcentajeNotReady': [], 'PorcentajeOutbound': [], 'PorcentajeWait': [], 'TPromediosInbound': [],
               'TPromediosOutbound': [], 'TiempoACW': [], 'TiempoHold': [], 'TiempoInbound': [], 'TiempoLogin': [],
               'TiempoNotReady': [], 'TiempoOutbound': [], 'TiempoReady': [], 'TiempoWait': []}

        """ Save data on dictionary """

        cont = 0
        for row in df4.itertuples():
            dic['object'].append(row[0][0])
            dic['Fecha'].append(row[0][1].replace('.1', '').replace('.2', ''))
            dic['DetalleProdLogin'].append(row[1])
            dic['DetalleTMO'].append(row[2])
            dic['LlamadosInbound'].append(row[3].replace('n/a', '0'))
            dic['LlamadosOutbound'].append(row[4].replace('n/a', '0'))
            dic['LlamadosTotal'].append(get_positive(row[5]))
            dic['NotReadyNotReadyActExtra'].append(get_sec(row[6].replace('n/a', '00:00:00')))
            dic['NotReadyNotReadyBano'].append(get_sec(row[7].replace('n/a', '00:00:00')))
            dic['NotReadyNotReadyBreak'].append(get_sec(row[8].replace('n/a', '00:00:00')))
            dic['NotReadyNotReadyCapacitacion'].append(get_sec(row[9].replace('n/a', '00:00:00')))
            dic['NotReadyNotReadyCoaching'].append(get_sec(row[10].replace('n/a', '00:00:00')))
            dic['NotReadyNotReadyEscuchallamadas'].append(get_sec(row[11].replace('n/a', '00:00:00')))
            dic['PorcentajeACW'].append(row[12])
            dic['PorcentajeInbound'].append(row[13])
            dic['PorcentajeNotReady'].append(row[14])
            dic['PorcentajeOutbound'].append(row[15])
            dic['PorcentajeWait'].append(row[16])
            dic['TPromediosInbound'].append(get_sec(row[17].replace('n/a', '00:00:00')))
            dic['TPromediosOutbound'].append(get_sec(row[18].replace('n/a', '00:00:00')))
            dic['TiempoACW'].append(get_sec(row[19].replace('n/a', '00:00:00')))
            dic['TiempoHold'].append(get_sec(row[20].replace('n/a', '00:00:00')))
            dic['TiempoInbound'].append(get_sec(row[21].replace('n/a', '00:00:00')))
            dic['TiempoLogin'].append(get_sec(row[22].replace('n/a', '00:00:00')))
            dic['TiempoNotReady'].append(get_sec(row[23].replace('n/a', '00:00:00')))
            dic['TiempoOutbound'].append(get_sec(row[24].replace('n/a', '00:00:00')))
            dic['TiempoReady'].append(get_sec(row[25].replace('n/a', '00:00:00')))
            dic['TiempoWait'].append(get_sec(row[26].replace('n/a', '00:00:00')))   # .replace('n/a', '00:00:00')
            cont += 1

        print("#" * 5, " ¡Diccionario a Dataframe! ", '\n')

        df5 = pd.DataFrame(data=dic)

        df5.fillna('00:00:00', inplace=True)

        df5['Fecha'] = pd.to_datetime(df5['Fecha'], dayfirst=True)
        df5['Servicio'] = file[:-9]
        df5['FileName'] = os.path.basename(dafra)
        df5['LoadDate'] = datetime.now()

        return df5

    except :
        type_class = str(sys.exc_info()[0]).replace("<class ", "").replace(">", "").replace("'", "")
        type_desc = str(sys.exc_info()[1]).replace("<", "").replace(">", "")

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e_line = exc_tb.tb_lineno
        file_or_reason = file

        event_error(e_class= type_class,
                    e_desc= type_desc,
                    e_file= fname,
                    e_line= e_line,
                    file_or_reason= file_or_reason)

        a = html_two().format(type_class, type_desc, fname, e_line, file_or_reason, path_to_move)
        send_the_event(7, body_html=a, cuenta=cuenta)