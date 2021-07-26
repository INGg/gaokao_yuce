import requests
import re
import time
import os
import pprint


def get_html(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        'Connection': 'close'
    }

    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    time.sleep(5)
    return r.text


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'w', encoding='GBK')
    # for i in range(len(data)):
    #     s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
    #     s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
    file.write(str(data))
    file.close()
    print("保存文件成功")


def get_majon():
    data = {
        '本科': {},
        '专科': {}
    }

    url = "https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=1&level2=&page=" + "{}" + "&signsafe=&size=30&sort=&uri=apidata/api/gkv3/special/lists"

    for _ in range(1, 26): # 一共25页
        url_page = url.format(_)

        flag = False

        while not flag:

            h5 = eval(get_html(url_page))  # 获取每一页的信息

            if h5['code'] != '0000' and h5['message'] != '成功':
                print("被限制，现在是{}，休息2min".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())))
                continue
            else:
                print("正在爬取第{}页".format(_))

            h5 = h5['data']['item']

            for i in range(len(h5)):
                major = h5[i]

                #  每个分类如果存在就用，不存在就创建

                level2_name = major['level2_name']  # 一级学科
                level3_name = major['level3_name']  # 二级学科
                major_name = major['name']  # 专业名称
                limit_year = major['limit_year']  # 修读年限
                code = major['spcode']  # 专业代码
                view = major['view_total']  # 浏览量
                degree = major['degree']  # 授予学位

                if major['level1_name'] == '本科':
                    if not data['本科'].get(level2_name, False):
                        data['本科'][level2_name] = {}
                    if not data['本科'][level2_name].get(level3_name, False):
                        data['本科'][level2_name][level3_name] = []
                    data['本科'][level2_name][level3_name].append(
                        {
                            '专业名称' : major_name,
                            '专业代码' : code,
                            '修读年限' : limit_year,
                            '授予学位' : degree,
                            'view' : view
                        }
                    )
                else:
                    if not data['专科'].get(level2_name, False):
                        data['专科'][level2_name] = {}
                    if not data['专科'][level2_name].get(level3_name, False):
                        data['专科'][level2_name][level3_name] = []
                    data['专科'][level2_name][level3_name].append(
                        {
                            '专业名称': major_name,
                            '专业代码': code,
                            '修读年限': limit_year,
                            '授予学位': degree,
                            'view': view
                        }
                    )

            flag = True


    print("\n\n\n\n\n ----------------- \n\n\n\n\n")

    pprint.pprint(data)

    text_save("专业.txt", data)



if __name__ == '__main__':
    get_majon()
    file = open("专业.txt", 'r', encoding='GBK')
    data = eval(file.read())
    pprint.pprint(data['本科'].keys())