# Resume Analyzer & Improver

A simple OpenAI Agents SDK project for AI-powered resume review and rewriting.

## Overview

This repository demonstrates:
- OpenAI Agents SDK usage with at least 1 agent and 2 tools
- Structured JSON-style output for resume feedback
- Memory persistence for adapting future suggestions based on past interactions
- A minimal CLI interface (Gradio UI is optional and not included)

## Features

- `analyze_resume`: reviews resume text and returns strengths, weaknesses, role fit, and formatting recommendations
- `suggest_improvements`: rewrites resume content with stronger language and measurable results
- `MemoryStore`: stores past interactions and lets the agent adapt to prior feedback

## Project structure

- `main.py`: CLI entrypoint for running the Resume Analyzer agent
- `agent.py`: OpenAI Agent SDK wrapper, tools, and structured outputs
- `memory_store.py`: persistent memory storage for past interactions
- `ARCHITECTURE.md`: architecture explanation and diagram
- `sample_outputs.md`: sample agent outputs and data format
- `VIDEO_SCRIPT.md`: script for a demo video explanation
- `requirements.txt`: Python dependencies

## Setup

1. Create a Python environment

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the CLI and follow the options:

```bash
python main.py
```

Then choose:
1. Analyze a resume
2. Rewrite and improve a resume
3. Show memory history
4. Exit

## Notes

- The repository uses the OpenAI Agents SDK pattern to define two tools and orchestrate resume analysis.
- Memory is stored in `resume_memory.json` so the system can reference previous interactions.
- Structured output is returned as Python dictionaries and printed as JSON.
