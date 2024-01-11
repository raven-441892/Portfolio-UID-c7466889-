# Using command-line arguments involves the sys module. Review the docs for this
# module and using the information in there write a short program that when run
# from the command-line reports what operating system platform is being used.

import sys  # Import the sys module for accessing system-specific information

def report_platform():  # Define a function to report the operating system platform
    platform = sys.platform  # Get the platform information using sys.platform
    if platform.startswith('linux'):  # Check if the platform starts with 'linux'
        print("Linux platform detected.")
    elif platform.startswith('win'):  # Check if the platform starts with 'win'
        print("Windows platform detected.")
    elif platform.startswith('darwin'):  # Check if the platform starts with 'darwin'
        print("MacOS platform detected.")
    else:
        print("Unknown platform detected.")  # Print if the platform is not recognized

if __name__ == "__main__":  # Check if the script is being run as the main program
    report_platform()  # Call the report_platform function to display the detected platform
