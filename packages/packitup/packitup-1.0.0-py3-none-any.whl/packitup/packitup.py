import os
import mimetypes
import pyperclip
import argparse
from datetime import datetime
import shutil
import colorama
from colorama import Fore, Style, Back
import json
import yaml
import fnmatch
from tqdm import tqdm
import zipfile

SKIP_FOLDERS = [
    # Version control
    '.git', '.svn', '.hg', '.bzr',
    
    # Dependencies and package managers
    'node_modules', 'bower_components', 'jspm_packages',
    'vendor', 'packages', 'composer.phar',
    
    # Python
    'venv', '.venv', 'env', '.env', '__pycache__', '.pytest_cache',
    'pip-wheel-metadata', '.eggs', '*.egg-info',
    
    # Build outputs
    'dist', 'build', 'out', 'target', 'bin', 'obj',
    
    # IDE and editor specific
    '.idea', '.vscode', '.vs', '*.sublime-*',
    '.atom', '.eclipse', '.settings',
    
    # OS specific
    '.DS_Store', 'Thumbs.db',
    
    # Logs and temporary files
    'logs', '*.log', 'tmp', 'temp',
    
    # Configuration and local settings
    '.env.local', '.env.*.local',
    
    # Docker
    '.docker',
    
    # Coverage reports
    'coverage', '.coverage', 'htmlcov',
    
    # Documentation builds
    'docs/_build', 'site',
    
    # Compiled source
    '*.com', '*.class', '*.dll', '*.exe', '*.o', '*.so',
]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
CHUNK_SIZE = 1 * 1024 * 1024  # 1 MB

def load_gitignore(path):
    gitignore_patterns = []
    gitignore_path = os.path.join(path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return gitignore_patterns

def should_skip(path, skip_patterns, gitignore_patterns):
    name = os.path.basename(path)
    if any(fnmatch.fnmatch(name, pattern) for pattern in skip_patterns + gitignore_patterns):
        return True
    return False

def get_file_metadata(file_path):
    stats = os.stat(file_path)
    return {
        'size': stats.st_size,
        'modified': datetime.fromtimestamp(stats.st_mtime).isoformat(),
        'permissions': oct(stats.st_mode)[-3:]
    }

def get_file_content(file_path, output_dir, relative_path, single_file=False, include_content=True):
    if not include_content:
        return get_file_metadata(file_path)
    
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE and not single_file:
        return handle_large_file(file_path, output_dir, relative_path)
    
    mime_type, _ = mimetypes.guess_type(file_path)
    
    if mime_type and mime_type.startswith('text'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return {**get_file_metadata(file_path), 'content': content}
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='iso-8859-1') as file:
                    content = file.read()
                return {**get_file_metadata(file_path), 'content': content}
            except Exception:
                return {**get_file_metadata(file_path), 'content': f"[Unable to read {os.path.basename(file_path)}]"}
    else:
        return {**get_file_metadata(file_path), 'content': f"[{os.path.splitext(file_path)[1]} file]"}

def handle_large_file(file_path, output_dir, relative_path):
    file_name = os.path.basename(file_path)
    parts_dir = os.path.join(output_dir, f"{file_name}_parts")
    os.makedirs(parts_dir, exist_ok=True)
    part_num = 1
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            part_file = os.path.join(parts_dir, f"{file_name}.part{part_num}")
            with open(part_file, 'wb') as part:
                part.write(chunk)
            part_num += 1

    return {**get_file_metadata(file_path), 'content': f"[Large file split into {part_num - 1} parts. See {os.path.relpath(parts_dir, output_dir)}]"}

def generate_content(path, output_dir, skip_patterns, gitignore_patterns, tree_only=False, single_file=False, include_content=True):
    content = {}
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if should_skip(item_path, skip_patterns, gitignore_patterns):
            continue
        if os.path.isdir(item_path):
            content[item] = generate_content(item_path, output_dir, skip_patterns, gitignore_patterns, tree_only, single_file, include_content)
        else:
            if tree_only:
                content[item] = None
            else:
                content[item] = get_file_content(item_path, output_dir, item, single_file, include_content)
    return content

def content_to_markdown(content, indent=''):
    md_content = []
    for key, value in content.items():
        if value is None or isinstance(value, dict) and 'content' not in value:
            md_content.append(f"{indent}- {key}/")
            if value:
                md_content.extend(content_to_markdown(value, indent + '  '))
        else:
            md_content.append(f"{indent}- {key}")
            if isinstance(value, dict) and 'content' in value:
                md_content.append(f"{indent}  ```")
                md_content.append(f"{indent}  {value['content']}")
                md_content.append(f"{indent}  ```")
    return md_content

def compress_output(output_dir, compressed_file):
    with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), output_dir))

