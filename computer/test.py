import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyArrowPatch

class ConvolutionalCode:
    def __init__(self, polynomial1, polynomial2, polynomial3):
        self.polynomial1 = polynomial1
        self.polynomial2 = polynomial2
        self.polynomial3 = polynomial3
        self.memory = self.calculate_memory()
        self.num_states = 2 ** self.memory  # 状态数 = 2^记忆长度
        self.transitions = self.calculate_transitions()

    def calculate_memory(self):
        return len(self.polynomial1) - 1  # 最高次幂为记忆长度

    def calculate_transitions(self):
        transitions = []
        for state in range(self.num_states):
            for input_bit in [0, 1]:
                next_state = ((state << 1) | input_bit) & (self.num_states - 1)
                next_state_bin = f"{next_state:0{self.memory}b}"
                output = self.calculate_output(state, input_bit)
                transitions.append((state, next_state_bin, output))
        return transitions

    def calculate_output(self, state, input_bit):
        output = []
        for polynomial in [self.polynomial1, self.polynomial2, self.polynomial3]:
            output_value = 0
            for i, coeff in enumerate(polynomial):
                if coeff == '1':
                    output_value ^= (state >> i) & 1
            output_value ^= input_bit
            output.append(str(output_value))
        return ''.join(output)

    def draw_state_diagram(self):
        G = nx.DiGraph()

        for i in range(self.num_states):
            G.add_node(i)

        for (src, dest, label) in self.transitions:
            G.add_edge(src, dest, label=label)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')

        plt.figure(figsize=(10, 6))


        plt.title('Convolutional Code State Diagram (Three Outputs)')
        plt.axis('off')
        plt.show()

# 示例使用
if __name__ == "__main__":
    polynomial1 = '100'  # 代表第一个输出的多项式 (1 + x^2 + x^3)
    polynomial2 = '111'  # 代表第二个输出的多项式 (1 + x + x^3)
    polynomial3 = '101'  # 代表第三个输出的多项式 (1 + x + x^2)
    code = ConvolutionalCode(polynomial1, polynomial2, polynomial3)
    code.draw_state_diagram()