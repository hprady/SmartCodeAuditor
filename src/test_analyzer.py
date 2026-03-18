import embedding_engine
import fix_generator

code = """
for i in range(10):
    print(i)
"""

embedding = embedding_engine.get_code_embedding(code)

print("\nEmbedding Shape:")
print(embedding.shape)


import vector_search

# add some bug examples

vector_search.add_bug_pattern(
    "eval(user_input)",
    "Use ast.literal_eval() instead",
    "Unsafe eval usage"
)

vector_search.add_bug_pattern(
    "while True:",
    "Add a break condition",
    "Possible infinite loop"
)

# search similar bug

test_code = "eval(input())"

results = vector_search.search_similar_bug(test_code)

print("\nSimilar Bug Patterns:")
print(results)



bug_info = "Unsafe eval usage"

fix_output = fix_generator.generate_fix(
    test_code,
    bug_info,
    results
)

print("\nGenerated Fix Prompt:")
print(fix_output)