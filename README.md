# 🧠 Strategic Requirements AI

Turn raw stakeholder chaos into clean, sprint-ready documentation — in seconds.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-purple?logo=openai&logoColor=white)
![Model](https://img.shields.io/badge/GPT--4-Enabled-8a2be2)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 🚀 Overview

Strategic Requirements AI takes unstructured stakeholder input — meeting notes, interview fragments, or hallway conversations — and transforms it into structured Agile documentation.

Built for Business Analysts, Product Managers, and Agile teams who want **clarity over confusion** and **speed without sacrificing depth**.

### ✨ Features

- Converts messy input into:
  - ✅ High-level Business Requirements
  - ✅ Functional / Non-functional Requirements
  - ✅ Sprint-Ready User Stories
  - ✅ Acceptance Criteria
  - ✅ Risks, Constraints & Assumptions
- Powered by LLM-backed prompt engineering
- Comes with built-in stakeholder scenarios
- Fully interactive UI with copy-to-clipboard output
- Designed with BA best practices

> 🔐 Note: LLM integration implemented but kept private in this repo.


---

## 🧪 Try It Live

Paste unstructured input like:

- [PM] Users are abandoning checkout.
- [UX] The payment form is long.
- [Dev] Needs to support mobile.
- [Stakeholder] Add Apple Pay support?



And receive structured Agile artifacts in seconds.

---

## 🛠️ Local Setup

- bash
- git clone https://github.com/abisla/ai-requirements-generator.git
- cd ai-requirements-generator
- pip install -r requirements.txt
- python app.py
- Then open http://localhost:5000 in your browser.

## 🧠 Prompt Logic (Partial)
- You are a senior business analyst assistant. Your job is to convert raw stakeholder input into...
Custom-tuned to extract business logic from informal conversations, while maintaining traceability.

## 📂 Folder Structure

├── app.py # Flask backend
├── index.html # Frontend UI
├── prompt.txt # LLM instruction prompt
├── requirements.txt
└── .env # API keys (not included)



## 📈 Metrics

| KPI                 | Value     |
|---------------------|-----------|
| Time Saved          | 95%       |
| Processing Time     | < 1 min   |
| Output Sections     | 8         |
| Format Compatibility| ✅ JIRA   |

## 🤝 Connect

Built by Amar Bisla  
Business Analyst × AI Systems Builder  
[LinkedIn](https://www.linkedin.com/in/abisla)

## 🛡️ License
MIT License — [View License](LICENSE)
