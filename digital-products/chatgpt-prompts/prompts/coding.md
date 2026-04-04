# Coding Prompts (35)

## Debugging
```
Debug this code and identify the issue:
[LANGUAGE]: [CODE]

Explain:
- What's wrong
- Why it's happening
- How to fix it
- How to prevent it in future
```

```
Find all bugs in this [LANGUAGE] code:
[CODE]

Priority: Critical → Major → Minor
Each bug: line number, issue, fix
```

## Code Review
```
Review this code for:
[CODE]

Check for:
- Security vulnerabilities
- Performance issues
- Code smells
- Best practices violations
- Memory leaks

Provide a report with severity levels.
```

## Refactoring
```
Refactor this [LANGUAGE] code:
[CODE]

Goals:
- Improve readability
- Reduce complexity
- Better naming
- Remove duplication
- Add comments where needed

Keep functionality identical.
```

## Explain Code
```
Explain what this code does in simple terms:
[CODE]

Language: [LANGUAGE]
Include:
- Overall purpose
- Line-by-line breakdown
- Any gotchas
```

## Write Tests
```
Write unit tests for this code:
[CODE]

Framework: [FRAMEWORK]
Include:
- Happy path
- Edge cases
- Error handling
- Mock dependencies
```

## Optimize Performance
```
Optimize this [LANGUAGE] code for performance:
[CODE]

Current bottleneck: [DESCRIBE]
Focus on: [AREAS]

Show before/after with benchmarks.
```

## Security Audit
```
Audit this code for security vulnerabilities:
[CODE]

Check for:
- SQL injection
- XSS
- CSRF
- Authentication issues
- Data exposure
- Input validation

Provide fixes for each finding.
```

## Document Code
```
Generate documentation for this code:
[CODE]

Include:
- Function/method descriptions
- Parameter descriptions
- Return values
- Examples
- Edge cases
```

## Convert Language
```
Convert this code from [LANGUAGE1] to [LANGUAGE2]:
[CODE]

Maintain:
- Same functionality
- Idiomatic to [LANGUAGE2]
- Best practices for target language
```

## SQL Queries
```
Write optimized SQL query to:
[REQUIREMENT]

Database: [TYPE]
Tables: [DESCRIBE]

Include:
- Main query
- Index suggestions
- Explanation
- Alternative approaches
```

## API Design
```
Design REST API for [RESOURCE]:
Endpoints needed:
- [LIST]

Include:
- HTTP methods
- Request/response formats
- Error codes
- Authentication

OpenAPI format preferred.
```

## Regex Patterns
```
Write regex to match [PATTERN]:
Test cases:
- Should match: [EXAMPLES]
- Should not match: [EXAMPLES]

Language: [LANGUAGE]
```

## Algorithm
```
Implement [ALGORITHM] in [LANGUAGE]:
Requirements:
- [DESCRIBE]

Include:
- Time complexity
- Space complexity
- Test cases
```

## Shell Scripts
```
Write shell script to:
[REQUIREMENT]

OS: [LINUX/MAC]
Include:
- Error handling
- Usage message
- Logging
```

## Dockerfile
```
Write Dockerfile for [APPLICATION]:
Tech stack: [LIST]

Best practices:
- Multi-stage build
- Minimal layers
- Security hardening
- Cache optimization
```

## Git Hooks
```
Write pre-commit hook to:
[REQUIREMENT]

Language: [BASH/NODE]
Include:
- Checks to run
- Error handling
- Clear error messages
```

## CI/CD Pipeline
```
Write GitHub Actions workflow for:
[PROJECT]

Language: [LANGUAGE]
Include:
- Lint
- Test
- Build
- Deploy stages
```

## React Components
```
Create React component for [FEATURE]:
Requirements:
- Props: [LIST]
- State: [LIST]
- Hooks: [LIST]

Style: [CSS/STYLED/Tailwind]
```

