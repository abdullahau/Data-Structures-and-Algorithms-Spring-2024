# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored
def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)

# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
current, peak = tracemalloc.get_traced_memory()
print("Peak Memory Usage (MB)", round(peak/(1024**2), 3))

# stopping the library
tracemalloc.stop()