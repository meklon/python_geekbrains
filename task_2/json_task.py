import json
import os


def write_order_to_json(item: str, quantity: int, price: float, buyer: str, date: str, output_file: str) -> None:
    order = {"item": item,
             "quantity": quantity,
             "price": price,
             "buyer": buyer,
             "date": date}

    with open(output_file, 'w') as file:
        json.dump(order, file, indent=4)


def check_mkdir_output_path(path_output: str) -> None:
    # Function checks if the output path exists and creates it if not
    if not os.path.exists(path_output):
        os.mkdir(path_output)


def main():
    check_mkdir_output_path('result/')
    output_file = 'result/orders.json'
    # Write some data
    write_order_to_json("GFD-14 Neurotoxin", 23, 599.99, "Andrew Wiggin", "2018-08-03T10:51:42", output_file)


if __name__ == "__main__":
    main()
