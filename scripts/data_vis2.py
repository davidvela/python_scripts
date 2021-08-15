### cheatsheet.

# https://realpython.com/pandas-plot-python/
# ```python
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()
# ```
# Survey Your Data
# ```python
median_column = df["Median"]
type(median_column)
median_column.plot(kind="hist")
top_5 = df.sort_values(by="Median", ascending=False).head()
top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
top_medians = df[df["Median"] > 60000].sort_values("Median")
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
# ```
# Check for Correlation
# ```python
df.plot(x="Median", y="Unemployment_rate", kind="scatter")
# ```
# Analyze Categorical Data
# ```python
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values() #grouping 
cat_totals
cat_totals.plot(kind="barh", fontsize=4)
# ```
# Determining Ratios
# ```python
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]
# Adding a new item "Other" with the sum of the small categories
small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
big_cat_totals = big_cat_totals.append(small_sums)
big_cat_totals.plot(kind="pie", label="")
# ```
# Zooming in on Categories
# ```python
df[df["Major_category"] == "Engineering"]["Median"].plot(kind="hist")
# ```


# Conclusion
# * Histogram = Get an overview of your dataset’s distribution
# * Scatter plot = Discover correlation
# * bar plots = Analyze categories with  and their 
#     * pie plots = ratios with 