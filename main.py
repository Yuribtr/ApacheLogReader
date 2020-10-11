import csv
import tqdm as tqdm
import glob


def get_top_ips(items, max_qty=10):
    result = {}
    # join all words in dict, where word is a key, and count is a value
    for item in items:
        result[item['ip']] = result.get(item['ip'], 0) + 1
    # making two-dimensional array from dict
    result = [[x, y] for x, y in result.items()]
    # sorting in reverse order by second element (prev value) and cut first 10 elements
    result = sorted(result, key=lambda x: x[1], reverse=True)[:(max_qty + 1)]
    return result


def get_user_agents(items, ip: str):
    result = {}
    for item in items:
        if item['ip'] == ip:
            result[item['user-agent']] = result.get(item['user-agent'], 0) + 1
    result = [[x, y] for x, y in result.items()]
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result


files_list = []
for file in glob.glob("*access.log*"):
    files_list.append(file)

log = []
print(f'Loading file "{files_list[0]}". Please wait...')
with open(files_list[0]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    for row in tqdm.tqdm(csv_reader):
        tmp_url = row[5].split()
        try:
            log += [{'ip': row[0],
                     'datetime': row[3][1:] + row[4][:-1],
                     'method': tmp_url[0],
                     'url': tmp_url[1],
                     'protocol': tmp_url[2],
                     'code': row[6],
                     'size': row[7],
                     'referrer': row[8],
                     'user-agent': row[9],

                     }]
        except IndexError:
            pass
print('We found these IP\'s:')
print(*get_top_ips(log, 50), sep='\n')
print()
while True:
    ip = input('Pls input IP to analyze or press "q" to exit: ')
    if ip == 'q':
        break
    print(*get_user_agents(log, ip), sep='\n')
    print()
