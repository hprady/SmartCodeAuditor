import ast

class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.functions = []
        self.variables = []
        self.imports = []

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.append(target.id)
        self.generic_visit(node)

    def visit_Import(self, node):
        for name in node.names:
            self.imports.append(name.name)

def analyze_code(code):

    tree = ast.parse(code)

    analyzer = CodeAnalyzer()
    analyzer.visit(tree)

    return {
        "functions": analyzer.functions,
        "variables": analyzer.variables,
        "imports": analyzer.imports
    }