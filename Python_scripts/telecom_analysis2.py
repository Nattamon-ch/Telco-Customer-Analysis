import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/preem.ds/Desktop/m/telecom_users2.csv'
telecom_data = pd.read_csv(file_path)

# Filtering and analyzing the data

# 1. Total Male Subscribers (Not Senior Citizens) with Specific Services
criteria_male = (telecom_data['gender'] == 'Male') & (telecom_data['SeniorCitizen'] == 0)
male_subscribers = telecom_data[criteria_male]

# 2. Total Female Subscribers (Not Senior Citizens) with Specific Services
criteria_female = (telecom_data['gender'] == 'Female') & (telecom_data['SeniorCitizen'] == 0)
female_subscribers = telecom_data[criteria_female]

# Counting services for both male and female subscribers
services = ['PhoneService', 'InternetService', 'DeviceProtection', 'StreamingTV', 'PaperlessBilling']
male_counts = {service: male_subscribers[service].value_counts().get('Yes', 0) for service in services}
female_counts = {service: female_subscribers[service].value_counts().get('Yes', 0) for service in services}

# 3. Additional Summaries: Analyzing contract types and their churn rates
contract_churn = telecom_data.groupby(['Contract', 'Churn']).size().unstack()

# 4. Data Visualization: Creating visualizations for the analyzed data

# Visualization for Male and Female Subscribers
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.barplot(x=list(male_counts.keys()), y=list(male_counts.values()), ax=axes[0])
sns.barplot(x=list(female_counts.keys()), y=list(female_counts.values()), ax=axes[1])
axes[0].set_title('Services Subscribed by Male (Non-Senior Citizens)')
axes[1].set_title('Services Subscribed by Female (Non-Senior Citizens)')

# Visualization for Contract Types and Churn Rates
fig, ax = plt.subplots(figsize=(8, 6))
contract_churn.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Contract Types and Churn Rates')
plt.tight_layout()

plt.show()

# Returning the counts and additional summaries
male_counts, female_counts, contract_churn


