import re

path = "/Users/oicoko/workspace/pycharm/scavenger/chore/a_副本.txt"


if __name__ == '__main__':
    items = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pk = re.findall(r'documentPrimaryField":"(.+?)",', line)
            items.append("'{}'".format(pk[0]))
    print('select * from ea_document_attachment WHERE other_system_id in ({});'.format(','.join(items)))

