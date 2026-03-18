import os
import sys
import streamlit as st

# Make src importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from ast_analyzer import analyze_code
from bug_detector import detect_bugs
from vector_search import add_bug_pattern, search_similar_bug
from fix_generator import generate_fix

st.set_page_config(page_title="SmartCode Auditor", layout="wide")

st.title("SmartCode Auditor")
st.subheader("AI-Driven Bug Detection & Remediation")

st.write("Paste Python code below and click Analyze.")

code_input = st.text_area("Enter Python code", height=300)

if st.button("Analyze Code"):
    if not code_input.strip():
        st.warning("Please paste some Python code first.")
    else:
        st.info("Analyzing code...")

        analysis = analyze_code(code_input)
        bugs = detect_bugs(code_input)

        # Seed known bug patterns
        try:
            add_bug_pattern(
                "eval(user_input)",
                "Use ast.literal_eval() instead",
                "Unsafe eval usage"
            )
        except:
            pass

        try:
            add_bug_pattern(
                "while True:",
                "Add a break condition",
                "Possible infinite loop"
            )
        except:
            pass

        similar_results = search_similar_bug(code_input)

        if bugs:
            bug_info = bugs[0]["bug"]
        else:
            bug_info = "No major rule-based bug detected, but review similar patterns."

        fix_output = generate_fix(code_input, bug_info, similar_results)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## Code Analysis")
            st.write(f"**Functions:** {analysis.get('functions', [])}")
            st.write(f"**Variables:** {analysis.get('variables', [])}")
            st.write(f"**Imports:** {analysis.get('imports', [])}")

            st.markdown("## Detected Bugs")
            if bugs:
                for bug in bugs:
                    st.error(f"{bug['bug']} — Severity: {bug['severity']}")
            else:
                st.success("No rule-based bugs detected.")

        with col2:
            st.markdown("## Similar Bug Patterns")

            ids = similar_results.get("ids", [[]])[0]
            metadatas = similar_results.get("metadatas", [[]])[0]
            distances = similar_results.get("distances", [[]])[0]

            if ids and metadatas:
                for i in range(len(ids)):
                    st.write(f"**Pattern:** {ids[i]}")
                    st.write(f"**Description:** {metadatas[i].get('description', 'N/A')}")
                    st.write(f"**Suggested Fix:** {metadatas[i].get('fix', 'N/A')}")
                    if i < len(distances):
                        st.write(f"**Distance:** {distances[i]:.2f}")
                    st.markdown("---")
            else:
                st.info("No similar bug patterns found.")

            st.markdown("## AI Fix Suggestion")
            st.write(fix_output)