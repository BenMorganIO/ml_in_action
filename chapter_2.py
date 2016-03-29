from numpy import *
import operator

class KNearestNeighbor:
  GROUP = array([1.0, 1.1], [1.0, 1.0],
                [0, 0],     [0, 0.1])
  LABELS = ['A', 'A', 'B', 'B']

  def createDataSet():
    return GROUP, LABELS
