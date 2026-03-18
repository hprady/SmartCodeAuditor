from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_fix(code, bug_info, similar_results):
    prompt = f"""
You are an expert Python code reviewer.

Analyze the following code:

{code}

Bug:
{bug_info}

Similar Results:
{similar_results}

Give:
1. Explanation
2. Fixed code
3. Best Practice
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"""
Explanation:
The code triggered this detected issue: {bug_info}.

Fallback Reason:
LLM provider could not be reached. Error: {str(e)}

Fix:
- Avoid using unsafe patterns such as eval() on user input.
- Replace bare except with `except Exception as e`.
- Add proper loop exit conditions.
- Validate external input before using it.

Best Practice:
Use static analysis + retrieval results as fallback when the LLM is unavailable. This makes the system more reliable in real-world production environments.
"""