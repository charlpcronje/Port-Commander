#!/usr/bin/env python3
import subprocess
import argparse

def find_process(port):
    try:
        result = subprocess.check_output(["lsof", "-i", f":{port}", "-t"], text=True).strip()
        pid = result.split('\n')[0] if result else None
        if pid:
            proc_name = subprocess.check_output(["ps", "-p", pid, "-o", "comm="], text=True).strip()
            return pid, proc_name
        return None, None
    except Exception as e:
        print(f"Error finding process: {e}")
        return None, None

def kill_process(pid):
    try:
        subprocess.run(["kill", pid], check=True)
        print("Process killed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error killing process: {e}")

def list_ports(range_start=1, range_end=65535):
    print(f"Listing processes for ports {range_start} to {range_end}:")
    for port in range(range_start, range_end + 1):
        pid, proc_name = find_process(port)
        if pid:
            print(f"Port: {port} -> PID: {pid}, Process: {proc_name}")

def main():
    parser = argparse.ArgumentParser(description="Manage applications by port.")
    parser.add_argument('port', nargs='?', type=int, help="Port number to investigate.")
    parser.add_argument('--kill', action='store_true', help="Kill the process running on the specified port.")
    parser.add_argument('--list', nargs='*', type=int, help="List all ports or a range (start end).")
    args = parser.parse_args()

    if args.list is not None:
        if len(args.list) == 2:
            list_ports(args.list[0], args.list[1])
        else:
            list_ports()
    elif args.port:
        pid, proc_name = find_process(args.port)
        if pid:
            print(f"Port: {args.port} -> PID: {pid}, Process: {proc_name}")
            if args.kill:
                confirm = input("Do you want to kill this process? [y/N] ")
                if confirm.lower() == 'y':
                    kill_process(pid)
            else:
                print("Use --kill to kill the process.")
        else:
            print("No process found on this port.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
