import pytest
from player import Player

class TestPlayer():

    def test_change_name(self):
        player = Player()
        assert player.change_name('new_name') != 'new_name'

    def test_add_points(self):
        player = Player()
        assert player.add_points(10) == 10


