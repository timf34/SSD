import time


class Timer:
    def __init__(self):
        self.start_time: int
        self.end_time: int
        self.elapsed_time: int
        self.average_time: int = 0
        self.steps: int
        self.episodes: int = 0

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        # self.average_time = self.elapsed_time / self.episodes

    def update_episodes(self):
        self.episodes += 1

    def update_individual_step(self):
        self.steps += 1

    def update_batch_steps(self, steps: int):
        self.steps += steps

    def print_stats(self):
        # print("Start time:", self.start_time)
        # print("End time:", self.end_time)
        print("Elapsed time:", self.elapsed_time)
        if self.episodes > 0:
            print("Average time:", self.elapsed_time / self.episodes)
        # print("Average time per episode:", self.average_time)
        # In general we can assume there are 1000 steps per episode but that kinda just complicates things here rn
        # Not needed for the moment unless I decide to chnage the number of steps from 1000
        # print("Average time per step:", self.average_time / self.steps)