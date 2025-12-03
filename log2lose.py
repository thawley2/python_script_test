import csv

# Create reward.csv with column headers
with open('next_reward.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'payment'])
    writer.writerow([1680, 5.0])