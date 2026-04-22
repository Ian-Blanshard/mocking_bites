from lib.music_library import *
from unittest.mock import Mock

"""
when a new instance of musiclibrary is created the tracks list is empty
"""
def test_new_instances_empty_tracks_list():
    my_library = MusicLibrary()
    result = my_library.tracks
    assert result == []

"""
test add correctly adds track to tracks list
"""
def test_add_to_tracks_list():
    my_library = MusicLibrary()
    mocked_track = Mock()
    mocked_track.artist = 'Metallica'
    mocked_track.title = 'Disposable Heroes'
    my_library.add(mocked_track)
    result = my_library.tracks
    assert result == [mocked_track]

