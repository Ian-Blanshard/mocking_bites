from lib.music_library import *
from lib.track import *

"""
when a track is added to music library and the word in title is searched 
that track is returned
"""
def test_correct_track_when_word_in_title_searched():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    result = my_library.search('Kyoto') 
    assert result == [track_one]

"""
when multiple tracks are added to music library and the word in title is searched 
for one of the tracks the correct one is returned
"""
def test_correct_track_when_word_in_title_searched_multiple_tracks():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    track_two = Track('Came out swinging', 'The Wonder Years')
    my_library.add(track_two)
    result = my_library.search('swinging') 
    assert result == [track_two]

"""
when multiple tracks are added to music library and a word in title is searched 
which is present in multiple of the tracks the correct tracks are returned
"""
def test_correct_tracks_when_word_in_title_searched_multiple_tracks_contain_word():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    track_two = Track('Came Out Swinging', 'The Wonder Years')
    my_library.add(track_two)
    track_three = Track('In the End', 'Linkin Park')
    my_library.add(track_three)
    result = my_library.search('in') 
    assert result == [track_one, track_three]

"""
when multiple tracks are added to music library and a word in title is searched 
which is present in multiple of the tracks the correct tracks are returned
for different artists
"""
def test_correct_tracks_when_word_in_artist_searched_multiple_tracks_contain_word():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    track_two = Track('Came Out Swinging', 'The Wonder Years')
    my_library.add(track_two)
    track_three = Track('In the End', 'Linkin Park')
    my_library.add(track_three)
    result = my_library.search('wonder') 
    assert result == [track_one, track_two]

"""
when multiple tracks are added to music library and a word in title is searched 
which is present in both track titles and artist the correct tracks are returned
"""
def test_correct_tracks_when_word_in_artist_and_title_searched_multiple_tracks_contain_word():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    track_two = Track('Came Out Swinging', 'The Wonder Years')
    my_library.add(track_two)
    track_three = Track('In the End', 'Linkin Park')
    my_library.add(track_three)
    track_four = Track('Wonder', 'All Time Low')
    my_library.add(track_four)
    result = my_library.search('wonder') 
    assert result == [track_one, track_two, track_four]

"""
when multiple tracks are added to music library and a word which is not present
in any of the tracks an empty list is returned
"""
def test_empty_list_returned_when_word_not_in_artist_or_title():
    my_library = MusicLibrary()
    track_one = Track('Raining in Kyoto', 'The Wonder Years')
    my_library.add(track_one)
    track_two = Track('Came Out Swinging', 'The Wonder Years')
    my_library.add(track_two)
    track_three = Track('In the End', 'Linkin Park')
    my_library.add(track_three)
    track_four = Track('Wonder', 'All Time Low')
    my_library.add(track_four)
    result = my_library.search('dog') 
    assert result == []