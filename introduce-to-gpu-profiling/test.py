import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 生成一些随机数据
x = torch.randn(100, 1) * 10  # 输入特征
y = 2 * x + 3 + torch.randn(100, 1)  # 目标值，添加一些噪声

# 定义线性回归模型
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 输入维度1，输出维度1

    def forward(self, x):
        return self.linear(x)

# 实例化模型
model = LinearRegressionModel()

# 定义损失函数和优化器
criterion = nn.MSELoss()  # 均方误差损失
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    model.train()  # 设置模型为训练模式

    # 前向传播
    outputs = model(x)
    loss = criterion(outputs, y)

    # 反向传播和优化
    optimizer.zero_grad()  # 清空梯度
    loss.backward()  # 计算梯度
    optimizer.step()  # 更新参数

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 查看训练结果
print("模型参数：")
for name, param in model.named_parameters():
    print(f"{name}: {param.data}")

# 绘制训练结果
model.eval()  # 设置模型为评估模式
with torch.no_grad():
    predicted = model(x)

# 绘制结果
plt.scatter(x.numpy(), y.numpy(), label='真实数据', color='blue')
plt.plot(x.numpy(), predicted.numpy(), label='模型预测', color='red')
plt.xlabel('输入特征')
plt.ylabel('目标值')
plt.title('训练结果')
plt.legend()
plt.show()

# 进行推理
new_x = torch.tensor([[4.0], [5.0], [6.0]])  # 新的特征值
model.eval()  # 设置模型为评估模式
with torch.no_grad():
    predictions = model(new_x)

print("推理结果：")
for i, x_val in enumerate(new_x):
    print(f"输入: {x_val.item()}, 预测: {predictions[i].item()}")
