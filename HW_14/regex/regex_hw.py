import re


my_string = "Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for delivery of goods: 31.12.2024"

if __name__ == '__main__':
    data = {
        'country': re.search(r'\d{5},\s+([A-Z][a-z]+)', my_string).group(1),
        'region': re.search(r'([A-Z][a-z]+)\s+Region,', my_string).group(),
        'city': re.search(r'\w+,\s+([A-Z][a-z]+),\s[a-z]', my_string).group(1),
        'postal': re.search(r'\d{5}', my_string).group(),
        'address': re.search(r'\s[a-z]{3}.\s[A-Z][a-z]+,\s\d', my_string).group(),
        'deadline': re.search(r'\d{2}.\d{2}.\d{4}', my_string).group(),
    }
    print(data)
