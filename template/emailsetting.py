def sendmail(namereport=None, sender=None, to='', cc='', bcc='',
             name=None, subjectmail=None, bodymail=None, include_report=None, file=None):
    import os, sys
    import smtplib
    from datetime import datetime
    from template.createfolder import lsss
    from template.capture_of_event import event_error
    # import ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase

    port = 465  # Para Ssl
    password = 'Pr0c3505_CDG@'

    """ Creacion de seguridad contexto SSL """
    # context = ssl.create_default_context() la configuracion de este servidor no admite este metodo.

    """ COnfiguracion de envios """

    date = datetime.now()
    message = MIMEMultipart()   # 'alternative', se retira fragmento de codigo, ya que no siempre envia los archivos
    # adjuntos a todos los servidores de correo.
    message['Subject'] = subjectmail.format(namereport, str(date))
    message['From'] = sender
    # message['Reply-to'] = 'responder-aca@example.com' # Se puede responder el email enviado a esta direccion asignada.
    message['To'] = to
    message['Cc'] = cc
    message['Bcc'] = bcc
    message['X-Priority'] = '2'
    rcpt = cc.split(";") + bcc.split(";") + to.split(";")
    # html = """\
    # <html>
    # <body>
    #     <p>Hi,<br>
    #     How are you?<br>
    #     <a href="http://www.realpython.com">Real Python</a>
    #     has many great tutorials.
    #     </p>
    # </body>
    # </html>
    # """

    bodymail = bodymail.format(name)
    message.attach(MIMEText(bodymail, 'html'))
    # part2 = MIMEText(html, 'html')

    # message.attach(part1)
    # message.attach(part2)
    count_files = 0
    if include_report == 1:
        pathfile = file
        # Desde aqui se puede iterrar para enviar varios archivos al correo
        for f in lsss(pathfile):
            filename = f
            path_and_file = os.path.join(pathfile, filename)

            if os.path.isfile(path_and_file):
                with open(path_and_file, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition",
                    "attachment", filename=filename,
                )
                message.attach(part)
                count_files = count_files + 1
            else:
                print("No se encontro archivo en ")

    print("{0} archivo(s) adjuntdo(s)".format(count_files))

    text = message.as_string()

    try:
        with smtplib.SMTP_SSL('172.57.154.49', port) as server:
            server.login(sender, password)
            server.sendmail(sender, rcpt, text)
            a = 'The email went to sent successfully.'
    except Exception:
        a = "ALERT!!!! It doesn't could to send the email. Please you review the file info_event_log.csv"
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
    return print(a)
