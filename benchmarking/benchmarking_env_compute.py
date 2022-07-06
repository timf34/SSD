import itertools
import numpy as np
import time

from social_dilemmas.envs.env_creator import get_env_creator
from benchmarking.timer import Timer

"""
    This file is for testing and approximating how long it will take to run each of these environments
    
    TODO: I should probably clean this up a bit, I don't think I have written things the most optimal way here...

"""


def benchmark_envs():
    """
    Benchmarks environments steps by executing random actions in a cleanup environment with 5 agents.
    """

    # Note that I know this is messy, but it seems to give the most accuarte results (or at least the fastest)
    # see my code below which seems to act a bit weirder...

    envs = ["cleanup", "harvest"]
    for env in envs:
        print("Starting benchmark for: ", env)

        # Get the environments
        env = get_env_creator(env, 5, {})(0)
        # harvest_env = get_env_creator("harvest", 5, {})(0)

        agent_ids = ["agent-" + str(agent_number) for agent_number in range(5)]

        actions = {}

        warmup = Timer()
        warmup.start()

        env.reset()

        for __ in range(1000):
            for agent_id in agent_ids:
                actions[agent_id] = np.random.randint(8)
            env.step(actions)
        env.reset()
        warmup.stop()
        print("Warmup time...")
        warmup.print_stats()

        # Initialize timer
        t = Timer()
        t.start()
        for _ in range(1000):
            for agent_id in agent_ids:
                actions[agent_id] = np.random.randint(8)
            env.step(actions)
        env.reset()

        t.stop()
        t.print_stats()
        env.reset()

        t2 = Timer()
        t2.start()

        for __ in range(10):
            for _ in range(1000):
                for agent_id in agent_ids:
                    actions[agent_id] = np.random.randint(8)
                env.step(actions)
            t2.update_episodes()
            env.reset()

        t2.stop()
        t2.print_stats()

        env.reset()



if __name__ == '__main__':
    benchmark_envs()
    print("Done!")























def benchmark_cleanup_weird():
    """
    Benchmarks environments steps by executing random actions in a cleanup environment with 5 agents.

    There is some very strange behaviour going on here... I am going to redo this function more simply and copy this
    function below to look at laster...

    Here is some sample output, but really everything has been strange...
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