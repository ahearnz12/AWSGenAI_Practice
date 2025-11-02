# AWS GenAI Practice Exercises

A comprehensive collection of hands-on exercises exploring AWS Bedrock and generative AI capabilities. This repository demonstrates practical applications of AWS GenAI services including video generation, guardrails, prompt management, and AI agents.

## 📚 Repository Structure

### Exercise 1: Video Generation with Amazon Nova Reel
**Location:** `exercise1/`

**Main Topics:**
- Asynchronous video generation using Amazon Nova Reel model
- S3 integration for storing generated video content
- AWS Bedrock runtime client usage
- Streaming responses from foundation models

**Key Concepts:**
- TEXT_VIDEO generation with customizable parameters (FPS, duration, dimensions)
- Job submission and status monitoring patterns
- `invoke_model` vs `invoke_model_with_response_stream` methods
- Practical implementation of Amazon Nova Micro for text generation

**Files:**
- `genai-exercise-video.ipynb` - Interactive notebook demonstrating video generation and model invocation

---

### Exercise 2: Task Tracker Web Application
**Location:** `exercise2/code/`

**Main Topics:**
- Flask-based web application development
- RESTful API design
- Data persistence with JSON file storage
- Object-oriented programming in Python

**Key Concepts:**
- Model-View-Controller (MVC) architecture
- Task management with priority sorting
- API endpoint design (GET, POST, DELETE)
- Automatic state persistence between sessions
- Class-based design (Task and TaskManager classes)

**Files:**
- `app.py` - Flask backend with API endpoints
- `task_tracker.py` - Task and TaskManager class definitions
- `templates/index.html` - Frontend interface
- `requirements.txt` - Python dependencies

**Teaching Points:**
- Building production-ready web applications
- Separation of concerns in application architecture
- Error handling and input validation
- File I/O operations in Python

---

### Exercise 3: AWS Bedrock Guardrails
**Location:** `exercise3/code/`

**Main Topics:**
- Content filtering and moderation using Bedrock Guardrails
- PII (Personally Identifiable Information) detection and redaction
- Prompt injection attack prevention
- Grounding and hallucination detection

**Key Concepts:**
- `apply_guardrail` API for content validation
- Guardrail configuration with multiple content qualifiers
- Tag-based guardrail application in prompts
- Input/output filtering strategies
- Trace enablement for debugging guardrail behavior

**Files:**
- `genai-exercise3-guardrail.ipynb` - Interactive demonstrations of guardrail features
- `CLAUDE.md` - Development guidance and environment setup

**Teaching Points:**
- Responsible AI practices and safety measures
- Protecting against prompt injection attacks
- Validating AI-generated responses for accuracy
- Multi-layered content filtering approaches

---

### Exercise 4: Prompt Management & Lambda Integration
**Location:** `exercise4/code/`

**Main Topics:**
- AWS Bedrock Prompt Management
- Prompt versioning and deployment
- Lambda function integration with Bedrock
- Template-based prompt engineering

**Key Concepts:**
- Creating reusable prompt templates with variables
- Prompt version control and management
- Input variable configuration
- Inference parameter optimization (temperature, topP, maxTokens)
- Production-ready prompt deployment strategies

**Files:**
- `prompt_management.ipynb` - Prompt creation, versioning, and invocation
- `genai-exercise5-lambda.ipynb` - Lambda integration examples

**Teaching Points:**
- Professional prompt engineering practices
- Managing prompts as code
- Separating prompt logic from application code
- Consistent AI behavior through versioned prompts

---

### Exercise 5: Advanced Guardrails & Multi-Turn Conversations
**Location:** `exercise5/code/`

**Main Topics:**
- Multi-turn conversation management with Bedrock
- Context-aware travel recommendation system
- Custom guardrail creation for domain-specific validation
- Converse API for chat-based interactions

**Key Concepts:**
- System prompts and conversation state management
- Message history tracking and context preservation
- Custom guardrail logic for business rule validation
- Travel agent prompt with structured screening questions
- Temperature tuning for consistent responses

