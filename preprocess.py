import re

def clean_text(text):
    # lowercase the text
    text = text.lower()
    # remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    # remove mentions and hashtags
    text = re.sub(r'\@\w+|\#','', text)
    # remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text
