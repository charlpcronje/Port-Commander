### Port Commander

```markdown
# PORT COMMANDER

## Overview

PORT COMMANDER is a Command Line Interface (CLI) tool designed for Linux administrators and developers. It allows users to manage applications running on specific ports of a Rocky Linux 9.3 system. With PORT COMMANDER, you can easily identify what application is running on a given port, terminate unwanted applications, and list all active ports along with the applications running on them.

## Installation

To get started with PORT COMMANDER, follow these simple installation steps:

1. Ensure you have Python 3 installed on your system.
2. Clone this repository to your local machine:

```bash
git clone https://github.com/charlpcronje/Port-Commander.git
```

3. Navigate to the PORT COMMANDER directory:

```bash
cd Port-Commander
```

4. Make the script executable:

```bash
chmod +x port_cmd.py
```

5. Create a symbolic link to run PORT COMMANDER from anywhere:

```bash
sudo ln -s $(pwd)/port_cmd.py /usr/local/bin/pc
```

## Usage

After installation, PORT COMMANDER can be used with the following commands:

- To find which application is running on a specific port:

```bash
pc <port_number>
```

- To kill the application running on a specified port:

```bash
pc <port_number> --kill
```

- To list all applications running on all ports:

```bash
pc --list
```

- To list applications within a specific range of ports:

```bash
pc --list <start_port> <end_port>
```

For additional help, run:

```bash
pc --help
```

## Contributions

Contributions to Port Commander are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork the repository, make changes, and submit a pull request. You can also open an issue in the GitHub repository if you find any bugs or have feature requests.

## Contact

For support or to get in touch, please add your contact details here or reach out to me directly at [charl@webally.co.za](mailto:charl@webally.co.za).

## Conclusion

Port Commander aims to simplify the process of managing applications on various ports for Linux users. It's a handy tool for developers and system administrators looking for a quick way to monitor and control the
