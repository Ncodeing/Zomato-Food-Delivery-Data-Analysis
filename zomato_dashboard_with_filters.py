import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("🍽️ Zomato Restaurant Orders Dashboard")

# Load Data
df = pd.read_csv("Zomato_data.csv")

# Clean 'rate' column
def rateclean(i):
    i = str(i).split('/')[0]
    return float(i)

df['rate'] = df['rate'].apply(rateclean)

# Sidebar filters
st.sidebar.header("Filters")

# Order mode filter
order_mode = st.sidebar.selectbox("Select Order Mode", ["All", "Yes", "No"])


# Restaurant Type filter
types = sorted(df['listed_in(type)'].dropna().unique())
selected_types = st.sidebar.multiselect("Select Restaurant Type(s)", types, default=types)

# Price Filter
min_price = int(df['approx_cost(for two people)'].min())
max_price = int(df['approx_cost(for two people)'].max())
price_range = st.sidebar.slider("Approx Cost for Two Range", min_price, max_price, (min_price, max_price))

# Apply Filters
filtered_df = df[
    (df['listed_in(type)'].isin(selected_types)) &
    (df['approx_cost(for two people)'] >= price_range[0]) &
    (df['approx_cost(for two people)'] <= price_range[1])
]

if order_mode != "All":
    filtered_df = filtered_df[filtered_df['online_order'] == order_mode]

# Show Raw Data
if st.sidebar.checkbox("Show Raw Data"):
    st.write(filtered_df.head())

# ------------------------
# KPIs Section
st.header("📊 Key Performance Indicators (KPIs)")

total_orders = filtered_df.shape[0]
average_rating = round(filtered_df['rate'].mean(), 2)
average_price = round(filtered_df['approx_cost(for two people)'].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", total_orders)
col2.metric("Average Rating", average_rating)
col3.metric("Avg. Price for Two", f"₹ {average_price}")

# ------------------------
# Visuals Section

# Count of Restaurant Types
st.subheader("Count of Restaurant Types")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.countplot(x=filtered_df['listed_in(type)'], ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Total Votes by Restaurant Type
st.subheader("Total Votes by Restaurant Type")
group = filtered_df.groupby('listed_in(type)')['votes'].sum().reset_index(name='votes')
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.stripplot(data=group, x='listed_in(type)', y='votes', size=10, color='blue', ax=ax2)
plt.xticks(rotation=45)
plt.title('Total Votes by Restaurant Type')
st.pyplot(fig2)

# Rating Distribution
st.subheader("Ratings Distribution")
fig3, ax3 = plt.subplots()
plt.hist(filtered_df['rate'], bins=6, color='skyblue')
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
st.pyplot(fig3)

#Total Votes by Restaurant Type
st.subheader("Total Votes by Restaurant Type")
group=df.groupby('listed_in(type)')['votes'].sum()
#result=pd.DataFrame({'votes':group})
result = group.reset_index(name='votes')
fig10, ax10 = plt.subplots(figsize=(12, 6))
sns.stripplot(data=result, x='listed_in(type)', y='votes', size=10,color='blue')# Add titles and labels
plt.title('Total Votes by Category', fontsize=16)
plt.xlabel('Types of restaurants', fontsize=12)
plt.ylabel('Total Votes', fontsize=12)
st.pyplot(fig10)

# Pie Chart of Table Booking Availability
st.subheader("Table Booking Availability")
table_booking_counts = filtered_df['book_table'].value_counts()
fig11, ax11 = plt.subplots(figsize=(8, 6))
plt.pie(table_booking_counts, labels=table_booking_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62'])
plt.title('Table Booking Availability')
plt.ylabel('')
st.pyplot(fig11)

# Price Distribution for Online Orders
st.subheader("Price Distribution for Online Orders (If Available)")
price_filter = filtered_df[filtered_df['online_order'] == "Yes"]['approx_cost(for two people)']

if not price_filter.empty:
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.countplot(x=price_filter, ax=ax4)
    plt.xticks(rotation=45)
    plt.title("Approx Cost for Two (Online Orders)")
    st.pyplot(fig4)
else:
    st.info("No online orders in current selection.")

# Rating Comparison by Order Mode
st.subheader("Average Rating by Order Mode")
rating = filtered_df.groupby('online_order')['rate'].mean().reset_index()

fig5, ax5 = plt.subplots()
sns.barplot(data=rating, x='online_order', y='rate', palette='pastel', ax=ax5)
plt.title("Average Rating: Online vs Offline")
st.pyplot(fig5)

# Rating Spread
st.subheader("Rating Spread by Order Mode")
fig6, ax6 = plt.subplots()
sns.boxplot(x='online_order', y='rate', data=filtered_df, ax=ax6)
st.pyplot(fig6)

#Correlation Heatmap (Numerical Insights)
st.subheader("Correlation Heatmap between Numerical Features")
corr = df[['rate', 'votes', 'approx_cost(for two people)']].corr()
fig12, ax12 = plt.subplots(figsize=(12, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap between Numerical Features")
st.pyplot(fig12)

# Offline Orders by Restaurant Type
st.subheader("Offline Orders by Restaurant Type")
offline_orders = filtered_df[filtered_df['online_order'] == "No"]
offline_counts = offline_orders['listed_in(type)'].value_counts()

if not offline_counts.empty:
    fig7, ax7 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=offline_counts.index, y=offline_counts.values, palette='pastel', ax=ax7)
    plt.xticks(rotation=45)
    plt.title('Offline Orders by Restaurant Type')
    st.pyplot(fig7)
else:
    st.info("No offline orders in current selection.")

#Votes Distribution for Online vs Offline Orders
st.subheader("Votes Distribution for Online vs Offline Orders")
fig13, ax13 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='online_order', y='votes', data=df, palette='Set2')
plt.title('Votes Distribution for Online vs Offline Orders')
st.pyplot(fig13)

# Heatmap: Orders by Type and Mode
st.subheader("Heatmap: Orders by Restaurant Type and Mode")
heatmap_data = filtered_df.pivot_table(
    index='listed_in(type)',
    columns='online_order',
    aggfunc='size',
    fill_value=0
)

fig8, ax8 = plt.subplots(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax8)
st.pyplot(fig8)

# Grouped Bar Plot: Online vs Offline Orders by Type
st.subheader("Online vs Offline Orders by Restaurant Type")
order_counts = filtered_df.groupby(['listed_in(type)', 'online_order']).size().reset_index(name='Total Orders')

fig9, ax9 = plt.subplots(figsize=(12, 6))
sns.barplot(data=order_counts, x='listed_in(type)', y='Total Orders', hue='online_order', palette='pastel', ax=ax9)
plt.xticks(rotation=45)
plt.title("Orders by Restaurant Type and Mode")
st.pyplot(fig9)

#Online Order Impact on Cost
st.subheader("Online Order Impact on Cost for Two People")
fig14, ax14 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='online_order', y='approx_cost(for two people)', data=df, palette='pastel')
plt.title('Cost for Two: Online vs Offline Orders')
st.pyplot(fig14)