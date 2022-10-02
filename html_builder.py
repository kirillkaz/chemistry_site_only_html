def make_main_html(mendeleev_tablet):
    html_str = '<!DOCTYPE html>\n<html>'
    html_str += '\t<body bgcolor=#f7f7f7>\n'

    # блок меню
    html_str += '\t\t<fieldset>\n' \
                '\t\t\t<legend><font size=32><b>Меню</b></font></legend>\n' \
                '\t\t\t<a href=tablet.html><font size=14>Таблица химических элементов</font></a>' \
                '\t\t</fieldset>\n\n'
    # блок галерея
    html_str += f'\t\t<fieldset>\n' \
                f'\t\t\t<legend><font size=32><b>Галерея</b></font></legend>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[2].lat_name}.html><img src={mendeleev_tablet[2].img} width=220 heigth=220></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[4].lat_name}.html><img src={mendeleev_tablet[4].img} width=200 heigth=200></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[6].lat_name}.html><img src={mendeleev_tablet[6].img} width=165 heigth=165></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[8].lat_name}.html><img src={mendeleev_tablet[8].img} width=200 heigth=200></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[12].lat_name}.html><img src={mendeleev_tablet[12].img} width=163 heigth=163></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[16].lat_name}.html><img src={mendeleev_tablet[16].img} width=167 heigth=167></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[17].lat_name}.html><img src={mendeleev_tablet[17].img} width=178 heigth=178></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[7].lat_name}.html><img src={mendeleev_tablet[7].img} width=230 heigth=230></a>\n' \
                f'\t\t\t<a href=elements_pages/{mendeleev_tablet[13].lat_name}.html><img src={mendeleev_tablet[13].img} width=236 heigth=236></a>\n' \
                f'\t\t</fieldset>\n\n'

    # блок описания
    opisanie = 'Хими́ческий элеме́нт — совокупность атомов[K 1][K 2] с одинаковым зарядом атомных ядер. Атомное ядро состоит из протонов, число которых равно атомному номеру элемента, и нейтронов, число которых может быть различным. Каждый химический элемент имеет своё латинское название и химический символ, состоящий из одной или пары латинских букв, регламентированные ИЮПАК и приводятся, в частности, в таблице Периодической системы элементов Менделеева. ' \
               ' Формой существования химических элементов в свободном виде являются простые вещества (одноэлементные). Необходимо различать химические элементы — виртуальные абстрактные объекты, созданные путём логического обобщения эмпирических данных и описываемые через свои специфические характеристики, и соответствующие им материальные объекты — простые вещества, обладающие определёнными физико-химическими свойствами.' \
               ' По состоянию на 2016 год известно 118 химических элементов. 94 из них встречаются в природе (некоторые лишь в микроколичествах), а остальные 24 искусственно синтезированы.'
    html_str += '\t\t<fieldset>\n' \
                '\t\t\t<legend><font size=32><b>Описание</b></font></legend>\n' \
                f'\t\t\t<p align=justify>{opisanie}</p>' \
                '</fieldset>\n\n'
    html_str += '\t\t<br>\n'
    html_str += f'\t\t<details><summary><font size = 14>Список химических элементов</font></summary>\n'
    html_str += f'\t\t<ol>\n'
    for i in mendeleev_tablet:
        html_str += f'\t\t<li>\n'

        # название элемента
        html_str += f'\t\t\t<font size=14><b>{i.name}</b></font>\n'
        html_str += f'\t\t\t<br>\n'

        # картинка к элементу
        if 'https' not in i.img:
            html_str += f'\t\t\t<a href=elements_pages/{i.lat_name}.html>{i.img}</a><br><br>\n'
        else:
            html_str += f'\t\t\t<a href=elements_pages/{i.lat_name}.html><img src={i.img}></a>\n'

        # таблица с инфой
        html_str += f'\t\t\t<table border=1>\n'
        html_str += f'\t\t\t\t<tr>\n' \
                    f'\t\t\t\t\t<th>№</th>\n' \
                    f'\t\t\t\t\t<th>Название</th>\n' \
                    f'\t\t\t\t\t<th>Символ</th>\n' \
                    f'\t\t\t\t\t<th>Латинское название</th>\n' \
                    f'\t\t\t\t\t<th>Период</th>\n' \
                    f'\t\t\t\t\t<th>Группа</th>\n' \
                    f'\t\t\t\t\t<th>Атомная масса</th>\n' \
                    f'\t\t\t\t\t<th>Плотность</th>\n' \
                    f'\t\t\t\t\t<th>Температура плавления</th>\n' \
                    f'\t\t\t\t\t<th>Температура кипения</th>\n' \
                    f'\t\t\t\t</tr>\n'

        html_str += f'\t\t\t\t<tr>\n' \
                    f'\t\t\t\t\t<td>{i.num}</td>\n' \
                    f'\t\t\t\t\t<td>{i.name}</td>\n' \
                    f'\t\t\t\t\t<td>{i.simv}</td>\n' \
                    f'\t\t\t\t\t<td>{i.lat_name}</td>\n' \
                    f'\t\t\t\t\t<td>{i.period}</td>\n' \
                    f'\t\t\t\t\t<td>{i.group}</td>\n' \
                    f'\t\t\t\t\t<td>{i.mass}</td>\n' \
                    f'\t\t\t\t\t<td>{i.density}</td>\n' \
                    f'\t\t\t\t\t<td>{i.melting_temp}</td>\n' \
                    f'\t\t\t\t\t<td>{i.boiling_temp}</td>\n' \
                    f'\t\t\t\t</tr>\n'

        html_str += f'\t\t\t</table>\n'

        html_str += f'\t\t</li>\n\n'
        html_str += f'\t\t<hr>\n\n'
    html_str += f'\t\t</ol>'
    html_str += f'\t\t</details>\n'
    html_str += '\t</body>\n'
    html_str += '</html>'

    with open('main.html', 'w') as file:
        file.write(html_str)


