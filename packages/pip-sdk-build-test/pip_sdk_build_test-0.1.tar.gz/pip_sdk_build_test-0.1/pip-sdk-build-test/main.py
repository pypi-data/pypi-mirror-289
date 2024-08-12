import subprocess
import sys
import os


def checkDockerInstalled():
    try:
        # Run 'docker --version' to check if Docker is installed
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True, check=True)
        print("Docker is installed.")
        print(f"Docker version: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking Docker version: {e}")
        return False
    except FileNotFoundError:
        print("Docker is not installed.")
        return False

def checkDockerRunning():
    try:
        # Run 'docker info' to check if Docker is running
        result = subprocess.run(['docker', 'info'], capture_output=True, text=True, check=True)
        print("Docker is running.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking Docker status: {e}")
        return False
    except FileNotFoundError:
        print("Docker command not found, which means Docker is not installed.")
        return False

def installDockerInstruction():
    # Provide installation instructions for Docker
    print("\nFor Linux/Ubuntu:")
    print("1. Follow the installation instructions specific to your distribution from https://docs.docker.com/engine/install/")
    print("2. For example, on Ubuntu, you can run:")
    print("   sudo apt-get update")
    print("   sudo apt-get install docker-ce docker-ce-cli containerd.io")
    print("3. After installation, Docker should be available in your system's PATH.")



def runDockerContainer():
    # Define the Docker command
    
     # Change the working directory
    target_directory = '/home/ub/Edgeble/sdk-6.1'
    os.chdir(target_directory)
    
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")
    
    docker_command = [
        'sudo', 'docker', 'run', '--rm', '--tty', '--interactive',
        '--privileged',
        '--net', 'host',
        '-v', f"{os.getcwd()}:/home/build/shared",
        '-w', '/home/build/shared',
        'ghcr.io/edgeble/easy-dock/ubuntu:22.04-v2',,
        'bash', './build.sh rockchip_ncm6a_cam1_defconfig && && make'
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

    
    

if __name__ == "__main__":
    
    runDockerContainer()
    if not checkDockerInstalled():
        installDockerInstruction()
        sys.exit(1)
        
    print("Docker is installed and running.")

