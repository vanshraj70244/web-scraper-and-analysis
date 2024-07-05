import pandas as pd
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://results.eci.gov.in/PcResultGenJune2024/Constituencywise"

# List of state and union territory codes
state_codes = [
    "S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
    "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20",
    "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "S29", "S30",
    "S31", "S32", "S33", "S34", "S35", "S36"
]

union_territory_codes = [
    "U01", "U02", "U03", "U04", "U05", "U06", "U07", "U08", "U09"
]

# Define the column names based on the expected structure of the table
column_names = ["S.N.", "Candidate", "Party", "EVM Votes", "Postal Votes","Total Votes","Percentage of Votes"]

def get_election_results(code, constituency):
    # Construct the URL
    url = f"{base_url}{code}{constituency}.htm"

    # Send an HTTP request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract specific data (modify this part based on the actual HTML structure)
        rows = soup.find_all('tr')
        data = []
        for row in rows:
            columns = row.find_all('td')
            column_data = [col.text.strip() for col in columns]
            data.append(column_data)

        # Create DataFrame from data and specify column names
        df = pd.DataFrame(data, columns=column_names)

        # Save data to CSV file
        filename = f"{code}_{constituency}.csv"
        df.to_csv(filename, index=False)  # Save without index

        print(f"Results saved to {filename}")
    else:
        print(f"Failed to retrieve data for code {code} and constituency {constituency}. HTTP Status Code: {response.status_code}")


# Loop through all states and constituencies
for state_code in state_codes:
    for constituency_number in range(1, 86):
        constituency_code = f"{constituency_number:02d}"  # Format as two-digit number
        get_election_results(state_code, constituency_code)

# Loop through all union territories and constituencies
for ut_code in union_territory_codes:
    for constituency_number in range(1, 86):
        constituency_code = f"{constituency_number:02d}"  # Format as two-digit number
        get_election_results(ut_code, constituency_code)
