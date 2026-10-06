import ast
import importlib.util
import pathlib
import unittest

_source_path = pathlib.Path(__file__).parent / "dynamic-array.py"
_spec = importlib.util.spec_from_file_location("dynamic_array", _source_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
DynamicArray = _module.DynamicArray


class TestInit(unittest.TestCase):
    def test_new_array_is_empty(self):
        arr = DynamicArray(1)
        self.assertEqual(arr.getSize(), 0)

    def test_new_array_has_given_capacity(self):
        self.assertEqual(DynamicArray(1).getCapacity(), 1)
        self.assertEqual(DynamicArray(5).getCapacity(), 5)


class TestPushback(unittest.TestCase):
    def test_pushback_increments_size(self):
        arr = DynamicArray(4)
        arr.pushback(10)
        arr.pushback(20)
        self.assertEqual(arr.getSize(), 2)

    def test_pushback_appends_in_order(self):
        arr = DynamicArray(4)
        for n in [7, 8, 9]:
            arr.pushback(n)
        self.assertEqual([arr.get(i) for i in range(3)], [7, 8, 9])

    def test_pushback_within_capacity_does_not_resize(self):
        arr = DynamicArray(3)
        arr.pushback(1)
        arr.pushback(2)
        arr.pushback(3)
        self.assertEqual(arr.getCapacity(), 3)

    def test_pushback_when_full_doubles_capacity(self):
        arr = DynamicArray(1)
        arr.pushback(1)
        self.assertEqual(arr.getCapacity(), 1)
        arr.pushback(2)
        self.assertEqual(arr.getCapacity(), 2)
        arr.pushback(3)
        self.assertEqual(arr.getCapacity(), 4)

    def test_capacity_grows_by_doubling_over_many_pushes(self):
        arr = DynamicArray(1)
        for n in range(9):
            arr.pushback(n)
        self.assertEqual(arr.getSize(), 9)
        self.assertEqual(arr.getCapacity(), 16)

    def test_elements_survive_resize(self):
        arr = DynamicArray(2)
        values = [5, 6, 7, 8, 9]
        for n in values:
            arr.pushback(n)
        self.assertEqual([arr.get(i) for i in range(len(values))], values)


class TestGetSet(unittest.TestCase):
    def test_set_overwrites_value(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        arr.pushback(2)
        arr.set(1, 3)
        self.assertEqual(arr.get(1), 3)

    def test_set_does_not_change_size_or_neighbors(self):
        arr = DynamicArray(4)
        for n in [1, 2, 3]:
            arr.pushback(n)
        arr.set(1, 99)
        self.assertEqual(arr.getSize(), 3)
        self.assertEqual(arr.get(0), 1)
        self.assertEqual(arr.get(2), 3)

    def test_get_first_and_last(self):
        arr = DynamicArray(3)
        for n in [4, 5, 6]:
            arr.pushback(n)
        self.assertEqual(arr.get(0), 4)
        self.assertEqual(arr.get(2), 6)


class TestPopback(unittest.TestCase):
    def test_popback_returns_last_element(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        arr.pushback(2)
        self.assertEqual(arr.popback(), 2)
        self.assertEqual(arr.popback(), 1)

    def test_popback_decrements_size(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        arr.pushback(2)
        arr.popback()
        self.assertEqual(arr.getSize(), 1)

    def test_popback_does_not_shrink_capacity(self):
        arr = DynamicArray(1)
        arr.pushback(1)
        arr.pushback(2)
        arr.popback()
        arr.popback()
        self.assertEqual(arr.getCapacity(), 2)
        self.assertEqual(arr.getSize(), 0)

    def test_pushback_after_popback_reuses_slot(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        arr.pushback(2)
        arr.popback()
        arr.pushback(3)
        self.assertEqual(arr.get(1), 3)
        self.assertEqual(arr.getSize(), 2)
        self.assertEqual(arr.getCapacity(), 2)


class TestResize(unittest.TestCase):
    def test_resize_doubles_capacity(self):
        arr = DynamicArray(3)
        arr.resize()
        self.assertEqual(arr.getCapacity(), 6)

    def test_resize_keeps_size_and_elements(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        arr.pushback(2)
        arr.resize()
        self.assertEqual(arr.getSize(), 2)
        self.assertEqual(arr.get(0), 1)
        self.assertEqual(arr.get(1), 2)


class TestNeetCodeExamples(unittest.TestCase):
    def test_example_1(self):
        arr = DynamicArray(1)
        self.assertEqual(arr.getSize(), 0)
        self.assertEqual(arr.getCapacity(), 1)

    def test_example_2(self):
        arr = DynamicArray(1)
        arr.pushback(1)
        self.assertEqual(arr.getCapacity(), 1)
        arr.pushback(2)
        self.assertEqual(arr.getCapacity(), 2)

    def test_example_3(self):
        arr = DynamicArray(1)
        self.assertEqual(arr.getSize(), 0)
        self.assertEqual(arr.getCapacity(), 1)
        arr.pushback(1)
        self.assertEqual(arr.getSize(), 1)
        self.assertEqual(arr.getCapacity(), 1)
        arr.pushback(2)
        self.assertEqual(arr.getSize(), 2)
        self.assertEqual(arr.getCapacity(), 2)
        self.assertEqual(arr.get(1), 2)
        arr.set(1, 3)
        self.assertEqual(arr.get(1), 3)
        self.assertEqual(arr.popback(), 3)
        self.assertEqual(arr.getSize(), 1)
        self.assertEqual(arr.getCapacity(), 2)


def _storage(arr):
    lists = [v for v in vars(arr).values() if isinstance(v, list)]
    if len(lists) != 1:
        raise AssertionError(
            f"expected exactly one list attribute as backing storage, found {len(lists)}"
        )
    return lists[0]


class TestFixedStorage(unittest.TestCase):
    def test_storage_is_allocated_to_capacity_up_front(self):
        arr = DynamicArray(4)
        self.assertEqual(len(_storage(arr)), 4)

    def test_storage_length_matches_capacity_after_growth(self):
        arr = DynamicArray(2)
        for n in range(5):
            arr.pushback(n)
        self.assertEqual(len(_storage(arr)), arr.getCapacity())

    def test_resize_allocates_new_storage(self):
        arr = DynamicArray(2)
        arr.pushback(1)
        before = _storage(arr)
        arr.resize()
        after = _storage(arr)
        self.assertIsNot(after, before)
        self.assertEqual(len(after), 4)

    def test_popback_does_not_shrink_storage(self):
        arr = DynamicArray(4)
        for n in [1, 2, 3]:
            arr.pushback(n)
        arr.popback()
        self.assertEqual(len(_storage(arr)), 4)

    def test_does_not_use_growable_list_methods(self):
        banned = {"append", "extend", "insert", "pop", "remove", "clear"}
        tree = ast.parse(_source_path.read_text())
        used = sorted(
            {
                node.func.attr
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in banned
            }
        )
        self.assertEqual(used, [], f"list methods that grow or shrink the list: {used}")


if __name__ == "__main__":
    unittest.main()
