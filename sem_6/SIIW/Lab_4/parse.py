import os

DATA_PATH = './data'

output = ''
for name in os.listdir(DATA_PATH):
    vals = []
    file_path = DATA_PATH + '/' + name

    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        for file in files:
            with open(file_path + '/' + file) as f:
                vals.append(f.readlines())

    with open('./train/' + name + '.txt', 'a') as f:
        for record in zip(*vals):
            record_str = '\t'.join(map(lambda x: x.replace('\n', ''), record)) + '\n' 
            f.write(record_str)
            output += record_str

with open('./train_data.csv', 'w') as f:
    f.write(output)