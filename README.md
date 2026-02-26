# Automated Financial Briefing

This project is a full-stack data pipeline designed to bridge the gap between raw economic indicators and actionable insights. It aggregates real-time data from the St. Louis FED (FRED) and NewsAPI, processes it using Pandas, and delivers a curated financial briefing directly to a user's email inbox.

---

## Current Features

**Multi-Source Data Aggregation**
- Integrated with the FRED API to track 11+ key macroeconomic indicators:
  - Federal Funds Rate  
  - Yield Curve  
  - GDP  
  - Unemployment  
  - Additional macro indicators  
- Integrated with NewsAPI for real-time business and financial headlines.

**Data Transformation Pipeline**
- Utilizes Pandas to:
  - Clean raw JSON responses  
  - Handle missing observations  
  - Align disparate time-series data  
  - Structure outputs into unified DataFrames  

**RESTful API Architecture**
- Modular Flask-RESTful backend serving as the central data retrieval hub.

**Automated Email Delivery**
- Dedicated SMTP engine to:
  - Format daily financial briefings  
  - Standardize timestamps  
  - Include proper source attribution  
  - Dispatch reports securely  

---

## Tech Stack

**Language**
- Python

**Framework**
- Flask  
- Flask-RESTful  

**Data Science**
- Pandas  
- NumPy  

**APIs**
- St. Louis FED (FRED)  
- NewsAPI.org  

**DevOps / Infrastructure**
- Dotenv (environment variable management)  
- SMTP_SSL (secure email delivery)  

---

## System Architecture

**app.py**
- Core API service and project entry point.

**functions.py**
- Data processing engine.
- Handles complex cleaning logic and DataFrame transformations.

**email.py**
- SMTP handshake management.
- Email formatting and dispatch logic.

---

## Roadmap: Path to a SaaS Platform

The project is currently evolving from a local automation script into a scalable subscription-based intelligence platform.

---

### Phase 1: Persistence & User Growth (In Progress)

- Implement PostgreSQL for subscriber database management.
- Develop a Flask + Jinja2 frontend for:
  - User registration  
  - Email preference management  
  - Subscriber dashboard functionality  

---

### Phase 2: Intelligence & Visualization

**Data Visualization**
- Generate dynamic macro trend charts (e.g., Yield Curve spreads) using Plotly.

**NLP Sentiment Analysis**
- Integrate TextBlob or OpenAI models.
- Produce a daily "Market Sentiment" score based on aggregated headlines.

---

### Phase 3: Automation & Scaling

- Deploy to Render or AWS using Gunicorn.
- Implement Celery with Redis for:
  - Asynchronous task scheduling  
  - Background email processing  
  - Improved scalability and reliability  