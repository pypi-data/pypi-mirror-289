import os
import io
import logging
import gettext

os.environ['AZ_BUFFER_SIZE'] = str(io.DEFAULT_BUFFER_SIZE)
os.environ['TF_BUFFER_SIZE'] = str(io.DEFAULT_BUFFER_SIZE)

os.environ['AZ_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if ((not ('AZ_LOG_HANDLER' in os.environ)) or (os.environ['AZ_LOG_HANDLER'] == '')):
  logging.getLogger('actionzero').setLevel(logging.CRITICAL)
  logging.getLogger('az4data').setLevel(logging.CRITICAL)
  os.environ['AZ_LOG_DOMAIN_I'] = gettext.textdomain()
  os.environ['AZ_LOG_DOMAIN_O'] = gettext.textdomain()

if ((not ('TF_LOG_HANDLER' in os.environ)) or (os.environ['TF_LOG_HANDLER'] == '')):
  logging.getLogger('tensorflow').setLevel(logging.CRITICAL)
  logging.getLogger('tf2onnx').setLevel(logging.CRITICAL)
  os.environ['TF_LOG_DOMAIN_I'] = gettext.textdomain()
  os.environ['TF_LOG_DOMAIN_O'] = gettext.textdomain()

if ((not ('KERAS_BACKEND' in os.environ)) or (os.environ['KERAS_BACKEND'] == '')):
  os.environ['KERAS_BACKEND'] = 'tensorflow'

if ((not ('KERAS_DOWNEND' in os.environ)) or (os.environ['KERAS_DOWNEND'] == '')):
  os.environ['KERAS_DOWNEND'] = 'tensorflow'

from .opsys import *
from .fsbase import *
from .rtenv import *
from .shuten import *
from .horology import *
from .calendro import *
from .regex import *
from .matf import *
from .randna import *
from .gensysco import *
from .mtnetbri import *
from .tensorflow import *
from .keras import *
from .hptuner import *
from .sklearn import *
from .dataprep import *
from .pandas import *
from .numpy import *
from .matplotlib import *
from .pyplot import *
from .tawizard import *
from .onnxkit import *

os.environ['AZ_CPP_MIN_LOG_LEVEL'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
