import os
import sys

# print(min(32, (os.cpu_count() or 1) + 4))

print("CPU count:", os.cpu_count())
print("System platform:", sys.platform)