import sys
import yaml

if __name__ == "__main__":


  with open('rollback.yaml') as f:
      original = yaml.load(f)

  replicas = original['spec']['replicas']
  image = original['spec']['template']['spec']['containers'][0]['image'].split(":")[0]
  tag = original['spec']['template']['spec']['containers'][0]['image'].split(":")[1]
  env = original['spec']['template']['spec']['containers'][env]


  with open('values.yaml') as f:
      content = yaml.load(f)

      content['production_image']['repository1'] = image
      content['production_image']['tag1'] = tag
      content['production_deployment']['replicas'] = replicas
      content['env1_production'] = env

      content['preprod_image']['repository1'] = image
      content['preprod_image']['tag1'] = tag
      content['preprod_deployment']['replicas'] = 0
      content['env1_preprod'] = env

      content['staging_deployment']['enable'] = 'true'
      content['staging_deployment']['replicas'] = 1
      content['staging_image']['repository1'] = sys.argv[1]
      content['staging_image']['tag1'] = sys.argv[2]
  with open('staging_values.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['staging_deployment']['enable'] = 'false'
      content['staging_deployment']['replicas'] = 0
      content['preprod_deployment']['enable'] = 'true'
      content['preprod_deployment']['replicas'] = 1
      content['preprod_image']['repository1'] = sys.argv[1]
      content['preprod_image']['tag1'] = sys.argv[2]
      content['env1_preprod'] = content['env1_staging']
  with open('preprod_values_1.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['preprod_deployment']['enable'] = 'true'
      if int(replicas) / 4 == 0:
          content['preprod_deployment']['replicas'] = 1
      else:    
          content['preprod_deployment']['replicas'] = int(replicas) / 4
      content['env1_preprod'] = content['env1_staging']
  with open('preprod_values_2.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['preprod_deployment']['enable'] = 'true'
      if int(replicas) / 2 == 0:
          content['preprod_deployment']['replicas'] = 1
      else:
          content['preprod_deployment']['replicas'] = int(replicas) / 2
      content['env1_preprod'] = content['env1_staging']
  with open('preprod_values_3.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['preprod_deployment']['enable'] = 'true'
      if int(replicas) / 4 * 3 == 0:
          content['preprod_deployment']['replicas'] = 1
      else:
          content['preprod_deployment']['replicas'] = int(replicas)
      content['env1_preprod'] = content['env1_staging']
  with open('preprod_values_4.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['preprod_deployment']['enable'] = 'true'
      content['preprod_deployment']['replicas'] = 0
      content['production_deployment']['replicas'] = int(replicas)
      content['production_image']['repository1'] = sys.argv[1]
      content['production_image']['tag1'] = sys.argv[2]
      content['env1_production'] = content['env1_staging']
  with open('production_values.yaml', 'w') as nf:
      yaml.dump(content, nf)

