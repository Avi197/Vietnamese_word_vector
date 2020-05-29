
from Word_vector_github import file_path
import jsonlines

input = 'vnn'
output = input + '_data'

count = 0
with jsonlines.open(input + '.json') as file:
    with open(output, 'w', encoding='utf-8') as out:
        for obj in file:
            out.write(obj['title'] + '\n')
            out.write(obj['lead'] + '\n')
            for paragraph in obj['content']:
                out.write(paragraph + '\n')
            print('done line {0}'.format(count))
            count += 1
