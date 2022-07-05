import cProfile
import pstats
import numpy as np

from social_dilemmas.envs.env_creator import get_env_creator
from benchmarking.timer import Timer


def run_harvest_env():
    harvest_env = get_env_creator("harvest", 5, {})(0)
    harvest_env.reset()

    agent_ids = ["agent-" + str(agent_number) for agent_number in range(5)]

    actions = {}

    for _ in range(1000):
        for agent_id in agent_ids:
            actions[agent_id] = np.random.randint(8)
        harvest_env.step(actions)

    print("done")


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    run_harvest_env()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.print_stats(20)

