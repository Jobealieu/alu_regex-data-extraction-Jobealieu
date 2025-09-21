import re

class RegexExtractor:
    def extract_emails(self, text):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)

    def extract_urls(self, text):
        pattern = r'https?://[a-zA-Z0-9.-]+\.[a-z]{2,}(/\S*)?'
        return re.findall(pattern, text)

    def extract_phone_numbers(self, text):
        pattern = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
        return re.findall(pattern, text)

    def extract_credit_cards(self, text):
        pattern = r'(\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4})'
        return re.findall(pattern, text)

    def extract_time(self, text):
        pattern = r'((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?)'
        return re.findall(pattern, text)

    def extract_html_tags(self, text):
        pattern = r'<[^>]+>'
        return re.findall(pattern, text)

    def extract_hashtags(self, text):
        pattern = r'#\w+'
        return re.findall(pattern, text)

    def extract_currency(self, text):
        pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        return re.findall(pattern, text)