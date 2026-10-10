import unittest
import json

from main import create_app, db
from main.models import User


class TestDeleteUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testenv.cfg")
        self.app.config["TESTING"] = True

        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_delete_existing_user(self):
        user = User("delete_test@example.com", "password123")
        db.session.add(user)
        db.session.commit()
        user_id = user.id

        response = self.client.delete(
            "/delete",
            data=json.dumps({"id": user_id}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["email"],
            "delete_test@example.com"
        )
        self.assertIsNone(db.session.get(User, user_id))

    def test_delete_missing_user(self):
        response = self.client.delete(
            "/delete",
            data=json.dumps({"id": 999999}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.get_json(),
            {"error": "data not found"}
        )


if __name__ == "__main__":
    unittest.main()
