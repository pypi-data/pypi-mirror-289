from keras import *

from elefanpy import shuten
from elefanpy import onnxkit

def define(kind, term, style = 'auto', check = 'default'):
  result = None
  if (style == 'auto'):
    style = 'item' if (kind != 'metric') else 'list'
  if (style == 'item'):
    if (kind == 'activation'):
      if (term == 'none'):
        result = None
      elif (term == 'linear'):
        result = 'linear'
      elif (term == 'exponential'):
        result = 'exponential'
      elif (term == 'tanh'):
        result = 'tanh'
      elif (term == 'mish'):
        result = 'mish'
      elif (term == 'elu'):
        result = 'elu'
      elif (term == 'selu'):
        result = 'selu'
      elif (term == 'gelu'):
        result = 'gelu'
      elif (term == 'relu'):
        result = 'relu'
      elif (term == 'prelu'):
        result = 'prelu'
      elif (term == 'lrelu'):
        result = 'leaky_relu'
      elif (term == 'srelu'):
        result = 'stucky_relu'
      elif (term == 'ztrelu'):
        result = 'relu3'
      elif (term == 'zsrelu'):
        result = 'relu6'
      elif (term == 'silu'):
        result = 'silu'
      elif (term == 'hsilu'):
        result = 'hard_silu'
      elif (term == 'sigmoid'):
        result = 'sigmoid'
      elif (term == 'hsigmoid'):
        result = 'hard_sigmoid'
      elif (term == 'softmax'):
        result = 'softmax'
      elif (term == 'lsoftmax'):
        result = 'log_softmax'
      elif (term == 'softplus'):
        result = 'softplus'
      elif (term == 'softsign'):
        result = 'softsign'
      else:
        result = (eval(term) if (check == 'eval') else term)
    elif (kind == 'optimizer'):
      if (term == 'none'):
        result = None
      elif (term == 'sgd'):
        result = 'SGD'
      elif (term == 'sgdp'):
        result = 'SGDprop'
      elif (term == 'rms'):
        result = 'RMS'
      elif (term == 'rmsp'):
        result = 'RMSprop'
      elif (term == 'adam'):
        result = 'adam'
      elif (term == 'adamw'):
        result = 'adamw'
      elif (term == 'adamv'):
        result = 'adamv'
      elif (term == 'adadelta'):
        result = 'adadelta'
      elif (term == 'adagrad'):
        result = 'adagrad'
      elif (term == 'adamax'):
        result = 'adamax'
      elif (term == 'adafactor'):
        result = 'adafactor'
      elif (term == 'nadam'):
        result = 'nadam'
      elif (term == 'ftrl'):
        result = 'ftrl'
      elif (term == 'lion'):
        result = 'lion'
      elif (term == 'lscaleop'):
        result = 'loss_scale_optimizer'
      elif (term == 'lcheckop'):
        result = 'loss_check_optimizer'
      elif (term == 'inssgd'):
        result = eval('optimizers.SGD()')
      elif (term == 'inssgdp'):
        result = eval('optimizers.SGDprop()')
      elif (term == 'insrms'):
        result = eval('optimizers.RMS()')
      elif (term == 'insrmsp'):
        result = eval('optimizers.RMSprop()')
      elif (term == 'insadam'):
        result = eval('optimizers.Adam()')
      elif (term == 'insadamw'):
        result = eval('optimizers.AdamW()')
      elif (term == 'insadamv'):
        result = eval('optimizers.AdamV()')
      elif (term == 'insadadelta'):
        result = eval('optimizers.Adadelta()')
      elif (term == 'insadagrad'):
        result = eval('optimizers.Adagrad()')
      elif (term == 'insadamax'):
        result = eval('optimizers.Adamax()')
      elif (term == 'insadafactor'):
        result = eval('optimizers.Adafactor()')
      elif (term == 'insnadam'):
        result = eval('optimizers.Nadam()')
      elif (term == 'insftrl'):
        result = eval('optimizers.Ftrl()')
      elif (term == 'inslion'):
        result = eval('optimizers.Lion()')
      elif (term == 'inslscaleop'):
        result = eval('optimizers.LossScaleOptimizer()')
      elif (term == 'inslcheckop'):
        result = eval('optimizers.LossCheckOptimizer()')
      else:
        result = (eval(term) if (check == 'eval') else term)
    elif (kind == 'loss'):
      if (term == 'none'):
        result = None
      elif (term == 'mse'):
        result = 'mean_squared_error'
      elif (term == 'msle'):
        result = 'mean_squared_logarithmic_error'
      elif (term == 'mae'):
        result = 'mean_absolute_error'
      elif (term == 'mape'):
        result = 'mean_absolute_percentage_error'
      elif (term == 'cossim'):
        result = 'cosine_similarity'
      elif (term == 'cosvar'):
        result = 'cosine_variance'
      elif (term == 'huber'):
        result = 'huber'
      elif (term == 'huberlf'):
        result = 'huber_loss'
      elif (term == 'logch'):
        result = 'logch'
      elif (term == 'logcosh'):
        result = 'log_cosh'
      elif (term == 'bince'):
        result = 'binary_crossentropy'
      elif (term == 'binfce'):
        result = 'binary_focal_crossentropy'
      elif (term == 'sbince'):
        result = 'sparse_binary_crossentropy'
      elif (term == 'catce'):
        result = 'categorical_crossentropy'
      elif (term == 'catfce'):
        result = 'categorical_focal_crossentropy'
      elif (term == 'scatce'):
        result = 'sparse_categorical_crossentropy'
      elif (term == 'poisson'):
        result = 'poisson'
      elif (term == 'reductsum'):
        result = 'reductsum'
      elif (term == 'ctc'):
        result = 'ctc'
      elif (term == 'hfk'):
        result = 'hfk'
      elif (term == 'kldiv'):
        result = 'kl_divergence'
      elif (term == 'azdiv'):
        result = 'az_divergence'
      elif (term == 'wringe'):
        result = 'wringe'
      elif (term == 'hinge'):
        result = 'hinge'
      elif (term == 'shinge'):
        result = 'squared_hinge'
      elif (term == 'ahinge'):
        result = 'absolute_hinge'
      elif (term == 'binhinge'):
        result = 'binary_hinge'
      elif (term == 'cathinge'):
        result = 'categorical_hinge'
      elif (term == 'insmse'):
        result = eval('losses.MeanSquaredError()')
      elif (term == 'insmsle'):
        result = eval('losses.MeanSquaredLogarithmicError()')
      elif (term == 'insmae'):
        result = eval('losses.MeanAbsoluteError()')
      elif (term == 'insmape'):
        result = eval('losses.MeanAbsolutePercentageError()')
      elif (term == 'inscossim'):
        result = eval('losses.CosineSimilarity()')
      elif (term == 'inscosvar'):
        result = eval('losses.CosineVariance()')
      elif (term == 'inshuber'):
        result = eval('losses.Huber()')
      elif (term == 'inshuberlf'):
        result = eval('losses.HuberLoss()')
      elif (term == 'inslogch'):
        result = eval('losses.Logch()')
      elif (term == 'inslogcosh'):
        result = eval('losses.LogCosh()')
      elif (term == 'insbince'):
        result = eval('losses.BinaryCrossentropy()')
      elif (term == 'insbinfce'):
        result = eval('losses.BinaryFocalCrossentropy()')
      elif (term == 'inssbince'):
        result = eval('losses.SparseBinaryCrossentropy()')
      elif (term == 'inscatce'):
        result = eval('losses.CategoricalCrossentropy()')
      elif (term == 'inscatfce'):
        result = eval('losses.CategoricalFocalCrossentropy()')
      elif (term == 'insscatce'):
        result = eval('losses.SparseCategoricalCrossentropy()')
      elif (term == 'inspoisson'):
        result = eval('losses.Poisson()')
      elif (term == 'insreductsum'):
        result = eval('losses.Reductsum()')
      elif (term == 'insctc'):
        result = eval('losses.CTC()')
      elif (term == 'inshfk'):
        result = eval('losses.HFK()')
      elif (term == 'inskldiv'):
        result = eval('losses.KLDivergence()')
      elif (term == 'insazdiv'):
        result = eval('losses.AZDivergence()')
      elif (term == 'inswringe'):
        result = eval('losses.Wringe()')
      elif (term == 'inshinge'):
        result = eval('losses.Hinge()')
      elif (term == 'insshinge'):
        result = eval('losses.SquaredHinge()')
      elif (term == 'insahinge'):
        result = eval('losses.AbsoluteHinge()')
      elif (term == 'insbinhinge'):
        result = eval('losses.BinaryHinge()')
      elif (term == 'inscathinge'):
        result = eval('losses.CategoricalHinge()')
      else:
        result = (eval(term) if (check == 'eval') else term)
    elif (kind == 'metric'):
      if (term == 'none'):
        result = None
      elif (term == 'mse'):
        result = 'mean_squared_error'
      elif (term == 'msle'):
        result = 'mean_squared_logarithmic_error'
      elif (term == 'rmse'):
        result = 'root_mean_squared_error'
      elif (term == 'mae'):
        result = 'mean_absolute_error'
      elif (term == 'mape'):
        result = 'mean_absolute_percentage_error'
      elif (term == 'bmae'):
        result = 'base_mean_absolute_error'
      elif (term == 'cossim'):
        result = 'cosine_similarity'
      elif (term == 'cosvar'):
        result = 'cosine_variance'
      elif (term == 'huberlfe'):
        result = 'huber_loss_error'
      elif (term == 'logcoshe'):
        result = 'log_cosh_error'
      elif (term == 'bince'):
        result = 'binary_crossentropy'
      elif (term == 'sbince'):
        result = 'sparse_binary_crossentropy'
      elif (term == 'catce'):
        result = 'categorical_crossentropy'
      elif (term == 'scatce'):
        result = 'sparse_categorical_crossentropy'
      elif (term == 'poisson'):
        result = 'poisson'
      elif (term == 'reductsum'):
        result = 'reductsum'
      elif (term == 'kldiv'):
        result = 'kl_divergence'
      elif (term == 'zkldiv'):
        result = 'kullback_leibler_divergence'
      elif (term == 'azdiv'):
        result = 'az_divergence'
      elif (term == 'zazdiv'):
        result = 'auto_zone_divergence'
      elif (term == 'suitability'):
        result = 'suitability'
      elif (term == 'accuracy'):
        result = 'accuracy'
      elif (term == 'binaccuracy'):
        result = 'binary_accuracy'
      elif (term == 'sbinaccuracy'):
        result = 'sparse_binary_accuracy'
      elif (term == 'cataccuracy'):
        result = 'categorical_accuracy'
      elif (term == 'scataccuracy'):
        result = 'sparse_categorical_accuracy'
      elif (term == 'tkcataccuracy'):
        result = 'top_k_categorical_accuracy'
      elif (term == 'stkcataccuracy'):
        result = 'sparse_top_k_categorical_accuracy'
      elif (term == 'wringe'):
        result = 'wringe'
      elif (term == 'hinge'):
        result = 'hinge'
      elif (term == 'shinge'):
        result = 'squared_hinge'
      elif (term == 'ahinge'):
        result = 'absolute_hinge'
      elif (term == 'binhinge'):
        result = 'binary_hinge'
      elif (term == 'cathinge'):
        result = 'categorical_hinge'
      elif (term == 'zfoscore'):
        result = 'f1_score'
      elif (term == 'zfbscore'):
        result = 'fbeta_score'
      elif (term == 'zrtscore'):
        result = 'r2_score'
      elif (term == 'zrbscore'):
        result = 'rbeta_score'
      elif (term == 'insmse'):
        result = eval('metrics.MeanSquaredError()')
      elif (term == 'insmsle'):
        result = eval('metrics.MeanSquaredLogarithmicError()')
      elif (term == 'insrmse'):
        result = eval('metrics.RootMeanSquaredError()')
      elif (term == 'insmae'):
        result = eval('metrics.MeanAbsoluteError()')
      elif (term == 'insmape'):
        result = eval('metrics.MeanAbsolutePercentageError()')
      elif (term == 'insbmae'):
        result = eval('metrics.BaseMeanAbsoluteError()')
      elif (term == 'inscossim'):
        result = eval('metrics.CosineSimilarity()')
      elif (term == 'inscosvar'):
        result = eval('metrics.CosineVariance()')
      elif (term == 'inshuberlfe'):
        result = eval('metrics.HuberLossError()')
      elif (term == 'inslogcoshe'):
        result = eval('metrics.LogCoshError()')
      elif (term == 'insbince'):
        result = eval('metrics.BinaryCrossentropy()')
      elif (term == 'inssbince'):
        result = eval('metrics.SparseBinaryCrossentropy()')
      elif (term == 'inscatce'):
        result = eval('metrics.CategoricalCrossentropy()')
      elif (term == 'insscatce'):
        result = eval('metrics.SparseCategoricalCrossentropy()')
      elif (term == 'inspoisson'):
        result = eval('metrics.Poisson()')
      elif (term == 'insreductsum'):
        result = eval('metrics.Reductsum()')
      elif (term == 'inskldiv'):
        result = eval('metrics.KLDivergence()')
      elif (term == 'inszkldiv'):
        result = eval('metrics.KullbackLeiblerDivergence()')
      elif (term == 'insazdiv'):
        result = eval('metrics.AZDivergence()')
      elif (term == 'inszazdiv'):
        result = eval('metrics.AutoZoneDivergence()')
      elif (term == 'inssuitability'):
        result = eval('metrics.Suitability()')
      elif (term == 'insaccuracy'):
        result = eval('metrics.Accuracy()')
      elif (term == 'insbinaccuracy'):
        result = eval('metrics.BinaryAccuracy()')
      elif (term == 'inssbinaccuracy'):
        result = eval('metrics.SparseBinaryAccuracy()')
      elif (term == 'inscataccuracy'):
        result = eval('metrics.CategoricalAccuracy()')
      elif (term == 'insscataccuracy'):
        result = eval('metrics.SparseCategoricalAccuracy()')
      elif (term == 'instkcataccuracy'):
        result = eval('metrics.TopKCategoricalAccuracy()')
      elif (term == 'insstkcataccuracy'):
        result = eval('metrics.SparseTopKCategoricalAccuracy()')
      elif (term == 'inswringe'):
        result = eval('metrics.Wringe()')
      elif (term == 'inshinge'):
        result = eval('metrics.Hinge()')
      elif (term == 'insshinge'):
        result = eval('metrics.SquaredHinge()')
      elif (term == 'insahinge'):
        result = eval('metrics.AbsoluteHinge()')
      elif (term == 'insbinhinge'):
        result = eval('metrics.BinaryHinge()')
      elif (term == 'inscathinge'):
        result = eval('metrics.CategoricalHinge()')
      elif (term == 'inszfoscore'):
        result = eval('metrics.F1Score()')
      elif (term == 'inszfbscore'):
        result = eval('metrics.FBetaScore()')
      elif (term == 'inszrtscore'):
        result = eval('metrics.R2Score()')
      elif (term == 'inszrbscore'):
        result = eval('metrics.RBetaScore()')
      else:
        result = (eval(term) if (check == 'eval') else term)
  elif (style == 'list'):
    result = []
    for item in term.split(','):
      result.append(define(kind, item, 'item', check))
  return result

