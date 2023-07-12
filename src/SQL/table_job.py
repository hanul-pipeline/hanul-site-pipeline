# MODULE IMPORT
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '../../lib/MySQL')
sys.path.append(relative_path)
import connector_lib as lib

# PARAMETERS
JSON_DIR = "../../datas/JSON/404"
TABLE_NAME = 'measurement'

# UPDATE DATABASE
lib.JSON_to_table(JSON_DIR, TABLE_NAME)