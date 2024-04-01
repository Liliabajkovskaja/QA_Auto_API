from api_service.base_api import BaseApi


class StoreAPI:
    api_executor = BaseApi()
    base_url = "https://petstore.swagger.io/v2"
    store_order_url = f"{base_url}/store/order"

    def get_order(self, id: int, headers=None):
        return self.api_executor.get(
            url=f"{self.store_order_url}/{id}",
            headers=headers,
            expected_status_code=200
        )

    def add_order(self, body: dict, headers=None):
        return self.api_executor.post(
            url=self.store_order_url,
            headers=headers,
            body=body,
            expected_status_code=200
        )

    def delete_order(self, id: int, headers=None):
        return self.api_executor.delete(
            url=f"{self.store_order_url}/{id}",
            headers=headers,
            expected_status_code=200
        )
