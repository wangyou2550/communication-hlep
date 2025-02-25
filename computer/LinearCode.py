import numpy as np


class LinearCode:
    def __init__(self, generator_matrix):
        """
        初始化线性分组码的生成矩阵。

        参数：
        generator_matrix : numpy.ndarray
            输入的生成矩阵。
        """
        self.G = generator_matrix

    def to_standard_generator_matrix(self):
        """
        将生成矩阵 G 转换为典型生成矩阵。

        返回：
        numpy.ndarray
            典型生成矩阵。
        """
        num_rows, num_cols = self.G.shape
        G_rref = np.copy(self.G)
        row = 0

        for col in range(num_cols):
            if row >= num_rows:
                break

            # 找到当前列的主元
            pivot_row = np.argmax(G_rref[row:num_rows, col]) + row
            if G_rref[pivot_row, col] == 0:
                continue

            # 交换当前行和主元行
            G_rref[[row, pivot_row]] = G_rref[[pivot_row, row]]

            # 将主元归一化
            G_rref[row] = G_rref[row] / G_rref[row, col]

            # 消元
            for r in range(num_rows):
                if r != row:
                    G_rref[r] = G_rref[r] - G_rref[r, col] * G_rref[row]

            row += 1

        # 形成典型生成矩阵
        identity = np.eye(num_rows)
        P = G_rref[:, num_rows:]  # 提取 P 矩阵
        standard_G = np.hstack((identity, P))

        return standard_G


# 示例
G = np.array([[1, 0, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]])

linear_code = LinearCode(G)
standard_G = linear_code.to_standard_generator_matrix()
print("典型生成矩阵:\n", standard_G)