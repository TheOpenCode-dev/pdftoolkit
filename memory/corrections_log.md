# corrections_log.md — Raw Log of All Corrections

# Format per entry:
# [LOG-XXX] | YYYY-MM-DD HH:MM | domain: [project/general]
# Trigger: [exact words Kunal used]
# What was wrong: [one sentence]
# Rule extracted: [what Jarvis learned]
# Repetition count: 1 of 3
# Status: watching | pending_promotion | promoted | rejected

# Active corrections being tracked:

[LOG-001] | 2026-04-03 04:00 | domain: system
Trigger: nightly-review found empty correction tracking
What was wrong: The self-improvement system (corrections_log + hot_memory) was never populated — system has no mechanism to learn from repeated patterns.
Rule extracted: Every nightly-review must log at least one learning or improvement, even if nothing went wrong.
Repetition count: 1 of 3
Status: watching