import yaml

with open ('yamling.yaml') as samerpy:
    yaml_sample = samerpy.read()

yaml_dict= yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(yaml_dict)