def main():
    colorama.init(autoreset=True)
    parser = argparse.ArgumentParser(description="Generate project structure and contents.")
    parser.add_argument('path', nargs='?', default='.', help="Path to pack (default: current directory)")
    parser.add_argument('-t', '--tree', action='store_true', help="Generate file tree only (no file contents)")
    parser.add_argument('-l', '--list', action='store_true', help="List files and directories in the specified directory")
    parser.add_argument('-s', '--singlefile', action='store_true', help="Ignore file splitting and return as a single file")
    parser.add_argument('-p', '--purge', action='store_true', help="Purge all saved PackItUp data")
    parser.add_argument('-f', '--format', choices=['markdown', 'json', 'yaml'], default='markdown', help="Output format (default: markdown)")
    parser.add_argument('-m', '--max-size', type=int, help="Maximum file size in bytes (default: 5MB)")
    parser.add_argument('-c', '--compress', action='store_true', help="Compress the output files")
    parser.add_argument('-e', '--exclude', nargs='+', help="Additional patterns to exclude")
    parser.add_argument('--no-content', action='store_true', help="Exclude file contents, only include metadata")
    args = parser.parse_args()

    if args.purge:
        purge_data()
        return

    if args.max_size:
        global MAX_FILE_SIZE
        MAX_FILE_SIZE = args.max_size

    root_dir = os.path.abspath(args.path)

    if args.list:
        list_directory(root_dir)
        return

    gitignore_patterns = load_gitignore(root_dir)
    skip_patterns = SKIP_FOLDERS + (args.exclude or [])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    root_folder_name = os.path.basename(root_dir)

    output_dir = f"{root_folder_name}_structure_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{root_folder_name}_structure_{timestamp}.{args.format}")

    print(f"Generating project structure for {root_dir}...")
    content = generate_content(root_dir, output_dir, skip_patterns, gitignore_patterns, 
                               args.tree, args.singlefile, not args.no_content)

    if args.format == 'markdown':
        output_content = '\n'.join(["# Project Structure", ""] + content_to_markdown(content))
    elif args.format == 'json':
        output_content = json.dumps(content, indent=2)
    else:  # yaml
        output_content = yaml.dump(content, default_flow_style=False)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)

    if args.compress:
        compressed_file = f"{output_file}.zip"
        print(f"Compressing output to {compressed_file}...")
        compress_output(output_dir, compressed_file)
        print(f"Compressed file saved to {compressed_file}")

    pyperclip.copy(output_content)

    print_styled_header("PackItUp Completed Successfully!")

    print_styled_section("📁 Output Location", [
        f"📌 Local: {Fore.YELLOW}{make_clickable(os.path.abspath(output_dir))}"
    ])

    print_styled_section("📄 Main File", [
        f"📌 Local: {Fore.YELLOW}{make_clickable(os.path.abspath(output_file))}"
    ])

    print_styled_section("ℹ️  Info", [
        f"📋 Content has been copied to clipboard.",
        f"📂 Large files have been split and saved in parts if necessary.",
        f"🗂️  Skipped patterns: {', '.join(skip_patterns + gitignore_patterns)}"
    ])

if __name__ == "__main__":
    main()