#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import json


# In[ ]:


#function for testing data frame column values
def testing(df):
    if df['BMI'] <= 18.4:
        return "underweight"
    elif df['BMI']>=18.5 and df['BMI']<=24.9 :
        return "normal_weight"
    elif df['BMI']>=25 and df['BMI']<=29.9: 
        return "overweight"
    elif df['BMI']>=30 and df['BMI']<=34.9:
        return "Moderately obese"
    elif df['BMI']>=35 and df['BMI']<=39.9:
        return "severely obese"
    else:
        return "very severely obese"
 


# In[199]:


#defining function so that we can automate it by using scheduler
def BMI_Detection():
    #reading from json file
    df = pd.read_json('/users/ankitabhardwaj/Downloads/abc.json',orient='index')
    #converting columns into meters
    df['HeightCm']=df['HeightCm']/100
    df = df.rename(columns={'HeightCm': 'Height_meters'})
    df['BMI']=(df['WeightKg']/df['Height_meters']).round(1)
    df['RESULT'] = df.apply(testing, axis=1)
    df.to_csv('/users/ankitabhardwaj/Downloads/results.csv')
    return "File got saved successfully"


# In[200]:


BMI_Detection()


# In[203]:


get_ipython().system('pip install schedule')


# In[ ]:



#calling scheduler so that we can schedule job 
import schedule
import time

def BMI_Detection():
    print ("Started")
    return

schedule.every().day.at("09:00").do(BMI_Detection)

while True:
    schedule.run_pending()
    time.sleep() # wait one minute


# In[ ]:





# In[ ]:




