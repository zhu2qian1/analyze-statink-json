import json
import yaml
from DictTransferrer import DictTransferrer
from Constants import Constants


def main():
    ls = None
    with open(Constants.json_path, "r") as f:
        ls = load_stat(f)

    # TODO
    extracted_list = [extract_info(d) for d in ls]
    ids = find_most_golden_eggs(extracted_list)
    records = [rec for rec in extracted_list if rec["id"] in ids]
    for record in records:
        print(record)
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


def extract_info(src_dict) -> dict:
    ret = {}
    df = DictTransferrer(ret, src_dict)
    df.transfer(
        "id",
        "url",
        "user",
        "stage",
        "danger_rate",
        "golden_eggs",
        "power_eggs",
        "waves",
        "start_at",
        "shift",
    )
    return ret


def load_stat(f) -> list | dict:
    return json.load(f)


if __name__ == "__main__":
    main()
