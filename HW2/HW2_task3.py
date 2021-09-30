import zipfile, os
with zipfile.ZipFile('main.zip', 'r') as zip:
    zip.extractall()

answer_list = []
with open('answer3', 'w') as answer:
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                answer_list.append(current_dir)
                break  # перейдем к след. директории
    answer_list = sorted(answer_list)
    answer.write('\n'.join(answer_list))
