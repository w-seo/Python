import os
import time
import requests

from bs4 import BeautifulSoup

def save_pdf(filename, pdf):
    # filenameは保存先のディレクトリ/保存するファイル名.pdf
    # pdfはレスポンスボディ
    with open(filename, "wb") as f: 
        f.write(pdf)

def create_filepath(url, path):
    # save_pdf()に与えるfilenameを作成する
    # pdfのファイル名はurlにあるpdfのファイル名を利用する（というかそのまんま）
    return path + url.split("/")[-1]

def download_pdf(pdf_url):
    # 個々のpdfのURLにリクエストしてレスポンスボディを返す
    # save_pdf()に与えるpdf
    res = requests.get(pdf_url)
    return res.content

def url_check(response):
    if "text/html" in response.headers["content-type"]:    
        html = response.text
        print("exist")

    return html

def url_connect(list_number, page_number):

    url = "対象のURL"

    response = requests.get(url)

    html = url_check(response)

    soup = BeautifulSoup(html, "html.parser")
    #beautifulsoupオブジェクトを生成
    #HTMLパーサーについて警告が出る場合は、第二引数にパーサーを指定する

    td = soup.find_all("td", class_="width_hs_pass") # tdタグでかつclassがwidth_hs_passのものをすべて抽出
    path = "対象の保存パス"

    return td, path

if __name__ == "__main__":

    list_number = 2
    page_number = 1

#     search_url = "絶対パスが必要場合"

    try :
        while(True):
            td, path = url_connect(list_number, page_number)

            if not os.path.isdir(path): # 保存先のディレクトリがなければディレクトリを作成
                os.mkdir(path)

            print(list_number, page_number)

            if len(td) <= 0:
                list_number += 1
                page_number = 1
                td, path = url_connect(list_number, page_number)

                # print(list_number, page_number)

            for link in td:

                report_url = link.a.get('href')

                trial_report_url = search_url + report_url
                # print(result_report_url)

                pdf = download_pdf(trial_report_url)
                filename = create_filepath(trial_report_url, path)
                save_pdf(filename, pdf)
                print("Downloaded: " + filename) # 保存できていることを確認するため、保存したfilenameを表示

                time.sleep(1) # アクセスの間隔が1秒空くようにする

            page_number += 1

    except Exception as e:
        print(e)
