from simple_elastic import ElasticIndex
from collections import Counter
from multiprocessing import Pool
import re
import json

if __name__ == '__main__':
    url_counter = Counter()
    domain_counter = Counter()
    counter = Counter()
    hold = Counter()
    copy = Counter()

    index = ElasticIndex('swissbib-*', 'logs')

    query = {
        '_source': ['search_params.trackurl'],
        'query': {
            'exists': {
                'field': 'search_params.trackurl'
            }
        }
    }

    with open('common-urls.json', 'r') as fp:
        common_urls = json.load(fp)

    pool = Pool(processes=4)
    process_results = list()
    for results in index.scroll(query=query, size=10000):

        for item in results:
            url = item['search_params']['trackurl']
            if not isinstance(url, str):
                print('NO STRING: ', url)
                continue

            url_counter[url] += 1

            if url in common_urls:
                continue

            domain = re.match('http[s]://(www\.)?(.*\.[a-z]{2,3})/(.*)', url)

            if domain:
                domain_counter[domain.group(2)] += 1

            match_hold = re.match('/Record/(.*)/Hold', url)
            match_copy = re.match('/Record/(.*)/Copy', url)
            if match_hold:
                counter['hold-requests'] += 1
                hold[match_hold.group(1)] += 1
            elif match_copy:
                counter['copy-requests'] += 1
                copy[match_copy.group(1)] += 1
            elif not url.startswith('http'):
                counter['none-http'] += 1
            elif re.search('nebis', url):
                counter['nebis'] += 1
            elif re.search('ub\.unibas', url):
                counter['ub.unibas'] += 1
            elif re.search('aleph\.unibas', url):
                counter['aleph-unibas'] += 1
            elif re.search('baselbern\.swissbib\.ch', url):
                counter['bb'] += 1
            elif re.search('sfx', url):
                counter['sfx'] += 1
            elif re.search('d-nb\.info', url):
                counter['dnb-content'] += 1
            elif re.search('unibe', url):
                counter['unibe'] += 1
            elif re.search('rero', url):
                counter['rero'] += 1
            elif re.search('unisg', url):
                counter['unisg'] += 1
            elif re.search('unibas\.summon\.serialssolutions', url):
                counter['summons'] += 1
            elif re.search('helveticat', url):
                counter['helveticat'] += 1
            elif re.search('degruyter', url):
                counter['de-gruyter'] += 1
            elif re.search('renouvaud', url):
                counter['renouvaud'] += 1
            elif re.search('safaribooks', url):
                counter['safari-books'] += 1
            elif re.search('zora\.uzh', url):
                counter['zora-uzh'] += 1
            elif re.search('edoc\.unibas\.ch', url):
                counter['edoc-unibas'] += 1
            elif re.search('unine', url):
                counter['unine'] += 1
            elif re.search('unilu', url):
                counter['unilu'] += 1
            elif re.search('link\.springer', url):
                counter['springer'] += 1
            elif re.search('aleph', url):
                counter['other-aleph'] += 1
            elif re.search('doi', url):
                counter['doi'] += 1
            elif re.search('elsevier', url):
                counter['elsevier'] += 1
            elif re.search('iluplus', url):
                counter['iluplus'] += 1
            elif re.search('wiley', url):
                counter['wiley'] += 1
            elif re.search('login\.eduid', url):
                counter['login'] += 1
            elif re.search('e-periodica', url):
                counter['e-periodica'] += 1
            else:
                counter['else'] += 1
                print(url)

    common_urls = dict()
    for url, count in url_counter.items():
        if count >= 100:
            common_urls[url] = count

    with open('common-urls.json', 'w') as fp:
        json.dump(common_urls, fp, ensure_ascii=False, indent=4)

    common_domains = dict()
    for url, count in domain_counter.items():
        if count >= 10:
            common_domains[url] = count

    with open('common-domains.json', 'w') as fp:
        json.dump(common_domains, fp, ensure_ascii=False, indent=4)

    print('Hold Requests')
    for key, count in hold.items():
        if count > 5:
            print(key, count)

    print('Copy Requests')
    for key, count in copy.items():
        if count > 5:
            print(key, count)

    for c in counter.items():
        print(c)

    print('Total: ', sum(counter.values()))