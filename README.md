# Дипломная работа на тему: "От нейросетевого анализа к словарному: методы разработки морфологических анализаторов на основе данных, размеченных нейросетью"
## Diploma "From neural network analysis to word analysis: methods for developing morphological analysers based on neural network-marked data
### Автор: _Феоктистова Эмма Александровна, 4 курс ФиКЛ_
### Научный руководитель: _Проф. Ляшевская О. Н._
  
#### 1. Данные:
- Датасет GSD (_train_ - 74900 токенов, _val_ - 11710 токенов, _test_ - 11385 токенов)
- Датасет SynTagRus (_train_ - 1206300 токенов, _val_ - 153590 токенов, _test_ - 157990 токенов)
- Датасет Taiga (_train_ - 176630 токенов, _val_ - 10095 токенов, _test_ - 10275 токенов)

Исользуемые данные в папке `data\raw_data`, предобработанные данные в полном и в сокращенных форматах в папке `data\prepared_data`.

  Пример полного формата данных:  
<img src="./images/image_full_data.png" width="2500" height="250" />
  
  Пример сокращенного формата данных:  
<img src="./images/image_data.png" width="500" height="200" />
  
  Все данные находятся по ссылке: https://drive.google.com/drive/u/0/folders/1MFgqQ3WmkVTk22NmeOX1UYWjCvu0l3mL
  
#### 2. Кластеризация
Используемые методы кластеризации:
- K-means
- DBSCAN
- Agglomerative Clustering
- Naive Bayes
- Random Forest
