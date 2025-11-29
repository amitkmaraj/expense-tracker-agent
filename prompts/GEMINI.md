# Expense Tracker Agent - Project Context

## Project Overview
AI-powered expense tracking agent built with Google ADK that helps users manage personal finances through natural language.

## Code Standards

### Python Style
- Use type hints for all function parameters and returns
- Follow PEP 8 naming conventions
- Keep functions under 50 lines
- Use docstrings with Args and Returns sections
- Prefer dataclasses for structured data

### Error Handling
- Always wrap external operations in try-except blocks
- Provide clear, user-friendly error messages
- Log errors with context for debugging
- Never expose internal errors to users

### ADK Agent Patterns
- Keep tools focused - one responsibility per tool
- Use descriptive tool names and docstrings (LLM uses these for routing)
- Return structured data from tools (dicts or dataclasses)
- Include examples in tool docstrings
- Test tools independently before agent integration

### Testing Requirements
- Unit tests for all tools
- Integration tests for agent workflows
- Test edge cases (empty data, invalid inputs)
- Mock external dependencies
- Aim for 80%+ code coverage

## Data Storage
- Use SQLite for development (simple, portable)
- Design schema for easy migration to PostgreSQL
- Never store sensitive data unencrypted
- Include timestamps on all records

## Deployment
- Cloud Run for hosting
- Environment variables for configuration
- Health check endpoint at /health
- Structured logging (JSON format)

## New Features
- Start with PRD in /docs folder
- Update this GEMINI.md with new patterns
- Add examples to /examples folder
- Update tests before merging
- Update the pyproject.toml file with new dependencies whenever they are added/changed
