# test_models.py

import pytest
from mixer.backend.django import mixer
from castles.main.models import Castle
pytestmark = pytest.mark.django_db


class TestCastle:
    def test_model(self):
        obj = mixer.blend(Castle)
        assert obj.pk == 1, 'should create a Castle instance'
