import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 16
project_path = file_path[0:end]
sys.path.append(project_path)

'''
TOPIC
'''

# 同花顺新增概念TOPIC
REDIS_MSG_TOPIC = 'REDIS_MSG_TOPIC'
'''
MSG
'''
THS_NEW_CONCEPT_ADD_MSG = 'ths_new_concept_add_msg'
