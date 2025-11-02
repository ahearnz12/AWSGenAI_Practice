# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Exercise 3 of an AWS GenAI workshop series, focused on implementing guardrails for generative AI applications. The project uses Jupyter notebooks to demonstrate AWS Bedrock guardrail concepts.

## Environment Setup

This project uses a Python 3.9 virtual environment located at the project root.

**Activate the virtual environment:**
```bash
source bin/activate
```

**Deactivate when done:**
```bash
deactivate
```

## Running Notebooks

The main notebook is located in `code/genai-exercise3-guardrail.ipynb`.

**Start Jupyter Lab:**
```bash
jupyter lab
```

**Start Jupyter Notebook (classic interface):**
```bash
jupyter notebook
```

The notebook will open in your browser, typically at `http://localhost:8888`.

## Key Dependencies

- **boto3/botocore** - AWS SDK for Python, used to interact with AWS Bedrock and other AWS services
- **jupyter/jupyterlab** - Interactive notebook environment for development and demonstration
- **httpx/httpcore** - HTTP client library for API interactions

## Architecture

This exercise is part of a series:
- **exercise1** - Video processing with GenAI
- **exercise2** - Task tracker web application (Flask-based)
- **exercise3** - Guardrails for GenAI applications (this project)

The notebook-based approach allows for interactive exploration of AWS Bedrock guardrails, which are used to:
- Control AI-generated content
- Filter sensitive information
- Enforce content policies
- Validate inputs and outputs

## AWS Integration

This project interacts with AWS services, particularly AWS Bedrock. Ensure you have:
1. AWS credentials configured (via `~/.aws/credentials` or environment variables)
2. Appropriate IAM permissions for Bedrock access
3. Access to the required Bedrock models and guardrail APIs

## Development Workflow

1. Activate the virtual environment
2. Launch Jupyter Lab or Jupyter Notebook
3. Open `code/genai-exercise3-guardrail.ipynb`
4. Execute cells sequentially to explore guardrail concepts
5. AWS Bedrock API calls will be made from within notebook cells using boto3
