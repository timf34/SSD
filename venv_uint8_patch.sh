# This patch fixes two bugs in ray.

# Find Python folder name so that this patch can run correctly on different versions of Python.
python_folder_name=$(ls venv/lib)

# Apply patches for https://github.com/ray-project/ray/issues/7946
# Note: I am hardcoding python3.8 as python_folder_name wouldn't work.
# got this: /site-packages/ray/rllib/models/catalog.py: No such file or directory

# Note: I also hardcoded this: ray-0.8.5-py3.8-linux-x86_64.egg/  into the file path as thats just the way it was in my
# venv
sed -i '119s/tf.float32/tf.uint8/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/policy/dynamic_tf_policy.py # Hardcoded observation space to uint8.
sed -i '76s/np.float32/np.uint8/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/models/preprocessors.py # Same as above.
sed -i '231s/np.zeros(self.shape)/np.zeros(self.shape, dtype=self.observation_space.dtype)/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/models/preprocessors.py # Change observation shape to what we actually provide
sed -i '214s/tf.int64/action_space.dtype/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/models/catalog.py # Change action shape to what we actually provide
sed -i '56s/tf.math.argmax(self.inputs, axis=1)/tf.math.argmax(self.inputs, axis=1, output_type=tf.int32)/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/models/tf/tf_action_dist.py # Actions should not sample at int64, int32 is the lowest that multinomial takes
sed -i '84s/tf.multinomial(self.inputs, 1)/tf.multinomial(self.inputs, 1, output_dtype=tf.int32)/' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/models/tf/tf_action_dist.py # Same as above
sed -i '656i\        actions = np.array(actions, dtype=policy.action_space.dtype)' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/rllib/evaluation/sampler.py # Insert action to uint8 conversion to save even more memory

# Apply patch for https://github.com/ray-project/ray/pull/8491 (fixed in ray 0.8.6, remove this when upgrading to ray >= 0.8.6)
sed -i '164i\        return self.sess.run(self.variables)' venv/lib/python3.8/site-packages/ray-0.8.5-py3.8-linux-x86_64.egg/ray/experimental/tf_utils.py