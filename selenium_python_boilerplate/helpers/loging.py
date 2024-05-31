import sys
import time 

def write_log(log: str, level: str="info") -> None:
    if level == "error":
        sys.stderr.write(f"{time.strftime('%X %x %Z')} {level}:{log}")
        return
    sys.stdout.write(f"{time.strftime('%X %x %Z')} {level}:{log}")
