import os
from tensorflow import keras
run_logdir = os.path.join(os.curdir, "my_logs", "run_001")
tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)
print("TensorBoard callback configured for:", run_logdir)
