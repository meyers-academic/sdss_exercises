from .load_and_print_fits import (load_file,
                                 load_and_print_file_list)

TEST_FILE = '../../data_files/spec-10000-57346-0002.fits'


def test_load_file():
    hdu_list = load_file(TEST_FILE)
    assert len(hdu_list) == 4


def test_load_and_print_file_list():
    load_and_print_file_list([TEST_FILE, TEST_FILE])
