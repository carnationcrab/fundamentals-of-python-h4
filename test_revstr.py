# SAM MARTORANA

# ################################# [H4_2] ################################# #
# Write PyTest unit tests for your reverse() function of the previous problem.
# You should test your function with at least ten (10) different unit test
# functions (name them test_...), with asserts within each that test for 10
# different input values. You must copy your reverse() function of [H4-1] into
# the test_revstr.py file for your submission.
#
# To avoid this copying, it's possible to import revstr for testing into your
# separate test_revstr file, using the if __name__ == '__main__':  approach
# we'll discuss in class. Unfortunately, this won't work for Canvas
# submissions, since it renames the file names when I download them.  So be
# sure to submit  your reverse() function and your PyTest code both within the
# same .py file for this problem.
#
# Remember that PyTest does not allow your imported module to read or write
# anything to the console: it will report such attempts as failures when
# running the tests.
# ########################################################################## #

# TO TEST
def reverse(s):

    reversed_str = ''

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str

# TESTING

def test_hello():
    assert 'olleh' == reverse('hello')

def test_my():
    assert 'ym' == reverse('my')

def test_name():
    assert 'eman' == reverse('name')

def test_is():
    assert 'si' == reverse('is')

def test_sam():
    assert 'mas' == reverse('sam')

def test_and():
    assert 'dna' == reverse('and')

def test_im():
    assert "m'i" == reverse("i'm")

def test_a():
    assert 'a' == reverse('a')

def test_software():
    assert 'erawtfos' == reverse('software')

def test_engineer():
    assert 'reenigne' == reverse('engineer')