"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""
# Third-party libraries
from datetime import datetime
import pandas as pd
import os
import shutil
import time
import logging

# Own package
from template.readfiles import readxlsx
from template.getdatasources import htmltrafico, htmltiempos
from template.insertdatabase import insertsqlserver
from template.validationfiles import validate
from template.deletedatabase import deletetable
from template.createfolder import index_absolute_sub_dir_file, index_files_subdirectories, filemoveto

# Use if you will use for to read a file of the configuration
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create and configure logger
LOG_FORMAT = '%(levelname)s:%(name)s %(asctime)s - %(message)s'
logging.basicConfig(filename=os.path.join(ROOT_DIR + r"\logs", "log.log"),
                    level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger()

# It doesn't remove this code. This code have the time of execute
startprocess = datetime.now()
time.sleep(2)

pd.set_option("display.expand_frame_repr", False)
""" Reading start of file of configuration. """

# Use this code if you will read a file of the configuration
path = os.path.join(ROOT_DIR, 'setting.xlsx')
typo = 0                                                            # 0 = xlsx;
sheet = 'Hoja1'
index = '0'
setting = readxlsx(path=path, type_file=typo, sheet=sheet, index=index)
# setting = setting[setting["id_setting"] == 0]
index = 0
logger.info(f'Access path of configure {path}'.format(path=path))

# Use this if you want to iterate you file setting
for i in setting.itertuples():                                    # Travel the columns of the configuration file.
    """ Add parameters to variable. """
    path_root = setting['path_root'].values[index]
    directory_root = setting['directory_root'].values[index]
    process_month = setting['process_month'].values[index]
    host_sftp = setting['host_sftp'].values[index]
    port_sftp = setting['port_sftp'].values[index]
    user_sftp = setting['user_sftp'].values[index]
    pwd_sftp = setting['pwd_sftp'].values[index]
    # index += 1
    print(path_root)
    """ Creating file Process """
    # Ruta donde están los archivos
    # dir_ = index_files_subdirectories(path)[0]

    # Lista las carpetas del directorio(ruta)
    # dir_list = index_files_subdirectories(path)[1]
    # dir_to_move = os.path.join(dir_, name_file_move_to)

    # Inicia proceso con la creación de Procesados
    # filemoveto(name_file_move_to, dir_list, 1
    #            , dir_to_move)


    # for file in index_absolute_sub_dir_file(path):
    #     ruta = os.path.join(path, file)
    #     if "TRAFICO" in file:
    #         """ Read Files """  # Traffic
    #         df_html = htmltrafico(ruta,
    #                               file,
    #                               cuenta=cuenta,
    #                               path_to_move=dir_to_move)
    #
    #         if df_html is None:
    #             print(df_html)
    #         else:
    #
    #             """ Validate file """
    #             # Save date, name and quantity of row and columns
    #             msg_error_avoid_valid = validate(df_html,
    #                                              file,
    #                                              cuenta=cuenta,
    #                                              path_to_move=dir_to_move)
    #
    #             """ Delete date to Sql Server in Database """
    #             if msg_error_avoid_valid == 1:
    #                 msg_error_avoid_inserting = deletetable(0,
    #                                                         file,
    #                                                         server,
    #                                                         database,
    #                                                         user,
    #                                                         password,
    #                                                         table_trafico,
    #                                                         scheme,
    #                                                         criterion_delete,
    #                                                         cuenta=cuenta,
    #                                                         path_to_move=dir_to_move)
    #
    #                 """ Insert data to Sql Server in Database """
    #                 insertsqlserver(df_html,
    #                                 server,
    #                                 database,
    #                                 user,
    #                                 password,
    #                                 script,
    #                                 table_trafico,
    #                                 scheme,
    #                                 msg_error_avoid_inserting,
    #                                 cuenta=cuenta,
    #                                 path_to_move=dir_to_move)
    #
    #             # This code moves the file process to the directory Process
    #             if os.path.exists(os.path.join(dir_to_move, file)):
    #                 os.remove(os.path.join(dir_to_move, file))
    #             shutil.move(ruta, dir_to_move)
    #
    #     elif "TIEMPO" in file:
    #
    #         """ Read Files """  # Time
    #         df_html = htmltiempos(ruta,
    #                               file,
    #                               cuenta=cuenta,
    #                               path_to_move=dir_to_move)
    #
    #         if df_html is None:
    #             print(df_html)
    #         else:
    #             """ Validate file """
    #             msg_error_avoid_valid = validate(df_html,
    #                                              file,
    #                                              cuenta=cuenta,
    #                                              path_to_move=dir_to_move)  # Save date, name and quantity of row and columns
    #
    #             """ Delete date to Sql Server in Database """
    #             if msg_error_avoid_valid == 1:
    #                 msg_error_avoid_inserting = deletetable(0,
    #                                                         file,
    #                                                         server,
    #                                                         database,
    #                                                         user,
    #                                                         password,
    #                                                         table_tiempo,
    #                                                         scheme,
    #                                                         criterion_delete,
    #                                                         cuenta=cuenta,
    #                                                         path_to_move=dir_to_move)
    #
    #                 """ Insert data to Sql Server in Database """
    #                 insertsqlserver(df_html,
    #                                 server,
    #                                 database,
    #                                 user,
    #                                 password,
    #                                 script,
    #                                 table_tiempo,
    #                                 scheme,
    #                                 msg_error_avoid_inserting,
    #                                 cuenta= cuenta,
    #                                 path_to_move= dir_to_move)
    #
    #             # This code moves the file process to the directory Process
    #             if os.path.exists(os.path.join(dir_to_move, file)):
    #                 os.remove(os.path.join(dir_to_move, file))
    #             shutil.move(ruta, dir_to_move)

                                                          # The variable increments one by one for the

# It doesn't remove this code. This code have time of end of the process
endprocess = datetime.now()
timeexec = endprocess - startprocess

print("\nJob ends, please you review the logs en the directory logs")
print('Inicio:  %s' % startprocess.strftime('%Y-%m-%d %H:%M:%S'))
print('Fin:     %s' % endprocess.strftime('%Y-%m-%d %H:%M:%S'))
print('Tiempo de ejecución: %s' % timeexec)
