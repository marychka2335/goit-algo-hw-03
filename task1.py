import os
import shutil
import argparse

def copy_and_sort_files(source_dir, dest_dir="dist"):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                new_dest_dir = os.path.join(dest_dir, item)
                os.makedirs(new_dest_dir, exist_ok=True)
                copy_and_sort_files(source_path, new_dest_dir)
            elif os.path.isfile(source_path):
                file_extension = os.path.splitext(item)[1].lower()
                extension_dir = os.path.join(dest_dir, file_extension[1:])
                os.makedirs(extension_dir, exist_ok=True)
                shutil.copy2(source_path, os.path.join(extension_dir, item))
    except (OSError, IOError) as e:
        print(f"Помилка при обробці '{source_path}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіювання файлів та їх сортування за розширеннями.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії.")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist').")
    args = parser.parse_args()
    
    if not os.path.exists(args.source_dir):
        print(f"Вихідна директорія '{args.source_dir}' не існує.")
    else:
        os.makedirs(args.dest_dir, exist_ok=True)
        copy_and_sort_files(args.source_dir, args.dest_dir)
        print(f"Файли скопійовані та відсортовані до директорії '{args.dest_dir}'.")