def publish(model, folder, name = 'model', format = 'entire'):
  result = None
  if (format != None):
    result = []
  if ((format == 'entire') or (format == 'tfsm')):
    output = folder + '/' + name + '.' + 'tfsm'
    model.save(output, save_format = 'tf')
    result.append(output)
  if ((format == 'entire') or (format == 'tfca')):
    output = folder + '/' + name + '.' + 'tfca'
    model.save(output, save_format = 'tf')
    resource = output
    output = folder + '/' + name + '.' + 'zip'
    shuten.make_archive(output.replace(('.' + 'zip'), ''), 'zip', resource)
    shuten.rmtree(resource)
    result.append(output)
  if ((format == 'entire') or (format == 'tfpb')):
    output = folder + '/' + name + '.' + 'tfpb'
    model.save(output, save_format = 'tf')
    resource = output
    output = folder + '/' + name + '.' + 'pb'
    shuten.copy((resource + '/' + 'saved_model' + '.' + 'pb'), output)
    shuten.rmtree(resource)
    result.append(output)
  if ((format == 'entire') or (format == 'keras')):
    output = folder + '/' + name + '.' + 'keras'
    model.save(output, save_format = 'keras')
    result.append(output)
  if ((format == 'entire') or (format == 'onnx')):
    output = folder + '/' + name + '.' + 'onnx'
    onnxkit.convert.from_keras(model, output_path = output)
    result.append(output)
  return result
