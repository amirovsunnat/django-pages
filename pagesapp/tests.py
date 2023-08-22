from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    """Templateslarimizni test qilish uchun klass"""
    def test_home_page(self):
        """Home pageni test qilish"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        """About pageni test qilish"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_news_page(self):
        """News pageni test qilish"""
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_compatations_page(self):
        """Compatations pageni test qilish"""
        response = self.client.get('/compatations/')
        self.assertEqual(response.status_code, 200)