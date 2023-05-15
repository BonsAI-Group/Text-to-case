import requests

from auth.ApiAuthorization import ApiAuthorization

class FormRequesterService:
    """
    A service that sends GET requests to the Zenya API to retrieve forms.
    """
    @staticmethod
    def requestForm(url):
        """
        Sends a GET request to the specified URL and returns the response as a JSON object.

        Args:
        url (str): The URL to send the GET request to.

        Returns:
        dict: The response from the GET request as a JSON object.
        """
        api_key = ApiAuthorization.getAuthorizationToken()
        api_key_name = ApiAuthorization.getAuthorizationTokenName()
        headers = {api_key_name: api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Request failed with status code {response.status_code}')
    
    @staticmethod
    def getFormById(id) -> dict:
        """
        Sends a GET request to the Zenya API to retrieve a form by its ID.

        Args:
        id (int): The ID of the form to retrieve.

        Returns:
        dict: The form object as a JSON object.
        """
        url = f'https://ai.zenya.work/api/cases/reporter_forms/{id}?include_design=true'            
        
        response = FormRequesterService.requestForm(url)
        return response
    
    @staticmethod
    def getAllForms() -> dict:
        """
        Sends a GET request to the Zenya API to retrieve all forms.

        Returns:
        dict: The list of forms as a JSON object. These do not include the form design.
        """
        url = 'https://ai.zenya.work/api/cases/reporter_forms/'
        return FormRequesterService.requestForm(url)
