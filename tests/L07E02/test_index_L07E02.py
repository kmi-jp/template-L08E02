import types

from data.index import Index


def test_iter():
    test_labels = ["key 1", "key 2", "key 3", "key 4", "key 5"]

    idx = Index(labels=test_labels)

    assert isinstance(idx.__iter__(), types.GeneratorType)

    assert [label for label in idx] == test_labels
