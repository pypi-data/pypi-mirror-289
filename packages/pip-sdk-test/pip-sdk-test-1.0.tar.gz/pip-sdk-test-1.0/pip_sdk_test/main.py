# pip_helloworld/main.py

import subprocess
import sys
import os


def runDockerContainer():
    # Define the Docker command
    
     # Change the working directory
   
    
    current_directory = os.getcwd()
    
    
    target_directory = os.getcwd()
    os.chdir(target_directory)
    
    print(f"Current working directory: {current_directory}")
    
    docker_command = [
        'sudo', 'docker', 'run', '--rm', '--tty', '--interactive',
        '--privileged',
        '--net', 'host',
        '-v', f"{os.getcwd()}:/home/build/shared",
        '-w', '/home/build/shared',
        'ghcr.io/edgeble/easy-dock/ubuntu:22.04-v2',
        'bash','-c','./build.sh rockchip_ncm6a_cam1_defconfig && ./build.sh'
    ]

    try:
        # Output the command for debugging purposes
        print("Running Docker command:")
        print(" ".join(docker_command))
        
        # Run the Docker command with interactive shell
        subprocess.run(docker_command)
        
        # This part will only be reached after the shell exits
        print("Docker container executed and shell exited successfully.")
    except subprocess.CalledProcessError as e:
        # Print the command that failed and its output
        print("Error running Docker container:")
        print(f"Command: {' '.join(e.cmd)}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error: {e.stderr}")
    except FileNotFoundError:
        print("Docker is not installed or the command was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def main():
    print("Docker is running......")
    runDockerContainer()

if __name__ == "__main__":
    main()

