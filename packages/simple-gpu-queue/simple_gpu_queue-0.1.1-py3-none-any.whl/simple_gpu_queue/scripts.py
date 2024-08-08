import tyro
from simple_gpu_queue import GPUQueueServer
import sys

def start_server():
    args = sys.argv[1:]
    server = tyro.cli(GPUQueueServer, args=args)
    server.run()