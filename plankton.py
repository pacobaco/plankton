# Plankton: DAO Whale Alignment Scoring Toolkit

"""
Plankton is a deployable Python-based toolkit for real-time analysis of DAO wallets.
It computes whale alignment scores, extracts proposal embeddings, clusters coalition behavior,
and provides an API endpoint for querying wallet alignment.
"""

from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer, util
import requests
import json
import os
import hashlib
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import streamlit as st

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

# --- Proposal Embedding Cache ---
CACHE_FILE = "proposal_cache.json"
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        EMBEDDING_CACHE = json.load(f)
else:
    EMBEDDING_CACHE = {}


def get_cached_embedding(text):
    key = hashlib.sha256(text.encode()).hexdigest()
    if key in EMBEDDING_CACHE:
        return np.array(EMBEDDING_CACHE[key])
    embedding = model.encode(text)
    EMBEDDING_CACHE[key] = embedding.tolist()
    with open(CACHE_FILE, "w") as f:
        json.dump(EMBEDDING_CACHE, f)
    return embedding


# --- DAO Data Fetching (Placeholder) ---
def fetch_wallet_votes(wallet_address):
    # Replace with Snapshot/Tally/DeepDAO integrations
    return [
        {"title": "Launch zk infrastructure grants", "vote": "yes"},
        {"title": "Fund DAO resilience program", "vote": "yes"},
        {"title": "Create a treasury diversification strategy", "vote": "yes"},
        {"title": "Oppose short-term rent extraction", "vote": "no"}
    ]


# --- Whale Alignment Scoring ---
def calculate_alignment_score(new_proposal_text, wallet_address):
    past_votes = fetch_wallet_votes(wallet_address)
    new_vec = get_cached_embedding(new_proposal_text)
    scores = []
    for vote in past_votes:
        if vote["vote"].lower() == "yes":
            vec = get_cached_embedding(vote["title"])
            similarity = float(util.cos_sim(new_vec, vec))
            scores.append(similarity)
    return round(sum(scores) / len(scores), 2) if scores else 0.0


# --- Proposal Clustering ---
def cluster_proposals(wallet_address):
    votes = fetch_wallet_votes(wallet_address)
    titles = [v["title"] for v in votes if v["vote"] == "yes"]
    embeddings = [get_cached_embedding(t) for t in titles]
    kmeans = KMeans(n_clusters=min(len(embeddings), 3))
    labels = kmeans.fit_predict(embeddings)
    return list(zip(titles, labels))


# --- API Endpoint ---
@app.route("/wallet/<wallet>", methods=['GET'])
def wallet_insight(wallet):
    query = request.args.get("proposal", default="Fund ecosystem development")
    score = calculate_alignment_score(query, wallet)
    clusters = cluster_proposals(wallet)
    response = {
        "wallet": wallet,
        "alignment_score": score,
        "reference_proposal": query,
        "clustered_votes": clusters,
        "whale_cluster": "Alpha Ring (stub)"
    }
    return jsonify(response)


# --- Streamlit Dashboard ---
def render_dashboard():
    st.title("🐋 Plankton: DAO Whale Alignment Dashboard")
    wallet = st.text_input("Wallet Address", "0x1234...abcd")
    proposal = st.text_area("New Proposal", "Fund ecosystem development")

    if st.button("Analyze"):
        score = calculate_alignment_score(proposal, wallet)
        clusters = cluster_proposals(wallet)
        st.metric("Alignment Score", score)
        st.write("### Clustered Proposals")
        for title, label in clusters:
            st.write(f"[{label}] {title}")


if __name__ == '__main__':
    import sys
    if "dashboard" in sys.argv:
        render_dashboard()
    else:
        app.run(debug=True)
