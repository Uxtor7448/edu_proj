def test_calculate_total_ok():
    order = Order(id="1", lines=[OrderLine("p1", 2, 100.0)])
    assert calculate_total(order) == 200.0

def test_calculate_total_empty():
    with pytest.raises(EmptyOrderError):
        calculate_total(Order(id="1"))
