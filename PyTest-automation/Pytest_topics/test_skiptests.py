import sys

import pytest
import sys
pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="only run in windows")
const = 9/5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float


# @pytest.mark.skipif(sys.version_info > (3, 11), reason="Does not work on python version above 3.8")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test, so skipping ")
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(pytest.__version__ < "7.1.1", reason="pytest version is less")
def test_case03():
    assert cent_to_fah(38) == 100.4
