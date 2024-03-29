def html_re_process():
    body_html = """<html> 
                <body style="margin: 0; padding: 0;"> 
                <table border="0" width="100%" cellpadding="0" bgcolor="#032556" style="padding: 20px; background-color: #ededed; border-collapse:separate;"> 
                    <tbody> 
                      <!-- HEADER -->
                      <tr
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: #032556; padding: 20px; border-collapse:separate;">
                            <tr>
                              <td valign="middle" style="font-size:20px; color:white; font-weight: bold;">
                                  <!--<span style="font-size:20px; color:white; font-weight: bold;">-->
                                      Konecta
                                  <!--</span>-->
                              </td>
                              <td valign="middle" align="right">
                                  <span style="color: white">
                                      AVISO!
                                  </span>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
        
                      <!-- CONTENT -->
                      <tr>
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: rgb(255, 255, 255); padding: 20px; border-collapse:separate;">
                            <tbody>
                              <td valign="top" style="font-family:Arial,Helvetica,sans-serif; color: #555; font-size: 14px;">
                                  <strong>Este es un mensaje de {0}:</strong><br><br>Se env&iacute;a  <strong style="color:#032556;">Descripci&oacute;n del mensaje</strong>.<br><br>Saludos.
                              </td>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <!-- FOOTER -->
                        <td align="center">
                            Powered by <a target="_blank" href="https://www.python.org">Python</a>.
                        </td>
                      </tr>
                    </tbody> 
                </table> 
                </body> 
                </html>"""
    return body_html


def html_one():
    body_html = """<html>
                <body style="margin: 0; padding: 0;">
                <table border="0" width="100%" cellpadding="0" bgcolor="#032556" style="padding: 20px; background-color: #ededed; border-collapse:separate;">
                    <tbody>
                      <!-- HEADER -->
                      <tr>
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: #032556; padding: 20px; border-collapse:separate;">
                            <tr>
                              <td valign="middle" style="font-size:20px; color:white; font-weight: bold;">
                                  <!--<span style="font-size:20px; color:white; font-weight: bold;">-->
                                      Konecta
                                  <!--</span>-->
                              </td>
                              <td valign="middle" align="right">
                                  <span style="color: white">
                                      AVISO!
                                  </span>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>

                      <!-- CONTENT -->
                      <tr>
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: rgb(255, 255, 255); padding: 20px; border-collapse:separate;">
                            <tbody>
                              <td valign="top" style="font-family:Arial,Helvetica,sans-serif; color: #555; font-size: 14px;">
                                  <strong>Equipo Desarrollo</strong><br><br>Se env&iacute;a Notificacion de alerta por los siguientes motivos:
                                  <br><br> - Se analiz&oacute; el nombre del archivo <strong style="color:#032556;">{0}</strong> pero el contenido del archivo tiene la fecha <strong style="color:#EC1C1C;">{1}</strong>
                                  <br> - Ruta del archivo: <strong style="color:#032556;"><a href="{2}">{2}</a></strong>
                                  . <br><br>Por favor, corregir el nombre del archivo o realizar nuevamente la descarga que corresponda.
                                  <br><br>Saludos.
                              </td>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <!-- FOOTER -->
                        <td align="center">
                            Powered by <a target="_blank" href="http://144.217.87.110:8069/">Wixus</a>.
                        </td>
                      </tr>
                    </tbody>
                </table>
                </body>
                </html>"""
    return body_html


def html_two():
    body_html = """<html>
                <body style="margin: 0; padding: 0;">
                <table border="0" width="100%" cellpadding="0" bgcolor="#032556" style="padding: 20px; background-color: #ededed; border-collapse:separate;">
                    <tbody>
                      <!-- HEADER -->
                      <tr>
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: #032556; padding: 20px; border-collapse:separate;">
                            <tr>
                              <td valign="middle" style="font-size:20px; color:white; font-weight: bold;">
                                  <!--<span style="font-size:20px; color:white; font-weight: bold;">-->
                                      Konecta
                                  <!--</span>-->
                              </td>
                              <td valign="middle" align="right">
                                  <span style="color: white">
                                      AVISO!
                                  </span>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>

                      <!-- CONTENT -->
                      <tr>
                        <td align="center" style="min-width: 590px;">
                          <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: rgb(255, 255, 255); padding: 20px; border-collapse:separate;">
                            <tbody>
                              <td valign="top" style="font-family:Arial,Helvetica,sans-serif; color: #555; font-size: 14px;">
                                  <strong>Equipo Desarrollo</strong><br><br>El proceso de carga ha tenido una o varias excepciones en el proceso de carga.
                                  <br>Se env&iacute;a informaci&oacute;n de las excpeciones generadas.
                                  <br><br><strong style="color:#032556;">Tipo de error: </strong>{0}.
                                  <br><strong style="color:#032556;">Descripci&oacute;n del error: </strong>{1}
                                  <br><strong style="color:#032556;">Nombre del paquete donde se produce el error: </strong>{2}
                                  <br><strong style="color:#032556;">Linea de c&oacute;digo donde se produce el error: </strong>{3}
                                  <br><strong style="color:#032556;">Nombre del archivo que causo la excepci&oacute;n: </strong>{4}
                                  <br><strong style="color:#032556;">Ruta: </strong>{5}
                                  <br><br>Por favor, corregir el archivo o realizar nuevamente la descarga que corresponda.
                                  <br><br>Saludos.
                              </td>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <!-- FOOTER -->
                        <td align="center">
                            Powered by <a target="_blank" href="http://144.217.87.110:8069/">Wixus</a>.
                        </td>
                      </tr>
                    </tbody>
                </table>
                </body>
                </html>"""
    return body_html
