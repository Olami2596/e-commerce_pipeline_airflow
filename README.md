# E-Commerce Data Pipeline 🚀

An automated pipeline for monitoring e-commerce orders with Airflow, dbt, Snowflake, and MailHog.

---

## ⚡ What It Does

- Transforms raw orders/customers/shipments with **dbt**  
- Loads data into **Snowflake**  
- Detects **delayed orders**  
- Sends alerts (captured in **MailHog**)  
- Orchestrated by **Airflow** (runs hourly)

---

## 🛠️ Tech Stack

**Airflow · dbt · Snowflake · Python · Docker · PostgreSQL · Redis · MailHog**

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/Olami2596/e-commerce_pipeline_airflow
cd e-commerce_airflow
````

1. Configure Snowflake and dbt (`profiles.yml` + YAML config files).
2. Build the containers:

```bash
docker-compose build
```

3. Initialize Airflow:

```bash
docker-compose up airflow-init
```

4. Start services:

```bash
docker-compose up -d
```

### Access Interfaces

* **Airflow UI** → [http://localhost:8080](http://localhost:8080) (`airflow/airflow`)
* **MailHog UI** → [http://localhost:8025](http://localhost:8025)

---

## ▶️ Running the Pipeline

* **DAG:** `order_monitoring_dag` (runs hourly or trigger manually)
* **Flow:**

```
dbt models → check_delayed_orders.py → MailHog alert
```

---

## 📧 Alerts

* **Subject:** “🚨 Delayed Orders Alert”
* Captured in **MailHog** (not sent externally)

---

## Pipeline Flow Diagram

```
                ┌──────────────┐
                │   Raw Data   │
                │ (CSV / SF)   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │     dbt      │
                │Transforms to │
                │ Staging/Marts│
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Snowflake   │
                │  OrderStatus │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ check_delayed│
                │  _orders.py  │
                └──────┬───────┘
                       │
            ┌──────────▼──────────┐
            │   Airflow DAG       │
            │ (Runs hourly)       │
            └─────────┬───────────┘
                      │
                      ▼
               ┌──────────────┐
               │   MailHog    │
               │ (View Alerts)│
               └──────────────┘
```

---

