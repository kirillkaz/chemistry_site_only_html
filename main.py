import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Pool
from html_builder import make_main_html, make_element_page


class chem_elem():
    def __init__(self, num: int = None, name: str = None, simv: str = None, lat_name: str = None, period: int = None, group: int = None,
                 mass: float = None, density: float = None, melting_temp: float = None, boiling_temp: float = None, img: str = None, comment: str = None):
        self.num = num
        self.name = name
        self.simv = simv
        self.lat_name = lat_name
        self.period = period
        self.group = group
        self.mass = mass
        self.density = density
        self.melting_temp = melting_temp
        self.boiling_temp = boiling_temp
        self.img = img
        self.comment = comment

    def print_elem(self):
        print(self.num)
        print(self.name)
        print(self.simv)
        print(self.lat_name)
        print(self.period)
        print(self.group)
        print(self.mass)
        print(self.density)
        print(self.melting_temp)
        print(self.boiling_temp)
        print(self.img)
        print(self.comment)

    def get_string_elem_data(self) -> str:
        stroke = ''
        stroke+= f'{self.num}|{self.name}|{self.simv}|{self.lat_name}|{self.period}' \
                 f'|{self.group}|{self.mass}|{self.density}|{self.melting_temp}|{self.boiling_temp}|{self.img}|{self.comment}\n'
        return stroke


def fill_data_page_file(url: str, headers: dict, filename: str):
    """write html from url to your file"""
    req = requests.get(url=url, headers=headers)
    with open(f'{filename}', 'w') as file:
        file.write(req.text)


def get_image(url: str, headers: dict) -> str:
    """get link to img from url"""
    req = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(req.text, 'lxml')
    table = soup.find(attrs={'data-name': 'Химический элемент'})

    soup = BeautifulSoup(str(table), 'lxml')
    img_block = soup.find(class_='plainlist')

    soup = BeautifulSoup(str(img_block), 'lxml')
    img = soup.find('img')
    result = ''
    if img == None:
        result = soup.text.strip()
    else:
        result = f'https://{img["src"]}'

    return result


def get_comment(url: str, headers: dict) -> str:
    req = requests.get(url=url, headers=headers)
    src = req.text
    try:
        src = req.text[0:req.text.index('<div style="clear:left;">')]
    except Exception as ex:
        print(ex)

    soup = BeautifulSoup(src, 'lxml')

    comment_text = soup.find_all('p')
    result = ''

    for i in comment_text:
        stroke = i.text.strip().replace("\n","")
        result+= f'{stroke}'
    print(result)
    return result


def parce_data_from_strokes(strokes: list) -> chem_elem:
    """parce data from arr of strokes about chem_elem from str format to chem_elem"""
    elem = chem_elem()
    if strokes[0].text != '':
        elem.num = strokes[0].text.strip()

    if strokes[1].text != '':
        elem.name = strokes[1].text.strip()

    if strokes[2].text != '':
        elem.simv = strokes[2].text.strip()

    if strokes[3].text != '':
        elem.lat_name = strokes[3].text.strip()

    if strokes[4].text.strip() != '':
        period_group = strokes[4].text.split(', ')
        elem.period = int(period_group[0].strip())
        if len(period_group) == 2:
            elem.group = int(period_group[1].strip())

    if strokes[5].text.strip() != '':
        stroke = strokes[5].text
        if '(' in strokes[5].text:
            stroke = strokes[5].text[0:strokes[5].text.index('(')]
        elif strokes[5].text[0] == '[':
            stroke = strokes[5].text[1:strokes[5].text.index(']')]
        elem.mass = float(stroke.replace(',', '.').strip())

    if strokes[6].text.strip() != '':
        stroke = strokes[6].text
        if 'г/л' in strokes[6].text:
            stroke = strokes[6].text[0:strokes[6].text.index('г')]
        elem.density = float(stroke.replace(',', '.').strip())

    if strokes[7].text.strip() != '':
        stroke = strokes[7].text
        if '(' in strokes[7].text:
            stroke = strokes[7].text[0:strokes[7].text.index('(')]
        elem.melting_temp = float(stroke.replace(',', '.').strip())

    if strokes[8].text.strip() != '':
        stroke = strokes[8].text
        if '(' in strokes[8].text:
            stroke = strokes[8].text[0:strokes[8].text.index('(')]
        elem.boiling_temp = float(stroke.replace(',', '.').strip())
    return elem


def process(table):
    """filling file with chemistry elements in file in multiprocessing mode"""
    elem = chem_elem()
    elem_soup = BeautifulSoup(str(table), 'lxml')
    strokes = elem_soup.find_all('td')

    link = f"https://ru.wikipedia.org{BeautifulSoup(str(strokes[1]), 'lxml').find('a')['href']}"

    elem = parce_data_from_strokes(strokes=strokes)

    elem.img = get_image(url=link, headers=headers)

    elem.comment = get_comment(url=link, headers=headers)
    with open('mendeleev_table_file.txt', 'a') as file:
        file.write(f'{elem.get_string_elem_data()}')

    print(f'{elem.name} обработан. Номер элемента: {elem.num}')


def parce_file_with_elements(filename: str) -> list:
    str_file = ''
    with open(f'{filename}', 'r') as file:
        str_file = file.read()

    str_elements = str_file.split('\n')

    elems_arr = []

    for i in str_elements:
        elem_info = i.split('|')
        elem = chem_elem()
        elem.num = elem_info[0]
        elem.name = elem_info[1]
        elem.simv = elem_info[2]
        elem.lat_name = elem_info[3]
        elem.period = elem_info[4]
        elem.group = elem_info[5]
        elem.mass = elem_info[6]
        elem.density = elem_info[7]
        elem.melting_temp = elem_info[8]
        elem.boiling_temp = elem_info[9]
        elem.img = elem_info[10]
        elem.comment = elem_info[11]
        elems_arr.append(elem)
    return elems_arr


def main():
    url = 'https://ru.wikipedia.org/wiki/Список_химических_элементов'
    headers = {
        'Accept': 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.2.0"',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }
    req = requests.get(url=url, headers=headers)

    #запись
    fill_data_page_file(url=url, headers=headers, filename='data_page.txt')

    soup = BeautifulSoup(req.text, 'lxml')
    table = soup.find(class_='wikitable sortable')
    soup = BeautifulSoup(str(table), 'lxml')
    table = soup.find_all('tr')

    processes = []

    for i in range(1, len(table)):
        p = Process(target=process, args=(table[i],))
        processes.append(p)

    for i in processes:
        i.start()

    for i in processes:
        i.join()


if __name__ == '__main__':
    headers = {
        'Accept': 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.2.0"',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }
    # main()
    mendeleev_tablet = parce_file_with_elements('mendeleev_table_file.txt')
    mendeleev_tablet.sort(key=lambda x: int(x.num))

    make_main_html(mendeleev_tablet=mendeleev_tablet)
    for i in mendeleev_tablet:
        make_element_page(i)
