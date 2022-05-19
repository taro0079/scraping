from unittest import TestCase
import scraping


class TestSuumo(TestCase):

    def setUp(self) -> None:
        self.url = "https://suumo.jp/chintai/jnc_000073405253/?bc=100277964465"
        self.scraping = scraping.Suumo(self.url)

    def test_station(self):
        self.assertEqual(self.scraping.station(), ['東京メトロ丸ノ内線/淡路町駅 歩3分', '都営新宿線/小川町駅 歩4分', 'ＪＲ山手線/神田駅 歩6分'])

    def test_rent_fee(self):
        self.assertEqual(self.scraping.rent_fee(), '17万円')

    def test_address(self):
        self.assertEqual(self.scraping.address(),'東京都千代田区神田司町２')
