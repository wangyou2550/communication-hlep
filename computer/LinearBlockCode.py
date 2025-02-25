# 线性分组码译码
# 代码说明
# LinearBlockCode 类:
# 初始化时接受接收到的码字和监督矩阵（校验矩阵）。
# calculate_syndrome 方法:
# 计算伴随式（Syndrome），使用矩阵乘法并取模 2。
# find_error_pattern 方法:
# 检查伴随式以识别错误的位置。如果找到了错误，返回错误位置的索引。
# decode 方法:
# 调用 find_error_pattern 方法来识别并纠正错误。如果没有发现错误，直接返回接收到的码字作为译码结果。
import numpy as np


class LinearBlockCode:
    def __init__(self, received_codeword, parity_check_matrix):
        self.received_codeword = np.array(received_codeword)
        self.H = np.array(parity_check_matrix)

    def calculate_syndrome(self):
        # 计算伴随式
        syndrome = np.dot(self.received_codeword, self.H.T) % 2
        return syndrome

    def find_error_pattern(self):
        # 计算错误图样
        syndrome = self.calculate_syndrome()
        # 遍历每一列校验矩阵与伴随式比较
        for i in range(self.H.shape[1]):
            if np.array_equal(syndrome, self.H[:, i]):
                return i + 1  # 返回错误位置（从1开始计数）
        return None  # 如果没有找到错误

    def decode(self):
        error_position = self.find_error_pattern()
        if error_position is not None:
            print(f"错误图样: 位置 {error_position} 有错误")
            # 纠正错误
            corrected_codeword = self.received_codeword.copy()
            corrected_codeword[error_position - 1] ^= 1  # 翻转错误位
            return corrected_codeword
        else:
            print("没有发现错误，译码结果为:")
            return self.received_codeword


def convert_to_matrix(binary_strings):
    # 处理只有一个元素的情况
    if len(binary_strings) == 1:
        return np.array([int(char) for char in binary_strings[0]])

    # 计算行数和列数
    num_rows = len(binary_strings)
    num_cols = len(binary_strings[0]) if num_rows > 0 else 0

    # 创建一个空矩阵
    matrix = np.zeros((num_rows, num_cols), dtype=int)

    # 填充矩阵
    for i in range(num_rows):
        for j in range(num_cols):
            matrix[i, j] = int(binary_strings[i][j])

    return matrix



# 示例使用
if __name__ == "__main__":

    received_codeword = convert_to_matrix(["1101011"])
    print(received_codeword)
    # 监督矩阵
    parity_check_matrix = convert_to_matrix(["1110100","1101010","0111001"])

    code = LinearBlockCode(received_codeword, parity_check_matrix)
    syndrome = code.calculate_syndrome()
    print("伴随式:", syndrome)
    decoded_codeword = code.decode()
    print("译码结果:", decoded_codeword)