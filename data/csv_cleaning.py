import pandas as pd
import os

# Function to clean a single DataFrame
def clean_dataframe(df):
    # Remove any empty rows
    df.dropna(how='all', inplace=True)
    
    # Ensure columns exist and convert them to numeric, handling missing values
    if 'EVM Votes' in df.columns:
        df['EVM Votes'] = pd.to_numeric(df['EVM Votes'], errors='coerce').fillna(0).astype(int)
    if 'Postal Votes' in df.columns:
        df['Postal Votes'] = pd.to_numeric(df['Postal Votes'], errors='coerce').fillna(0).astype(int)
    if 'Total Votes' in df.columns:
        df['Total Votes'] = pd.to_numeric(df['Total Votes'], errors='coerce').fillna(0).astype(int)
    if 'Percentage of Votes' in df.columns:
        df['Percentage of Votes'] = df['Percentage of Votes'].astype(str).str.replace('%', '')
        df['Percentage of Votes'] = pd.to_numeric(df['Percentage of Votes'], errors='coerce').fillna(0)
    
    # Further cleaning operations as needed
    # Example: Remove any rows where 'Candidate' is empty
    if 'Candidate' in df.columns:
        df = df[df['Candidate'].notna()]
    
    return df

# Directory containing the CSV files
csv_directory = 'C:\\Users\\VANSHRAJ\\Downloads\\Documents\\web scraper'  # Update this to your directory containing the CSV files

# Loop through all files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Clean the DataFrame
        cleaned_df = clean_dataframe(df)
        
        # Save the cleaned data back to the CSV file
        cleaned_df.to_csv(file_path, index=False)
        
        print(f"Cleaned {filename}")

print("All files have been cleaned.")
