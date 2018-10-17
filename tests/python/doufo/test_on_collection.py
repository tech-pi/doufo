from doufo import head, tail, take, List, flatten, concat
import pytest

@pytest.mark.skip()
@pytest.mark.parametrize('n,xs',[
    (1,[1,2,3]),
    (2,[1,2,3]),
    (3,[1,2,3])
])
def test_take(n,xs):
    assert take(n,xs) == [1,2,3][0:n]

@pytest.mark.parametrize('xs,expect', [
    ([1, 2, 3], [2, 3]),
    (List([1, 2, 3]), List([2, 3]))
])
def test_tail(xs, expect):
    assert tail(xs) == expect


@pytest.mark.parametrize('xs,expect', [
    ([1, 2, 3], 1),
    (List([1, 2, 3]), 1)
])
def test_head(xs, expect):
    assert head(xs) == expect


@pytest.mark.parametrize('xs,expect', [
    ((1, 2, 3), (1, 2, 3)),
    ((1, (2, 3)), (1, 2, 3)),
    ([1, [3, 4]], [1, 3, 4]),
    ([1,2], [1,2]),
    ((2,3), (2,3)),
])
def test_flatten(xs, expect):
    assert flatten(xs) == expect


@pytest.mark.parametrize('xs,expect', [
    ([[1], [2], [3]], [1, 2, 3]),
])
def test_concat(xs, expect):
    assert concat(xs, None) == expect


import doufo.on_collections
@pytest.mark.parametrize('xss,op,acc,result',[
    (lambda x,y:x+y,[1,2],None,3),
    (lambda x,y:x+y,[2,3],1,6),
])
def test_concat_kernel(xss,op,acc,result):
    assert doufo.on_collections.concat_kernel(op, xss, acc) == result