#!/usr/bin/env python3

import tldextract
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import argparse

def parse_url(url):
    parsed_url = urlparse(url)
    domain_info = tldextract.extract(url)
    return domain_info, parsed_url

def check_blacklist(url):
    blacklist = ["malicious.com", "phishing.com"]
    return any(domain in url for domain in blacklist)

def analyze_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        return f"Found {len(forms)} form(s) on the page."
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def extract_features(url):
    features = []
    features.append(len(url))
    features.append(int(url.startswith("https")))
    return np.array(features).reshape(1, -1)

def generate_report(url, domain_info, parsed_url, blacklist_status, content_analysis, prediction):
    report = f"""
    === Phishing Link Scanner Report ===
    URL: {url}
    Domain: {domain_info.domain}
    Subdomain: {domain_info.subdomain}
    TLD: {domain_info.suffix}
    Scheme: {parsed_url.scheme}
    Blacklist Status: {'Phishing' if blacklist_status else 'Not Found'}
    Prediction: {'Phishing' if prediction else 'Legitimate'}
    Content Analysis: {content_analysis}
    ===================================
    """
    print(report)

def main():
    parser = argparse.ArgumentParser(description="Advanced Phishing Link Scanner")
    parser.add_argument("url", help="URL to scan")
    
    args = parser.parse_args()
    url = args.url
    
    domain_info, parsed_url = parse_url(url)
    blacklist_status = check_blacklist(url)
    content_analysis = analyze_content(url)
    features = extract_features(url)
    
    # Load your trained model (you can comment this out if you don't have a model)
    try:
        with open('phishing_model.pkl', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict(features)
    except FileNotFoundError:
        prediction = False
    
    generate_report(url, domain_info, parsed_url, blacklist_status, content_analysis, prediction)

if __name__ == "__main__":
    main()
