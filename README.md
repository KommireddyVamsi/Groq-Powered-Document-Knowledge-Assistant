# Groq-Powered Document Knowledge Assistant

## Overview

This project demonstrates how to build a simple AI-powered knowledge assistant using the Groq API and the Qwen 3.6 27B model.

The application loads information from a local text file (`knowledge.txt`) and uses that content as the knowledge source for answering user questions. Users can interact with the assistant through a command-line interface, and the AI generates responses based on the provided document.

This project is a lightweight alternative to traditional RAG systems and is ideal for learning document-grounded AI applications.

---

## Features

* Local document-based knowledge source
* Groq API integration
* Qwen 3.6 27B language model
* Interactive command-line chat
* Simple implementation with minimal dependencies
* Custom knowledge-based AI assistant

---

## How It Works

### Step 1: Load Knowledge File

The application reads content from:

```text
knowledge.txt
```

Example:

```python
with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()
```

---

### Step 2: User Asks a Question

Example:

```text
Ask AI: What is the company leave policy?
```

---

### Step 3: Inject Knowledge into the Prompt

The contents of the document are passed to the model through a system message:

```python
{
    "role": "system",
    "content": f"Answer only from this document:\n\n{knowledge}"
}
```

This instructs the model to use the document as the source of truth when answering questions.

---

### Step 4: Send Request to Groq

The application sends:

* Knowledge document
* User question

to the Groq-hosted Qwen model.

```python
response = client.chat.completions.create(
    model="qwen/qwen3.6-27b",
    messages=[...]
)
```

---

### Step 5: Display AI Response

The generated answer is printed to the console.

```python
print(response.choices[0].message.content)
```

---

## Architecture

```text
knowledge.txt
      │
      ▼
Python Application
      │
      ▼
System Prompt Injection
      │
      ▼
Groq API
      │
      ▼
Qwen 3.6 27B
      │
      ▼
AI Response
      │
      ▼
Console Output
```

---

## Technology Stack

* Python
* Groq API
* Qwen 3.6 27B
* OpenAI SDK (Groq-Compatible)
* Prompt Engineering

---

## Learning Objectives

This project helps developers understand:

* Groq API Integration
* Large Language Model Usage
* Knowledge-Based AI Assistants
* Prompt Engineering
* Document Question Answering
* Context Injection Techniques
* Foundation Concepts Behind RAG

---

## Example

### Knowledge File

```text
Company Name: ABC Technologies
Annual Leave: 24 Days
Work Mode: Hybrid
```

### Question

```text
What is the work mode?
```

### Response

```text
Hybrid
```

---

## Current Limitation

The entire document is sent to the model for every question.

For larger documents, this can:

* Increase token consumption
* Increase latency
* Increase API costs

For enterprise-scale knowledge bases, a Retrieval-Augmented Generation (RAG) architecture is recommended.

---

## Future Enhancements

* Vector Database Integration
* Semantic Search
* RAG Pipeline
* PDF Support
* DOCX Support
* Multiple Knowledge Sources
* Web-Based User Interface
* Conversation Memory
* Enterprise Knowledge Management System

---

## Use Cases

* Company Policy Assistant
* Internal Knowledge Base Search
* FAQ Chatbot
* Employee Self-Service Assistant
* Technical Documentation Search
* Learning and Training Assistant

---

## Disclaimer

This project uses prompt-based document grounding. While the model is instructed to answer from the provided document, strict source enforcement may require additional validation or RAG techniques for production environments.
