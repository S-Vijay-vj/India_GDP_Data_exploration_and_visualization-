# %% [markdown]
# # DATA VISUALIZATION USING PANDAS AND MATPLOTLIB.
#
#
# ---
# ---
#

# %% [markdown]
# ## Importing pandas and matplotlib library

# %%
import pandas as pd
import matplotlib.pyplot as plt


# %% [markdown]
# ## Importing csv file

# %%
df = pd.read_csv('India_GDP_Data.csv')

# %%
df

# %%
# sorting data in ascending order

df.sort_values('Year', ascending=True, inplace=True)
df

# %%
# getting info about dataset

df.shape


# %% [markdown]
# ## Data cleaning

# %%
# checking for empty cells

df.info()

# %%
df.isnull().sum()

# %%
# checking for duplicate cells
df.duplicated().sum()

# %% [markdown]
# ---
#  > **since there is no null values in any of the columns, there is no need to remove or replace the empty cells.**
#
#
# likewise there is no
#
# *   data in wrong format
# *   duplicate data.
#
#
#
#
#
#
#  ---
#

# %% [markdown]
# # Statisical Description

# %%
df.describe().T

# %% [markdown]
# ## Finding Correlation

# %%
df.corr()

# %% [markdown]
# ---
#
# ### important observation from the above is
#  * GDP depends on both `year` and `Per capita` and increses as both increases.
#  *  likewise "Per Capita" depends on both `year` and `GDP`
#  *  but "Percentage growth" doesn't depend much on any factors. so there is not much variations with respect to other factors.
#
#  ---
#
#
#
#

# %%
df

# %% [markdown]
# # DATA VISUALIZATION

# %% [markdown]
# LINE PLOT

# %%
# GDP Plot
plt.figure(figsize=(10, 4))
plt.plot(df["Year"], df["GDP_In_Billion_USD"], color="orange")
plt.title('GDP over time', color='green', size=16, family='serif')
plt.xlabel('Year', color='green', size=12, family='serif')
plt.ylabel('GDP(in Billion USD', color='green', size=12, family='serif')
plt.show()


# %%
# GDP over past 5 years
GDP_5 = df.sort_values('Year', ascending=False).head().reset_index()
GDP_5[['Year', 'GDP_In_Billion_USD']]

# %% [markdown]
#  From the above plot, `GDP` increases as the `Year` gets increases
#
#
# ---

# %%
# Per Capita Plot
plt.figure(figsize=(10, 4))
plt.plot(df['Year'], df['Per_Capita_in_USD'], '-b')
plt.title('Per Capita change over time', size=16, family='serif', color="red")
plt.xlabel("Year", size=12, color='red')
plt.ylabel('Per Capita(in USD)', size=12, color='red')
plt.show()


# %%
GDP_5.columns

# %%
# Per Capita over past 5 years
GDP_5 = df.sort_values('Year', ascending=False).head().reset_index()
GDP_5[['Year', 'Per_Capita_in_USD']]

# %% [markdown]
# From the above plot,`Per Capita` increases with increase in `Year`
#
# ---

# %%
# percentage growth plot
plt.figure(figsize=(10, 4))
plt.plot(df["Year"], df["Percentage_Growth "], '-g')
plt.title('Percentage Growth over time', size=16,
          family='serif', color="orange")
plt.xlabel('Year', size=12, color='orange')
plt.ylabel('Percentage Growth', size=12, color='orange')
plt.show()

# %%
# Percentage growth over past 5 years
GDP_5 = df.sort_values('Year', ascending=False).head().reset_index()
GDP_5[['Year', 'Percentage_Growth ']]

# %% [markdown]
# From the above plot, the `percencentage growth` does not depend on `Year` and `Percentage Growth` keeps on flactuating throughout years.
#
# ---
#
#

# %%

plt.figure(figsize=(17, 4))


# GDP Plot
plt.subplot(1, 3, 1)
plt.plot(df["Year"], df["GDP_In_Billion_USD"], color="orange")
plt.title('Year vs GDP', color='green', size=16, family='serif')
plt.xlabel('Year', color='green', size=12, family='serif')
plt.ylabel('GDP(in Billion USD', color='green', size=12, family='serif')

# Per Capita Plot
plt.subplot(1, 3, 2)
plt.plot(df['Year'], df['Per_Capita_in_USD'], '-b')
plt.title('Year vs Per Capita', size=16, family='serif', color="red")
plt.xlabel("Year", size=12, color='red')
plt.ylabel('Per Capita(in USD)', size=12, color='red')

