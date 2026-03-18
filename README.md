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

## 💡 Why This Project Stands Out

**This is not just a basic rule-based checker.** It integrates multiple advanced AI engineering concepts:

✅ **Static analysis (AST)**  
✅ **Semantic code search (embeddings)**  
✅ **Vector databases (ChromaDB)**  
✅ **Retrieval-Augmented Generation (RAG)**  
✅ **LLM integration with fallback handling**  
✅ **Explainable, human-readable output**  
✅ **Interactive, deployable UI (Streamlit)**  

### 🎯 Great for portfolios targeting:
- **AI/ML Engineering**
- **Applied AI / AI Agents**
- **Developer Tools & Code Intelligence**
- **Secure Software Engineering**

---

## 📈 Real-World Relevance

**SmartCode Auditor** can be extended into:

🤖 **A GitHub PR review bot**  
🧩 **A VS Code extension**  
⚙️ **A CI/CD code quality gate**  
🔐 **An enterprise secure coding assistant**  
📊 **A developer productivity analytics tool**  

---

## 🧪 Current Detection Capabilities

The system currently demonstrates detection or partial handling of:

✅ **Unsafe `eval()` / `exec()` usage**  
✅ **Bare `except:` clauses**  
✅ **Possible infinite loops (`while True` without break)**  
✅ **Retrieval of related bug patterns from vector store**  
✅ **AI-generated explanations and fix suggestions**  

---

### 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/hprady/SmartCodeAuditor.git
cd SmartCodeAuditor

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# Windows PowerShell:
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set your API key
# For Groq:
export GROQ_API_KEY="your_key_here"

# Windows PowerShell:
$env:GROQ_API_KEY="your_key_here"

5️⃣ Run the test pipeline
```bash
python src/test_analyzer.py

6️⃣ Launch the Streamlit app
```bash
streamlit run app/streamlit_app.py

🛡️ Key Engineering Learnings
This project highlights real-world challenges in AI system design:
🔄 Embedding shape handling & normalization for vector DBs
🔁 API integration + provider fallback logic (Groq/OpenAI)
🗑️ Handling model deprecations and endpoint changes
🧯 Graceful degradation when LLM services fail
🔐 Secure secret management via environment variables
🎨 Turning backend pipelines into user-friendly tools

📌 Future Improvements
Priority
Feature
🔥 High
ML-based severity classification
📁 High
.py file upload support in Streamlit
🧪 Medium
Larger, labeled bug dataset for retrieval
🧩 Medium
GitHub PR comment integration via Actions
🛠️ Medium
Advanced static analysis (taint tracking, data flow)
📊 Low
Interactive similarity scoring visualization
🔐 High
SQL injection / command injection detection
🌍 Low
Multi-language support (JS, Java, Go)


👨‍💻 Author
Pradyumna
Built as an AI engineering portfolio project to explore how program analysis + semantic retrieval + generative AI can work together in a practical, explainable code review assistant.

⭐ If You Found This Project Interesting...
→ Give it a star ⭐ on GitHub
→ Connect if you'd like to discuss AI engineering, developer tools, or intelligent code analysis!
"The best code review doesn't just find bugs — it teaches better coding."
