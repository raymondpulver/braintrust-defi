from os.path import splitext, basename
from json import loads
from glob import glob

def read_entire_file(p):
    handle = open(p)
    content = handle.read()
    handle.close()
    return content


def read_artifacts(p):
    return dict(
        [(splitext(basename(x))[0], loads(read_entire_file(x))) for x in list(glob(p))]
    )
