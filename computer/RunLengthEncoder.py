class RunLengthEncoder:
    def __init__(self, sequence):
        self.sequence = sequence
        self.run_count = 0
        self.runs = []

    def calculate_runs(self):
        if not self.sequence:
            return 0, []

        current_element = self.sequence[0]
        current_length = 1

        for i in range(1, len(self.sequence)):
            if self.sequence[i] == current_element:
                current_length += 1  # 增加当前游程的长度
            else:
                # 游程结束，记录游程
                self.runs.append((current_element, current_length))
                self.run_count += 1
                current_element = self.sequence[i]  # 更新当前元素
                current_length = 1  # 重置长度

        # 记录最后一个游程
        self.runs.append((current_element, current_length))
        self.run_count += 1

        return self.run_count, self.runs

# 示例使用
sequence = "1011100"
encoder = RunLengthEncoder(sequence)
run_count, run_details = encoder.calculate_runs()

print("游程数量:", run_count)
print("游程详细信息:", run_details)