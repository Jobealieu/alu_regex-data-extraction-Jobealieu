from regex_extraction import RegexExtractor

extractor = RegexExtractor()

sample_text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM
HTML: <p>, <div class="example">, <img src="image.jpg" alt="description">
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56
"""

print("Emails:", extractor.extract_emails(sample_text))
print("URLs:", extractor.extract_urls(sample_text))
print("Phone Numbers:", extractor.extract_phone_numbers(sample_text))
print("Credit Cards:", extractor.extract_credit_cards(sample_text))
print("Times:", extractor.extract_time(sample_text))
print("HTML Tags:", extractor.extract_html_tags(sample_text))
print("Hashtags:", extractor.extract_hashtags(sample_text))
print("Currency:", extractor.extract_currency(sample_text))