import gym
from gym import register

# 注册自定义环境
register(
    id='myrobot-v0',
    entry_point='gym.envs.my_robot:MyEnv',  # 替换成你的环境类所在的模块和类名
    max_episode_steps=100,  # 可选参数，设置最大的步数限制
)
