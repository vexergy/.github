# .github

### Overview
This repo provides useful resources for members of the Vexergy Developer community as well as those who use our software and services. **_Welcome!_**

### [License](./LICENSE)
All open source code released publically will be licensed appropriately (typically under the MIT License) as determined by the nature and purpose of the code itself.

### Security
Please see the [SECURITY.md](./SECURITY.md) file for more information regarding our organization's security policy.

### Down Detection
In order to check the status of our websites and applications, provided in this repo is a simple script to verify if all our systems are online and operational.  

**Usage:**
* Clone this GitHub repository to your local computer.

* **Python:** Create a virtual environment (.venv) with the necessary dependencies listed in the [requirements.txt](./requirements.txt) file in the cloned folder and run the python file titled `vexergy_status.py` and you should see the following output to your terminal:

<img width="250" alt="image" src="https://github.com/user-attachments/assets/0016f897-ead9-49d8-91ac-cba11cf07520" />

* You can also execute this python script remotely from Git Bash if you `cd` into the cloned repo directory and then run the command `chmod +x vexergy_check.sh` and `./vexergy_check.sh` to run the [Shell](./vexergy_check.sh) script.
* Alternatively, you can do the same by running the provided [PowerShell](./vexergy_check.ps1) version of this script on Windows.
* A [Dockerfile](./Dockerfile) is also included with containerization details.
