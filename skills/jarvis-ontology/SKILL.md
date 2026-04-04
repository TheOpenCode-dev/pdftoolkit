---
name: jarvis-ontology
description: 'A typed vocabulary and constraint system for representing Kunal’s knowledge as a verifiable graph. Use for structured memory, project tracking, and complex dependency mapping.'
---

# Jarvis Ontology System

A local, append-only knowledge graph stored in `memory/ontology/`.

## Core Types
*   **Entity:** `{ id, type, properties, created }`
*   **Relation:** `{ from_id, type, to_id }`

## Workflows
1.  **Create:** `python3 scripts/ontology.py create --type Project --props '{"name":"SkyRoads"}'`
2.  **Relate:** `python3 scripts/ontology.py relate --from proj_001 --rel depends_on --to skill_001`
3.  **Query:** `python3 scripts/ontology.py query --type Task --where '{"status":"open"}'`
4.  **Validate:** `python3 scripts/ontology.py validate`

## Agent Integration
*   **Long-term Memory:** I use this to track your preferences, active projects, and technical constraints.
*   **Constraint Checking:** Before I suggest a plan, I check the graph for "blockers" or "dependencies."
*   **Append-Only:** I never overwrite the graph; I only add new facts to preserve history.

## Storage
*   **Graph:** `memory/ontology/graph.jsonl`
*   **Schema:** `memory/ontology/schema.yaml`