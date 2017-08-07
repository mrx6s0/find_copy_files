#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import re
import shutil
 
# função para encontrar os arquivos

def find_files(pattern, path):
    for path, dirs, files in os.walk(path):
        for filename in files:
            full_file_name = os.path.join(path, filename)
            match = re.match(pattern, full_file_name)
            if match:
                yield full_file_name

# função para copiar os arquivos encontrados
 
def copy_files(pattern, src_path, dest_path):
    for full_file_name in find_files(pattern, src_path):
        print(full_file_name)
 
        try:
            shutil.copy(full_file_name, dest_path)
        except IOError:
            pass
       
 
if __name__ == '__main__':

    copy_files('.', '/home', '/home/teste')
