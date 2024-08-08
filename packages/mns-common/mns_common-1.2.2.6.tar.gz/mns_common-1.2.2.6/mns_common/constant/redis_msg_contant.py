import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 16
project_path = file_path[0:end]
sys.path.append(project_path)
# 同花顺新增概念TOPIC
THS_NEW_CONCEPT_ADD = 'ths_new_concept_add'

