import os
import time
import shutil
import argparse




def main():
    parser = argparse.ArgumentParser(description="Clean up the virtual environment")
    parser.add_argument("--path", default="", help="Path to the virtual environments directory")
    parser.add_argument("-t", "--time", default=3600, help="Time in seconds to wait before checking for new virtual environments (default: 3600)", type=int)
    parser.add_argument("--ignore-list", default=[], help="List of virtual environments NAMES to ignore", nargs="*")
    args = parser.parse_args()

    if args.path != "" and not os.path.exists(args.path):
        raise ValueError(f"The path {args.path} does not exist")
    
    path = os.path.join(os.path.expanduser('~'), ".local", "share", "virtualenvs", "") if args.path == "" else args.path
    if not os.path.exists(path):
        raise ValueError(f"The path {path} does not exist")

    while True:
        venvs = []
        for folder in os.listdir(path):
            if os.path.isdir(os.path.join(path, folder)):
                folderPath = os.path.join(path, folder)
                for file in os.listdir(folderPath):
                    if file == ".project":
                        with open(os.path.join(folderPath, file), "r") as f:
                            projectPath = f.read().strip()
                            venvs.append((folderPath, projectPath))

        for folder, env in venvs:
            if not os.path.exists(env):
                if folder.split("/")[-1].split("-")[0] in args.ignore_list:
                    print(f"Ignoring {folder}")
                    continue
                print(f"Removing {folder}")
                shutil.rmtree(folder)
        time.sleep(args.time)





if __name__ == "__main__":
    main()
