import csv

# Create reward.csv with column headers
with open('next_reward.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'reward'])
    writer.writerow([1680, 6.0])