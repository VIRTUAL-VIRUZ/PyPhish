**PyPhish: Advanced Phishing Link Scanner**

PyPhish is a terminal-based tool designed to detect and analyze phishing URLs. It combines URL parsing, blacklist comparison, content analysis, and machine learning to identify potential phishing threats and report on the possible harm they might cause.

**Features**

- URL Parsing: Analyzes and extracts information from URLs, including domain, subdomain, TLD, and scheme.
- Blacklist Comparison: Checks URLs against a local blacklist of known phishing sites.
- Content Analysis: Fetches and analyzes the content of a webpage to identify phishing forms and suspicious elements.
- Machine Learning: Uses a pre-trained model to predict the likelihood of a URL being a phishing site.
- Detailed Reporting: Generates a comprehensive report on the potential risks associated with the scanned URL.

**Requirements**

- Python 3.x
- Python Libraries:
  - `requests`
  - `beautifulsoup4`
  - `tldextract`
  - `scikit-learn`
- Optional: A pre-trained machine learning model (`phishing_model.pkl`).

**Installation**

1. Clone the repository or download the script files.
2. Install the required Python libraries:

   ```
   pip install requests beautifulsoup4 tldextract scikit-learn
   ```

3. Make the scripts executable:

   ```
   chmod +x pyphish.py
   chmod +x pyphish.sh
   ```

4. (Optional) Move the Bash wrapper script to a directory in your `PATH` for easy access:

   ```
   sudo mv pyphish.sh /usr/local/bin/pyphish
   ```

**Usage**

You can run the tool with a single command from your terminal:

```
pyphish http://example.com
```

This command will analyze the provided URL and generate a report in the terminal.

**Example Output**

```
=== Phishing Link Scanner Report ===
URL: http://example.com/login
Domain: example
Subdomain: 
TLD: com
Scheme: http
Blacklist Status: Not Found
Prediction: Legitimate
Content Analysis: Found 1 form(s) on the page.
===================================
```

**Customization**

**Blacklist**

You can customize the blacklist by editing the `check_blacklist` function in `pyphish.py`. Add or remove domains based on your specific needs.

**Machine Learning Model**

If you have a dataset and want to train your own model:

1. Train your model using Scikit-learn or another machine learning library.
2. Save the model as `phishing_model.pkl`.
3. Place the model file in the same directory as `pyphish.py`, or update the script to point to the correct path.

**Troubleshooting**

- **Error fetching the URL**: This usually happens if the target website is down or the URL is incorrect. Verify the URL and try again.
- **Model not found**: If you haven't trained a model or don't need machine learning predictions, you can comment out the model-related code in `pyphish.py`.

**Contributing**

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

**License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

**Acknowledgments**

- The Python community for the amazing libraries that make this tool possible.
- Open-source phishing databases like PhishTank for their contributions to online safety.

---

