import re
from datetime import datetime


def extract_dates(text):
    date_pattern = r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b"
    matches = re.findall(date_pattern, text)

    formatted_dates = []
    for day, month, year in matches:
        if len(year) == 2:  # Convert two-digit years to four-digit
            year = "20" + year if int(year) < 50 else "19" + year
        formatted_date = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y").strftime("%Y-%m-%d")
        formatted_dates.append(formatted_date)

    return formatted_dates


# Example usage
text = "The project started on 12/08/23 and will end by 05-11-2024."
print(extract_dates(text))  # Output: ['2023-08-12', '2024-11-05']

# Why? This snippet extracts dates from text, normalizes two-digit years, and converts them into a consistent
# YYYY-MM-DD format. It's useful for parsing logs, processing documents, and handling unstructured data formats in
# real-world applications.
