import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

from src.data.load_data import load
from src.nlp.url_features import url_features
from src.nlp.html_text import extract_text
from src.vision.embed import embed_image

OUT = "data/processed/features.joblib"

def main():
    df = load()

    # URL features
    url_feat_df = pd.DataFrame(df["url"].apply(url_features).tolist())

    # HTML TF-IDF
    texts = df["html_path"].apply(extract_text).tolist()
    tfidf = TfidfVectorizer(max_features=3000, stop_words="english")
    X_text = tfidf.fit_transform(texts)

    # Vision embeddings
    vision_embs = np.vstack(df["screenshot_path"].apply(embed_image).values)

    joblib.dump(tfidf, "src/models/tfidf.joblib")

    joblib.dump(
        {
            "url_features": url_feat_df.values,
            "text_features": X_text,
            "vision_features": vision_embs,
            "labels": df["label"].values,
        },
        OUT
    )

if __name__ == "__main__":
    main()
