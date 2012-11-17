import path
import argparse
from hashlib import sha256

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('directories', metavar='DIR', type=str, nargs='+',
                   help='directory to be parsed')
parser.add_argument('--output,-o', type=str, help='output directory')

args = parser.parse_args()

for dr in args.directories:
    with open(dr.replace('/', '_')+ '.hashes', 'w') as output:
        for f in path.path(dr).walkfiles():
            with open(f) as fp:
                digest = sha256(fp.read()).hexdigest()
            output.write('%s %s\n' % (f, digest))
