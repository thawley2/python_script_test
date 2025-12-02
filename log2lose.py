import csv

# Create reward.csv with column headers
with open('reward.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'payment'])