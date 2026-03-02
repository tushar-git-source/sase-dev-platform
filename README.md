# sase-dev-platform
# DevEx Platform Assignment – SASE Dev Environment

This repository demonstrates a Developer Experience (DevEx) focused platform setup for a sample SASE core networking service.

The goal of this project is to:

- Provide a reproducible local development environment
- Enforce code quality and security gates
- Automate repository hygiene
- Integrate AI-based workflow enhancement
- Ensure CI/CD reliability with fail-fast design
- Avoid hardcoded secrets and support mock mode

---

# 🏗 Architecture Overview

The solution consists of:

- Flask-based sample service (`app.py`)
- Dockerized development environment
- GitHub Actions CI pipeline
- Repository hygiene automation
- AI-based PR summarization tool
- Security scanning (dependencies + secrets)

## 📁 Repository Structure

```text
sase-dev-platform/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
│
├── tests/
│   └── test_app.py
│
├── scripts/
│   ├── repo_hygiene.py
│   └── ai_pr_summary.py
│
├── docs/
│   └── PR_SUMMARY.md
│
└── .github/
    └── workflows/
        └── ci.yml
```