# percentage growth plot
plt.subplot(1, 3, 3)
plt.plot(df["Year"], df["Percentage_Growth "], '-g')
plt.title('Year vs Percentage Growth', size=16, family='serif', color="orange")
plt.xlabel('Year', size=12, color='orange')
plt.ylabel('Percentage Growth', size=12, color='orange')

plt.suptitle('LINE PLOT', size=16, family='serif')
plt.show()

# %%
df.corr()

# %% [markdown]
# ---
# BOXPLOT

# %%
plt.figure(figsize=(20, 6))
plt.suptitle('BOX PLOT', size=16, color="k")

# Year
plt.subplot(1, 4, 1)
plt.boxplot(df['Year'])
plt.title('Year', size=16, family='serif', color="green")

# GDP
plt.subplot(1, 4, 2)
plt.boxplot(df['GDP_In_Billion_USD'])
plt.title('GDP_In_Billion_USD', size=16, family='serif', color="orange")

# Per Capita
plt.subplot(1, 4, 3)
plt.boxplot(df['Per_Capita_in_USD'])
plt.title('Per_Capita_in_USD', size=16, family='serif', color="blue")

# Percentage Growth
plt.subplot(1, 4, 4)
plt.boxplot(df['Percentage_Growth '])
plt.title('Percentage_Growth ', size=16, family='serif', color="green")

plt.show()

# %%
df.describe().T

# %% [markdown]
#
#
# > From the above `Boxplots`, median, range, IQR(Interquartile Range) and outliers can be visualised.
#
# ---
#
# HISTOGRAM
#

# %%
df.columns

# %%
plt.figure(figsize=(20, 5))
plt.suptitle('HISTOGRAM', size=16, family='serif')

# GDP
plt.subplot(1, 3, 1)
plt.hist(df['GDP_In_Billion_USD'], color="orange")
plt.title('GDP(in Billion USD)', color="orange", size=15, family='serif')

# Per Capita
plt.subplot(1, 3, 2)
plt.hist(df['Per_Capita_in_USD'], color='blue')
plt.title('Per Capita(in USD)', color='blue', size=15, family='serif')

# Percentage Growth
plt.subplot(1, 3, 3)
plt.hist(df['Percentage_Growth '], color='green')
plt.title('Percentage Growth', color='green', size=15, family='serif')

plt.show()

# %% [markdown]
# > From the above `HISTOGRAM`, the frequency distribution of the data can be visualised.
#
# ---

# %% [markdown]
# SCATTER PLOT

# %%
df.columns

# %%
# scatter plotting for 'GDP and Per Capita' vs 'Per_Capita_in_USD'

plt.figure(figsize=(14, 4))
plt.scatter(df['GDP_In_Billion_USD'], df['Per_Capita_in_USD'],
            color='orange', marker='p')
plt.title("SCATTER PLOT", size=16, family='serif')
plt.xlabel('GDP_In_Billion_USD', size=15, color='blue')
plt.ylabel('Per Capita', size=15, color='blue')
plt.show()

# %%
# scatter plotting for 'GDP' vs 'Percentage growth'

plt.figure(figsize=(14, 4))
plt.scatter(df['GDP_In_Billion_USD'],
            df['Percentage_Growth '], color='r', marker='p')
plt.title("SCATTER PLOT", size=16, family='serif')
plt.xlabel('GDP_In_Billion_USD', size=15, color='blue')
plt.ylabel('Percentage_Growth ', size=15, color='blue')
plt.show()

# %%
# scatter plotting for 'Per Capita' vs 'Percentage growth'

plt.figure(figsize=(14, 4))
plt.scatter(df['Per_Capita_in_USD'],
            df['Percentage_Growth '], color='g', marker='p')
plt.title("SCATTER PLOT", size=16, family='serif')
plt.xlabel('Per Capita', size=15, color='blue')
plt.ylabel('Percentage_Growth', size=15, color='blue')
plt.show()

# %% [markdown]
#  > This `SCATTER PLOT` shows the relation across different variables.

# %% [markdown]
# ---
# ---
#
# ### Conclusion
#  >A dataset is imported,cleaned and visualized using `PANDAS` and `MATPLOTLIB`
#
#  ---
#  ---
