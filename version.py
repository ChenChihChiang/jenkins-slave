import yaml
import sys
import os


if os.path.isfile('values/version.yaml'):
   with open("version.yaml", 'r') as f:
        content = yaml.load(f)
   content[sys.argv[1]].update({sys.argv[2]: [{'helm_revision': sys.argv[3], 'deploy_date': sys.argv[4]}]})
else:
   content = {}
   content[sys.argv[1]] = {sys.argv[2]: [{'helm_revision': sys.argv[3], 'deploy_date': sys.argv[4]}]}

with open("values/version.yaml", 'w') as nf:
     yaml.dump(content, nf)
