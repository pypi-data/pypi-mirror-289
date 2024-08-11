import subprocess
import os

def run():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, '../Arpier.sh')
    subprocess.run(['sudo', 'bash', script_path])

if __name__ == "__main__":
    run()
