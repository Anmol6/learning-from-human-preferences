from gym import Wrapper


class PongWrapper(Wrapper):
    def __init__(self, env):
        super(PongWrapper, self).__init__(env)
        assert str(env) == '<TimeLimit<AtariEnv<PongNoFrameskip-v4>>>'

    def step(self, action):
        observation, reward, _, info = self.env.step(action)
        if reward != 0:
            done = True
        else:
            done = False
        return observation, reward, done, info
