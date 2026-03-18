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

Give:
Explanation:
Fix:
Best Practice:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content