# HTML-Sanitize
sanitization ensures that any HTML code provided by users

HTML sanitization is the process of cleaning and filtering HTML code to remove or neutralize potentially harmful or insecure elements, attributes, and scripts. The goal of HTML sanitization is to prevent security vulnerabilities like cross-site scripting (XSS) attacks, where malicious code is injected into a web application and executed in the context of a user's browser.

In short, HTML sanitization ensures that any HTML code provided by users or from untrusted sources is safe to be rendered on a web page, reducing the risk of security breaches and protecting against potential threats.

To sanitize HTML input from the command line using Python, you can use the `html-sanitizer` library. You can install this library using pip if you don't have it already:

`pip install html-sanitizer`

`python sanitize_html.py "<your_html_input>"`

Replace `<your_html_input>` with the HTML you want to sanitize. The script will sanitize the HTML and print the sanitized version to the console.

**Example:**
```
python sanitize_html.py "<h1 id=test>dirty html"
Sanitized HTML:
<h1>dirty html</h1>
```
