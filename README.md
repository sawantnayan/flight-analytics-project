# flight-analytics-project

FLIGHT SCHEDULES & AVIATION LOGISTICS: END-TO-END DATA ANALYTICS CAPSTONE PROJECT
1. Project Overview & Problem Statement
Project Title: Global Flight Schedules and Airport Logistics Optimization

Project Overview: This project analyzes flight schedule records to evaluate route distributions, airport traffic volumes, and operational scheduling efficiency.

Problem Statement: Aviation and logistics planners lack granular insight into route congestion bottlenecks and high-traffic hub distribution. This project analyzes the flight schedule dataset to uncover operational patterns and provide data-driven recommendations for scheduling and capacity management.

3. Data Cleaning & Preparation (Task 3)
Inspection & Shape: Verified dataset dimensions (6,000 rows × 11 columns). Checked data types and identified missing entries.

Missing Values: Checked for nulls. Columns modified_by and modified_dtm contained 6,000 nulls (indicating unedited rows), which were handled appropriately by keeping them as uninitialized timestamps.

Duplicates: Checked for duplicate rows (df.duplicated().sum()) and confirmed zero duplicate records.

Data Standardization: Standardized column types, ensuring proper indexing for flight_id and package_id.

4. Exploratory Data Analysis / EDA (Task 4)
Descriptive Statistics:

Total Flights Analyzed: 6,000

Unique Flight Numbers: 3,867

Total Unique Airports: 14 departure/arrival hubs.

Traffic Distribution: SIN (Singapore) and HKT (Phuket) lead departure volumes, while LHR (London Heathrow) and JFK (New York) handle the highest arrival volumes.

Outliers: Flight schedules show a balanced distribution across package_id ranging from ID 2 to 7,000 with no disruptive outlier anomalies.

5. Data Visualization (Task 5)
The project generated 3 core visualizations (and can be expanded to 5 for your report):

Top Departure Airports (Bar Chart): Highlights SIN, HKT, and GOI as the busiest departure hubs.

Top Arrival Airports (Bar Chart): Shows LHR, JFK, and SFO leading destination traffic volumes.

Package ID Distribution (Histogram & KDE): Illustrates uniform distribution spread across package allocations.

6. Power BI Dashboard Structure (Task 6)
Build your Power BI dashboard using tbl_flight_schedules.csv with the following layout:

3 KPI Cards:

Total Flights: 6,000

Total Airports Handled: 14

Unique Flight Numbers: 3,867

4 Core Visualizations: Top Departure Airports Bar Chart, Top Arrival Airports Bar Chart, Flight Frequency by Package ID, and Route Table Matrix.

Slicers/Filters: Departure Airport Slicer, Arrival Airport Slicer, and Package ID Filter.

7. Business Insights & Recommendations (Task 7)
Business Insights:
Hub Concentration: Traffic is heavily concentrated across major international hubs like SIN, LHR, and JFK, accounting for a significant portion of total operations.

Route Balancing: Certain routes experience higher arrival density than departures, indicating potential aircraft repositioning requirements.

Package Allocation: Package IDs are evenly distributed, demonstrating consistent operational batching across scheduling cycles.

Schedule Uniformity: Departure and arrival times reflect high-frequency scheduling patterns throughout the operational day.

Data Integrity: Zero duplicate records confirm clean underlying database logging systems.

Data-Driven Recommendations:
Capacity Optimization: Increase ground crew and gate availability at high-congestion destination hubs (LHR and JFK) during peak arrival windows.

Dynamic Scheduling: Implement automated schedule rebalancing to align departure frequencies more closely with destination turnaround capacity.


# Commit 1: Add dataset
git add tbl_flight_schedules.csv
git commit -m "Commit 1: Added flight schedules raw dataset"

# Commit 2: Add Python analysis script / Jupyter Notebook
git add flight_analysis.py
git commit -m "Commit 2: Added data cleaning and EDA script"

# Commit 3: Add README documentation and push to GitHub
git add README.md
git commit -m "Commit 3: Added final project documentation and insights"
git push origin main


Commit 3: Added final README documentation and report
