"""
#####################################
# Author: Ernesto Quito Gonzales    #
# Date: 02/07/2019                  #
#####################################
"""
from setting import setting_web
import json

class BecomeRpa:
    def __init__(self, parm_1, parm_2):
        self.parm_1 = parm_1
        self.parm_2 = parm_2
        print(f'{self.parm_1}, {self.parm_2}\n')


a = BecomeRpa('Variable_1', 'Variable_2')
