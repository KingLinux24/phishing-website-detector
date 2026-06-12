import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

DATA = "data/processed/features.joblib"

def main():
    data = joblib.load(DATA)

    X_url = data["url_features"]
    X_text = data["text_features"]
    X_vision = data["vision_features"]
    y = data["labels"]

    X_ut = np.hstack([X_url, X_text.toarray()])

    X_ut_tr, X_ut_te, y_tr, y_te = train_test_split(X_ut, y, test_size=0.2, stratify=y)
    X_v_tr, X_v_te, _, _ = train_test_split(X_vision, y, test_size=0.2, stratify=y)

    clf_text = LogisticRegression(max_iter=1000)
    clf_text.fit(X_ut_tr, y_tr)

    clf_vis = RandomForestClassifier(n_estimators=300, n_jobs=-1)
    clf_vis.fit(X_v_tr, y_tr)

    p_text = clf_text.predict_proba(X_ut_te)[:,1]
    p_vis = clf_vis.predict_proba(X_v_te)[:,1]

    p_final = 0.6 * p_text + 0.4 * p_vis
    auc = roc_auc_score(y_te, p_final)

    print(f"Fusion ROC-AUC: {auc:.4f}")

    joblib.dump(clf_text, "src/models/text_model.joblib")
    joblib.dump(clf_vis, "src/models/vision_model.joblib")

if __name__ == "__main__":
    main()
