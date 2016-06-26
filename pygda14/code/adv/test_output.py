def test_print(capsys):
    print('hahaha')
    out, err = capsys.readouterr()

    assert out == 'hahaha'
