

def test_empty_event(client):
    response = client.get('/event/')
    assert b'[]' in response.data


def test_post_event(client):
    response = client.post('/event/', json={
        "id":               1,
        "name":            "test",
        "start_date_time": "2022-10-07T18:00:50+00:00",
        "end_date_time":   "2022-10-07T18:30:00+00:00",
        "category":        "tst",
        "tags":            "a,b,c",
        "author_id":       "test"
    })
    assert response.status_code == 200
