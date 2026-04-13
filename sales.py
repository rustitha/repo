import pandas as pd

# 1. EXTRACT: Read data from a CSV file with personal info
# This is our "source" data with sales and customer information.
try:
    source_df = pd.read_csv('customer_sales.csv')
    print("--- Data Extracted Successfully ---")
    print(source_df.head())
    print("\n")
except FileNotFoundError:
    print("Error: 'customer_sales.csv' not found. Creating a new file for demonstration.")
    sample_data = {
        'order_id': [101, 102, 103, 104, 105],
        'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
        'price_usd': [1200.00, 25.50, 75.00, 300.00, 1500.00],
        'quantity': [1, 2, 1, 1, 3],
        'first_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'last_name': ['Smith', 'Johnson', 'Williams', 'Brown', 'Davis'],
        'email': ['alice.s@example.com', 'bob.j@example.com', 'charlie.w@example.com', 'diana.b@example.com', 'eve.d@example.com'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'state': ['NY', 'CA', 'IL', 'TX', 'AZ']
    }
    source_df = pd.DataFrame(sample_data)
    source_df.to_csv('customer_sales.csv', index=False)
    print("Created 'customer_sales.csv' with sample data.")
    print("--- Data Extracted Successfully ---")
    print(source_df.head())
    print("\n")

# 2. TRANSFORM: Manipulate and clean the data
# We'll create a full name, anonymize emails, and create a full address.

# Combine first_name and last_name into a single 'full_name' column
source_df['full_name'] = source_df['first_name'] + ' ' + source_df['last_name']

# Anonymize or mask the 'email' for privacy (e.g., for reporting or analytics)
# This is a common practice in data integration for privacy compliance.
source_df['anonymized_email'] = source_df['email'].apply(lambda x: f"****{x.split('@')[0][-4:]}@****")

# Concatenate city and state to form a 'full_address'
source_df['full_address'] = source_df['city'] + ', ' + source_df['state']

# Drop the original, more granular personal data columns if they're not needed
# This is a key step in data integration for security and to streamline the final dataset.
processed_df = source_df.drop(columns=['first_name', 'last_name', 'email', 'city', 'state'])

print("--- Data Transformed Successfully ---")
print(processed_df.head())
print("\n")

# 3. LOAD: Save the processed data to a new CSV file
# This file contains the integrated data with transformed personal elements.
processed_df.to_csv('processed_customer_sales.csv', index=False)

print("--- Data Loaded Successfully ---")
print("Processed data with integrated personal elements saved to 'processed_customer_sales.csv'")
