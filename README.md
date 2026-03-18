# 🛡️ SmartCode Auditor: AI-Driven Bug Detection & Remediation

> An intelligent code review system that combines static analysis, semantic retrieval, and LLM-powered remediation to detect bugs, explain risks, and suggest fixes for Python code.

---

## 📌 Overview

**SmartCode Auditor** is an AI-powered code review agent built to analyze Python code beyond simple keyword matching.

Instead of only checking for hardcoded patterns, it combines:

- 🌳 **AST-based static code analysis**
- 🧠 **Code embeddings using CodeBERT**
- 🔎 **Vector similarity search with ChromaDB**
- 🤖 **LLM-generated fix suggestions and explanations**
- 🖥️ **Interactive Streamlit UI**

### 🎯 Goal
Simulate a real-world AI code review assistant that can:
- Understand code structure
- Detect risky patterns
- Retrieve similar bug examples
- Generate human-readable fixes with explanations

---

## ✨ Why This Project?

Modern software teams need tools that do more than just say *"this is wrong."* They need systems that can also answer:

| Question | Answer Provided By |
|----------|-------------------|
| ❓ Why is this risky? | LLM explanation + severity scoring |
| 🛠️ How can I fix it? | AI-generated remediation code |
| 🔍 What similar issue does this resemble? | ChromaDB vector retrieval |
| ✅ What best practice should I follow? | Embedded secure coding guidelines |

### 💼 Ideal For:
- 🔐 Secure coding assistance
- ⚡ Developer productivity
- 🎯 Interview-worthy AI engineering demonstration
- 🧾 Explainable bug remediation

---

## 🧠 Core Features

### 🌳 1. AST-Based Code Parsing
Parses Python code into an **Abstract Syntax Tree (AST)** to understand:
- Functions, variables, imports
- Loops, conditionals, control flow

### 🐛 2. Rule-Based + AST-Based Bug Detection
Detects risky patterns like:
- `eval()` usage
- Bare `except:` clauses
- Possible infinite loops
- Unsafe input handling

### 🔗 3. Code Embeddings with CodeBERT
Converts code snippets into dense vector embeddings using **CodeBERT**, enabling semantic similarity understanding.

### 🗂️ 4. Vector Search with ChromaDB
Stores known buggy patterns and retrieves the most semantically similar matches using **vector similarity search**.

### 🤖 5. AI Fix Suggestion Engine
Uses an LLM to:
- Explain the bug in plain language
- Generate a safer, corrected code snippet
- Suggest relevant best practices

### 🖥️ 6. Streamlit User Interface
A clean, interactive UI where users can:
- Paste Python code
- Click **Analyze**
- View detected bugs + severity
- Inspect similar known patterns
- Get AI-generated remediation

---

## 🏗️ System Architecture

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



---

## ⚙️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | 🐍 Python |
| **Frontend** | 🖥️ Streamlit |
| **Static Analysis** | 🌳 AST, `ast` module |
| **Embeddings** | 🤗 Transformers / CodeBERT |
| **Vector DB** | 🧠 ChromaDB |
| **Data/ML** | 🔢 NumPy, Pandas, scikit-learn |
| **LLM Backend** | ⚡ Groq API / OpenAI-compatible endpoints |

---

## 📂 Project Structure

SmartCodeAuditor/
│
├── app/
│ └── streamlit_app.py # Main Streamlit UI
│
├── src/
│ ├── ast_analyzer.py # AST parsing logic
│ ├── bug_detector.py # Rule + AST-based detection
│ ├── embedding_engine.py # CodeBERT embedding generation
│ ├── vector_search.py # ChromaDB integration
│ ├── fix_generator.py # LLM prompt + response handling
│ └── test_analyzer.py # End-to-end test pipeline
│
├── data/ # Sample buggy/safe code snippets
├── models/ # (Optional) fine-tuned model artifacts
├── embeddings/ # Cached embedding vectors
│
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


---

## 🔍 How It Works

1️⃣ **User submits Python code**  
→ Paste code into the Streamlit interface.

2️⃣ **AST analyzer parses the code**  
→ Code is converted into an AST for structural understanding.

3️⃣ **Bug detector checks risky patterns**  
→ Rule-based + AST-based checks flag issues like `eval()` or bare `except:`.

4️⃣ **Embedding engine converts code into vectors**  
→ Snippet is transformed into a semantic vector using CodeBERT.

5️⃣ **Vector database retrieves similar bug patterns**  
→ ChromaDB searches for semantically similar known bugs.

