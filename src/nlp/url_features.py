import re
import tldextract

SUSPICIOUS = {"login", "verify", "update", "secure", "account", "bank"}

def url_features(url: str) -> dict:
    ext = tldextract.extract(url)
    tokens = re.split(r"[./\-?_=&]", url.lower())

    return {
        "url_length": len(url),
        "dot_count": url.count("."),
        "has_ip": int(bool(re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", url))),
        "suspicious_token_count": sum(t in SUSPICIOUS for t in tokens),
        "tld_length": len(ext.suffix or ""),
    }
