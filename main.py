from typing import List
import pyperclip


def main():
    raw_data: str = input('Paste data separated by spaces\n> ')
    formatted_list: str = list_to_string(raw_to_list(raw_data))
    try:
        pyperclip.copy(formatted_list)
        print('Data copied to clipboard.')
    except:
        print('Could not copy to clipboard.')
    print(formatted_list)


def raw_to_list(raw_data: str) -> List[float]:
    data_as_strings: List[str] = raw_data.split()
    data_as_floats: List[float] = []
    for item in data_as_strings:
        data_as_floats.append(float(item))
    return data_as_floats


def list_to_string(data: List[float], separator: str = ';') -> str:
    output: str = '['
    for index, item in enumerate(data):
        output += f'{item}'
        if index != len(data) - 1:
            output += '; '
    output += ']'
    return output


if __name__ == '__main__':
    main()
