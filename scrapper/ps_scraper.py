from bs4 import BeautifulSoup

def get_ele_data(column_name, key):
    if(column_name in ['KYC/Audit', 'Links', 'profile_link']):
        if(column_name=='KYC/Audit'):
            svg_group = key.find_all('svg')
            out = {
                'Doxx': False,
                'Safu': False,
                'KYC':  False,
                'Audit':False
            }
            for validity, ele in zip(out.keys(), svg_group):
                path = ele.find("path", {"d": "M699 353h-46.9c-10.2 0-19.9 4.9-25.9 13.3L469 584.3l-71.2-98.8c-6-8.3-15.6-13.3-25.9-13.3H325c-6.5 0-10.3 7.4-6.5 12.7l124.6 172.8a31.8 31.8 0 0 0 51.7 0l210.6-292c3.9-5.3.1-12.7-6.4-12.7z"})
                if(path!=None):
                    out[validity]=True
            return out
        elif(column_name=='Links'):
            a_group = key.find_all('a')
            out = {
                'website': None,
                'twitter': None,
                'telegram':None,
                'discord': None
            }
            platform_selector = {
                'website': b'<circle cx="12" cy="12" r="10"></circle><line x1="2" x2="22" y1="12" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>',
                'twitter': b'<path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>',
                'telegram':b'<path d="M446.7 98.6l-67.6 318.8c-5.1 22.5-18.4 28.1-37.3 17.5l-103-75.9-49.7 47.8c-5.5 5.5-10.1 10.1-20.7 10.1l7.4-104.9 190.9-172.5c8.3-7.4-1.8-11.5-12.9-4.1L117.8 284 16.2 252.2c-22.1-6.9-22.5-22.1 4.6-32.7L418.2 66.4c18.4-6.9 34.5 4.1 28.5 32.2z"></path>',
                'discord': b'<path d="M297.216 243.2c0 15.616-11.52 28.416-26.112 28.416-14.336 0-26.112-12.8-26.112-28.416s11.52-28.416 26.112-28.416c14.592 0 26.112 12.8 26.112 28.416zm-119.552-28.416c-14.592 0-26.112 12.8-26.112 28.416s11.776 28.416 26.112 28.416c14.592 0 26.112-12.8 26.112-28.416.256-15.616-11.52-28.416-26.112-28.416zM448 52.736V512c-64.494-56.994-43.868-38.128-118.784-107.776l13.568 47.36H52.48C23.552 451.584 0 428.032 0 398.848V52.736C0 23.552 23.552 0 52.48 0h343.04C424.448 0 448 23.552 448 52.736zm-72.96 242.688c0-82.432-36.864-149.248-36.864-149.248-36.864-27.648-71.936-26.88-71.936-26.88l-3.584 4.096c43.52 13.312 63.744 32.512 63.744 32.512-60.811-33.329-132.244-33.335-191.232-7.424-9.472 4.352-15.104 7.424-15.104 7.424s21.248-20.224 67.328-33.536l-2.56-3.072s-35.072-.768-71.936 26.88c0 0-36.864 66.816-36.864 149.248 0 0 21.504 37.12 78.08 38.912 0 0 9.472-11.52 17.152-21.248-32.512-9.728-44.8-30.208-44.8-30.208 3.766 2.636 9.976 6.053 10.496 6.4 43.21 24.198 104.588 32.126 159.744 8.96 8.96-3.328 18.944-8.192 29.44-15.104 0 0-12.8 20.992-46.336 30.464 7.68 9.728 16.896 20.736 16.896 20.736 56.576-1.792 78.336-38.912 78.336-38.912z"></path>'
            }
            for platform in out.keys():
                for ele in a_group:
                    svg_ele = ele.find('svg')
                    if(svg_ele.encode_contents()==platform_selector[platform]):
                        out[platform]=ele['href']
            return out
        elif(column_name=='profile_link'):
            # launchpad profile
            return 'https://www.pinksale.finance'+key.find('a')['href']
    return key.text

def get_tokens_data(table_data):
    soup = BeautifulSoup(table_data, 'html.parser')
    arr = soup.find_all('th')
    table_heading = []
    head_name_map = {}
    for i in range(len(arr)):
        if(arr[i].text==''):
            table_heading.append('profile_link')
            head_name_map['profile_link']=i
        else:
            table_heading.append(arr[i].text)
            head_name_map[arr[i].text]=i
    tokens_data = soup.find('tbody').find_all('tr')
    tokens_arr = []
    for single_token_data in tokens_data:
        values = single_token_data.find_all('td')
        token_data_arr = []
        token_dir = {}
        for key in table_heading:
            token_dir[key]=get_ele_data(key, values[head_name_map[key]])
        tokens_arr.append(token_dir)
    return tokens_arr
