# .github

### Overview
This repo provides useful resources for members of the Vexergy Developer community as well as those who use our software and services. **_Welcome!_**

### Support
For support services related to any of our products and projects, please view the [SUPPORT.md](./SUPPORT.md) file to learn more about our support policy.

### [License](./LICENSE)
All open source code released publicly will be licensed appropriately (typically under the MIT License) as determined by the nature and purpose of the code itself.

### Security
Please see the [SECURITY.md](./SECURITY.md) file for more information regarding our organization's security policy.

### Down Detection
In order to check the status of our websites and applications, provided in this repo is a simple script to verify if all our systems are online and operational.  

**Usage:**
* Clone this GitHub repository to your local computer.
* **Python:** Create a virtual environment (.venv) with the necessary dependencies listed in the [requirements.txt](./requirements.txt) file in the cloned folder and run the python file titled `vexergy_status.py` and you should see the output to your terminal.
* You can also execute this python script remotely from Git Bash, Linux, or macOS if you `cd` into the cloned repo directory and then run the command `chmod +x shell.sh` and `./shell.sh` to run the [Shell](./shell.sh) script.
* Alternatively, you can do the same by running the provided [PowerShell](./powershell.ps1) version of this script on Windows.
* A [Dockerfile](./Dockerfile) is also included with containerization details.