6️⃣ **LLM generates explanation and remediation**  
→ Prompt includes: detected bug + similar examples + context → LLM returns:
   - Plain-language explanation
   - Corrected code snippet
   - Best-practice guidance

7️⃣ **Results are shown in the UI**  
→ Clean, readable output with bug, severity, fix, and rationale.

---

## 🎯 Example Use Case

### 🔹 Input
```python
x = 5
eval(input())

🔹 Output

🚨 Bug Detected: Unsafe eval() usage
🔴 Severity: Critical
🔍 Similar Pattern: eval(user_input) in dataset #42
🛠️ Suggested Fix: 
   Use ast.literal_eval() or validate input against allowlist

💡 Explanation: 
   eval() executes arbitrary code and can introduce major 
   security risks like remote code execution (RCE).



⚙️ Tech Stack

🐍 Python

🖥️ Streamlit

🌳 AST (Abstract Syntax Tree)

🤗 Transformers / CodeBERT

🧠 ChromaDB

🔢 NumPy / Pandas

📊 scikit-learn

⚡ Groq API / LLM integration

📂 Project Structure
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
🔍 How It Works
1️⃣ User submits Python code

The user pastes code into the Streamlit interface.

2️⃣ AST analyzer parses the code

The code is converted into an AST so the system can understand its structure.

3️⃣ Bug detector checks risky patterns

Rule-based and AST-based checks identify likely issues such as unsafe eval() or bare exceptions.

4️⃣ Embedding engine converts code into vectors

The snippet is transformed into a semantic representation using CodeBERT.

5️⃣ Vector database retrieves similar bug patterns

The system searches a vector database of known buggy code examples and retrieves related issues and fixes.

6️⃣ LLM generates explanation and remediation

The retrieved context and detected bug information are passed to the LLM, which produces:

explanation

corrected code

best-practice guidance

7️⃣ Results are shown in the UI

The user sees a full analysis pipeline output in an easy-to-read format.

🎯 Example Use Case
Input
x = 5
eval(input())
Output

Bug Detected: Unsafe eval() usage

Severity: Critical

Similar Bug Pattern: eval(user_input)

Suggested Fix: Use ast.literal_eval() or safer input validation

Explanation: eval() executes arbitrary code and can introduce major security risks

💡 Why This Project Stands Out

This is not just a basic rule-based checker.

It combines multiple important AI engineering concepts in one system:

✅ Static analysis

✅ Semantic search

✅ Embeddings

✅ Vector databases

✅ Retrieval-Augmented Generation (RAG)

✅ LLM integration

✅ Explainable AI output

✅ Interactive deployment

This makes it a strong portfolio project for roles in:

AI Engineering

ML Engineering

Applied AI

Developer Tools / AI Agents

Code Intelligence Systems

📈 Real-World Relevance

SmartCode Auditor can be extended into:

a GitHub PR review bot

a VS Code extension

a CI/CD code quality gate

a secure code assistant

an enterprise developer productivity tool

🧪 Current Detection Examples

The project currently demonstrates detection or partial handling of patterns such as:

unsafe eval() usage

bare except:

possible infinite loops

retrieval of related bug patterns from vector storage

AI-generated explanations and fixes

🚀 Getting Started
1. Clone the repository
git clone https://github.com/hprady/SmartCodeAuditor.git
cd SmartCodeAuditor
2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate

For Windows PowerShell:

.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Set your API key

For Groq:

export GROQ_API_KEY="your_key_here"

For Windows PowerShell:

$env:GROQ_API_KEY="your_key_here"
5. Run the test pipeline
python src/test_analyzer.py
6. Launch the Streamlit app
streamlit run app/streamlit_app.py
🛡️ Key Engineering Learnings

This project highlights several real-world engineering challenges:

embedding shape handling for vector databases

API integration and provider switching

model deprecations and endpoint changes

fallback handling for LLM service failures

keeping secrets secure with environment variables

turning raw backend pipelines into user-facing tools

📌 Future Improvements

🔥 Severity classification using ML models

📁 Upload .py file support in Streamlit

🧪 Larger labeled bug dataset

🧩 GitHub pull request integration

🛠️ More advanced static analysis rules

📊 Better similarity scoring visualization

🔐 Detection of SQL injection / command injection

🧠 Multi-language support beyond Python

👨‍💻 Author

Built as an AI engineering portfolio project to explore how program analysis + semantic retrieval + generative AI can work together in a practical code review assistant.

⭐ If You Found This Project Interesting...

Give it a star and connect if you’d like to discuss AI engineering, developer tools, or intelligent code analysis.
