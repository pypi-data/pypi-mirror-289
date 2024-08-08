from typing import List, Tuple


def dict_num_zip(values: List[str], keys: Tuple):
    return {
        key: int(values[index].replace(',', ''))
        for index, key in enumerate(keys)
    }
