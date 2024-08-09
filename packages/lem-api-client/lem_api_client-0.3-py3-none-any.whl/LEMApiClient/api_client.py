import requests
import logging


class LEMApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        logging.basicConfig(level=logging.DEBUG)

    def create_queue(self, queue_name, equipment_ids, test_cases, test_session_id):
        try:
            url = f"{self.base_url}/api/create_queue"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "queue_name": queue_name,
                    "equipment_ids": equipment_ids,
                    "test_cases": test_cases,
                    "test_session": test_session_id
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Queue {queue_name} created successfully")
            else:
                return logging.error(f"Failed to create queue: {response.json()}")
        except Exception as e:
            logging.error(e)
        

    def end_queue(self, queue_name):
        try:
            url = f"{self.base_url}/api/end_queue"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "queue_name": queue_name
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Queue ended successfully for {queue_name}")
            else:
                return logging.error(f"Failed to end queue: {response.json()}")
        except Exception as e:
            logging.error(e)

    def allocate_equipment(self, queue_name, equipment_ids):
        try:
            url = f"{self.base_url}/api/allocate_equipment"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "queue_name": queue_name,
                    "equipment_list": equipment_ids
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Equipment allocated successfully for queue {queue_name}")
            else:
                return logging.error(f"Failed to allocate equipment: {response.json()}")
        except Exception as e: 
            logging.error(e)

    def start_test(self, equipment_ids, test_name):
        try:
            url = f"{self.base_url}/api/start_test"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "equipment_id": equipment_ids,
                    "test_id": test_name
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Test {test_name} started successfully for equipment/s {equipment_ids}")
            else:
                return logging.error(f"Failed to start test: {response.json()}")
        except Exception as e:
            logging.error(e)
            

    def end_test(self, test_name, equipment_ids):
        try:
            url = f"{self.base_url}/api/end_test"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "test_id": test_name,
                    "equipment_ids": equipment_ids
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Test ended successfully for equipment/s {equipment_ids}")
            else:
                return logging.error(f"Failed to end test: {response.json()}")
        except Exception as e:
            logging.error(e)

    def add_test(self, test_name, test_description):
        try:
            url = f"{self.base_url}/api/add_test"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "test_name": test_name,
                    "test_description": test_description
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Test {test_name} added successfully")
            else:
                return logging.error(f"Failed to add test: {response.json()}")
        except Exception as e:
            logging.error(e)

    def create_equipment(self, nickname, type_name, location_name):
        try:
            url = f"{self.base_url}/api/create_equipment"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "nickname": nickname,
                    "type_name": type_name,
                    "location_name": location_name
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                return logging.info(f"Equipment {nickname} created successfully")
            else:
                return logging.error(f"Failed to create equipment: {response.json()}")
        except Exception as e:
            logging.error(e)


    def get_eqp_id(self, location_name, nickname):
        try:
            url = f"{self.base_url}/api/eqp_id"
            data = {
            "location": location_name,
            "nickname": nickname
            }

            response = requests.get(url, headers=self.headers, json=data)
            if response.status_code == 200:
                response = response.json()
                if response['reply']['fields']['executed']:
                    return response['reply']['fields']['eqp-id']
                else:
                    logging.error(f"Failed to get equipment ID: {response['reply']['fields']['error-message']}")
                return 
            else:
                return logging.error(f"Failed to get equipment ID: {response.json()}")
        except Exception as e:
            logging.error(e)


    def create_test_session(self, session_name):
        try:
            url = f"{self.base_url}/api/create_test_session"
            data = {
            "command": {
                "protocol-version": "00.01",
                "fields": {
                    "session_name": session_name
                    }
                }
            }

            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                response = response.json()
                if response['reply']['fields']['executed']:
                    return response['reply']['fields']['session-id']
                else:
                    logging.error(f"Failed to create test session: {response['reply']['fields']['error-message']}")
            else:
                return logging.error(f"Failed to create test session: {response.json()}")
        except Exception as e:
            logging.error(e)

    def clear_tables(self):
        try:
            url = f"{self.base_url}/api/clear_tables"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return logging.info("Tables cleared successfully")
            else:
                return logging.error(f"Failed to clear tables: {response.json()}")
        except Exception as e:
            logging.error(e)

        

def main():
    print("LEMApiClient command line interface")
