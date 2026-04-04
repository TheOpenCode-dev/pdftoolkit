---
name: claw-commit
description: 'Create semantic git commits for any project. Analyzes diffs to generate Conventional Commits, stages files logically, and ensures security best practices. Use when the user wants to "commit", "save", or "push" work.'
---

# Claw Commit Skill

A universal tool for creating standardized, semantic git commits using the Conventional Commits specification.

## Core Rules

1.  **Conventional Commits:** Follow `<type>[scope]: <description>`.
2.  **Security First:** Never commit secrets (`.env`, `credentials.json`, private keys).
3.  **Logical Grouping:** Stage files that belong to the same logical change together.

## Commit Types

| Type       | When to use                                      |
| ---------- | ------------------------------------------------ |
| `feat`     | A new feature                                    |
| `fix`      | A bug fix                                        |
| `docs`     | Documentation only changes                       |
| `style`    | Changes that do not affect the meaning of the code (white-space, formatting, etc) |
| `refactor` | A code change that neither fixes a bug nor adds a feature |
| `perf`     | A code change that improves performance          |
| `test`     | Adding missing tests or correcting existing tests |
| `build`    | Changes that affect the build system or external dependencies |
| `ci`       | Changes to our CI configuration files and scripts |
| `chore`    | Other changes that don't modify src or test files |

## Workflow

### 1. Analyze Diff
```bash
git status --porcelain
git diff
```

### 2. Stage Files
```bash
# Stage specific logical groups
git add path/to/file1 path/to/file2
```

### 3. Generate & Commit
Analyze the changes to determine the type and scope.
```bash
git commit -m "feat(auth): add NetSuite OAuth handler"
```

## Best Practices

- **Imperative Mood:** Use "add" instead of "added" or "adds".
- **Concise:** Keep the first line under 72 characters.
- **Body:** Use the body for more detailed explanations if needed.
- **Safety:** If a commit fails due to pre-commit hooks, address the hook's feedback before retrying.