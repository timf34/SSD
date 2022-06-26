import itertools
import numpy as np
import time

from social_dilemmas.envs.env_creator import get_env_creator
from benchmarking.timer import Timer

"""
    This file is for testing and approximating how long it will take to run each of these environments
    
    TODO: I should probably clean this up a bit, I don't think I have written things the most optimal way here...

"""


def benchmark_cleanup():
    """
    Benchmarks environments steps by executing random actions in a cleanup environment with 5 agents.
    """
    # Get the environments
    cleanup_env = get_env_creator("cleanup", 5, {})(0)
    harvest_env = get_env_creator("harvest", 5, {})(0)

    # We will run the environment twice to warm it up
    env_loop(environment=cleanup_env, num_episodes=2)

    # Initialize timer
    t = Timer()
    t.start()

    # Now lets run it and benchmark it
    for _ in range(2):
        env_loop(environment=cleanup_env, num_episodes=1)
        t.update_episodes()

    t.stop()
    t.print_stats()

    # Lets try again without the for loop
    print("round 2")

    t = Timer()
    t.start()
    env_loop(environment=cleanup_env, num_episodes=1)
    t.update_episodes()
    env_loop(environment=harvest_env, num_episodes=1)
    t.update_episodes()
    t.stop()
    t.print_stats()


def env_loop(environment, num_episodes: int = 1, episode_length: int = 1000) -> None:
    """
    Runs the environment for a number of episodes.
    """
    # Get the agent ids
    agent_ids = [f"agent-{str(agent_number)}" for agent_number in range(5)]

    # Set empty dict for actions
    actions = {}

    while num_episodes > 0:
        for __ in range(episode_length):
            for agent_id in agent_ids:
                actions[agent_id] = np.random.randint(8)
                environment.step(actions)
        num_episodes-=1



if __name__ == '__main__':
    benchmark_cleanup()

    for _ in range(2):
        print("yolo")
    print("Done!")