## Python Scripts
```
Write Python script to:
[REQUIREMENT]

Include:
- CLI interface (argparse)
- Error handling
- Logging
- Type hints
- Docstrings
```

## Node.js Modules
```
Write Node.js module for [FEATURE]:
Include:
- Exports
- Async/await
- Error handling
- Tests
```

## Data Structures
```
Implement [DATA STRUCTURE] in [LANGUAGE]:
Operations needed:
- [LIST]

Time complexity for each operation.
```

## Error Handling
```
Improve error handling in:
[CODE]

Goals:
- Specific exceptions
- User-friendly messages
- Logging
- Recovery options
```

## Code Comments
```
Add meaningful comments to:
[CODE]

Focus on:
- Why (not what)
- Complex logic
- Non-obvious decisions
- TODOs
```

## Design Patterns
```
Refactor this code to use [PATTERN]:
[CODE]

Explain:
- Why this pattern fits
- Benefits
- Implementation details
```

## Database Schema
```
Design database schema for [APPLICATION]:
Entities: [LIST]

Include:
- Tables with columns
- Data types
- Relationships
- Indexes
- Constraints
```

## Config Files
```
Write config for [APPLICATION]:
Requirements:
- Development
- Production
- Testing

Use [FORMAT]: YAML/TOML/JSON
```

## Deployment Config
```
Write deployment config for [PLATFORM]:
Target: [HEROKU/AWS/VERCEL]

Include:
- Environment variables
- Build settings
- Health checks
- Rollback strategy
```

## Logging
```
Add logging to this code:
[CODE]

Include:
- Log levels
- What to log
- Format
- Rotation
```

## Environment Setup
```
Write setup instructions for [PROJECT]:
Include:
- Prerequisites
- Installation steps
- Configuration
- Running locally
- Testing
```

## Dependency Management
```
Suggest dependency updates for [PROJECT]:
Current versions: [LIST]

Check:
- Security vulnerabilities
- Deprecated packages
- Breaking changes
```

## Type Definitions
```
Add type definitions to:
[CODE]

Language: [TYPESCRIPT/PYTHON]
Include:
- Interfaces
- Types
- Generics
```

## GraphQL Resolvers
```
Write GraphQL resolvers for [API]:
Schema: [DESCRIBE]

Include:
- Query resolvers
- Mutation resolvers
- Error handling
```

## Microservices
```
Design microservice architecture for [APP]:
Services: [LIST]

Include:
- Responsibilities
- Communication
- Data ownership
- Deployment
```

## Event-Driven Architecture
```
Design event-driven system for [USE CASE]:
Events: [LIST]

Include:
- Event types
- Producers
- Consumers
- Error handling
```

## Docker Compose
```
Write docker-compose.yml for [STACK]:
Services: [LIST]

Include:
- Dependencies
- Environment
- Volumes
- Networks
```

## Kubernetes Config
```
Write Kubernetes manifests for [APP]:
Include:
- Deployments
- Services
- ConfigMaps
- Secrets
```

## Prometheus Metrics
```
Add Prometheus metrics to:
[CODE]

Metrics:
- Counter for [EVENT]
- Gauge for [STATE]
- Histogram for [DURATION]

Include labels for [DIMENSIONS].
```

## Authentication
```
Implement JWT authentication for [APP]:
Include:
- Token generation
- Token validation
- Refresh token
- Middleware
```

## Rate Limiting
```
Add rate limiting to [API]:
Limit: [NUMBER] per [TIME]

Include:
- Algorithm
- Storage
- Response headers
```

## Caching Strategy
```
Design caching strategy for [APP]:
Cache: [REDIS/MEMORY]

Include:
- Cache keys
- TTL by data type
- Invalidation
- Warming
```

## Data Validation
```
Add validation to input:
[CODE]

Include:
- Schema
- Custom rules
- Error messages
- Sanitization
```

## File Processing
```
Write code to process [FILE TYPE]:
[REQUIREMENT]

Include:
- Streaming
- Error handling
- Progress tracking
```