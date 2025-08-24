### 🍽️ **Zomato-Food-Delivery-Data-Analysis with Interactive Dashboard**
A dynamic, interactive data visualization tool built to explore zomato food delivery data.

### **Purpose**
This project explores customer ordering behavior, restaurant types, and spending patterns using a real-world Zomato dataset. Python was used for data cleaning and exploratory visualizations, while Power BI was used to create a professional interactive dashboard that helps identify key metrics, trends, and recommendations for business decisions.

### **Tech Stack**

The dashboard was built using the following tools and technologies:<br>
•	Power BI Desktop – Main data visualization platform used for report creation.<br>
•	Python – Used for Data wrangling, cleansing, analysis.<br>
•	DAX (Data Analysis Expressions) – Used for calculated measures, dynamic visuals, and conditional logic.<br>
•	Pandas – Used for Tabular data manipulation.<br>
•	Matplotlib/Seaborn –  For Data visualization in notebook.<br>

### **Data Source**

- Rows: 148
- Columns: 12
- Fields: `Restaurant Type`, `Online Order`, `Rating`, `Votes`, `Approx Cost`, `Location`, etc.
- Source: Provided as `Zomato_data.csv`


### **Highlights**

- ✅ Real-time interactive filters:  
   - **Order Mode** (Online / Offline)  
   - **Restaurant Type**  
   - **Price Range**  

- ✅ **Key Performance Indicators (KPIs)**:  
   - Total Orders  
   - Average Rating  
   - Average Price for Two  

- ✅ **Visual Explorations**:  
   - Count of Restaurant Types  
   - Total Votes by Restaurant Type  
   - Rating Distribution  
   - Table Booking Availability Pie Chart  
   - Price Distribution for Online Orders  
   - Average Ratings by Order Mode  
   - Correlation Heatmap (Ratings, Votes, Cost)  
   - Offline vs Online Order Trends  
   - Heatmap of Orders by Type and Mode  
   - Online Order Impact on Cost

### **Features**
- ✅ Cleaned and transformed raw Zomato data using Python (`zomato.ipynb`)
- ✅ Visualized key patterns using Matplotlib and Seaborn
- ✅ Built an interactive Power BI dashboard (`zomato.pbix`) with KPIs
- ✅ Created insights to guide marketing and platform strategy


### Demos
Show what the dashboard looks like. - ![Alt text](https://github.com/username/repo/assets/image.png)
Example: ![Dashboard Preview](https://github.com/the-mansi-goel/Ski-dashboard/blob/main/Snapshot%20of%20the%20Dahbaord.png)
An interactive **Streamlit dashboard** to analyze Zomato restaurant orders, ratings, price patterns, and customer behaviors with filters and visual insights.


## 📂 **Project Structure**

├── zomato.ipynb                       # Jupyter notebook <br>
├── zomato_dashboard_with_filters.py   # Streamlit Dashboard Code<br>
├── Zomato_data.csv                    # Dataset (local file)<br>
└── README.md                          # Project Documentation<br>
