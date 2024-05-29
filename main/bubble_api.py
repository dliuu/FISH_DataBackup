import requests
import json
from datetime import datetime

class BubbleAPI:
    def __init__(self, raw_url: str, apikey: str):
        self.raw_url = raw_url
        self.apikey = apikey
        self.headers = {
            'Content-type': 'application/json',
            'Authorization': f'ApiKey {apikey}',
        }

    def merge_constraints(self, key_list, type_list, value_list):
        if len(key_list) != len(type_list) or len(key_list) != len(value_list):
            raise ValueError("Input lists must have the same length")

        merged_dicts = []
        for i in range(len(key_list)):
            merged_dicts.append({
                "key": key_list[i],
                "constraint_type": type_list[i],
                "value": value_list[i]
            })
        return merged_dicts

    def get_datetime(self):
        return datetime.today().strftime('%Y-%m-%d')

    def GET_single_object(self, obj: str, **kwargs):
        url = f"{self.raw_url}/{obj}"
        r = requests.get(url)
        response = r.json()
        return response

    def GET_all_objects(self, obj: str, cursor:int, **kwargs, ):
        url = f"{self.raw_url}/{obj}"

        if kwargs:
            key_list = kwargs.get('key_list')
            type_list = kwargs.get('type_list')
            value_list = kwargs.get('value_list')

            constraints = self.merge_constraints(key_list, type_list, value_list)

            if len(constraints) == 0:
                r = requests.get(url, headers=self.headers)
                return r.json()
            else:
                url = f"{url}?constraints={constraints}"
                r = requests.get(url, headers=self.headers)
                return r.json()
        else:
            if cursor > 0:
                return_json = {}
                remaining_items = 1

                while remaining_items > 0:

                    r = requests.get(url= f"{url}?cursor={cursor}")
                    data = r.json()

                    if "response" in data:
                        if len(return_json) == 0:
                            return_json['data'] = data['response']['results']
                        else:
                            return_json['data'] += data['response']['results']

                    if data['response']['remaining'] > 0:
                        remaining_items = data['response']['remaining']
                        if remaining_items >= 100:
                            cursor+=100
                        else:
                            cursor+=data['response']['remaining']
                    else:
                        return json.dumps(return_json)

            else:
                r = requests.get(url)
                return r.json()

    def write_to_file(self, obj: str, api_type: str, filename: str):
        if api_type == 'single':
            raw_obj = self.GET_single_object(obj)
        elif api_type == 'all':
            raw_obj = self.GET_all_objects(obj)
        else:
            print('Error: Please input a valid api_type')
            return api_type

        json_obj = json.dumps(raw_obj, indent=4)
        day = self.get_datetime()

        with open(f"{day}-{filename}.json", "w") as outfile:
            outfile.write(json_obj)

    def write_snapshot_files(self):
        # Example usage:
        # Loan
        self.write_to_file(obj='Loan', api_type='all', filename='test-loans-snapshot')

        # Loan Application
        self.write_to_file(obj='Loan Application', api_type='all', filename='test-loan-applications-snapshot')

        # (FISH) Contact
        self.write_to_file(obj='(FISH) Contact', api_type='all', filename='test-contacts-snapshot')

        # (FISH) Company
        self.write_to_file(obj='(FISH) Company', api_type='all', filename='test-companies-snapshot')

        # (FISH) Property
        self.write_to_file(obj='(FISH) Property', api_type='all', filename='test-properties-snapshot')

        # (FISH) Payment
        self.write_to_file(obj='(FISH) Payments', api_type='all', filename='test-payments-snapshot')

        # (FISH) Funding
        self.write_to_file(obj='(FISH) Funding', api_type='all', filename='test-funding-snapshot')

        # (FISH) Disbursement_new
        self.write_to_file(obj='(FISH) Disbursement_new', api_type='all', filename='test-disbursements-snapshot')

        # (FISH)_Draw
        self.write_to_file(obj='(FISH)_Draw', api_type='all', filename='test-draws-snapshot')

        # Loan Extension
        self.write_to_file(obj='Loan Extension', api_type='all', filename='test-draws-snapshot')

        # Loan Payoff
        self.write_to_file(obj='Loan Payoff', api_type='all', filename='test-payoffs-snapshot')

        # User
        self.write_to_file(obj='User', api_type='all', filename='test-payoffs-snapshot')


raw_url = 'https://ifish.tech/version-test/api/1.1/obj'
apikey = 'ac090d3276b654b46f8dc62f52a50452'
bubble_api = BubbleAPI(raw_url, apikey)

#test for joe
return_json = bubble_api.GET_all_objects('(FISH) Payments', cursor=125)
print(return_json)

#bubble_api.write_snapshot_files()

