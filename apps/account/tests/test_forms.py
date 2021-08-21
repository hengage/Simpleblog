from django.test import SimpleTestCase, TestCase
from account.forms import CustomUserCreationForm

class TestCustomUserCreationForm(TestCase):

    def test_form_is_valid_data(self):
        form = CustomUserCreationForm(data={
            'first_name':'henry',
            'last_name':'chizoba',
            'username':'hengage',
            'password1':'dracula',
            'password2':'dracula',
            'date_of_birth':'jan-30-1994',
            'email':'hengage@yahoo.com',
            'gender':'male',
            'address':'umudagu',
            'result':None
        })

        self.assertTrue(form.is_valid())
