# src/launcher.py

import subprocess

def main():
    subprocess.run(["streamlit", "run", "img_db.py"])

if __name__ == "__main__":
    main()
