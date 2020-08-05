from django.test import TestCase
from .models import User
from copy import deepcopy

input_data = {"jméno": "name", "email": "example@seznam.cz", "ičo": "00064581"}


class TestUserForm(TestCase):
    def test_post_new_user(self):
        response = self.client.post("/user-forms/", data=input_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(**input_data).exists())
        self.assertEqual(response.content.decode("UTF-8"), "Vaše data byla uložena.")

    def test_post_missing_single_value_everytime(self):
        for key in input_data.keys():
            data = deepcopy(input_data)
            data.pop(key)
            response = self.client.post("/user-forms/", data=data)
            if key == "email":
                self.assertEqual(response.status_code, 200)
                self.assertTrue(User.objects.filter(**data).exists())
            else:
                self.assertEqual(response.status_code, 400)
                self.assertFalse(User.objects.filter(**data).exists())
                self.assertEqual(
                    response.content.decode("UTF-8"),
                    "Některé z polí mají chybnou hodnotu či jsou nevyplněná.",
                )

    def test_post_duplicate_ičo_data(self):
        response = self.client.post("/user-forms/", data=input_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(**input_data).exists())
        data = deepcopy(input_data)
        data["email"] = "diffmail@gmail.com"
        response = self.client.post("/user-forms/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.filter(**input_data).count(), 1)
        self.assertEqual(
            response.content.decode("UTF-8"),
            "Některé z polí mají chybnou hodnotu či jsou nevyplněná.",
        )

    def test_invalid_email(self):
        data = deepcopy(input_data)
        data["email"] = "diffmailgmail.com"
        response = self.client.post("/user-forms/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content.decode("UTF-8"),
            "Některé z polí mají chybnou hodnotu či jsou nevyplněná.",
        )

    def test_invalid_ičo(self):
        data = deepcopy(input_data)
        data["ičo"] = "42343243"
        response = self.client.post("/user-forms/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content.decode("UTF-8"),
            "Některé z polí mají chybnou hodnotu či jsou nevyplněná.",
        )

    def test_get_model_form(self):
        response = self.client.get("/user-forms/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "index.html")

    def test_methods_not_allowed(self):
        for method in ("put", "patch", "options", "head"):
            response = getattr(self.client, method)("/user-forms/")
            self.assertEqual(response.status_code, 405)
