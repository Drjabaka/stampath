Скрипт собирает все папки и файлы, и сохраняет в csv файл.

```python
from stampath import stamp
path = '/usr'
csv_file = stamp.csv
stamp(path, csv_file)

# возвращает список файлов и папок
```
