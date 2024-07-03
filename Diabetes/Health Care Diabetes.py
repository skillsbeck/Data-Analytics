#!/usr/bin/env python
# coding: utf-8

# ### Data Cleaning

# In[16]:


import pandas as pd

# Load the dataset
health_care_diabetes_data = pd.read_csv('health care diabetes.csv', encoding='ISO-8859-1')

# Filling missing values with mean or median where appropriate
health_care_diabetes_data['Glucose'].fillna(health_care_diabetes_data['Glucose'].mean(), inplace=True)
health_care_diabetes_data['BloodPressure'].fillna(health_care_diabetes_data['BloodPressure'].mean(), inplace=True)
health_care_diabetes_data['SkinThickness'].fillna(health_care_diabetes_data['SkinThickness'].median(), inplace=True)
health_care_diabetes_data['Insulin'].fillna(health_care_diabetes_data['Insulin'].median(), inplace=True)
health_care_diabetes_data['BMI'].fillna(health_care_diabetes_data['BMI'].median(), inplace=True)

# Create new feature Age Group 
health_care_diabetes_data['Age_Group'] = pd.cut(health_care_diabetes_data['Age'], bins=[20, 30, 40, 50, 60, 70, 80], labels=['20-30', '30-40', '40-50', '50-60', '60-70', '70-80'])

# Save the cleaned data
health_care_diabetes_data.to_csv('cleaned_diabetes.csv', index=False)

# Display cleaned dataset
health_care_diabetes_data.head()


# In[10]:


# Summary statistics
summary_stats = health_care_diabetes_data.describe()

summary_stats


# In[11]:


# Aggregating data by age group and outcome
age_group_outcome = health_care_diabetes_data.groupby(['Age_Group', 'Outcome']).size().unstack()

age_group_outcome


# ### Data Viz

# #### Glucose Levels Distribution

# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.histplot(data=health_care_diabetes_data, x='Glucose', hue='Outcome', kde=True, bins=30)
plt.title('Distribution of Glucose Levels by Diabetes Outcome')
plt.xlabel('Glucose Level')
plt.ylabel('Frequency')
plt.show()


# #### Age Distribution

# In[13]:


plt.figure(figsize=(12, 6))
sns.histplot(data=health_care_diabetes_data, x='Age', hue='Outcome', kde=True, bins=20)
plt.title('Age Distribution by Diabetes Outcome')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# #### BMI and Diabetes Pedigree Function

# In[14]:


plt.figure(figsize=(12, 6))
sns.scatterplot(data=health_care_diabetes_data, x='BMI', y='DiabetesPedigreeFunction', hue='Outcome')
plt.title('BMI vs Diabetes Pedigree Function')
plt.xlabel('BMI')
plt.ylabel('Diabetes Pedigree Function')
plt.show()


#  ### Age Group vs. Outcome

# In[15]:


plt.figure(figsize=(12, 6))
age_group_outcome.plot(kind='bar', stacked=True)
plt.title('Diabetes Outcome by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.legend(title='Outcome', labels=['No Diabetes', 'Diabetes'])
plt.show()


# In[ ]:




