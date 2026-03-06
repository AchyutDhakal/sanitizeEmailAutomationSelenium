def assert_true(condition, message, module, page):
    try:
        assert condition, message
    except AssertionError as e:
        page.take_screenshot(f"{module}_assertion_error")
        raise e

def assert_false(condition, message, module, page):
    try:
        assert not condition, message
    except AssertionError as e:
        page.take_screenshot(f"{module}_assertion_error")
        raise e

def assert_equal(actual, expected, message, module, page):
    try:
        assert actual == expected, message
    except AssertionError as e:
        page.take_screenshot(f"{module}_assertion_error")
        raise e

def assert_not_equal(actual, expected, message, module, page):
    try:
        assert actual != expected, message
    except AssertionError as e:
        page.take_screenshot(f"{module}_assertion_error")
        raise e