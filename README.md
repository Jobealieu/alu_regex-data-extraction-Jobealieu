<<<<<<< HEAD
# alu_regex-data-extraction-Jobealieu
=======
# Regex Data Extraction Project

## Overview
This project extracts structured data (emails, URLs, phone numbers, credit cards, time formats, HTML tags, hashtags, and currency amounts) from raw text using **Regular Expressions** in Python.

## Setup Instructions
1. Clone the repository or download the project.
2. Open the folder in VS Code.
3. Run the test file:
   ```bash
   python test_cases.py

   ```

## Example Output

Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Cards: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Times: ['14:30', '2:30 PM']
HTML Tags: ['<p>', '<div class="example">', '<img src="image.jpg" alt="description">']
Hashtags: ['#example', '#ThisIsAHashtag']
Currency: ['$19.99', '$1,234.56']

```
>>>>>>> 9e4ac02 (Initial commit: Regex data extraction project)
