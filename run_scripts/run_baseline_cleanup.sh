#!/usr/bin/env bash

python train.py \
--env cleanup \
--model baseline \
--algorithm PPO \
--num_agents 5 \
--num_workers 2 \
--rollout_fragment_length 1000 \
--num_envs_per_worker 16 \
--stop_at_timesteps_total $((500 * 10 ** 6)) \
--memory $((160 * 10 ** 7)) \
--cpus_per_worker 1 \
--gpus_per_worker 0 \
--gpus_for_driver 1 \
--cpus_for_driver 0 \
--num_samples 1 \
--entropy_coeff 0.00176 \
--lr_schedule_steps 0 20000000 \
--lr_schedule_weights .00126 .000012
