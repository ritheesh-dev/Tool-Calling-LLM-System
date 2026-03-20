# Autonomous Tool-Calling Agent

An LLM agent built from scratch using Ollama + Mistral that reasons,
selects tools dynamically, and dispatches real function calls —
no LangChain, no frameworks, just raw Python.

## Architecture
```
User Query
    ↓
tool_description.py    # Tool schemas exposed to the LLM
    ↓
action_selection.py    # LLM reasons and decides which tool to call
    ↓
parse.py               # Parses LLM output → (action_type, tool_name, argument)
    ↓
tool_dispatcher.py     # Executes the selected tool
    ↓
create_tools.py        # Tool implementations
    ↓
Ollama (follow-up)     # LLM generates final answer using tool result
```

## Available Tools
| Tool | Description |
|------|-------------|
| `get_weather` | Fetches live weather for any city via wttr.in |
| `calculate` | Safely evaluates math expressions |
| `get_current_date` | Returns today's date |

## Features
- Two-stage inference: reasoning → structured action → final answer
- Multi-turn loop — keeps running until user exits
- Dynamic tool dispatch based on query intent
- Real external API call (wttr.in weather)
- Safe math evaluation (no builtins exploit)
- Zero framework dependency — raw Ollama SDK only

## Tech Stack
- LLM: Mistral via Ollama
- Language: Python 3.x
- External: wttr.in (weather)

## Setup
```bash
ollama pull mistral
pip install -r requirements.txt
python src/main.py
```

## Example
```
Ask something (or 'exit' to quit): What's the weather in Chennai?
[using tool]: ('get_weather', 'Chennai')
[Tool result: Chennai: ⛅️ +31°C]
Answer: It's currently 31°C and partly cloudy in Chennai...

Ask something (or 'exit' to quit): What is 143 * 7?
[using tool]: ('calculate', '143 * 7')
[Tool result: 1001]
Answer: 143 multiplied by 7 is 1001.
```

## Why built from scratch?
Most tutorials abstract away the hard parts. This project intentionally
avoids LangChain to understand how tool-calling actually works —
how tools are described to the LLM, how outputs are parsed,
and how function dispatch is handled reliably.