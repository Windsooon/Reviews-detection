import os
import numpy as np
import pandas as pd
# from hmmlearn import hmm
from base import DATA_DIR

data = pd.read_excel(os.path.join(DATA_DIR, 'trans.xls'))