def make_element_page(elem):
    html_str = '<!DOCTYPE html>\n<html>\n'

    html_str += '\t<head>\n'
    html_str += f'\t\t<title>{elem.name}</title>\n'
    html_str += '\t</head>\n'

    html_str += '\t<body bgcolor=#F7F7F7>\n'

    html_str += '\t\t<a href=../main.html><img src=../home.png width=40 height=40></a>\n'

    html_str += f'\t\t<h1 align=center>{elem.name}</h1>\n'

    html_str += f'\t\t\t<table bgcolor=#61FAAB align=center cellpadding=4>\n' \
                f'\t\t\t\t<tr>\n' \
                f'\t\t\t\t\t<td><b>{elem.num}</b></td>' \
                f'\t\t\t\t\t<td><b>{elem.name}</b></td>' \
                f'\t\t\t\t</tr>\n' \
                f'\t\t\t\t<tr>\n' \
                f'\t\t\t\t\t<td colspan=2 align=center><font size=10><b>{elem.simv}</b></font></td>\n' \
                f'\t\t\t\t</tr>\n' \
                f'\t\t\t</table>\n\n'

    html_str += f'\t\t\t<p align=justify>\n' \
                f'\t\t\t\t{elem.comment}\n' \
                f'\t\t\t</p>\n'
    html_str += '\t</body>\n'
    html_str += '</html>'

    with open(f'elements_pages/{elem.lat_name}.html', 'w') as file:
        file.write(html_str)


