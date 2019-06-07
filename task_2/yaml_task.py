import os

import yaml


def check_mkdir_output_path(path_output: str) -> None:
    # Function checks if the output path exists and creates it if not
    if not os.path.exists(path_output):
        os.mkdir(path_output)


def write_data_to_yaml(data: dict, output_file: str) -> None:
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
    file.close()


def main():
    check_mkdir_output_path('result/')
    output_file = 'result/file.yaml'

    data = {'name': 'Commander Shepard',
            'Health': 98,
            'weapons': ['Plasma gun', 'Grenades', 'Bloody big knife'],
            'Symbols on tattoo': 'ये बेवकूफी भरे पत्र अलविश जैसे हैं'}

    write_data_to_yaml(data, output_file)


if __name__ == "__main__":
    main()
