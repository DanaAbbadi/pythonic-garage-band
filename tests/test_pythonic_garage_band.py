from pythonic_garage_band import __version__
from pythonic_garage_band.garage_band import  Band,Guitarist,Bassist,Drummer,Musician
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def prep_data():
    
    adam = Bassist("adam","Bassist")
    john = Guitarist("john")
    justin = Drummer("justin")
    maroon5 = Band("Maroon 5",[adam,john,justin],"She will be loved")
    return {'adam':adam, 'john':john, 'justin':justin , 'maroon5': maroon5}

def test_play_solos(prep_data):
    expected = ['tantantantan','wawawawawwawawa','dum dum dum dum']              
    actual = prep_data['maroon5'].play_solos()
    assert expected==actual

def test_to_list(prep_data):
    expected = Band.to_list()             
    actual = prep_data['maroon5'].to_list()
    assert expected == actual

def test_get_instrument(prep_data):
    expected = 'Guitar'             
    actual = prep_data['john'].get_instrument()
    assert expected == actual

def test_play_solo(prep_data):
    expected = 'tantantantan'             
    actual = prep_data['adam'].play_solo()
    assert expected == actual