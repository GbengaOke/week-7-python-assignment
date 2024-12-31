import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data for Line Chart
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 120, 150, 130, 170, 160]
}
df_sales = pd.DataFrame(data)

# Load the Iris dataset for other plots
df_iris = sns.load_dataset('iris')

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(df_sales['Month'], df_sales['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal_length', data=df_iris, ci=None, palette='muted')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_iris['petal_length'], bins=20, color='g', edgecolor='k')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_iris, x='sepal_length', y='petal_length', hue='species', palette='muted')
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
