import urllib.parse
import requests


class Users:
    def __init__(self, session, logger, base_url):
        self.session = session
        self.logger = logger
        self.base_url = base_url
        self.workspace_instance = None

    def createUsers(self, userPayload: list):
        """
        Create user.

        :param userPayload:
        :return:
        """
        try:
            userPayload = [i.model_dump(exclude_none=True) for i in userPayload]

            url = f"{self.base_url}/rest/v13/bulk/add/users"
            response = self.session.post(url, json=userPayload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"User profile successfully created.")
            else:
                raise ValueError(resp.get('message'))
            return resp["data"]
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e

    def editUsers(self, userPayload: list):
        """
        Create user.

        :param userPayload:
        :return:
        """
        try:
            newPayload = []
            for user in userPayload:
                if not user.EncryptedZviceID:
                    raise Exception("User data validation failed: Missing EncryptedZviceID.")
                elif not user.Profile.UserID:
                    raise Exception("User data validation failed: Missing UserID in Profile.")
                newPayload.append(user.model_dump(exclude_none=True))

            url = f"{self.base_url}/rest/v13/bulk/edit/users"
            response = self.session.put(url, json=newPayload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"User profile successfully created.")
            else:
                raise ValueError(resp.get('message'))
            return resp["data"]
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e

    def getUsers(self, userPayload: list = []):
        """
        Fetch user details.

        :param userPayload: [
                {
                    "operator":"=",
                    "value": "USER_EMAIL",
                    "column": "UserEmail"   # Other inputs you can pass are 'UserID', 'UserPhone',
                }
            ]
        :return:
        """
        filters = {
            "HideSpecialUserGroups": True
        }
        try:
            filter_dict = filters
            # Encoding the filter dictionary into query parameters
            filter_params = urllib.parse.urlencode(filter_dict)
            url = f"{self.base_url}/rest/v17/search/users?{filter_params}"
            response = self.session.post(url, json=userPayload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"PDF generated successfully for custom document {id}")
            else:
                raise ValueError(resp.get('message'))
            return resp["data"]
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e
