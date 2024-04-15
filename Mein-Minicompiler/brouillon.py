"""class IntermediateCodeGenerator:
    
    def __init__(self):
        self.instructions = []
        
    def generate(self, node):
       
        # Logique de génération des instructions pour chaque type de nœud
        if isinstance(node, NumberNode):
            self.instructions.append(f"PUSH {node.tok.value}" )
        elif isinstance(node, BinOpNode):
            self.generate(node.left_node)
            self.generate(node.right_node)
            if node.op_tok.type == TT_PLUS:
                self.instructions.append("ADD")
            elif node.op_tok.type == TT_MINUS:
                self.instructions.append("SUB")
            elif node.op_tok.type == TT_MUL:
                self.instructions.append("MUL")
            elif node.op_tok.type == TT_DIV:
                self.instructions.append("DIV")
            elif node.op_tok.type == TT_POW:
                self.instructions.append("POW")
        elif isinstance(node, UnaryOpNode):
            self.generate(node.node)
            if node.op_tok.type == TT_MINUS:
                self.instructions.append("NEGATE")

        return self.instructions"""



class NodeVisitor:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

class ZwischencodeGenerator(NodeVisitor):
    def __init__(self):
        self.temp_count = 0
        self.instructions = []

    def generate(self, node):
        self.visit(node)
        return self.instructions

    def get_temp_var(self):
        self.temp_count += 1
        return f't{self.temp_count}'

    def visit_NumberNode(self, node):
        temp_var = self.get_temp_var()
        self.instructions.append(f'{temp_var} = {node.tok.value}')

    def visit_BinOpNode(self, node):
        left_temp = self.get_temp_var()
        right_temp = self.get_temp_var()

        self.visit(node.left_node)
        self.instructions.append(f'{left_temp} = {self.instructions.pop()}')
        
        self.visit(node.right_node)
        self.instructions.append(f'{right_temp} = {self.instructions.pop()}')

        op = node.op_tok.value
        result_temp = self.get_temp_var()
        self.instructions.append(f'{result_temp} = {left_temp} {op} {right_temp}')

    def visit_UnaryOpNode(self, node):
        self.visit(node.node)
        temp_var = self.get_temp_var()
        op = node.op_tok.value
        self.instructions.append(f'{temp_var} = {op} {self.instructions.pop()}')
