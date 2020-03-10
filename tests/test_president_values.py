from ..ExtraDecorators.president_values import president_values

def test_simple_use_case():
    @president_values(count=0)
    def test(pres, should_be_count):
        assert pres.count == should_be_count
        pres.count += 1

    test(0); test(1); test(2); test(3)

    @president_values(value=None)
    def test_2(pres, new_value):
        pres.value = new_value
        assert pres.value == new_value

    test_2(123); test_2("string")

def test_outside_fucntion_getting():
    @president_values(count=0)
    def test(pres):
        pres.count += 1

    assert test.count == 0
    test()
    assert test.count == 1

    @president_values(value=None)
    def test(pres, new_value):
        pres.value = new_value

    assert test.value == None
    test("string")
    assert test.value == "string"

def test_key_funconality():
    @president_values(value=None)
    def test(pres, new_value):
        pres["value"] = new_value
        assert pres["value"] == new_value

    test(123); test("string")


def test_copy():
    @president_values(a="string", b=123, c=1234)
    def test(pres):
        pres.a = "other string"
        pres.b = 321
        pres.c = 4321
    test()

    new_test_1 = test.new_copy()
    assert new_test_1.a == "other string"
    assert new_test_1.b == 321
    assert new_test_1.c == 4321

    new_test_2 = test.new_copy(keep_values=False)
    assert new_test_2.a == "string"
    assert new_test_2.b == 123
    assert new_test_2.c == 1234
