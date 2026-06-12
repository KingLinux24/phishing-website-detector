# Phishing Website Detection Using NLP and Vision 🎣👁️

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-CPU_Only-ee4c2c.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg)

## 📌 Objective
- Build a multi-modal phishing website detector that works entirely offline  
- Combine NLP (URL + HTML) and Computer Vision (screenshots)  
- Output a phishing probability score using a fusion model  

---

## 🧠 Why Multi-Modal Detection?
- Detects both **textual deception** and **visual spoofing**
- Reduces false positives compared to single-method models
- Helps identify modern phishing techniques and zero-day attacks  

---

## 🏗️ Architecture

### 🔹 NLP Features (URL + HTML)
- URL length, dots, IP usage, suspicious keywords (`login`, `secure`, etc.)
- HTML parsing with BeautifulSoup
- TF-IDF vectorization (3000 features)

### 🔹 Vision Features (Screenshots)
- Uses **ResNet18 (PyTorch)**
- Extracts deep embeddings from screenshots (224x224)

### 🔹 Fusion Model
- Text Model → Logistic Regression  
- Vision Model → Random Forest  

**Final Score Formula:**
```
Final Risk Score = (0.6 * Text_Prob) + (0.4 * Vision_Prob)
```

---

## 📂 Project Structure

```text
phishing-website-detector/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── api/
│   ├── data/
│   ├── detection/
│   ├── features/
│   ├── models/
│   ├── nlp/
│   └── vision/
├── generate_mock_data.py
├── requirements.txt
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Clone Repository & Setup Environment
```bash
git clone https://github.com/<your-username>/phishing-website-detector.git
cd phishing-website-detector
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Core Dependencies
```bash
pip install -U pip
pip install numpy pandas scikit-learn matplotlib joblib pillow tldextract beautifulsoup4 lxml fastapi uvicorn anyio
```

### 3. Install PyTorch (CPU Version)
```bash
mkdir -p .venv/tmp
TMPDIR=.venv/tmp pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

---

## ⚙️ Running the Pipeline

### 1. Generate Mock Data
```bash
python generate_mock_data.py
```

### 2. Extract Features
```bash
python -m src.features.build_features
```

### 3. Train Model
```bash
python -m src.models.train
```

### 4. Start API Server
```bash
python -m uvicorn src.api.app:app --reload --port 8000
```

---

## 📡 API Usage

Swagger UI:
```
http://127.0.0.1:8000/docs
```

### Example Request
```bash
curl -X POST \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://safebank.com/login",
    "html_path": "data/raw/html/legit1.html",
    "screenshot_path": "data/raw/screenshots/legit1.png"
  }'
```

### Example Response
```json
{
  "phishing_probability": 0.209,
  "label": 0,
  "components": {
    "text_url_score": 0.024,
    "vision_score": 0.487
  }
}
```

---

## 🚧 Limitations & Future Work

- Requires **offline HTML + screenshots**
- Screenshots resized to 224x224 → may lose details
- Uses **mock dataset** → needs real-world training

Future Improvements:
- Selenium / Playwright integration
- Multi-crop image scanning
- Real phishing datasets (PhishTank, Alexa Top 1M)

---

## ⚠️ Ethical & Safety Notes

- For **educational and defensive cybersecurity only**
- No live crawling (avoids malicious interaction)
- Always run unknown HTML in a **sandbox / VM**

---

## 👨‍💻 Author

**Israel Mbiyavanga David (Mr. Linux)**  
Cybersecurity | Blue Team | Digital Forensics
