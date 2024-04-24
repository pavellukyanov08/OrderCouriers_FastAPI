from httpx import AsyncClient


async def test_add_courier(ac: AsyncClient):
    response = await ac.post('/couriers', json={
        "id": 1,
        "name": "ALex",
        "avg_order_complete_time": "2024-04-24T10:09:33.603Z",
        "avg_day_orders": 0,
        "active_order": None,
        "district": 2,
        "order": 1,
    })

    assert response.status_code == 200


async def test_get_courier(ac: AsyncClient):
    response = await ac.get('/couriers', params={
        "name": "ALex",
    })

    assert response.status_code == 200
    assert response.json()["status"] == {"success"}
    assert len(response.json()["data"]) == 1
