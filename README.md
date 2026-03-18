# 🚀 SmartCode Auditor: AI-Driven Bug Detection & Remediation

> An intelligent code review system that combines static analysis, semantic retrieval, and LLM-powered remediation to detect bugs, explain risks, and suggest fixes for Python code.

---

## 📌 Overview

**SmartCode Auditor** is an AI-powered code review agent built to analyze Python code beyond simple keyword matching.

Instead of only checking for hardcoded patterns, it combines:

- 🌳 AST-based static code analysis
- 🧠 Code embeddings using CodeBERT
- 🔎 Vector similarity search with ChromaDB
- 🤖 LLM-generated fix suggestions and explanations
- 🖥️ Interactive Streamlit UI

The goal of this project is to simulate a real-world AI code review assistant that can:

- understand code structure,
- detect risky patterns,
- retrieve similar bug examples,
- and generate human-readable fixes with explanations.

---

## ✨ Why This Project?

Modern software teams need tools that do more than just say *"this is wrong."*
They need systems that can also answer:

- **Why is this risky?**
- **How can I fix it?**
- **What similar issue does this resemble?**
- **What best practice should I follow instead?**

This project was built to solve exactly that problem.

It demonstrates how AI can be combined with software engineering techniques to create a smart code review pipeline that is useful for:

- secure coding assistance,
- developer productivity,
- interview-worthy AI engineering demonstration,
- and explainable bug remediation.

---

## 🧠 Core Features

### 🌳 1. AST-Based Code Parsing

Parses Python code into an Abstract Syntax Tree (AST) to understand structure such as:

- functions
- variables
- imports
- loops
- control flow patterns

### 🐛 2. Rule-Based + AST-Based Bug Detection

Detects risky patterns like:

- `eval()` usage
- bare `except:`
- possible infinite loops
- unsafe coding constructs

### 🔗 3. Code Embeddings with CodeBERT

Converts code snippets into dense vector embeddings using **CodeBERT**, allowing the system to understand semantic similarity between code patterns.

### 🗂️ 4. Vector Search with ChromaDB

Stores known buggy code patterns and retrieves the most similar matches using vector similarity search.

### 🤖 5. AI Fix Suggestion Engine

Uses an LLM to:

- explain the bug,
- generate a safer fix,
- suggest best practices.

### 🖥️ 6. Streamlit User Interface

Provides a clean UI where users can:

- paste Python code,
- click **Analyze**,
- view detected bugs,
- inspect similar known patterns,
- get AI-generated remediation.

---

## 🏗️ System Architecture

```
User Input (Streamlit UI)
        ↓
AST Parsing & Structural Analysis
        ↓
Rule-Based / AST-Based Bug Detection
        ↓
Code Embedding Generation (CodeBERT)
        ↓
Vector Similarity Search (ChromaDB)
        ↓
LLM-Based Explanation + Fix Generation
        ↓
User-Friendly Output (Bug + Severity + Fix + Explanation)
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI | Streamlit |
| Code Parsing | AST (Abstract Syntax Tree) |
| Embeddings | Transformers / CodeBERT |
| Vector DB | ChromaDB |
| Data | NumPy / Pandas / scikit-learn |
| LLM | Groq API |

---

## 📂 Project Structure

```
SmartCodeAuditor/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── ast_analyzer.py
│   ├── bug_detector.py
│   ├── embedding_engine.py
│   ├── vector_search.py
│   ├── fix_generator.py
│   └── test_analyzer.py
│
├── data/
├── models/
├── embeddings/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔍 How It Works

**1️⃣ User submits Python code**
The user pastes code into the Streamlit interface.

**2️⃣ AST analyzer parses the code**
The code is converted into an AST so the system can understand structure.

**3️⃣ Bug detector checks risky patterns**
Rule-based and AST-based checks identify likely issues such as unsafe `eval()` or bare exceptions.

**4️⃣ Embedding engine converts code into vectors**
The snippet is transformed into a semantic representation using CodeBERT.

**5️⃣ Vector database retrieves similar bug patterns**
The system searches a vector database of known buggy code examples and retrieves related issues and fixes.

**6️⃣ LLM generates explanation and remediation**
The retrieved context and detected bug information are passed to the LLM, which produces:
- explanation,
- corrected code,
- best-practice guidance.

**7️⃣ Results are shown in the UI**
The user sees a full analysis pipeline output in an easy-to-read format.

---

## 🎯 Example Use Case

**Input**
```python
x = 5
eval(input())
```

**Output**

| Field | Detail |
|---|---|
| 🐛 Bug Detected | Unsafe `eval` usage |
| ⚠️ Severity | **Critical** |
| 🔍 Similar Pattern | `eval(user_input)` |
| ✅ Suggested Fix | Use `ast.literal_eval()` or safer input validation |
| 📖 Explanation | `eval()` executes arbitrary code and can introduce major security risks |

---

## 💡 Why This Project Stands Out

This is **not** just a basic rule-based checker.

It combines multiple important AI engineering concepts in one system:

- ✅ Static analysis
- ✅ Semantic search
- ✅ Embeddings
- ✅ Vector databases
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ LLM integration
- ✅ Explainable AI output
- ✅ Interactive deployment

This makes it a strong portfolio project for roles in:

- AI Engineering
- ML Engineering
- Applied AI
- Developer Tools / AI Agents
- Code Intelligence Systems

---

## 📈 Real-World Relevance

**SmartCode Auditor** can be extended into:

- a GitHub PR review bot,
- a VS Code extension,
- a CI/CD code quality gate,
- a secure code assistant,
- or an enterprise developer productivity tool.

---

## 🧪 Current Detection Examples

The project currently demonstrates detection or partial handling of patterns such as:

- unsafe `eval()` usage
- bare `except:`
- possible infinite loops
- retrieval of related bug patterns from vector storage
- AI-generated explanations and fixes

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SmartCodeAuditor.git
cd SmartCodeAuditor
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

> **Windows PowerShell:**
> ```powershell
> .venv\Scripts\activate
> ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

```bash
export GROQ_API_KEY="your_key_here"
```

### 5. Run the test pipeline

```bash
python src/test_analyzer.py
```

### 6. Launch Streamlit app

```bash
streamlit run app/streamlit_app.py
```

---

## 🛡️ Key Engineering Learnings

This project highlights several real-world engineering challenges:

- embedding shape handling for vector databases
- API integration and provider switching
- model deprecations and endpoint changes
- fallback handling for LLM service failures
- keeping secrets secure with environment variables
- turning raw backend pipelines into user-facing tools

---

## 📌 Future Improvements

- 🔥 Severity classification using ML models
- 📁 Upload `.py` file support in Streamlit
- 🧪 Larger labeled bug dataset
- 🧩 GitHub pull request integration
- 🛠️ More advanced static analysis rules
- 📊 Better similarity scoring visualization
- 🔐 Detection of SQL injection / command injection
- 🧠 Multi-language support beyond Python

---

## 👨‍💻 Author

Built as an AI engineering portfolio project to explore how **program analysis + semantic retrieval + generative AI** can work together in a practical code review assistant.

---

## ⭐ Like This Project?

Give it a star ⭐ and connect if you'd like to discuss **AI engineering**, **developer tools**, or **intelligent code analysis**.
