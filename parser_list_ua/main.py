import string
import re
import requests
from bs4 import BeautifulSoup
import json
import codecs


def added(dictionary, key, value):
    dictionary[key] = value


def convert_to_eng_name_day(name_day):
    if name_day == 'Пн':
        return "Mon"
    if name_day == 'Вт':
        return "Tue"
    if name_day == 'Ср':
        return "Wed"
    if name_day == 'Чт':
        return "Thu"
    if name_day == 'Пт':
        return "Fri"
    if name_day == 'Сб':
        return "Sat"
    if name_day == 'Нд':
        return "Sun"
    return ""


data = []
for x in range(9):
    with open('C:/Users/user1/Desktop/responses/response{}.html'.format(x+1), 'r', encoding='utf-8') as content_file:
        content = content_file.read()
        soup = BeautifulSoup(content, 'lxml')

        items_list = soup.find(id='itemsList')

        item_search_list = items_list.find_all(class_='item-search row js-load-business-container')

        for item_from_list in item_search_list:
            url_item_class = item_from_list.find(class_='item-search__title mobile-hide').find('a', href=True)['href']

            response = requests.get("https://list.in.ua{}".format(url_item_class))

            # response = requests.get('https://list.in.ua/%D0%A2%D0%9E%D0%92/44979/23-%D1%80%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD%D0%B8-%D0%86%D0%B2%D0%B0%D0%BD%D0%BE-%D0%A4%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA')
            business_content = BeautifulSoup(response.content, 'lxml')
            print(response.url)

            # NAME BUSINESS
            name_business = ''
            metas = business_content.find_all('meta')

            for tag in metas:
                if tag.get("property", None) == "og:title":
                    name_business = tag.get("content", None)
            print(name_business)
            if '23 ресторани' in name_business.strip():
                continue
            if name_business.strip() == 'Golden Time':
                pass
            dict_schedule = {}
            company__table_wrap = business_content.find(class_='company__table-wrap')

            if company__table_wrap is None:
                continue
            # print(company__table_wrap)
            tr_list_table_wrap = company__table_wrap.find_all('tr')

            start_index = 1
            if name_business == 'Golden Time':
                start_index = 2

            for tr_item in tr_list_table_wrap[1:]:
                td_list = tr_item.find_all('td')
                for day in td_list[0].getText().split(','):
                    converted_day = convert_to_eng_name_day(day)
                    # if name_business == 'Golden Time':
                        # print(td_list)

                    # print(len(td_list))
                    if len(td_list) == 3:
                        tuple_hour = (td_list[1].getText(), td_list[2].getText())
                        added(dict_schedule, converted_day, tuple_hour)
                    elif len(td_list) == 2:
                        tuple_hour = ("-", "Closed")
                        added(dict_schedule, converted_day, tuple_hour)

            # if dict_schedule:
                # for day_schedule in dict_schedule:
                    # print("{} ->>> {}".format(day_schedule, dict_schedule[day_schedule]))

            # print(company__table_wrap.find_all("tr") is None)
            # if company__table_wrap:
            #     print(len(company__table_wrap.find_all("tr")))
            # print(company__table_wrap.find_all("tr")[1:])

            # schedule_list = company__table_wrap.find_all("tr")

            # if len(schedule_list) > 0:
            #     # parse schedule
            #     for trtd in schedule_list:
            #         all_td = trtd.find_all('td')
            #
            #         if len(all_td) > 2:
            #             days = all_td[0].getText().split(',')
            #             work_hours = all_td[1].getText().strip()
            #             break_hours = all_td[2].getText()
            #
            #             for day in days:
            #                 converted_day = convert_to_eng_name_day(day)
            #                 tuple_hour = (work_hours, break_hours)
            #                 added(dict_schedule, converted_day, tuple_hour)
            #
            # parse phones
            phones = []
            company_phones = business_content.find(class_='company-phone icon icon-phone')

            if company_phones:
                for phone_item in company_phones:
                    phone_str = re.sub("\D", "", phone_item.getText().strip().replace(' ', ''))
                    if len(phone_str):
                        phones.append('+{}'.format(phone_str))

             # print(phones)

            address_all_div = business_content.find(class_="company-address icon icon-location").find_all('div')
            if address_all_div:
                address = address_all_div[1].getText().strip()
                if len(address_all_div) > 2:
                    address += address_all_div[2].getText().strip()

            social_class_container = business_content.find(class_='company__info__tabs-container')
            # print(social_class_container)
            socials = {}
            if social_class_container is not None:
                social_class_div = social_class_container.find_all('div')
                for social_class in social_class_div:
                    link = social_class.find('a', href=True)['href']

                    if 'facebook.com/' in link:
                        socials['facebook'] = link
                    elif '@' in link:
                        socials['mail'] = link
                    elif 'instagram.com' in link:
                        socials['instagram'] = link
                    else:
                        socials['www'] = link

            my_dict = {
                'name': name_business,
                'address': address,
                'schedule': dict_schedule,
                'phones': phones,
                'socials': socials
            }

            data.append(my_dict)

# WRITE TO FILE
my_json = json.dumps(data, ensure_ascii=False)
file = codecs.open("parsed_file", "a", "utf-8")
file.write(my_json)
file.close()

# coord
# coord = {}

# all_scripts = business_content.find_all('script')
# print(business_content)
# for script in all_scripts:
#     content_script = script.contents
#     print(response.url)
#     print(content_script)
#     for content in content_script:
#         if 'var lng' in content:
#             content_lines = content.split(';')
#             lat = re.findall("\d+\.\d+", content_lines[1])
#             lng = re.findall("\d+\.\d+", content_lines[2])
#             # print(response.url)
#             # print(content_lines[1], content_lines[2])
#             # print('lat={}'.format(lat[0]))
#             print('lng={}'.format(lng[0]))
#             coord['lat'] = lat[0]
#             coord['lng'] = lng[0]

# if len(social_class_container) > 0:
#

# for social_class in social_class_div:
#     print(social_class)

# print(len(item_search_list))
