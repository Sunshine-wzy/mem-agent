# mem-agent

## Getting Started

### Environmental Setup

```bash
conda create -n mem_agent python=3.10
conda activate mem_agent
poetry install
```

### Usage

```bash
python main.py
```

## Evaluation

### Installation

```bash
poetry install --with eval
```

### Configuration

1. Copy the `.env-example` file to `.env`, and fill in the required environment variables according to your environment and API keys.

2. Copy the `configs-example/` directory to a new directory named `configs/`, and modify the configuration files inside it as needed. This directory contains model and API-specific settings.

### LoCoMo Evaluation
⚙️ To evaluate the **LoCoMo** dataset using one of the supported memory frameworks — `memos`, `mem0`, or `zep` — run the following [script](./scripts/run_locomo_eval.sh):

```bash
# Edit the configuration in ./scripts/run_locomo_eval.sh
# Specify the model and memory backend you want to use (e.g., mem0, zep, etc.)
./scripts/run_locomo_eval.sh
```
