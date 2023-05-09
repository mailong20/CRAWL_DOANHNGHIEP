import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from threading import Thread

import schema
from models import CompanyInfo


def get_number_page(link):
    response = requests.get(link)
    # Kiểm tra xem yêu cầu có thành công hay không
    if response.status_code == 200:
        # Nếu thành công, phân tích nội dung HTML bằng BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        last_page = soup.find("li", class_="last-page")
        last_page_num = int(last_page.find('a').get(
            "href").split('/')[-2].replace('trang-', ''))
        return last_page_num

    else:
        # Nếu không thành công, hiển thị mã lỗi HTTP
        print("Yêu cầu thất bại với mã lỗi HTTP", response.status_code)
        return False


def crawl_data(data, thread_number):
    for url in tqdm(data, mininterval=3, desc=f'Crawl: {thread_number}'):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        company_names = soup.find_all("h3", class_="company-name")
        for company_name in company_names:
            link = company_name.find("a").get("href")
            if link is not None:
                # print(link)
                response_company = requests.get(link)
                if response_company.status_code == 200:
                    soup_company = BeautifulSoup(
                        response_company.content, "html.parser")
                    company_info = soup_company.find(
                        "div", class_="company-info")
                    # print(company_info)
                    div_infos = company_info.find_all("div", class_="row")
                    company_info_list = []
                    for div_info in div_infos:

                        name_info = div_info.find(
                            "div", class_='col-xs-12 col-md-3')
                        info = div_info.find(
                            "div", class_='col-xs-12 col-md-9')
                        try:
                            company_info_list.append(
                                (name_info.text.strip(), info.text.strip()))
                        except:
                            pass
                    if len(company_info_list) > 5:
                        try:
                            schema.add_full_page(
                                link, company_info_list=company_info_list)
                        except:
                            pass


def crawl_data_threading(link,  number_page=22, thread_number=5):
    links = [f'{link}trang-{i}/' for i in range(1, number_page+1)]
    chunk_size = len(links) // thread_number
    remainder = len(links) % thread_number
    data_chunks = []
    for i in range(thread_number - 1):
        data_chunks.append(links[i * chunk_size: (i + 1) * chunk_size])
    data_chunks.append(links[(thread_number-1) * chunk_size: (thread_number-1)
                             * chunk_size + chunk_size + remainder])
    ts = []
    thread_number = 0
    for data in data_chunks:
        thread_number += 1
        t = Thread(target=crawl_data, args=(data, thread_number))
        t.setDaemon = True
        ts.append(t)
    for t in ts:
        t.start()


if __name__ == '__main__':
    link = input("Nhập link thành phố: ")
    number_page = get_number_page(link)
    if int(number_page) > 0:
        crawl_data_threading(link, int(number_page), 2)
