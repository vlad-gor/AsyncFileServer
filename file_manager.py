import io
import os
import json
import hashlib

class FileManager():

    def __init__(self):
        pass
        

    async def upload_file(self, request):
        print('upload_file')
        data = await request.post()
        print(data)
        file_field = data["file"]
        file_ = file_field.file
        file_hash = hashlib.md5()
        file_block = file_.read(io.DEFAULT_BUFFER_SIZE)
        while len(file_block) > 0:
            file_hash.update(file_block)
            file_block = file_.read(io.DEFAULT_BUFFER_SIZE)
        hash_file = file_hash.hexdigest()
        result = {'filename': file_field.filename, 'hash': hash_file}
        rash = file_field.filename.split('.')[-1]

        file_.seek(0)
        
        with open(os.path.join('store/', f'{hash_file}.{rash}'), 'wb') as f:
            file_block = file_.read(io.DEFAULT_BUFFER_SIZE)
            while len(file_block) > 0:
                f.write(file_block)
                file_block = file_.read(io.DEFAULT_BUFFER_SIZE)

        return json.dumps(result)
    
    def download(self):
        print('Download file')

    def delete_file(self):
        print('Delete file')