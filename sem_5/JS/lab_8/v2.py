from Console import *
from v1 import * 
from utils import read_data_as_list

while True:
  try:
    query = get_string('Enter search query')
    if query == 'exit':
      break
    print(proceed_arguments(query, read_data_as_list('Covid_.txt')))
  except Exception as err:
    print(err)
  finally:
    print()
