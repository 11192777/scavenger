import logging


from ArchiveResult import ArchiveResult


def check_response(response):
    assert "statusCode" in response, "检查一下token，需要加Bearer"
    if response['statusCode'] != '0000':
        logging.error('===> Failed message:{}'.format(response))
        return None
    else:
        return response['result']


def asert_status_code(response, status_code):
    assert "statusCode" in response, "检查一下token，需要加Bearer"
    if status_code is not None:
        assert response["statusCode"] == status_code, "Assert status code failed."
    return response["result"]


def assert_status(result: ArchiveResult, status):
    print(result.__dict__)
    print("Response status code is:{} and assert status code is:{}".format(result.status_code(), status))
    assert result.status_code() == status
    return result
