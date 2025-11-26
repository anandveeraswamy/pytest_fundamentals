from pytest import approx
import pytest
from triangle import area_of_a_triangle


def test_float_values_exact():
    """ Test areas when inputs are floats"""
    assert area_of_a_triangle(2.3, 5.7) == 6.555
    
def test_float_values_approx():
    """Test areas when inputs and output are floats using approx"""
    # these tests will fail without approx
    assert 0.1 + 0.2 == approx(0.3) 
    assert area_of_a_triangle(3.4556, 8.3567) == approx(14.43870626)
    assert area_of_a_triangle(3.4556, 8.3567) == approx(14.43, rel=1e-3)

def test_integer_values():
    """ Test areas when values are integers """
    assert area_of_a_triangle(2, 5) == 5

def test_zero_base():
    """ Test areas when base is zero """
    assert area_of_a_triangle(0, 5) == 0

def test_zero_height():
    """ Test areas when height is zero """
    assert area_of_a_triangle(5, 0) == 0

def test_zero_values():
    """ Test areas when base and height are zero """
    assert area_of_a_triangle(0, 0) == 0

def test_negative_base():
    """ Test that ValueError is raised when base is negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(-2, 5)

def test_negative_height():
    """ Test that ValueError is raised when height is negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(2, -5)

def test_negative_values():
    """ Test that ValueError is raised when both are negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(-2, -5)

def test_with_boolean():
    """ Test that TypeError is raised with boolean types """
    with pytest.raises(TypeError):
        area_of_a_triangle(True, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, False)

def test_with_string():
    """ Test that TypeError is raised with string types """
    with pytest.raises(TypeError):
        area_of_a_triangle('base', 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, 'height')

def test_with_nulls():
    """ Test that TypeError is raised with null types """
    with pytest.raises(TypeError):
        area_of_a_triangle(None, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, None)
