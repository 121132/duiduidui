import hashlib

def md5(data_string):
    obj = hashlib.md5('django-insecure-6!0n15=vi&6%x6m#v+q-b*rek1%a8t4xu-udzf0kg!v#idl8&y'.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()

print(md5('123'))