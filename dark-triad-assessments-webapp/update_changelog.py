import os
import re
import sqlite3
from datetime import datetime

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set the path to CHANGELOG.md relative to the script location
changelog_path = os.path.join(script_dir, 'CHANGELOG.md')

def get_current_version():
    try:
        with open(changelog_path, 'r') as f:
            content = f.read()
            match = re.search(r'## \[(\d+\.\d+\.\d+)\]', content)
            if match:
                return match.group(1)
    except FileNotFoundError:
        print(f"CHANGELOG.md not found at {changelog_path}. Creating a new one.")
        return "0.0.0"
    return "0.0.0"

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor}.{patch + 1}"

def get_commit_messages():
    # Get commit messages since the last tag
    try:
        from subprocess import check_output
        last_tag = check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
        commit_messages = check_output(['git', 'log', f'{last_tag}..HEAD', '--pretty=format:%s']).decode().split('\n')
    except:
        print("Error getting commit messages. Using placeholder.")
        commit_messages = ["Placeholder commit message"]
    return commit_messages

def update_changelog(new_version, commit_messages):
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"""## [{new_version}] - {today}

### Added
{format_commit_messages(commit_messages)}

"""
    try:
        with open(changelog_path, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(new_entry + content)
    except FileNotFoundError:
        with open(changelog_path, 'w') as f:
            f.write(new_entry)

def format_commit_messages(messages):
    return "\n".join(f"- {msg}" for msg in messages if msg)

def main():
    current_version = get_current_version()
    new_version = increment_version(current_version)
    commit_messages = get_commit_messages()
    update_changelog(new_version, commit_messages)
    print(f"CHANGELOG.md updated with version {new_version}")

if __name__ == "__main__":
    main()