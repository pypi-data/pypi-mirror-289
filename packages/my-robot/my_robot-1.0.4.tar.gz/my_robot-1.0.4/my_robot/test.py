import gym

# 创建自定义环境实例
env = gym.make('myrobot-v0')

# 使用环境进行交互，如执行动作、获取观察值等
observation = env.reset()
action = env.action_space.sample()
next_observation, reward, done, info = env.step(action)

# 关闭环境
env.close()
