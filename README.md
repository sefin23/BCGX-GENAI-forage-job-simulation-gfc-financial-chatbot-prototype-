# BCGX-GENAI-forage-job-simulation-gfc-financial-chatbot-prototype-

# Global Finance Corp (GFC) AI Financial Chatbot Prototype

An interactive, rule-based conversational chatbot built with Python and Pandas to analyze, clean, and retrieve key financial health disclosures from corporate SEC 10-K filings (FY2023–FY2025). This project replicates a client engagement with a major financial institution during a BCG GenAI Job Simulation.

##  Key Features
- **Data Engineering Pipeline:** Programmatically ingested unstructured 10-K financial metrics for Microsoft, Apple, and Tesla, automatically cleaning column trailing whitespaces to prevent schema errors.
- **Feature Engineering:** Calculated localized Year-over-Year (YoY) percentage changes for Revenue and Net Income using grouped lag-shifting arrays.
- **Rule-Based Conversational Engine:** Implemented keyword-matching logic and conversational state-management variables using terminal user input loops.
- **Error Fallbacks:** Built deterministic query validation to intercept unrecognized inputs and guide users gracefully.

##  Tech Stack & Libraries
- **Language:** Python
- **Libraries:** Pandas (for data manipulation, grouping, and aggregations)
- **Environment:** Jupyter Notebooks / Command Line Terminal

##  Data Coverage
The backend structures and processes primary financial statements, capturing:
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operating Activities


