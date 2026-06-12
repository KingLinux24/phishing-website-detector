import joblib
import numpy as np

from src.nlp.url_features import url_features
from src.nlp.html_text import extract_text
from src.vision.embed import embed_image

clf_text = joblib.load("src/models/text_model.joblib")
clf_vis = joblib.load("src/models/vision_model.joblib")
tfidf = joblib.load("src/models/tfidf.joblib")

def predict(url: str, html_path: str, screenshot_path: str) -> dict:
    uf = np.array([list(url_features(url).values())])
    text = tfidf.transform([extract_text(html_path)]).toarray()
    ut = np.hstack([uf, text])

    v = embed_image(screenshot_path).reshape(1, -1)

    p_text = clf_text.predict_proba(ut)[0,1]
    p_vis = clf_vis.predict_proba(v)[0,1]

    risk = 0.6 * p_text + 0.4 * p_vis

    return {
        "phishing_probability": round(float(risk), 3),
        "label": int(risk >= 0.5),
        "components": {
            "text_url_score": round(float(p_text), 3),
            "vision_score": round(float(p_vis), 3)
        }
    }
