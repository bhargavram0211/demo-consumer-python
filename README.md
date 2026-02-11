# Demo Consumer Repository - Python Flask API

This is a **demonstration repository** for testing [Sentinel-Flow](https://github.com/YOUR-GITHUB-USERNAME/sentinel-flow) secret scanning capabilities.

## ⚠️ IMPORTANT NOTICE

**This repository intentionally contains hardcoded secrets for testing purposes.**

The secrets in `app.py` and `config.py` are:
- Fake/example credentials (not real)
- Intentionally committed to demonstrate Gitleaks detection
- Should trigger security scan failures when creating PRs

**In a real application, NEVER hardcode credentials!** Always use environment variables or secret management services.

## 🎯 Purpose

This demo repository demonstrates:
1. How to integrate Sentinel-Flow into your project
2. How secret scanning detects hardcoded credentials
3. How PR checks block merges when secrets are found
4. How to suppress false positives using `.gitleaks.toml`

## 🚀 Setup

### Prerequisites

- Python 3.9+
- GitHub account
- Sentinel-Flow set up in your GitHub account

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/demo-consumer-python.git
cd demo-consumer-python
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 🧪 Testing Sentinel-Flow Integration

### Test 1: Create a PR with Existing Secrets

The current codebase has intentional secrets in:
- `app.py` - AWS keys, GitHub token, database credentials, API keys
- `config.py` - Slack webhook, Stripe key, SendGrid key, JWT secret

**Expected Result:** ❌ Security check should FAIL and block the PR

### Test 2: Create a PR without Secrets

1. Create a branch:
```bash
git checkout -b test/clean-code
```

2. Make a change that doesn't add secrets (e.g., update README):
```bash
echo "# Test" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "docs: add changelog"
git push origin test/clean-code
```

3. Create a PR

**Expected Result:** ✅ Security check should PASS

### Test 3: Add New Secret in PR

1. Create a branch:
```bash
git checkout -b test/new-secret
```

2. Add a new secret to `app.py`:
```python
NEW_API_KEY = "secret_key_123456789"
```

3. Commit and push:
```bash
git add app.py
git commit -m "feat: add new feature"
git push origin test/new-secret
```

4. Create a PR

**Expected Result:** ❌ Security check should FAIL and detect the new secret

### Test 4: Suppress False Positives

If you have a legitimate use case (test data, examples), create `.gitleaks.toml`:

```toml
[allowlist]
description = "Allowlist for known test secrets"

regexes = [
    '''EXAMPLETEST''',  # Suppress our test AWS key
]

paths = [
    '''.*test.*''',  # Ignore all test files
]
```

Commit this file and the scan will ignore the specified patterns.

## 📝 API Endpoints

- `GET /` - Home endpoint with API info
- `GET /health` - Health check endpoint
- `GET /api/data` - Sample data endpoint

Example:
```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/api/data
```

## 🔧 Configuration

The workflow is configured in `.github/workflows/security-secrets.yml`:

```yaml
uses: YOUR-GITHUB-USERNAME/sentinel-flow/.github/workflows/reusable-secrets.yml@main
with:
  gitleaks_mode: 'pr-only'
  fail_on_findings: true
  upload_sarif: true
```

### Configuration Options

- **gitleaks_mode**: 
  - `pr-only` (default) - Fast, scans only PR changes
  - `full-history` - Comprehensive, scans entire git history

- **fail_on_findings**:
  - `true` (default) - Block PR if secrets found
  - `false` - Report only, don't block

- **upload_sarif**:
  - `true` (default) - Upload to GitHub Security tab
  - `false` - Skip SARIF upload

## 🎓 Learning Objectives

By using this demo, you'll learn:

1. **Secret Detection** - How security scanners identify credentials in code
2. **GitHub Actions** - Reusable workflows and CI/CD integration
3. **SARIF Format** - Standardized security reporting
4. **DevSecOps** - Shift-left security practices
5. **False Positive Management** - Using allowlists appropriately

## 🤝 Contributing

This is a demo repository. Feel free to:
- Test different scenarios
- Report issues with Sentinel-Flow
- Suggest improvements

## 📄 License

MIT License - Feel free to use this as a learning resource

## 🔗 Links

- [Sentinel-Flow Repository](https://github.com/YOUR-GITHUB-USERNAME/sentinel-flow)
- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Remember:** This repository contains intentional test secrets. In real projects, always use environment variables and secret management services!

## Additional Info
