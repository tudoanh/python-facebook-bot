from unittest import TestCase

import facebook_bot

SAMPLE_LAT = 40.763871
SAMPLE_LONG = -73.979904
DISTANCE = 200
SAMPLE_PAGE_ID = 164606950371187


class TestBot(TestCase):
    def test_get_pages_id(self):
        s = facebook_bot.get_page_ids(SAMPLE_LAT, SAMPLE_LONG, distance=100)
        self.assertIsInstance(s, list)
        self.assertTrue(s)

    def test_get_events(self):
        s = facebook_bot.get_events(SAMPLE_PAGE_ID, base_time='2017-05-07')
        self.assertIsInstance(s, dict)
        self.assertTrue(s)

    def test_get_page_info(self):
        s = facebook_bot.get_page_info(SAMPLE_PAGE_ID)
        self.assertIsInstance(s, dict)
        self.assertTrue(s)

    def test_get_events_by_location(self):
        s = facebook_bot.get_events_by_location(SAMPLE_LAT,
                                                SAMPLE_LONG,
                                                distance=70,
                                                scan_radius=70)
        self.assertIsInstance(s, list)
        self.assertTrue(s)
