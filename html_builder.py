def make_main_html(mendeleev_tablet):
    html_str = '<!DOCTYPE html>\n<html>'
    html_str += '\t<body>\n'
    for i in mendeleev_tablet:
        html_str += f'\t\t<p>\n'

        # название элемента
        html_str += f'\t\t\t<h3>{i.name}</h3>\n'
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

        html_str += f'\t\t</p>\n\n'
        html_str += f'\t\t<hr>\n\n'
    html_str += '\t</body>\n'
    html_str += '</html>'

    with open('main.html', 'w') as file:
        file.write(html_str)


def make_element_page(elem):
    html_str = '<!DOCTYPE html>\n<html>\n'

    html_str += '\t<head>\n'
    html_str += f'\t\t<title>{elem.name}</title>\n'
    html_str += '\t</head>\n'

    html_str += '\t<body>\n'

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
