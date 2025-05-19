# COVID19-Visualization-and-Travel-Restrictions

> **Comprehensive visualization of COVID-19 data and travel restrictions between Türkiye and its neighboring countries**

---

## 📌 About the Project

This project aims to visualize travel restrictions between Türkiye and its neighboring countries during the COVID-19 pandemic using a **knowledge graph** model.  
Additionally, it includes separate visualizations of COVID-19 case and death data across different countries globally.

---

## 🚀 Key Features

- **Travel Restrictions Visualization:**  
  Travel restrictions between Türkiye and neighboring countries (Greece, Bulgaria, Georgia, Armenia, Iran, Iraq, and Syria) are represented using color-coded lines:  
  - Green — Open travel  
  - Orange — Partial restrictions  
  - Red — Restricted travel  

- **COVID-19 Case and Death Data Visualization:**  
  Worldwide statistics on confirmed cases and deaths are visualized through graphs, providing insights into the pandemic’s global impact.

- **Neo4j Knowledge Graph:**  
  Relationships between countries and their travel statuses are modeled in a Neo4j graph database.

- **Python Data Processing and Visualization:**  
  Libraries such as Py2neo, GeoPandas, Matplotlib, and Shapely are used to process geographic and relational data for meaningful visual representations.

---

## 🎯 Purpose

The project is designed to:

- Visually analyze border mobility restrictions during the pandemic,  
- Enable decision-makers and researchers to work with data-driven insights,  
- Demonstrate strong data visualization and knowledge graph modeling skills.

---

## ⚙️ Technologies Used

- **Database:** Neo4j  
- **Python Libraries:** py2neo, geopandas, matplotlib, shapely  
- **Data Sources:** Our World in Data (COVID-19 datasets)  
- **Tools:** DevExpress (used for UI/dashboard components)

---

## 📊 Visualization Details

- Country centers are marked with red dots.  
- Travel restriction statuses are shown with green, orange, and red lines.  
- Türkiye and neighboring countries are highlighted on a geographic map.  
- Global COVID-19 case and death statistics are presented using comparative charts.

---

## 🔎 Analysis & Insights

- Travel statuses between Türkiye and neighboring countries are easy to interpret.  
- Color coding provides instant clarity on the severity of restrictions.  
- Helps illustrate the regional impact of the pandemic on international travel.  
- Global COVID-19 data allows comparison of how countries handled the crisis.

---

## 🏁 How to Run

Clone the repository and run the project locally:

```bash
git clone https://github.com/gulcinisdogru/covid19-visualization-and-travel-restrictions.git
cd covid19-visualization-and-travel-restrictions
pip install -r requirements.txt
python main.py
