# AI Coding Agent

A toy version of a command-line AI coding agent that can list files, read and write files, and run Python scripts in the `calculator/` working directory. It uses OpenRouter to select and call tools based on your request. This project is not suitable for others to use.

## Setup

Set your OpenRouter API key in a `.env` file:

```env
OPENROUTER_API_KEY=your-api-key
```

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Run

Pass your request as a quoted argument:

```bash
uv run main.py "List the files"
```

For example, to run a script in the working directory:

```bash
uv run main.py "Run tests.py"
```

Add `--verbose` to show tool calls and token usage:

```bash
uv run main.py "List the files" --verbose
```