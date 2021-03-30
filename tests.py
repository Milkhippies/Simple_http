from server import client

res = client.get('/tutorials/')

data = {
    "id": 3,
    "title": 'Video #3. Test',
    "description": 'Tests'
}
post = client.post('/tutorials', json=data)


def test_get_status_code():
    assert res.status_code == 200


def test_get_len():
    assert len(res.get_json()) == 2


def test_get_id_is_num():
    assert res.get_json()[0]['id'] == 0


def test_post_status_code():
    assert post.status_code == 200


def test_post_len():
    assert len(post.get_json()) == 3


def test_post_last_post_data():
    assert post.get_json()[-1]['title'] == data['title']
