import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("destination_dir", nargs='?', default="dist", help="Path to the destination directory (default: dist)")
    return parser.parse_args()

def copy_files(src_dir, dest_dir):
    try:
        # Перебираємо всі елементи у директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                # Якщо елемент є директорією, викликаємо функцію рекурсивно
                copy_files(src_path, dest_dir)
            else:
                # Якщо елемент є файлом, обробляємо його для копіювання
                file_extension = os.path.splitext(item)[1][1:].lower()  # Отримуємо розширення файлу без крапки і в нижньому регістрі
                if not file_extension:
                    file_extension = "no_extension"  # Якщо файл не має розширення

                dest_path = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_path, exist_ok=True)  # Створюємо директорію, якщо вона не існує

                shutil.copy2(src_path, os.path.join(dest_path, item))  # Копіюємо файл
                print(f"Copied: {src_path} -> {os.path.join(dest_path, item)}")

    except Exception as e:
        print(f"Error copying files: {e}")

def main():
    args = parse_args()
    src_dir = args.source_dir
    dest_dir = args.destination_dir

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    os.makedirs(dest_dir, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує

    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
