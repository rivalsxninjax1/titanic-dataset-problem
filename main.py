import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the data set now 
titanic_df = sns.load_dataset('titanic')
print("initial dataset head :")
print(titanic_df.head())


#data information and missing values 
print("\n dataset information ")
print(titanic_df.info())
print("\n missing values")
print(titanic_df.isnull().sum())

#data cleaning 

titanic_df['age'] = titanic_df['age'].fillna(titanic_df['age'].median())
titanic_df['embarked'] = titanic_df['embarked'].fillna(titanic_df['embarked'].mode()[0])

if titanic_df['deck'].isnull().mean() > 0.5 :
    titanic_df.drop('deck',axis=1, inplace=True)
titanic_df['survived'] = titanic_df['survived'].astype('category')
print("\n cleaned data set information ")
print(titanic_df.info())

#univariate analysis --age disrtibution 
plt.figure(figsize=(10,5))
sns.histplot(titanic_df['age'], kde=True, bins=30)
plt.title("age distribution")
plt.xlabel("age")
plt.ylabel("Frequency")
plt.show()

#categorical analaysis---survival count

plt.figure(figsize=(10,5))
sns.countplot(x = 'survived', data=titanic_df)

plt.title("Survival Count")

plt.xlabel("Survived")
plt.ylabel("count")
plt.show()

#by variate analysis -survival vs gender 
plt.figure(figsize=(10,5))
sns.countplot( x='sex', hue='survived', data=titanic_df)
plt.title("survival count by gender")
plt.xlabel('gender')
plt.ylabel('count')
plt.legend(title ='Survived', labels=['No','Yes'])
plt.show()

#scatter pplot - age vs afre with surviver 

plt.figure(figsize=(10,5))
sns.scatterplot(x='age',y='fare', hue='survived', data=titanic_df, palette={0: 'red',1 :'green'})
plt.title('age vs fare with survival information ')
plt.xlabel('age')
plt.ylabel('Fare')
handles, _ = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles[0:], labels=['No', 'Yes'], title='Survived')

plt.show()

#multivariate alalysis -- correlation heatmap 

corr = titanic_df.select_dtypes(include=['float64','int64']).corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('correlation heatmap')
plt.show()

#this plot provides insight into the relstionship between several features
sns.pairplot(titanic_df.dropna(), hue="survived", diag_kind="kde")
plt.show()


