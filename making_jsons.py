import json
import requests

urls = [
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=1',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=2',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=3',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=4',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=5',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=6',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=7',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=8',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=9',
    'https://rutube.ru/api/video/person/21014334/?client=wdp&origin__type=rtb,rst,ifrm,rspa&page=10',
]

for url in urls:
    response = requests.get(url)
    data = response.json()
    url_pos = urls.index(url) + 1
    with open(f'test_{url_pos}.json', 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
