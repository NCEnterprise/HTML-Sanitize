import sys
from html_sanitizer import Sanitizer

def sanitize_html(input_html):
    sanitizer = Sanitizer()
    sanitized_html = sanitizer.sanitize(input_html)
    return sanitized_html

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sanitize_html.py <html_input>")
        sys.exit(1)

    html_input = sys.argv[1]
    sanitized_html = sanitize_html(html_input)

    print("Sanitized HTML:")
    print(sanitized_html)
