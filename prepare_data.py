from conllu import parse
import pandas as pd

# Указываем пути к данным в формате conllu:
train_data_path = "data/raw_data/UD_Russian-SynTagRus/ru_syntagrus-ud-train.conllu"
dev_data_path = "data/raw_data/UD_Russian-SynTagRus/ru_syntagrus-ud-dev.conllu"
test_data_path = "data/raw_data/UD_Russian-SynTagRus/ru_syntagrus-ud-test.conllu"

# Читаем файлы и сравниваем объемы обучающего, валидационного и тестового датасетов
with open(train_data_path, encoding='utf-8') as file1:
    train_data = file1.read()

with open(dev_data_path, encoding='utf-8') as file2:
    dev_data = file2.read()
    
with open(test_data_path, encoding='utf-8') as file3:
    test_data = file3.read()

sentences_train = parse(train_data)
sentences_dev = parse(dev_data)
sentences_test = parse(test_data)
print('Предложений в обучающем датасете: ' + str(len(sentences_train)))
print('Предложений в валидационном датасете: ' + str(len(sentences_dev)))
print('Предложений в тестовом датасете: ' + str(len(sentences_test)))

# Приводим данные в удобный формат
def create_database(file, name):
    new_lines = []

    for i in file:
        for word in i:
            new_line = {}
            new_line['sent_id'] = i.metadata['sent_id']
            new_line['text'] = i.metadata['text']
            for key,value in word.items():
                new_line[key] = value
            new_lines.append(new_line)
    
    df = pd.DataFrame(new_lines)
    
    df.to_csv(f'{name}.csv', sep=',', index=False)

# Указываем новые названия датасетов
name_train = 'syntagrus_train_full_data'
name_dev = 'syntagrus_dev_full_data'
name_test = 'syntagrus_test_full_data'

create_database(sentences_train, name_train)
create_database(sentences_dev, name_dev)
create_database(sentences_test, name_test)

# Оставляем только необходимые данные о характеристиках слова
def prepare_for_train(file, name):
  full_data = pd.read_csv(f'{file}.csv')
  need_data = full_data[['form','lemma','upos','feats']]

  all_feat = []
  for index, row in need_data.iterrows():
      features = row[['lemma','upos','feats']].tolist()
      if type(features[2]) == str:
          all_feats = [i for i in eval(features[2]).values()]
          all_feats.insert(0, features[0])
          all_feats.insert(1, features[1])
          all_feat.append(','.join(all_feats))
      else:
          features[2] = 'None'
          all_feat.append(','.join(features))

  need_data['data'] = all_feat
  need_data = need_data[['form', 'data']]
  need_data.to_csv(f'{name}.csv', index=False)

# Указываем новые названия датасетов
name_train_2 = 'syntagrus_train_data'
name_dev_2 = 'syntagrus_dev_data'
name_test_2 = 'syntagrus_test_data'

prepare_for_train(name_train, name_train_2)
prepare_for_train(name_dev, name_dev_2)
prepare_for_train(name_test, name_test_2)
