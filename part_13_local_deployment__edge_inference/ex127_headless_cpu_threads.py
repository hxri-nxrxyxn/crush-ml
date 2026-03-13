import os
os.environ["OMP_NUM_THREADS"] = "1"
print("Optimization: Restricting CPU threads for predictable performance in headless environments.")
