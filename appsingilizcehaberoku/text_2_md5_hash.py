import hashlib


def text_2_md5_hash(text):
    # just any string to md5 for pyt3
    md5_hasbeen = hashlib.md5(text.encode('utf-8')).hexdigest()
    
    return md5_hasbeen # just hashed