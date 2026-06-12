import pandas as pd
from PIL import Image
from pathlib import Path

# 1. Build directory structure safely
Path("data/raw/html").mkdir(parents=True, exist_ok=True)
Path("data/raw/screenshots").mkdir(parents=True, exist_ok=True)

# 2. Generate sample raw HTML web content files
for i in range(1, 6):
    Path(f"data/raw/html/legit{i}.html").write_text(f"<html><body><h1>Safe Portal {i}</h1><p>Welcome back. Please use secure keys.</p></body></html>")
    Path(f"data/raw/html/phish{i}.html").write_text(f"<html><body><h1>URGENT ALERT {i}</h1><p>Suspicious login attempt detected! update verify secure bank info immediately.</p></body></html>")

# 3. Generate dummy 224x224 screenshot images
for i in range(1, 6):
    Image.new("RGB", (224, 224), color="blue").save(f"data/raw/screenshots/legit{i}.png")
    Image.new("RGB", (224, 224), color="red").save(f"data/raw/screenshots/phish{i}.png")

# 4. Compile the structured index data matrix (10 samples ensures clean stratification splits)
data = [
    {"url": "https://safebank.com/login", "label": 0, "html_path": "data/raw/html/legit1.html", "screenshot_path": "data/raw/screenshots/legit1.png"},
    {"url": "http://192.168.1.100/verify-update-login-secure", "label": 1, "html_path": "data/raw/html/phish1.html", "screenshot_path": "data/raw/screenshots/phish1.png"},
    {"url": "https://myblog.org/about", "label": 0, "html_path": "data/raw/html/legit2.html", "screenshot_path": "data/raw/screenshots/legit2.png"},
    {"url": "http://secure-paypal-update-login.com/account", "label": 1, "html_path": "data/raw/html/phish2.html", "screenshot_path": "data/raw/screenshots/phish2.png"},
    {"url": "https://google.com", "label": 0, "html_path": "data/raw/html/legit3.html", "screenshot_path": "data/raw/screenshots/legit3.png"},
    {"url": "http://verify-your-netflix-login.xyz", "label": 1, "html_path": "data/raw/html/phish3.html", "screenshot_path": "data/raw/screenshots/phish3.png"},
    {"url": "https://github.com/trending", "label": 0, "html_path": "data/raw/html/legit4.html", "screenshot_path": "data/raw/screenshots/legit4.png"},
    {"url": "http://update-billing-amazon-security.cc/signin", "label": 1, "html_path": "data/raw/html/phish4.html", "screenshot_path": "data/raw/screenshots/phish4.png"},
    {"url": "https://wikipedia.org", "label": 0, "html_path": "data/raw/html/legit5.html", "screenshot_path": "data/raw/screenshots/legit5.png"},
    {"url": "http://10.2.3.4/bank-login-alert", "label": 1, "html_path": "data/raw/html/phish5.html", "screenshot_path": "data/raw/screenshots/phish5.png"}
]

# 5. Save out to CSV target layout
df = pd.DataFrame(data)
df.to_csv("data/raw/urls.csv", index=False)
print(" Successfully populated mock environment profiles!")
