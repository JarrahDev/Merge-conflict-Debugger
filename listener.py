import subprocess

def Listener(git_bash_path):
    # Open the Git Bash terminal and start listening
    process = subprocess.Popen([git_bash_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    try:
        while True:
            # Read a line of output from the terminal
            output = process.stdout.readline()

            # You can add specific conditions or patterns to detect here
            # For example, you can look for error messages or other signals
            if "error" in output.lower():
                print("Detected an error:", output)

            # You can add more conditions here to detect specific issues

    except KeyboardInterrupt:
        # Exit the loop if the user presses Ctrl+C
        pass

    # Close the terminal when done
    process.terminate()

if __name__ == '__main__':
    git_bash_path = r"D:\Git\git-bash.exe"  # Replace with your Git Bash path
    Listener(git_bash_path)
