---
name: kunal-github
description: 'Kunal’s personal GitHub command center. Automates repo management, PR reviews, and release tracking with built-in security checks.'
---

# Kunal's GitHub Command Center

A specialized skill for managing the "Zero-Human Company" codebase and contributing to open source.

## Core Workflows

### 1. The "Clean Commit" Check
Before any code is merged, use this workflow:
```bash
gh pr view --json files,additions,deletions
# Verify no .env or credentials are exposed
# Ensure conventional commits are used
```

### 2. Micro-SaaS Release Automation
When a project (like `ai-integration-sandbox`) is ready:
```bash
gh release create v1.0.0 --title "MVP Launch" --notes "Initial secure release"
```

### 3. Security Audit (ClawSec Integration)
Before pushing to `main` on any public repo:
- Run `clawsec-suite` checks.
- Use `gh api` to verify branch protection rules are active.

## Kunal-Specific Aliases
- **`gh revenue`**: A custom script alias to check Gumroad API sales and log them to our `jarvis-ontology` graph.
- **`gh deploy`**: A wrapper to trigger Render/Vercel deployments via webhook.

## Security Constraints
- **NEVER** commit `openclaw.json` or any file containing `__OPENCLAW_REDACTED__`.
- **ALWAYS** verify the remote URL before pushing to prevent accidental leaks to public forks.
- **REQUIRE** 2FA/SSH key authentication for all writes.

## Ontology Integration
Every PR merged or Issue closed should be logged in our **Ontology Mind Map** to track progress toward the $1M ARR goal.