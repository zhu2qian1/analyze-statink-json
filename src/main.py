import json
from DictTransferrer import DictTransferrer
from Constants import Constants
from pprint import pprint


def main():
    stats = load_stat()

    # TODO
    extracted_list = [extract_wkeys(stat, Constants.default_sr_keys) for stat in stats]
    ids = find_most_golden_eggs(extracted_list)
    records = [rec for rec in extracted_list if rec["id"] in ids]
    for record in records:
        pprint(record, indent=1, width=140, compact=True)
        print()


def find_most_golden_eggs(list: list[dict]):
    max = 0
    ids = []
    for i in list:
        ge = i["golden_eggs"]
        if ge > max:
            max = ge
            ids.clear()
            ids = [i["id"]]
        elif ge == max:
            ids.append(i["id"])
    return ids


def extract_wkeys(src_dict: dict, keys: tuple[str]) -> dict:
    ret = {}
    df = DictTransferrer(ret, src_dict)
    df.transfer(*keys)
    return ret


def load_stat() -> list | dict:
    ls = None
    with open(Constants.json_path, "r") as f:
        ls = json.load(f)
    return ls


if __name__ == "__main__":
    main()
