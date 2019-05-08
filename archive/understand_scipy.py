import numpy as np
from scipy import stats
np.random.seed(2019)

rvs1 = stats.norm.rvs(loc=5,scale=10,size=30)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=30)
print(stats.ttest_ind(rvs1,rvs2))