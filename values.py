import sys
import yaml

if __name__ == "__main__":

    with open('values.yaml') as f:
        content = yaml.load(f)
        
        content['staging_image']['repository1'] = sys.argv[1]
        content['staging_image']['tag1'] = sys.argv[2]

    with open('values.yaml', 'w') as nf:
        yaml.dump(content, nf)
