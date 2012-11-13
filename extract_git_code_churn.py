from pandas import *
import pandas as pd
import numpy as np

# date range that we're interested in (to match plot)
dates = np.asarray(date_range('9/13/2012','11/12/2012'))
#churn_slice =  by_date['insertions'].ix[dates] + by_date['deletions'].ix[dates]
churn_slice = np.maximum(by_date['insertions'].ix[dates], by_date['deletions'].ix[dates])
churn_slice_values = churn_slice.values
churn_slice_list = churn_slice_values.tolist()

# Filter out outliers (upgrades of third-party software, most likely)
churn_slice_list_filt = []
for c in churn_slice_list:
    if isnan(c):
        churn_slice_list_filt.append(0)
    elif c > 15000:
        churn_slice_list_filt.append(0)
    else:
        churn_slice_list_filt.append(c)

# Take a moving average since this is very noisy data, 3 day window
churn_slice_list_ma = zeros(2).tolist()
churn_slice_list_ma = churn_slice_list_ma + mlab.movavg(churn_slice_list_filt,3).tolist()
