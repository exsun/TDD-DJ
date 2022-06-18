from django.urls import reverse
import unittest
from selenium import webdriver

from . import MovieTest

class MovieTestViews(MovieTest):
    def test_movies_list_views(self):
        m = self.create_movie()
        print(m)
        url = reverse('movie-list')
        resp = self.client.get(url)
        print("resp",resp.content)

        self.assertEqual(resp.status_code, 200)
        # self.assertIn(m.movie_title, resp.content)


# class MovieListTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox(executable_path=r'E:\geckodriver.exe')

#     def test_list(self):
#         self.driver.get("http://localhost:8000/api/movies/")
#         self.driver.find_element_by_id('movie')
#         self.assertIn("http://localhost:8000", self.driver.current_url)

#     def tearDown(self):
#         return self.driver.quit


if __name__ == '__main__':
    unittest.main()