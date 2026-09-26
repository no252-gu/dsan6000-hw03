import os
import sys
from datetime import datetime, timedelta
import joblib
from mrjob.job import MRJob

class MatVecProduct(MRJob):
  def mapper_init(self):
    if os.path.isfile("b_small.pkl"):
      self.b = joblib.load("b_small.pkl")
    else:
      self.b = joblib.load("b_large.pkl")

  def mapper(self, _, line):
    line_elts = line.split()
    row_index = int(line_elts[0])
    col_index = int(line_elts[1])
    A_val = float(line_elts[2])
    # Your code here (use yield() in place of return())
    yield row_index, A_val * self.b[col_index]

  def reducer(self, key, values):
    # Your code here (use yield() in place of return())
    yield key, sum(values)

if __name__ == '__main__':
  start_time = datetime.now()
  MatVecProduct.run()
  end_time = datetime.now()
  elapsed_time = end_time - start_time
  sys.stderr.write(str(elapsed_time / timedelta(seconds=1)))
