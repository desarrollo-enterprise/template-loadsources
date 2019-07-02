"""
Created by: Ernesto Quito Gonzales
Date : 2019-04-08
"""
import os
from os import getcwd
from os import listdir
from os.path import abspath
from os import scandir
from os import walk


def index_absolute_sub_dir_file(ruta='.'):
    """
    List a Absolute path of directories, sub-directory and files.
    EXAMPLE:
    :return: ['\\root\directory\file.txt', \\root\directory\Process']
    """

    return next(walk(ruta))


def index_absolute_files(ruta=getcwd()):
    """
        List only sub-directory and files.
        EXAMPLE:
        :return: ['\\path\path2\file.txt', \\path\path2\file2.txt']
    """

    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]


def index_files_subdirectories(ruta='.'):
    """
    List only files and sub-directory
    :param ruta:
    :return: ['\\path\path2\file.txt', \\path\path2\file2.txt']
    """

    return listdir(ruta)


def filemoveto(namefilemoveto, dir_list_, typesearch, pathcompletemoveto):

    if namefilemoveto not in dir_list_ and typesearch == 1:
        os.mkdir(pathcompletemoveto)
    elif namefilemoveto not in dir_list_ and typesearch == 0:
        os.mkdir(pathcompletemoveto)
    return

