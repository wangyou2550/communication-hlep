import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class ConvolutionalCode:
    def __init__(self, polynomial1, polynomial2,polynomial3):
        self.polynomial1 = polynomial1
        self.polynomial2 = polynomial2
        self.polynomial3 = polynomial3
        self.memory = self.calculate_memory()
        self.num_states = 2 ** self.memory  # 状态数 = 2^记忆长度
        self.transitions = self.calculate_transitions()

    def calculate_memory(self):
        # 计算记忆长度
        return len(self.polynomial1) - 1  # 最高次幂为记忆长度

    def calculate_transitions(self):
        transitions = []
        for state in range(self.num_states):
            for input_bit in [0, 1]:
                # 计算下一个状态
                next_state = ((state << 1) | input_bit) & (self.num_states - 1)
                # 转换为二进制字符串
                next_state_bin = f"{next_state:0{self.memory}b}"
                state_bin = f"{state:0{self.memory}b}"
                # 计算输出
                output = self.calculate_output(state, input_bit)
                transitions.append((state_bin, next_state_bin, f"{output}({input_bit})"))
        return transitions

    def calculate_output(self, state, input_bit):
        # 计算输出
        output1 = 0
        output2 = 0
        output3 = 0

        # 计算第一个输出
        for i, coeff in enumerate(self.polynomial1):
            if coeff == '1':
                output1 ^= (state >> i) & 1  # 计算当前状态对输出的贡献
        output1 ^= input_bit  # 加上当前输入位

        # 计算第二个输出
        for i, coeff in enumerate(self.polynomial2):
            if coeff == '1':
                output2 ^= (state >> i) & 1  # 计算当前状态对输出的贡献
        output2 ^= input_bit  # 加上当前输入位
        # 计算第二个输出
        for i, coeff in enumerate(self.polynomial3):
            if coeff == '1':
                output3 ^= (state >> i) & 1  # 计算当前状态对输出的贡献
        output3 ^= input_bit  # 加上当前输入位

        return f"{output1}{output2}{output3}"  # 返回两个输出的组合

    def draw_state_diagram(self):
        G = nx.DiGraph()

        # 定义状态节点
        for i in range(self.num_states):
            node = f"{i:0{self.memory}b}"
            G.add_node(node)

        # 添加状态转移
        for (src, dest, label) in self.transitions:
            G.add_edge(src, dest, label=label)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        # # 自定义边标签位置
        # for (src, dest) in G.edges():
        #     # 计算边的中点
        #     x = (pos[src][0] + pos[dest][0]) / 2
        #     y = (pos[src][1] + pos[dest][1]) / 2
        #     # 获取边的标签
        #     label = edge_labels[(src, dest)]
        #     plt.text(x, y + 0.05, label, fontsize=10, color='red', ha='center')  # 调整y坐标使标签位于上方
        plt.title('Convolutional Code State Diagram (Two Outputs)')
        plt.axis('off')
        plt.show()


# 示例使用
if __name__ == "__main__":
    polynomial1 = '100'  # 代表第一个输出的多项式 (1 + x^2 + x^3)
    polynomial2 = '101'  # 代表第二个输出的多项式 (1 + x + x^3)
    polynomial3 = '111'  # 代表第二个输出的多项式 (1 + x + x^3)
    code = ConvolutionalCode(polynomial1, polynomial2,polynomial3)
    code.draw_state_diagram()