import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Directory containing the cleaned CSV files
csv_directory = 'C:\\Users\\VANSHRAJ\\Downloads\\Documents\\web scraper'  # Update this to your directory containing the CSV files

# Load all CSV files into a single DataFrame
all_data = pd.DataFrame()

for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Append to the main DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)

# Basic Analysis

# Summary statistics
print("Summary Statistics:")
print(all_data.describe())

# Group by Party and calculate total votes
party_votes = all_data.groupby('Party')['Total Votes'].sum().reset_index()
print("\nTotal Votes by Party:")
print(party_votes)

# Top 5 candidates by Total Votes
top_candidates = all_data.nlargest(5, 'Total Votes')[['Candidate', 'Party', 'Total Votes']]
print("\nTop 5 Candidates by Total Votes:")
print(top_candidates)



# Visualizations

# # Plot Total Votes by Party
# plt.figure(figsize=(10, 6))
# plt.bar(party_votes['Party'], party_votes['Total Votes'], color='skyblue')
# plt.xlabel('Party')
# plt.ylabel('Total Votes')
# plt.title('Total Votes by Party')
# plt.xticks(rotation=90)
# plt.show()

# Plot Percentage of Votes Distribution
plt.figure(figsize=(10, 6))
plt.hist(all_data['Percentage of Votes'], bins=30, color='lightgreen', edgecolor='black')
plt.xlabel('Percentage of Votes')
plt.ylabel('Frequency')
plt.title('Distribution of Percentage of Votes')
plt.show()

# Top 20 parties by Total Votes
top_20_parties = party_votes.nlargest(20, 'Total Votes')

# Calculate actual percentages
total_votes = top_20_parties['Total Votes'].sum()
actual_percentages = (top_20_parties['Total Votes'] / total_votes) * 100

# Create labels with actual percentages
labels = [f"{party} ({pct:.1f}%)" for party, pct in zip(top_20_parties['Party'], actual_percentages)]

# Create equal-sized slices
equal_slices = [1] * len(top_20_parties)

# Plot Top 20 Parties vs Votes Pie Chart with custom labels
plt.figure(figsize=(10, 10))
plt.pie(equal_slices, labels=labels, startangle=160, colors=sns.color_palette('Set2'), labeldistance=1.04)
plt.title('Top 20 Parties')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


df = pd.read_csv('C:\\Users\\VANSHRAJ\\Downloads\\Documents\\web scraper\\data.csv')
df.head()


# Plot total seats won by each party
plt.figure(figsize=(14, 8))
sns.barplot(data=df, x='Total', y='Party Abbreviation', palette='viridis')
plt.title('Number of Seats Won by every Party')
plt.xlabel('Total Seats')
plt.ylabel('Party')
plt.show()

# Sort party_votes by Total Votes and select top 30 parties
top_30_parties = party_votes.sort_values(by='Total Votes', ascending=False).head(30)

# Plot Total Votes by Top 30 Parties
plt.figure(figsize=(10, 6))
plt.bar(top_30_parties['Party'], top_30_parties['Total Votes'], color='skyblue')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.title('Total Votes by Top 30 Parties')
plt.xticks(rotation=90)
plt.show()
