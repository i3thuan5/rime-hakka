import json


def main():
    with open('wip.json') as 檔:
        資料 = sorted(json.load(檔), key=lambda pit: int(pit['檔名'][7:-5]))
    with open('wip2.json', 'wt') as tong:
        json.dump(資料, tong, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == '__main__':
    main()
