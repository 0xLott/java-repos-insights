import os
import subprocess

repo_path = './clones/'
base_output_path = './ck/output/'
ck_jar_path = './ck/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar'

def run_ck():
    os.makedirs(base_output_path, exist_ok=True)

    for repo_name in os.listdir(repo_path):
        output_path = os.path.join(base_output_path, repo_name)
        output_path += '/'

        os.makedirs(output_path, exist_ok=True)

        command = [
            'java', '-jar', ck_jar_path,
            repo_path, 'false', '0', 'true', output_path
        ]

        try:
            print(f"Running ck for: {repo_name}")
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run ck for {repo_name}: {e}")