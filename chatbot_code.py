#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\sefin\Downloads\Untitled SEC_10K_Financial_Data_2023_2025 - Sheet1.csv')
df.columns = df.columns.str.strip()


df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100

def financial_chatbot():
    print("🤖 GFC Financial Bot: Hello! I can answer questions about Microsoft, Apple, and Tesla for the years 2023-2025.")
    print("Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ").lower()

        if user_query == 'exit' or user_query == 'quit':
            print("🤖 GFC Financial Bot: Goodbye!")
            break


        elif "revenue" in user_query and "apple" in user_query and "2025" in user_query:
            rev = df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 'FY2025')]['Total Revenue'].values[0]
            print(f"🤖 GFC Financial Bot: Apple's total revenue for FY2025 was ${rev:,.0f} Millions.")


        elif "net income growth" in user_query and "microsoft" in user_query and "2025" in user_query:
            growth = df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 'FY2025')]['Net Income Growth (%)'].values[0]
            print(f"🤖 GFC Financial Bot: Microsoft's net income grew by {growth:.2f}% in FY2025 compared to the previous year.")


        elif "assets" in user_query and "tesla" in user_query and "2024" in user_query:
            assets = df[(df['Company'] == 'Tesla') & (df['Fiscal Year'] == 'FY2024')]['Total Assets'].values[0]
            print(f"🤖 GFC Financial Bot: Tesla's total assets for FY2024 were reported at ${assets:,.0f} Millions.")

        # Error Handling (The "else" rule)
        else:
            print("🤖 GFC Financial Bot: I'm sorry, I don't understand that specific query yet. Try asking about Apple's 2025 revenue, Microsoft's 2025 net income growth, or Tesla's 2024 assets.")


financial_chatbot()


# In[ ]:




