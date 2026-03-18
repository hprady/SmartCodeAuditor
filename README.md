# 🛡️ SmartCodeAuditor

**SmartCodeAuditor** is an AI-powered Python code analysis project that detects potential bugs, unsafe coding patterns, and vulnerable code snippets using a combination of:

- 🌳 **AST-based static analysis**
- 🤖 **CodeBERT embeddings**
- 🧠 **Vector similarity search with ChromaDB**

Its goal is to intelligently analyze Python code, identify risky patterns, and suggest possible fixes to improve code quality and security. 🚀

---

## 🚀 Features

### 🌳 AST-Based Bug Detection
Detects common Python code issues such as:

- ⚠️ Unsafe `eval()` usage
- 🚫 Bare `except:` blocks
- ♾️ Possible infinite loops like `while True`

### 🤖 Code Embedding with CodeBERT
Uses **Microsoft CodeBERT** to convert source code into semantic vector embeddings.

This helps the system understand code by **meaning**, not just by exact text. 🧩

### 🧠 Bug Pattern Search with ChromaDB
Stores known buggy code patterns in a vector database and searches for similar issues in new code.

This helps detect:

- 🐞 Similar vulnerabilities
- 🔁 Repeated bad coding practices
- 🚨 Known risky code structures

---

## 🏗️ Project Architecture

```text
📝 Python Code
    ↓
🌳 AST Parser
    ↓
🔍 Rule-Based Bug Detector
    ↓
🤖 CodeBERT Embedding Generator
    ↓
🧠 ChromaDB Vector Search
    ↓
🐞 Bug Matches + 🛠️ Suggested Fixes
