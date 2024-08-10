from numpy import *

def calculate_change(data, filter, step = 1):
  result = None
  if (result == None):
    result = []
    content = data[filter].values
    for index in range(len(content)):
      if (index < step):
        result.append(content[index] - content[index])
      else:
        result.append(content[index] - content[index - step])
  return result

def calculate_shift(data, filter, step = 1):
  result = None
  if (result == None):
    result = []
    content = data[filter].values
    for index in range(len(content)):
      if (index < (len(content) - step)):
        result.append(content[index] - content[index + step])
      else:
        result.append(content[index] - content[index])
  return result

def calculate_before(data, filter, step = 1):
  result = None
  if (result == None):
    result = []
    content = data[filter].values
    for index in range(len(content)):
      if (index < step):
        result.append(content[index])
      else:
        result.append(content[index - step])
  return result

def calculate_after(data, filter, step = 1):
  result = None
  if (result == None):
    result = []
    content = data[filter].values
    for index in range(len(content)):
      if (index < (len(content) - step)):
        result.append(content[index + step])
      else:
        result.append(content[index])
  return result

def determine_intrinsic(data, filter, step = 1, distance = 5, cohort = 5):
  result = None
  if (result == None):
    result = []
    change = calculate_change(data, filter, step)
    impact = absolute(nan_to_num(change))
    for index in range(len(impact)):
      min = (cohort / cohort) * -1.0
      max = (cohort / cohort) * 1.0
      if (index < distance):
        min = amin(impact[:(index + 1)])
        max = amax(impact[:(index + 1)])
      else:
        min = amin(impact[(index - distance + 1):(index + 1)])
        max = amax(impact[(index - distance + 1):(index + 1)])
      value = impact[index]
      value = (0.0 if ((max - min) == 0.0) else ((value - min) / (max - min)))
      value = multiply(value, (1.0 if (change[index] > 0.0) else -1.0))
      value = (absolute(value) if (value == 0.0) else value)
      result.append(value)
  return result

def determine_extrinsic(data, filter, step = 1, distance = 5, cohort = 5):
  result = None
  if (result == None):
    result = []
    intrinsic = determine_intrinsic(data, filter, step, distance, cohort)
    for index in range(len(intrinsic)):
      min = (cohort / cohort) * -1.0
      max = (cohort / cohort) * 1.0
      value = intrinsic[index]
      value = (0.0 if ((max - min) == 0.0) else ((value - min) / (max - min)))
      value = multiply(value, (cohort - 1.0))
      value = around(value)
      result.append(value)
  return result
