import os
import time
import shutil
import argparse




def main():
    parser = argparse.ArgumentParser(description="Clean up the virtual environment")
    parser.add_argument("--path", default=os.path.join(os.path.expanduser('~'), ".local", "share", "virtualenvs", ""), help="Path to the virtual environments directory")
    parser.add_argument("--ignore-list", default=[], help="List of virtual environments NAMES to ignore", nargs="*")
    args = parser.parse_args()


    if not os.path.exists(args.path):
        raise ValueError("The path f{args.path} does not exist")

    while True:
        venvs = []
        for folder in os.listdir(args.path):
            if os.path.isdir(os.path.join(args.path, folder)):
                folderPath = os.path.join(args.path, folder)
                for file in os.listdir(folderPath):
                    if file == ".project":
                        with open(os.path.join(folderPath, file), "r") as f:
                            projectPath = f.read().strip()
                            venvs.append((folderPath, projectPath))

        for folder, env in venvs:
            if not os.path.exists(env):
                print(folder)
                if folder.split("/")[-1] in args.ignore_list:
                    print(f"Ignoring {folder}")
                    continue
                print(f"Removing {folder}")
                shutil.rmtree(folder)
        time.sleep(15)





if __name__ == "__main__":
    main()
