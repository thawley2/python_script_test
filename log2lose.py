import csv

# Create reward.csv with column headers
with open('reward.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'payment'])
    writer.writerow([1605, 5.0])
    writer.writerow([1606, 10.0])
    writer.writerow([1607, 1.0])
    writer.writerow([1608, 2.0])
    writer.writerow([1609, 4.0])