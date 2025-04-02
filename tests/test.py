from humenv import make_humenv
env, _ = make_humenv()
observation, info = env.reset()
frames = [env.render()]
for i in range(60):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
    frames.append(env.render())
# render frames at 30fps