from stack import Stack
import pytest


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_insertion(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push()


# def test_non_int_val(empty_stack):
#     with pytest.raises(TypeError):
#         empty_stack.push('not a number')