def make_tablet_page(mendeleev_tablet):
    html_str = '<!DOCTYPE html>\n<html>\n'
    html_str += '\t<body bgcolor=#F7F7F7>\n'

    html_str += '\t\t<a href=main.html><img src=home.png width=40 height=40></a>\n'

    #форма
    html_str += f'\t\t<form>\n'
    html_str += f'\t\t\t<label>Минимальная атомная масса: <input value=0 type=number></label>\n'
    html_str += f'\t\t\t<br>\n'
    html_str += f'\t\t\t<label>Максимальная атомная масса: <input value=300 type=number></label>\n'

    html_str += f'\t\t\t<p>\n'
    html_str += f'\t\t\t\t<b>Отображаемые элементы:</b><br>\n'
    html_str += f'\t\t\t\t<select>\n' \
                f'\t\t\t\t\t<option>Все элементы</option>\n' \
                f'\t\t\t\t\t<option>Элементы с полными данными</option>\n' \
                f'\t\t\t\t</select>\n'
    html_str += f'\t\t\t</p>\n'

    html_str += f'\t\t\t<p>\n'
    html_str += f'\t\t\tСортировать элементы по:<br>\n'
    html_str += f'\t\t\t<input id="number" type=radio name="sort_table" value="number">\n' \
                f'\t\t\t<label for="number">Номеру</label><br>\n' \
                f'\t\t\t<input id="name" type=radio name="sort_table" value="name">\n' \
                f'\t\t\t<label for="name">Имени</label><br>\n' \
                f'\t\t\t<input id="period" type=radio name="sort_table" value="period">\n' \
                f'\t\t\t<label for="period">Периоду</label><br>\n' \
                f'\t\t\t<input id="group" type=radio name="sort_table" value="group">\n' \
                f'\t\t\t<label for="group">Группе</label><br>\n' \
                f'\t\t\t<input id="atom_mass" type=radio name="sort_table" value="atom_mass">\n' \
                f'\t\t\t<label for="atom_mass">Атомной массе</label><br>\n' \
                f'\t\t\t<input id="density" type=radio name="sort_table" value="density">\n' \
                f'\t\t\t<label for="density">Плотности</label><br>\n' \
                f'\t\t\t<input id="melting_temp" type=radio name="sort_table" value="melting_temp">\n' \
                f'\t\t\t<label for="melting_temp">Температуре плавления</label><br>\n' \
                f'\t\t\t<input id="boiling_temp" type=radio name="sort_table" value="boiling_temp">\n' \
                f'\t\t\t<label for="boiling_temp">Температуре кипения</label>\n'
    html_str += f'\t\t\t</p>\n'
    html_str += f'\t\t</form>\n\n'

    html_str += f'\t\t<br>\n'

    #таблица
    html_str += f'\t\t<table border=1 width=100%>\n'
    html_str += f'\t\t\t<tr>\n' \
                f'\t\t\t\t<th>№</th>\n' \
                f'\t\t\t\t<th>Название</th>\n' \
                f'\t\t\t\t<th>Символ</th>\n' \
                f'\t\t\t\t<th>Латинское название</th>\n' \
                f'\t\t\t\t<th>Период</th>\n' \
                f'\t\t\t\t<th>Группа</th>\n' \
                f'\t\t\t\t<th>Атомная масса</th>\n' \
                f'\t\t\t\t<th>Плотность</th>\n' \
                f'\t\t\t\t<th>Температура плавления</th>\n' \
                f'\t\t\t\t<th>Температура кипения</th>\n' \
                f'\t\t\t</tr>\n'

    for i in mendeleev_tablet:
        html_str += f'\t\t\t<tr>\n'
        if i.num != 'None':
            html_str += f'\t\t\t\t<td>{i.num}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.name != 'None':
            html_str += f'\t\t\t\t<td>{i.name}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.simv != 'None':
            html_str += f'\t\t\t\t<td>{i.simv}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.lat_name != 'None':
            html_str += f'\t\t\t\t<td>{i.lat_name}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.period != 'None':
            html_str += f'\t\t\t\t<td>{i.period}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.group != 'None':
            html_str += f'\t\t\t\t<td>{i.group}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.mass != 'None':
            html_str += f'\t\t\t\t<td>{i.mass}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.density != 'None':
            html_str += f'\t\t\t\t<td>{i.density}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.melting_temp != 'None':
            html_str += f'\t\t\t\t<td>{i.melting_temp}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        if i.boiling_temp != 'None':
            html_str += f'\t\t\t\t<td>{i.boiling_temp}</td>\n'
        else:
            html_str += f'\t\t\t\t<td></td>\n'

        html_str += f'\t\t\t</tr>\n'

    html_str += '\t\t</table>\n'

    html_str += '\t</body>\n'
    html_str += '</html>'

    with open('tablet.html', 'w') as file:
        file.write(html_str)
