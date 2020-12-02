from utils import *


def filter_type(arg, cases):
  if arg == 'zgony' or arg == 'zachorowania':
    return sorted(cases, key=lambda x: int(x[5 if arg == 'zgony' else 4]), reverse=True)
  raise Exception('Bad argument %s for zgony or zachorowania.' % arg)


def filter_location(arg, cases):
  if arg == 'swiat':
    return cases

  continents = flt(arg, 10, 2, cases)
  if len(continents) != 0:
    return continents

  countries = flt(arg, 6, 2, cases)
  if len(countries) == 0:
    raise Exception('Country or continent was not found.')

  return countries


def filter_date(args, cases):
  if args == 'wszystkie':
    return cases

  month = args
  days = cases
  months = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
  
  if type(args) == list and len(args) == 2:
    if not args[0].isnumeric() or int(args[0]) > 32 or int(args[0]) < 0:
      raise Exception('Day must be a valid number.')

    days = flt(args[0], 1, 1, cases)
    month = args[1]

  month_number = flt(month, 0, 4, months)
  if len(month_number) == 0:
    raise Exception('Month was not found.')
  else:
    month_number = months.index(month_number[0]) + 1

  data = flt(month_number, 2, 1, days)
  if len(data) == 0:
    raise Exception('Nothing was found.')

  return data


def proceed_arguments(query, cases, days = 10):
  if query == '?':
    return 'Use: <kraj|kontynent|swiat> <zgony|zachorowania> <dzien|miesiac|wszystkie>'

  query = query.split(' ')

  if 3 > len(query) or len(query) > 4:
    raise Exception('Invalid number of arguments.')

  location = filter_location(query[0], cases)                                
  date = filter_date(query[2:4] if len(query) == 4 else query[2], location)
  date = filter_type(query[1], date)[:days]
  date = sorted(date, key=lambda x: x[6])

  return '{:>10} {:>20} {:>20} {:>20} {:>20}\n'.format('Data', 'Wypdaki', 'Zgony', 'Kraj', 'Kontynent') + '\n'.join('{:>10} {:>20} {:>20} {:>20} {:>20}'.format(x[0], x[4], x[5], x[6], x[10]) for x in date)


if __name__ == '__main__':
  data = read_data_as_list('Covid_.txt')

  while True:
    query = input('Enter search query: ')

    if query == 'exit':
      break

    try:
      print(proceed_arguments(query, data))
    except Exception as err:
      print(err)
    finally:
      print()
