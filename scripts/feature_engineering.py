"""Handcrafted URL features reconstructed from report section 5.3."""

import re
import tldextract

FEATURE_NAMES = (
    "url_length",
    "num_dots",
    "has_ip",
    "num_subdomains",
    "num_special_chars",
)


def extract_features(url):
    """Return the report's five URL features in their original order."""
    extracted = tldextract.extract(url)
    subdomain_count = len(extracted.subdomain.split(".")) if extracted.subdomain else 0
    features = {
        "url_length": len(url),
        "num_dots": url.count("."),
        "has_ip": int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url))),
        "num_subdomains": subdomain_count,
        "num_special_chars": sum(url.count(char) for char in ("@", "-", "_", "=")),
    }
    return list(features.values())
