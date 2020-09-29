from rest_framework import serializers
from castles.main.models import Castle


class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Castle
        fields = ['itype', 'iid', 'geometry_type', 'geometry_coords_x', 'geometry_coords_y',
                  'geometry_name', 'gid', 'cchin', 'naam', 'plaats', 'info_link', 'datering',
                  'rijksmonnr', 'provincie', 'foto_thumb', 'foto_groot', 'bijschrift',
                  'zichtbaar', 'legenda', 'typering']

        # extra_kwargs = {
        #    "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        # }
