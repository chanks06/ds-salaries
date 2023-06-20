



import pandas as pd
import numpy as np
#%%

df=pd.read_csv('ds_salaries.csv')

print(df.head())
#%%

#we want to know if people in the US or EU get paid more
#theres a few ways to do this calculation but to keep it fair, I think its
#best to calculate the two averages after filtering for the same job
#and same level
#experience_level, job_title, employment_type, salary_currency, salary_in_usd

ds=df[df['job_title']=='Data Scientist']

#now we have a df with all the data science jobs

ds=ds[ds['employment_type']=='FT']

#now we have a df with all the ds jobs that are full time (ft)

ds=ds[ds['experience_level']=='EN']

#now it is entry level

us_mean=ds[ds['salary_currency']=='USD']['salary_in_usd'].mean()

eu_mean=ds[ds['salary_currency']=='EUR']['salary_in_usd'].mean()

print('the mean salary in the US is:',us_mean,'while in the eu it is:',eu_mean)

print('the difference is: (usa-eu)',us_mean-eu_mean)

print('americans make',us_mean/eu_mean,'times more than europeans in this field')
