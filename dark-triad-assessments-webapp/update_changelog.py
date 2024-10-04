import subprocess
import re
from datetime import datetime

def get_latest_commit_message():
    try:
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
        return commit_message
    except subprocess.CalledProcessError:
        return None

def get_current_version():
    with open('CHANGELOG.md', 'r') as f:
        content = f.read()
    match = re.search(r'\[(\d+\.\d+\.\d+)\]', content)
    if match:
        return match.group(1)
    return '0.0.0'

def increment_version(version, commit_message):
    major, minor, patch = map(int, version.split('.'))
    if 'BREAKING CHANGE' in commit_message:
        return f'{major + 1}.0.0'
    elif commit_message.startswith('feat'):
        return f'{major}.{minor + 1}.0'
    else:
        return f'{major}.{minor}.{patch + 1}'

def update_changelog(new_version, commit_message):
    with open('CHANGELOG.md', 'r') as f:
        lines = f.readlines()

    unreleased_index = next(i for i, line in enumerate(lines) if line.strip() == '## [Unreleased]')
    
    # Determine the type of change
    if commit_message.startswith('feat'):
        change_type = 'Added'
    elif commit_message.startswith('fix'):
        change_type = 'Fixed'
    elif commit_message.startswith('docs'):
        change_type = 'Documentation'
    elif commit_message.startswith('style'):
        change_type = 'Changed'
    elif commit_message.startswith('refactor'):
        change_type = 'Changed'
    elif commit_message.startswith('perf'):
        change_type = 'Changed'
    elif commit_message.startswith('test'):
        change_type = 'Changed'
    else:
        change_type = 'Changed'

    # Insert the new version and commit message
    new_lines = [
        f'\n## [{new_version}] - {datetime.now().strftime("%Y-%m-%d")}\n',
        f'\n### {change_type}\n',
        f'- {commit_message}\n'
    ]
    lines[unreleased_index + 1:unreleased_index + 1] = new_lines

    with open('CHANGELOG.md', 'w') as f:
        f.writelines(lines)

def main():
    commit_message = get_latest_commit_message()
    if not commit_message:
        print("Failed to get the latest commit message.")
        return

    current_version = get_current_version()
    new_version = increment_version(current_version, commit_message)
    update_changelog(new_version, commit_message)
    print(f"CHANGELOG.md updated with version {new_version}")

if __name__ == '__main__':
    main()