**Files:**
- `genai-exercise5-guardrail.ipynb` - Multi-turn conversations and custom guardrails

**Teaching Points:**
- Building conversational AI applications
- Managing conversation context and memory
- Domain-specific validation logic
- User intent classification and requirement gathering

---

### Exercise 6: Bedrock Agents with Function Calling
**Location:** `exercise6/code/`

**Main Topics:**
- AWS Bedrock Agents for agentic AI workflows
- Lambda function integration with agents
- Function-based action groups
- SQLite database integration
- IAM role and policy management for Bedrock services

**Key Concepts:**
- Agent configuration with custom instructions
- Function schema definitions for agent capabilities
- Lambda as agent action group executor
- Database operations in Lambda ephemeral storage
- Agent aliases and versioning
- Session management and invocation patterns
- Complete infrastructure setup using boto3

**Files:**
- `agent.ipynb` - Complete Bedrock Agent implementation notebook
- `lambda_function.py` - Lambda handler for vacation management
- `employee_database.db` - SQLite database with employee vacation data

**Teaching Points:**
- Building autonomous AI agents with decision-making capabilities
- Serverless architecture with Lambda and Bedrock
- Function calling vs API-based integration patterns
- Agent orchestration and tool use
- Production considerations for database persistence
- Complete AWS resource lifecycle management (create, configure, test, cleanup)
- IAM security best practices for multi-service integration

**Use Case:**
HR Assistant Agent that helps employees:
- Query available vacation days
- Reserve vacation time with validation
- Manage vacation schedules through natural language

---

## 🛠️ Technology Stack

- **AWS Services:** Bedrock, Lambda, S3, IAM
- **AI Models:** Amazon Nova Micro, Amazon Nova Reel, Claude 3 Sonnet
- **Languages:** Python 3.9+
- **Frameworks:** Flask, Jupyter, boto3
- **Storage:** SQLite, JSON, S3

## 🚀 Getting Started

Each exercise folder contains its own virtual environment and dependencies. To run an exercise:

1. **Navigate to the exercise folder:**
   ```bash
   cd exerciseX
   ```

2. **Activate the virtual environment:**
   ```bash
   source bin/activate
   ```

3. **Launch Jupyter (for notebook-based exercises):**
   ```bash
   jupyter lab
   ```

4. **Run Flask app (Exercise 2):**
   ```bash
   cd exercise2/code
   python app.py
   ```

## 🔑 Prerequisites

- AWS account with Bedrock access
- AWS credentials configured (`~/.aws/credentials` or environment variables)
- IAM permissions for:
  - Bedrock model invocation
  - Bedrock Agents and Guardrails
  - Lambda function management
  - S3 read/write access
  - IAM role creation (Exercise 6)

## 📖 Learning Path

**Recommended order:**
1. **Exercise 1** - Learn Bedrock basics and model invocation
2. **Exercise 2** - Build supporting infrastructure (web app skills)
3. **Exercise 3** - Implement safety measures with guardrails
4. **Exercise 4** - Master prompt engineering and management
5. **Exercise 5** - Create conversational AI experiences
6. **Exercise 6** - Build complete agentic AI systems

## 🎯 Key Takeaways

- **Bedrock Runtime:** Direct model invocation for text and video generation
- **Guardrails:** Essential for production AI applications to ensure safety and compliance
- **Prompt Management:** Version control and templating for consistent AI behavior
- **Agents:** Autonomous systems that can reason, plan, and execute actions
- **Serverless Integration:** Lambda functions as compute layer for AI-powered backends
- **Responsible AI:** Implementing safeguards, validation, and ethical considerations

## 📝 Notes

- Some exercises may incur AWS charges for Bedrock model usage
- Ensure proper cleanup of AWS resources after testing (especially Exercise 6)
- Lambda's `/tmp/` storage is ephemeral - use appropriate databases for production
- Guardrail IDs and model ARNs are environment-specific and may need updating

## 🤝 Contributing

This is a learning repository. Feel free to experiment, modify, and extend the exercises for your own learning purposes.

## 📄 License

Educational use only.