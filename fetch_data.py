import requests
import pandas as pd
import numpy as np

# Simulated API URL
api_url = "https://dummyjson.com/users"

# Step 1: Fetch data
response = requests.get(api_url)
data = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(data["users"])
df = df[["id", "firstName", "age", "gender"]]
df.rename(columns={"id": "interaction_id", "firstName": "agent_name"}, inplace=True)

# Step 3: Simulate metrics for AI vs Human comparison
df["agent_type"] = np.where(df["interaction_id"] % 2 == 0, "AI", "Human")
df["response_time_s"] = np.random.uniform(2.5, 6.0, len(df)).round(2)
df["satisfaction_score"] = np.random.randint(60, 100, len(df))
df["resolution_rate"] = np.random.choice([0, 1], size=len(df), p=[0.2, 0.8])

# Step 4: Save to CSV
df.to_csv("data/api_customer_service_data.csv", index=False)
print("✅ Data saved to data/api_customer_service_data.csv")
print(df.head())
