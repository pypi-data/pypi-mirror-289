from sklearn.preprocessing import *

from elefanpy import tensorflow
from elefanpy import keras
from elefanpy import pandas
from elefanpy import numpy

def produce_dataframe(data, base = 'auto', mode = 'auto'):
  result = None
  if ((isinstance(data, pandas.DataFrame) == True) or (mode == 'frame')):
    result = data.copy()
  else:
    result = (pandas if (base == 'auto') else base).DataFrame(data)
  return result

def produce_dataset(data, target = 'target', shuffle = True):
  result = None
  if (result == None):
    input = produce_dataframe(data, mode = 'frame')
    output = input.pop(target)
    result = tensorflow.data.Dataset.from_tensor_slices((dict(input), output))
    if (shuffle == True):
      result = result.shuffle(buffer_size = len(input))
  return result

def count_dataframe(data):
  result = None
  if (result == None):
    result = data.shape
  return result

def count_dataset(data):
  result = None
  if (result == None):
    result = []
    result.append((
      (len(data) if data else 0),
      (1, (data._batch_size.numpy() if data._batch_size else 0)),
      (len(data.take(1).element_spec[0]) if data.take(1) else 0),
    ))
    result.append((
      (len(data) if data else 0),
      (1, (data._batch_size.numpy() if data._batch_size else 0)),
      ('Y' if (data.take(1) and data.take(1).element_spec[1]) else 'N'),
    ))
  return result

def build_transformer(name, *args, **kwargs):
  result = None
  if (name == 'none'):
    result = FunctionTransformer(*args, **kwargs)
  if (name == 'power'):
    result = PowerTransformer(*args, **kwargs)
  if (name == 'quantile'):
    result = QuantileTransformer(*args, **kwargs)
  if (name == 'spline'):
    result = SplineTransformer(*args, **kwargs)
  return result

def build_scaler(name, *args, **kwargs):
  result = None
  if (name == 'none'):
    result = FunctionTransformer(*args, **kwargs)
  if (name == 'standard'):
    result = StandardScaler(*args, **kwargs)
  if (name == 'robust'):
    result = RobustScaler(*args, **kwargs)
  if (name == 'maxabs'):
    result = MaxAbsScaler(*args, **kwargs)
  if (name == 'minmax'):
    result = MinMaxScaler(*args, **kwargs)
  return result

def encode_numerical(data, part, base = 'auto', name = 'auto'):
  result = None
  if (base == 'auto'):
    base = keras.layers.Normalization()
  elif (base == 'normal'):
    base = keras.layers.Normalization()
  elif (base == 'discrete'):
    base = keras.layers.Discretization()
  if (name == 'auto'):
    name = part.__dict__['_name']
  material = data.map(lambda x, y: x[name] if x else y)
  material = material.map(lambda x: tensorflow.expand_dims(x, -1))
  base.adapt(material)
  result = base(part)
  return result

def encode_categorical(data, part, base = 'auto', name = 'auto'):
  result = None
  if (base == 'auto'):
    base = keras.layers.IntegerLookup()
  elif (base == 'intlu'):
    base = keras.layers.IntegerLookup()
  elif (base == 'strlu'):
    base = keras.layers.StringLookup()
  elif (base == 'caten'):
    base = keras.layers.CategoryEncoding()
  if (name == 'auto'):
    name = part.__dict__['_name']
  material = data.map(lambda x, y: x[name] if x else y)
  material = material.map(lambda x: tensorflow.expand_dims(x, -1))
  base.adapt(material)
  result = base(part)
  return result

def split_portion(data, split, portion):
  result = None
  if (result == None):
    result = numpy.array_split(data, split, axis = 0)[portion]
  return result

def split_fragment(data, split, fragment):
  result = None
  if (result == None):
    result = numpy.array_split(data, split, axis = 1)[fragment]
  return result

def split_variable(data, input, output):
  result = None
  ind, dep = [], []
  for index in range(len(data)):
    ind.append(data.iloc[index][input])
    dep.append(data.iloc[index][output])
  result = numpy.array(ind), numpy.array(dep)
  return result

def split_sequence(data, input, output):
  result = None
  ind, dep = [], []
  for index in range(len(data)):
    limit = index + input + output
    if (limit > len(data)):
      break
    if (input == 1):
      ind.append(data[index])
    elif (input > 1):
      ind.append(data[index:(index + input)])
    if (output == 1):
      dep.append(data[index + input])
    elif (output > 1):
      dep.append(data[(index + input):limit])
  result = numpy.array(ind), numpy.array(dep)
  return result
