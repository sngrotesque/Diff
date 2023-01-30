import hashlib
from os.path import exists
from os import stat

def sha256(data :object):
    hash = hashlib.sha256()
    hash.update(data)
    return hash.hexdigest()

def fread(fn :str):
    with open(fn, 'rb') as f:
        return f.read()

def diff(fn1 :str, fn2 :str) -> None:
    fn1 = fn1.strip().strip('"')
    fn2 = fn2.strip().strip('"')

    if not exists(fn1):
        print(f'无法读取文件: {fn1}')
        return

    if not exists(fn2):
        print(f'无法读取文件: {fn2}')
        return

    fn1_info = stat(fn1)
    fn2_info = stat(fn2)
    if fn1_info.st_size != fn2_info:
        print(f'文件{fn1}与{fn2}的长度不同！')
        return

    fn1_hash = sha256(fread(fn1))
    fn2_hash = sha256(fread(fn2))
    if fn1_hash != fn2_hash:
        print(f'文件1哈希: {fn1_hash}')
        print(f'文件2哈希: {fn2_hash}')
        print(f'文件不同！')
        return

if __name__ == '__main__':
    fn1 = input('请输入文件1的路径: ')
    fn2 = input('请输入文件2的路径: ')
    diff(fn1, fn2)

