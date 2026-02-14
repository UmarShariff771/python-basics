# 5. Use a lamda function to extract the year, month and day from a datetime object.

# Import datetime module
import datetime

# Get current date and time
todaysDate = datetime.datetime.now()

# Lambda function to extract year, month and day from datetime object
extract = lambda d: (f"{d.strftime('%Y')},{d.strftime('%m')},{d.strftime('%d')}")

# Call lambda function and store result
date = extract(todaysDate)

# Print extracted date values
print(date)