import itertools
import numpy as np
import time

from social_dilemmas.envs.env_creator import get_env_creator


def benchmark_cleanup():
    """
    Benchmarks environments steps by executing random actions in a cleanup environment with 5 agents.
    """
    # Get the environment
    cleanup_env = get_env_creator("cleanup", 5, {})(0)

    # Get the agent ids
    agent_ids = ["agent-" + str(agent_number) for agent_number in range(5)]

    # Set empty dict for actions
    actions = {}



    # We will run the environment a couple of time first to warm up the system (the first two times are ignored)
    for i in range(2):
        # Run the environment for 1000 steps (1 episode)
        for _, agent_id in itertools.product(range(1000), agent_ids):
            actions[agent_id] = np.random.randint(8)
            cleanup_env.step(actions)

    # Stop benchmarking
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Elapsed time for 1 episode:", elapsed_time)


def itertools_test():
    for i in itertools.repeat(None, 2):
        print(i)
        # This prints None twice?

if __name__ == '__main__':
    # benchmark_cleanup()
    itertools_test()
    print("Done!")
