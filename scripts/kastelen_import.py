import json
from django.db import IntegrityError
from castles.main.models import Castle


def create_obj(klass, dictionary):
    obj = klass()
    # check if object exists
    _naam = dictionary['naam']
    if Castle.objects.filter(naam=_naam).exists():
        print(' key exists, skipping.. ', end="")
        return False

    # set regular fields
    for field, value in dictionary.items():
        if not isinstance(value, list):
            setattr(obj, field, value)
    try:
        obj.save()
    except IntegrityError as e:
        print("Error saving obj {}".format(e))
        return False
    return True


def run():
    with open("kastelen_pp.json", "r") as json_file:
        data = json.load(json_file)
    json_file.close()

    count = 0
    for feature in data['features']:
        _dict = {}
        print(count)
        print(feature)
        count += 1
        _dict['itype'] = feature['type']
        _dict['iid'] = feature['id']
        _dict['geometry_type'] = feature['geometry']['type']
        _dict['geometry_coords_x'] = feature['geometry']['coordinates'][0]
        _dict['geometry_coords_y'] = feature['geometry']['coordinates'][1]
        _dict['geometry_name'] = feature['geometry_name']
        _dict['gid'] = int(feature['properties']['gid'])
        _dict['cchin'] = int(feature['properties']['cchin'])
        _dict['naam'] = feature['properties']['naam']
        _dict['plaats'] = feature['properties']['plaats']
        _dict['info_link'] = feature['properties']['info_link']
        _dict['datering_year'] = feature['properties']['datering']
        _dict['rijksmonnr'] = feature['properties']['rijksmonnr']
        _dict['provincie'] = feature['properties']['provincie']
        _dict['foto_thumb'] = feature['properties']['foto_thumb']
        _dict['foto_groot'] = feature['properties']['foto_groot']
        _dict['bijschrift'] = feature['properties']['bijschrift']
        if feature['properties']['zichtbaar'] == 'J':
            _dict['zichtbaar'] = True
        else:
            _dict['zichtbaar'] = False
        _dict['legenda'] = feature['properties']['legenda']
        _dict['typering'] = feature['properties']['typering']

        if create_obj(Castle, _dict):
            print(_dict)
