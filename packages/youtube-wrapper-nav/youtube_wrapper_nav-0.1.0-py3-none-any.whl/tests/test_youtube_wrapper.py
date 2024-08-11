import unittest
from youtube_wrapper import YouTubeWrapper

class TestYouTubeWrapper(unittest.TestCase):
    def setUp(self):
        self.wrapper = YouTubeWrapper(api_key='AIzaSyBXoy6o-kvM3gfm_Gtz3JsVLLhiwVUxA6s')

    def test_get_video_details(self):
        result = self.wrapper.data_api.get_video_details('pgTF5MFG7tk')
        self.assertIn('items', result)
        

    def test_get_transcript(self):
        result = self.wrapper.transcript_api.get_transcript('pgTF5MFG7tk')
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
