from typing import List
from time import sleep
import os
import signal
import pyperclip


def main():
    print('Enter q to quit\n----')
    while True:
        raw_data: str = input('Paste data separated by spaces\n> ')
        if raw_data == 'q':
            print('Adiós')
            sleep(0.25)
            try:
                os.kill(os.getppid(), signal.SIGHUP)
            except:
                print('err')
            break
        formatted_list: str = list_to_string(raw_to_list(raw_data))
        try:
            pyperclip.copy(formatted_list)
            print('Data copied to clipboard.')
        except:
            print('Could not copy to clipboard.')
        print(formatted_list)
        print()


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
