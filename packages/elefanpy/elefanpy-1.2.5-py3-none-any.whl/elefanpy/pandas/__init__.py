from pandas import *

from elefanpy import regex
from elefanpy import numpy

def create(data, style = 'auto', mode = 'auto'):
  result = None
  if ((len(numpy.array(data).shape) == 0) and (mode == 'critical')):
    print('EMPTY DATA RECEIVED AND PROGRAM WILL STOP')
    exit()
  else:
    result = DataFrame(data)
  if (style == 'metatrader'):
    result.rename(columns = { 'tick_volume': 'volume' }, inplace = True)
    result.drop(columns = 'real_volume', inplace = True)
  return result

def summary(data, head = 5, tail = 5):
  result = None
  if ((head == 0) and (tail == 0)):
    info = data.shape
    if (info[0] > 0):
      line = summary(data, 1, 1).split('\n')[0]
      result = f'DATA [R:{info[0]}] [C:{info[1]}] [T:{info[0] * info[1]}]'
      if (len(line) > len(result)):
        result = result + ' ' + ((len(line) - len(result) - 1) * '=')
  else:
    result = concat([data.head(head), data.tail(tail)])
    result = regex.sub('^\s', '#', result.to_string())
  return result
