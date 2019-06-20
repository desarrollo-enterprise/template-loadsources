"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""
import logging


def event_error(e_class= None, e_desc= None, e_file= None, e_line= None, file_or_reason= None):
    import os
    import pandas as pd
    from template.emailsetting import sendmail
    from datetime import datetime

    pd.set_option("display.expand_frame_repr", False)

    try:
        e_date = datetime.now()
        print("#" * 5, "Capture Exception!")
        if os.path.exists(r'logs\info_event_log.csv'):
            info_event_log = {'event_date': [],
                              'even_class': [],
                              'event_desc': [],
                              'event_file': [],
                              'event_line': [],
                              'file_or_reason': []}

            info_event_log['event_date'].append(str(e_date))
            info_event_log['even_class'].append(str(e_class))
            info_event_log['event_desc'].append(str(e_desc))
            info_event_log['event_file'].append(str(e_file))
            info_event_log['event_line'].append(str(e_line))
            info_event_log['file_or_reason'].append(str(file_or_reason))

            info_event_log = pd.DataFrame(data=info_event_log)

            info_event_log.to_csv(r'logs\info_event_log.csv', sep=';', index=False, encoding='Latin-1', mode='a',
                                  header=False)
        else:
            e_date = datetime.now()
            info_event_log = {'event_date': [],
                              'even_class': [],
                              'event_desc': [],
                              'event_file': [],
                              'event_line': [],
                              'file_or_reason': []}

            info_event_log['event_date'].append(str(e_date))
            info_event_log['even_class'].append(str(e_class))
            info_event_log['event_desc'].append(str(e_desc))
            info_event_log['event_file'].append(str(e_file))
            info_event_log['event_line'].append(str(e_line))
            info_event_log['file_or_reason'].append(str(file_or_reason))

            info_event_log = pd.DataFrame(data=info_event_log)

            info_event_log.to_csv(r'logs\info_event_log.csv', sep=';', index=False, encoding='Latin-1')
    except Exception:
        print("Alert error of capture.")

        sendmail(namereport= "",
                 sender= "procesosautomaticos@servicios.grupokonecta.pe",
                 to= "quito.gonz.ern@gmail.com",
                 cc="",
                 bcc= "",
                 name= "Develop Team",
                 subjectmail= "WARNING REVIEW PROCESS",
                 bodymail= r"{0} WARNING REVIEW PROCESS, C:\Users\equito\Documents\Proyectos Python\Entel Chile\template\capture_of_event.py",
                 include_report= 0,
                 file= "")


def send_the_event(*args, body_html=None, cuenta=''):

    import pandas as pd
    from template.emailsetting import sendmail
    from template.html import html_re_process

    pd.set_option('display.expand_frame_repr', False)
    df_mails = pd.read_csv(r'logs\excavate.csv', sep=";", encoding='Latin-1')
    df_mails.fillna('', inplace=True)

    for arg in args:
        filter_name = df_mails[df_mails['id_mail']==arg]
        name_dest = filter_name['name_dest'].values[0]
        subject_mail = filter_name['subject_mail'].values[0]
        from_mail = filter_name['from_mail'].values[0]
        to_mail = filter_name['to_mail'].values[0]
        cc_mail = filter_name['cc_mail'].values[0]
        bcc_mail = filter_name['bcc_mail'].values[0]
        body_mail = body_html # filter_name['body_mail'].values[0]
        send_file = filter_name['send_file'].values[0]
        path_file = filter_name['path_file'].values[0]

        sendmail(sender= from_mail,
                 to= to_mail,
                 cc= cc_mail,
                 bcc= bcc_mail,
                 name= name_dest,
                 bodymail= body_mail,
                 include_report= send_file,
                 file= path_file,
                 subjectmail= subject_mail.format(cuenta))
