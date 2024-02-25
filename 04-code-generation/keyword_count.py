import os
import re

# Initialize an empty list to store the results
results = []

# Loop through all PDF files in the current directory
for filename in os.listdir():
    if filename.endswith(".pdf"):
        # Initialize a counter for the number of times "data" appears
        data_count = 0

        # Open the PDF file in binary mode
        with open(filename, "rb") as f:
            # Read the PDF content in chunks
            for chunk in iter(lambda: f.read(4096), b""):
                # Convert the chunk to a string
                text = chunk.decode("utf-8", errors="ignore")

                # Count the number of occurrences of "data" (case-insensitive)
                data_count += len(re.findall(r"data", text, flags=re.IGNORECASE))

        # Append the results to the list
        results.append({"filename": filename, "data_count": data_count})

# Create a DataFrame from the results
import pandas as pd
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv("data_counts.csv", index=False)

print("Data counts saved to data_counts.csv")
