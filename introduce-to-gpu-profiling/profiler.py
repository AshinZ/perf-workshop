import torch
import torchvision.models as models
from torch.profiler import profile, record_function, ProfilerActivity

def check_cuda_device(device_id=0):
    try:
        # 检查CUDA是否可用
        if not torch.cuda.is_available():
            print("错误：CUDA不可用。可能原因：")
            print("- NVIDIA驱动未安装")
            print("- CUDA Toolkit未正确安装")
            print("- 设备无权限访问（如Linux未配置用户组）")
            return

        # 检查设备数量
        device_count = torch.cuda.device_count()
        if device_count == 0:
            print("错误：未检测到CUDA设备。")
            return

        # 检查设备ID是否有效
        if device_id < 0 or device_id >= device_count:
            print(f"错误：设备ID {device_id} 无效。可用设备ID范围: 0-{device_count - 1}")
            return

        # 获取设备属性
        prop = torch.cuda.get_device_properties(device_id)
        print(f"设备 {device_id} 属性:")
        print(f"- 名称: {prop.name}")
        print(f"- 计算能力: {prop.major}.{prop.minor}")
        print(f"- 显存大小: {prop.total_memory / 1024**3:.2f} GB")

    except RuntimeError as e:
        print(f"运行时错误: {str(e)}")
        print("可能原因：")
        print("- CUDA驱动版本与PyTorch不兼容")
        print("- 设备被其他进程占用")
    except Exception as e:
        print(f"未知错误: {str(e)}")

check_cuda_device(device_id=0) 
num_runs = 20  # 采样次数
warmup = 10     # 预热次数


if torch.cuda.is_available():
    device = 'cuda'
elif torch.xpu.is_available():
    device = 'xpu'
else:
    print('Neither CUDA nor XPU devices are available to demonstrate profiling on acceleration devices')
    import sys
    sys.exit(0)

print(device)
activities = [ProfilerActivity.CPU, ProfilerActivity.CUDA]
sort_by_keyword = device + "_time_total"


model = models.resnet50().to(device)

inputs = torch.randn(5, 3, 224, 224).to(device)
print("CUDA 是否可用:", torch.cuda.is_available())
print("当前设备:", torch.cuda.current_device())
print("输入数据设备:", inputs.device)
print("模型参数设备:", next(model.parameters()).device)
for _ in range(warmup):
    model(inputs)
with profile(activities=activities,
             record_shapes=True,
             profile_memory=True,
             with_stack=True,
             on_trace_ready=torch.profiler.tensorboard_trace_handler("./logs")) as prof:
    with record_function("model_inference"):
        for _ in range(num_runs):
            model(inputs)
        torch.cuda.synchronize() 

print(prof.key_averages().table(sort_by=sort_by_keyword, row_limit=10))