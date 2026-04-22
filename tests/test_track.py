from lib.track import Track

"""
artist and title are stored correctly for new instances of track
"""
def test_artist_title_stored_correctly_for_new_instances():
    my_track = Track('Unsainted', 'Slipknot')
    assert my_track.title == 'Unsainted'
    assert my_track.artist == 'Slipknot'

"""
matches works for words in title
"""
def test_matches_word_in_title():
    my_track = Track('Wasting Time', 'Four Year Strong')
    assert my_track.matches('wasting') == True

"""
matches works for words in artist
"""
def test_matches_word_in_artist():
    my_track = Track('Wasting Time', 'Four Year Strong')
    assert my_track.matches('Four') == True
