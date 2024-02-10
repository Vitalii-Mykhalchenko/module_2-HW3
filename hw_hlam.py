import time
from pathlib import Path
import shutil
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor


# функція по обробки файлу
def proceed_file(path_file: Path, root_folder: Path):
    file_extension = path_file.suffix[1:]  # png, txt....
    file_name = path_file.stem            # назва файлу
    create_folders = root_folder.joinpath(file_extension)
    create_folders.mkdir(exist_ok=True)
    target_file = create_folders.joinpath(file_name + "." + file_extension)
    shutil.move(path_file, target_file)


def proceed_folder(path, root_folder):  # функція яка обробляє файли

    for el in path.iterdir():              # переебираємо вкладенні єлементи у папку

        if el.is_dir():                    # якщо це папка ми знову пеербираємо папку
            # рекурсивно визиваємо саму себе
            proceed_folder(el, root_folder)
        else:
            # якщо це файл то обробляємо його як файл, результат виконання функції у батьківский каталог
            proceed_file(el, root_folder)
    else:
        # видаляємо порожні каталоги у корневій папці
        delete_empty_folder(path)


def delete_empty_folder(path: Path):  # видаляємо папки якщо вона пуста
    try:
        if path.is_dir() and len(list(path.iterdir())) == 0:
            path.rmdir()
            print(f"папка видалена {path}")
    except:
        # print( f"папка не пуста  {path}")
        pass


def main(folder_path: Path):

    if folder_path.exists() and folder_path.is_dir():
        proceed_folder(folder_path, folder_path)  # обробляємо корневий каталог

    else:
        print("Папка не існує або не є папкою.")


def main2(folder_path: Path):

    if folder_path.exists() and folder_path.is_dir():
        with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
            executor.submit(proceed_folder, folder_path, folder_path)

    else:
        print("Папка не существует или не является папкой.")


if __name__ == "__main__":
    source_folder = Path("first path")
    source_folder2 = Path("second path")

    star_time = time.time()
    main(source_folder)
    end_time = time.time()

    star_time2 = time.time()
    main2(source_folder2)
    end_time2 = time.time()

    print("main", end_time - star_time)
    print("main2", end_time2 - star_time2)
