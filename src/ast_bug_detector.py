import ast

class ASTBugDetector(ast.NodeVisitor):

    def __init__(self):
        self.bugs = []

    # Detect eval() calls
    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            if node.func.id == "eval":
                self.bugs.append({
                    "bug": "Unsafe eval() usage",
                    "severity": "Critical"
                })

        self.generic_visit(node)

    # Detect bare except
    def visit_ExceptHandler(self, node):

        if node.type is None:
            self.bugs.append({
                "bug": "Bare except block",
                "severity": "Major"
            })

        self.generic_visit(node)

    # Detect infinite loop
    def visit_While(self, node):

        if isinstance(node.test, ast.Constant) and node.test.value == True:
            self.bugs.append({
                "bug": "Possible infinite loop",
                "severity": "Major"
            })

        self.generic_visit(node)


def detect_ast_bugs(code):

    tree = ast.parse(code)

    detector = ASTBugDetector()
    detector.visit(tree)

    return detector.bugs