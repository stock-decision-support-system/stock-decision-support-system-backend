from django.test import TestCase
import shioaji as sj
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ShioajiTestCase(TestCase):
    def test_virtual_account_login(self):
        api = sj.Shioaji(simulation=True)  # 模擬模式
        api.login(
            api_key=config["shioaji"]["api_key"],
            secret_key=config["shioaji"]["secret_key"],
            contracts_cb=lambda security_type: print(
                f"{repr(security_type)} fetch done."
            ),  # 獲取商品檔Callback
        )
