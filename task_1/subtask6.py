from pathlib import Path

from chardet.universaldetector import UniversalDetector


def detect_file_encoding(path_file: Path) -> None:
    detector = UniversalDetector()
    with path_file.open(mode='rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break

    detector.close()
    print(detector.result)


def print_file_content_utf8(path_file: Path) -> None:
    with path_file.open(mode='r', encoding='utf-8') as f:
        print(f.read())
    f.close()


file_path = Path('data/test_file.txt')
detect_file_encoding(file_path)
print_file_content_utf8(file_path)
