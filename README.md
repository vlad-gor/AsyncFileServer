Выполнение тестового задания для DrWeb

"Хранилище файлов с доступом по http"  

Реализовать демон, который предоставит HTTP API для загрузки (upload) ,  
скачивания (download) и удаления файлов.  

Upload:  
- получив файл от клиента, демон возвращает в отдельном поле http  
response хэш загруженного файла  
- демон сохраняет файл на диск в следующую структуру каталогов:  
    store/ab/abcdef12345...  
где "abcdef12345..." - имя файла, совпадающее с его хэшем.  
/ab/ - подкаталог, состоящий из первых двух символов хэша файла.  
Алгоритм хэширования - на ваш выбор.  

Download:  
Запрос на скачивание: клиент передаёт параметр - хэш файла. Демон ищет  
файл в локальном хранилище и отдаёт его, если находит.  

Delete:  
Запрос на удаление: клиент передаёт параметр - хэш файла. Демон ищет  
файл в локальном хранилище и удаляет его, если находит.  

Результат работы должен быть в виде ссылки на git репозиторий с исходным  
кодом выполненного ТЗ.  

Примеры команд
для загрузки файла:
curl -F "file=@test.txt" http://127.0.0.1:8080/upload_file

для получения файла
curl -X GET http://127.0.0.1:8080/file/{idhash}

для удаления файла
curl -X DELETE http://127.0.0.1:8080/file/{idhash}

