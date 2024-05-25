
#include "cltest/macros.h"
#include "cltest/assert.h"
#include <iostream>

CLTEST(test_001) {
    assert_true(true);
    assert_false(false);

    assert_equals(0, 0);
    assert_different(0, 1);
    assert_less(0, 1);
    assert_greater(1, 0);
    assert_less_or_equal(0, 1);
    assert_greater_or_equal(1, 0);
}

// list of invalid test starters to validate finder

const char* u = " \" ' \" CLTEST(test_003) \\";
/* CLTEST(test_004) */
//CLTEST(test_002) {
//    std::cout << "Invalid Test STDOUT" << std::endl;
//    std::cerr << "Invalid Test STDERR" << std::endl;
//    assert_false(true);
//}