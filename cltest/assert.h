#pragma once

#include <cstdlib>

void assert_true (bool x) {
    if (!x) exit(1);
}
void assert_false (bool x) {
    assert_true(!x);
}

template <typename U, typename V>
void assert_equals (U a, V b) {
    assert_true(a == b);
}
template <typename U, typename V>
void assert_different (U a, V b) {
    assert_false(a == b);
}
template <typename U, typename V>
void assert_less (U a, V b) {
    assert_true(a < b);
}
template <typename U, typename V>
void assert_greater (U a, V b) {
    assert_true(a > b);
}
template <typename U, typename V>
void assert_less_or_equal (U a, V b) {
    assert_true(a <= b);
}
template <typename U, typename V>
void assert_greater_or_equal (U a, V b) {
    assert_true(a >= b);
}
