import sys
import yaml

if __name__ == "__main__":

  with open('values/env.yaml') as e:
      new_env = yaml.load(e)

  env_new = new_env['env1']

  with open('values/rollback.yaml') as f:
      original = yaml.load(f)

  replicas = original['spec']['replicas']
  image = original['spec']['template']['spec']['containers'][0]['image'].split(":")[0]
  tag = original['spec']['template']['spec']['containers'][0]['image'].split(":")[1]
  env_list = original['spec']['template']['spec']['containers'][0]['env']
  env = {}
  for i in range(0, len(env_list)):
      env.update({env_list[i]['name']:env_list[i]['value']})

  with open('values/values_prod.yaml') as f:
      content = yaml.load(f)

      content['production_image']['repository1'] = image
      content['production_image']['tag1'] = tag
      content['production_deployment']['replicas'] = replicas
      content['env1_production'] = env

      content['canary_image']['repository1'] = image
      content['canary_image']['tag1'] = tag
      content['canary_deployment']['replicas'] = 0
      content['env1_canary'] = env

      content['staging_deployment']['enable'] = 'true'
      content['staging_deployment']['replicas'] = 1
      content['staging_image']['repository1'] = sys.argv[1]
      content['staging_image']['tag1'] = sys.argv[2]
      content['env1_staging'] = env_new
      content['env1_staging']['ENV'] = 'staging'

      print (content['staging_image']['repository1'])
  with open('values/staging_values.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['staging_deployment']['enable'] = 'false'
      content['staging_deployment']['replicas'] = 0
      content['canary_deployment']['enable'] = 'true'
      content['canary_deployment']['replicas'] = 1
      content['canary_image']['repository1'] = sys.argv[1]
      content['canary_image']['tag1'] = sys.argv[2]
      content['env1_canary'] = env_new
      content['env1_canary']['ENV'] = 'canary'
  with open('values/canary_values_1.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['canary_deployment']['enable'] = 'true'
      if int(replicas) / 4 == 0:
          content['canary_deployment']['replicas'] = 1
      else:    
          content['canary_deployment']['replicas'] = int(replicas) / 4
  with open('values/canary_values_2.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['canary_deployment']['enable'] = 'true'
      if int(replicas) / 2 == 0:
          content['canary_deployment']['replicas'] = 1
      else:
          content['canary_deployment']['replicas'] = int(replicas) / 2
  with open('values/canary_values_3.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['canary_deployment']['enable'] = 'true'
      if int(replicas) / 4 * 3 == 0:
          content['canary_deployment']['replicas'] = 1
      else:
          content['canary_deployment']['replicas'] = int(replicas)
  with open('values/canary_values_4.yaml', 'w') as nf:
      yaml.dump(content, nf)


      content['canary_deployment']['enable'] = 'true'
      content['canary_deployment']['replicas'] = 0
      content['production_deployment']['replicas'] = int(replicas)
      content['production_image']['repository1'] = sys.argv[1]
      content['production_image']['tag1'] = sys.argv[2]
      content['env1_production'] = env_new
      content['env1_production']['ENV'] = 'production'
  with open('values/production_values.yaml', 'w') as nf:
      yaml.dump(content, nf)