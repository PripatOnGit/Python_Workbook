def test(x):

    try:
        y = int(x)
    except ValueError:
        print("failed")
    else:
        print("success")
    finally:
        print("done")


test('123')