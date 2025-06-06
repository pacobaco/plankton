Here is the README.md as plain text:

⸻



# 🐋 Plankton: DAO Whale Alignment Scoring Toolkit

Plankton is a real-time analytics engine that identifies how likely a DAO wallet (whale or voter) is to support a given proposal, based on past voting behavior and proposal similarity. It helps coalition builders, DAO strategists, and ecosystem contributors better understand and engage with influential on-chain actors.

---

## Features

- Alignment Scoring: Measures similarity between a wallet’s past votes and a proposed item using sentence embeddings.
- Proposal Clustering: Groups previously supported proposals using KMeans to uncover voting blocs or themes.
- Embedding Cache: Speeds up repeat queries with local caching of sentence vectors.
- REST API: Query alignment scores via wallet address and proposal string.
- Streamlit Dashboard: Interactive interface for live exploration.

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/plankton.git
cd plankton
pip install -r requirements.txt



⸻

Usage

Run API Server

python plankton.py

Then query:
GET /wallet/<wallet_address>?proposal=Your+proposal+text

Run Dashboard

python plankton.py dashboard



⸻

Example API Response

{
“wallet”: “0x1234…abcd”,
“alignment_score”: 0.86,
“reference_proposal”: “Fund decentralized R&D”,
“clustered_votes”: [
[“Launch zk infrastructure grants”, 0],
[“Fund DAO resilience program”, 1]
],
“whale_cluster”: “Alpha Ring (stub)”
}

⸻

Files
	•	plankton.py – Main logic (API + dashboard)
	•	requirements.txt – Dependencies
	•	.gitignore – Ignores cache, Python build files
	•	proposal_cache.json – Auto-generated vector cache

⸻

Roadmap
	•	Snapshot + Tally API integration
	•	Discord/Telegram notification bot
	•	Whale tracker leaderboard
	•	More clustering logic (e.g. DBSCAN, coalition fingerprinting)

⸻

Contributions Welcome

Feel free to open issues or PRs with enhancements, use cases, or DAO-specific modules!

⸻

License

MIT License © Juan Rodriguez & contributors

Let me know if you'd like to convert this into a `.txt`, `.pdf`, or zipped repo.
