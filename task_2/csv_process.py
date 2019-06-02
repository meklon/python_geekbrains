from os import listdir
from os.path import isfile, join
from pathlib import Path
from typing import Dict
from typing import List

from chardet.universaldetector import UniversalDetector
from pandas import DataFrame


def get_file_list(files_path: str) -> List[str]:
    files = [files for files in listdir(files_path) if isfile(join(files_path, files))]
    files = [join(files_path, file) for file in files]
    return files


def detect_file_encoding(path_file: Path) -> str:
    detector = UniversalDetector()
    with path_file.open(mode='rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break

    detector.close()
    f.close()
    encoding = detector.result["encoding"]
    return encoding


def list_from_file(path_file: Path, encoding: str) -> List[str]:
    with path_file.open(mode='r', encoding=encoding) as f:
        lines = f.read().splitlines()
    data = list(lines)
    f.close()
    filtered_data = filter_data(data)
    return filtered_data


def filter_data(data: List[str]) -> List[str]:
    # Filtering empty lines
    filtered_data = list(filter(None, data))
    # Removing duplicate whitespaces and newline characters
    filtered_data = [' '.join(line.split()) for line in filtered_data]
    return filtered_data


def parse_data(file_data: List[str]) -> Dict[str, str]:
    data_dict = {}
    for entry in file_data:
        if "Изготовитель системы" in entry:
            data_dict["Изготовитель системы"] = pick_value_from_string(entry)
        elif "Название ОС" in entry:
            data_dict["Название ОС"] = pick_value_from_string(entry)
        elif "Код продукта" in entry:
            data_dict["Код продукта"] = pick_value_from_string(entry)
        elif "Тип системы" in entry:
            data_dict["Тип системы"] = pick_value_from_string(entry)
    return data_dict


def pick_value_from_string(text: str) -> str:
    head, sep, tail = text.partition(': ')
    return tail


def get_df_total(files_paths: List[str]) -> DataFrame:
    columns = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы»"]
    df = DataFrame(index=[0], columns=columns)
    for file_path in files_paths:
        file_path = Path(file_path)
        encoding = detect_file_encoding(file_path)
        file_data = list_from_file(file_path, encoding)
        data_dict = parse_data(file_data)
        df = df.append(data_dict, ignore_index=True)

    # Removing empty row
    df = df.drop([0])
    return df


def save_to_csv(df: DataFrame, path: str) -> None:
    path = Path(path)
    df.to_csv(path, sep=';', index=False)


def main():
    files_paths = get_file_list('data/csv/')
    df = get_df_total(files_paths)
    print(df)
    save_to_csv(df, 'result/data.csv')


if __name__ == "__main__":
    main()
