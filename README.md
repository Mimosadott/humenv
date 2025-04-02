
<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1> HumEnv：用于强化学习的人形环境</h1>
    </summary>
  </ul>
</div>

# 概述

HumEnv是一个基于SMPL人形模型的环境，旨在实现人形控制的可复现研究。它专为促进强化学习（RL）、基于目标的RL、无监督RL和模仿学习的算法研究而设计。该环境包含基础环境接口，以及一个可选的基准测试模块，用于评估不同任务上的智能体表现。

## 核心特性

 * 支持在多种本体感觉任务中模拟真实人形的环境
 * 基于MuJoCo的人形机器人定义，优化了摩擦系数、关节驱动和运动范围等参数以实现更真实的行为
 * 9种可配置的奖励类别，支持学习基本人形技能（包括行走、旋转、跳跃、爬行等）
 * 基准测试代码，可评估三类任务的RL智能体：基于奖励、目标达成和动作追踪
 * 多样化初始化选项：静态"T字姿势"、随机跌倒、动作捕捉数据帧及其组合
 * 与Gymnasium完全兼容

# 安装指南

完整功能支持的基础安装（需Python 3.9+）：

```bash
pip install "git+https://github.com/facebookresearch/HumEnv.git"
```

若要使用动作捕捉（MoCap）和动作捕捉+跌倒初始化方案，需根据[数据准备说明](data_preparation/README.md)准备授权数据集。

包含所有基准测试功能的完整安装：

```bash
pip install "humenv[bench] @ git+https://github.com/facebookresearch/HumEnv.git"
```

# 快速入门

安装完成后，可使用与`gymnasium.make_vec`接口相似的`humenv.make_humenv`创建环境。示例代码如下：

```python
from humenv import make_humenv
env, _ = make_humenv()
observation, info = env.reset()
frames = [env.render()]
for i in range(60):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
    frames.append(env.render())
# 以30帧/秒渲染画面
```

更多示例请参考[tutorial.ipynb](tutorial.ipynb)。

# 引用格式
```
@article{tirinzoni2024metamotivo,
  title={通过行为基础模型实现零样本全身人形控制},
  author={Tirinzoni, Andrea 和 Touati, Ahmed 和 Farebrother, Jesse 和 Guzek, Mateusz 和 Kanervisto, Anssi 和 Xu, Yingchen 和 Lazaric, Alessandro 和 Pirotta, Matteo},
}
```

# 致谢

 * [SMPL](https://smpl.is.tue.mpg.de/)和[AMASS](https://amass.is.tue.mpg.de/)提供人形骨架和动作数据用于初始化追踪基准
 * [PHC](https://github.com/ZhengyiLuo/PHC)用于数据处理和目标达成任务的部分指标计算
 * [SMPLSm](https://github.com/ZhengyiLuo/SMPLSim)提供SMPL/AMASS数据集处理脚本及人形处理工具
 * [smplx](https://github.com/vchoutas/smplx.git)帮助移除chumpy依赖
 * [MuJoCo](https://github.com/google-deepmind/mujoco)作为后端仿真引擎
 * [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)提供API支持

# 许可协议

HumEnv采用CC BY-NC 4.0许可协议。详细条款请见[LICENSE](LICENSE)。