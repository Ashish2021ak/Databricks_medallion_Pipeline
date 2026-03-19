# Databricks Medallion Architecture Pipeline

## 📌 Overview

I built this project to understand how real-world data pipelines are designed using Azure Databricks. It follows the Medallion Architecture (Bronze, Silver, Gold) to process raw data into business-ready insights.

The pipeline ingests raw CSV data, performs transformations using PySpark, and generates aggregated outputs using Delta Lake.

---

## 🏗️ Architecture

The pipeline follows a layered architecture:

CSV Data → Bronze Layer → Silver Layer → Gold Layer
↓
Databricks Jobs (Orchestration)

---

## ⚙️ Technologies Used

* Azure Databricks
* PySpark
* Delta Lake

---

## 🔄 Pipeline Flow

### 🥉 Bronze Layer

* Ingest raw CSV data
* Store data in Delta format
* Acts as raw data layer

---

### 🥈 Silver Layer

* Data cleaning and transformation
* Casting data types
* Filtering invalid records
* Creating derived column `salary_flag`

---

### 🥇 Gold Layer

* Aggregated business-level data
* Example: employee count based on salary category

---

## 🚀 Orchestration

* Implemented using Databricks Jobs
* Task dependency flow:

  * Bronze → Silver → Gold

---

## 📂 Project Structure

* notebooks/ → Contains Bronze, Silver, Gold notebooks
* data/ → Sample dataset (CSV)
* README.md → Project documentation

---

## 📊 Sample Output

The Gold layer produces aggregated results such as:

* Employee count grouped by salary category

---

## 💡 Key Learnings

* Medallion Architecture design
* Delta Lake implementation
* Data transformation using PySpark
* Pipeline orchestration using Databricks Jobs

---

## 📌 Note

This project was built independently to understand end-to-end data pipeline design using Azure Databricks.
