try:
        from app import app
        import unittest
except Exception as e:
        print("Some Modules are missing {}".format(e))



class FlaskTest (unittest.TestCase):
    #check for response 200 on base entry page
    def test_base(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_user_routes(self):
        tester = app.test_client(self)
        response = tester.get("/api/users")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_user(self):
        tester = app.test_client(self)
        response = tester.get("/api/users")
        self.assertEqual(response.content_type, "application/json")
    
     def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Status' in response.data)





if __name__ == "__main__":
    unittest.main()