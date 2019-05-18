import json


def main():
    #
    # 程式頭
    #
    with open('hakka.dict.yaml', 'w', encoding='utf-8') as f:
        # 輸出字典踏話頭
        print(dict_header, file=f)
        # 印教典詞
        supio, tsuanpoo_lo = 提教典表()
        # 印傳統調號的羅馬字音節表
        for im in sorted(tsuanpoo_lo):
                # 一般
            print('{}\t{}\t10%'.format(im, im), file=f)
        for han, lo in sorted(supio, key=lambda tup: (tup[1], tup[0])):
            print('{}\t{}'.format(han, lo), file=f)


def 提教典表():
    with open('wip.json') as 檔:
        資料 = json.load(檔)
#     with open('wip2.json','wt') as tong:
#         json.dump(資料,tong,ensure_ascii=False,sort_keys=True,indent=2)
    tsuanpoo_lo = set()
    supio = set()
    for pit in 資料:
        try:
            han, lo = theh(pit)
            for l in lo.split():
                tsuanpoo_lo.add(l)
            supio.add((han, lo))
        except ValueError:
            pass
    return supio, tsuanpoo_lo


def theh(pit):
    try:
        han = pit['詞目'].strip().lstrip('【').rstrip('】')
        lo = pit['四縣音'].strip().split('）')[-1]
    except KeyError:
        raise ValueError('無資料！')
    return han, lo


dict_header = '''# Rime dictionary
# encoding: utf-8

---
name: hakka-xi-ien
version: "0.1"
sort: by_weight
use_preset_vocabulary: false
...'''

if __name__ == '__main__':
    main()
