
def test_hello(client):
    response = client.get('/event/')
    assert b'[]' in response.data
