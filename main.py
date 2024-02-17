import os

exclude_dirs = {
    '_static',
    '_settings',
    '_excalidraw', 
    '_Diary', 
    '.github', 
    '.git', 
    '.trash',
    '.obsidian',
    'Health',
    'Random',
}

def encode_path(path):
    # Замена пробелов на %20 для корректной обработки в Markdown
    return path.replace(' ', '%20')

def create_readme_for_directory(dir_path, parent_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # Исключаем директории, которые не должны обрабатываться
        dirs[:] = sorted([d for d in dirs if not any(ex_dir in os.path.join(root, d) for ex_dir in exclude_dirs)])
        files = sorted(files)
        
        readme_content = []
        readme_path = os.path.join(root, '.readme.md')
        
        # Получение относительного пути текущей директории относительно ее родителя
        relative_path = os.path.relpath(root, parent_path) if parent_path else '.'
        dirname = os.path.basename(root) if relative_path != '.' else parent_path
        readme_content.append(f'# {dirname}\n')

        # Добавление файлов в содержимое .readme, исключая .readme файл
        for file in files:
            if file != '.readme':
                readme_content.append(f'- [{file}]({encode_path(file)})')

        # Добавление поддиректорий в содержимое .readme
        for dir in dirs:
            readme_content.append(f'- [{dir}]({encode_path(dir + "/.readme.md")})')

        # Запись содержимого в .readme файл
        with open(readme_path, 'w') as f:
            f.write('\n'.join(readme_content))

def generate_readmes(start_dir):
    base_path = os.path.abspath(start_dir)
    parent_path = os.path.dirname(base_path)
    create_readme_for_directory(base_path, parent_path)


def generate_readmes_in_current_directory():
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        if os.path.isdir(item_path) and item not in exclude_dirs:
            create_readme_for_directory(item_path, os.path.dirname(item_path))

generate_readmes_in_current_directory()