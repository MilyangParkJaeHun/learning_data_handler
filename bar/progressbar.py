import sys
import time

class Progressbar(object):
  def __init__(self, total, prefix='', suffix='', decimals=1, barLength=50, time_gap=0.1):
    self.progress_time = 0
    self.total = total
    self.prefix = prefix
    self.suffix = suffix
    self.barLength = barLength
    self.time_gap = time_gap
    self.formatStr = "{0:." + str(decimals) + "f}"
    self.iteration = 0


  def progress(self):
    self.iteration += 1
    time_gap = time.time() - self.progress_time

    if time_gap >= self.time_gap or self.iteration == self.total:
      percent = self.formatStr.format(100 * (self.iteration / float(self.total)))
      filledLength = int(round(self.barLength * self.iteration / float(self.total)))
      bar = '#' * filledLength + '-' * (self.barLength - filledLength)
    
      sys.stdout.write('\r%s |%s| %s%s %s' % (self.prefix, bar, percent, '%', self.suffix))
      if self.iteration == self.total:
        sys.stdout.write('\n')
      sys.stdout.flush()
    
      self.progress_time = time.time()
