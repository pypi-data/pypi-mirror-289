# cronpulse/monitor.py
import requests
from urllib.parse import urlencode
from datetime import datetime
import asyncio
import sys

class Monitor:
    def __init__(self, job_key, base_url="https://app.cronpulse.live"):
        self.job_key = job_key
        self.base_url = base_url

    def ping(self, state_or_options):
        state = None
        message = ""

        # Handle both string and dictionary inputs (mimicking the Node.js behavior)
        if isinstance(state_or_options, str):
            state = state_or_options
        elif isinstance(state_or_options, dict):
            state = state_or_options.get('state')
            message = state_or_options.get('message', "")
        else:
            raise ValueError("Invalid argument: state_or_options must be a string or a dictionary.")

        endpoint = None
        query_params = {
            'client': 'cronpulse python',
        }

        if state == "beat":
            endpoint = f"/api/ping/{self.job_key}"
        elif state == "start":
            endpoint = f"/api/ping/{self.job_key}/start"
        elif state == "success":
            endpoint = f"/api/ping/{self.job_key}/success"
        elif state == "fail":
            endpoint = f"/api/ping/{self.job_key}/fail"
            query_params['errorMessage'] = message or True
        else:
            raise ValueError(f"Invalid state: {state}")

        return self.send_request(endpoint, query_params)

    def send_request(self, endpoint, query_params=None):
        if query_params is None:
            query_params = {}

        url = f"{self.base_url}{endpoint}"
        if query_params:
            url += f"?{urlencode(query_params)}"

        print(f"📡 Sending request to: {url}")

        response = requests.get(url)
        print(f"📊 Status Code: {response.status_code}")
        print(f"📬 Response body: {response.text}")

        response.raise_for_status()
        return response.text

def wrap(job_key, job_function):
    monitor = Monitor(job_key)
    start_time = datetime.now()
    original_exit = sys.exit
    exit_called = False
    error_occurred = False
    error_message = ""

    def custom_exit(code=0):
        nonlocal exit_called
        if exit_called:
            return
        exit_called = True

        final_state = "fail" if error_occurred else "success"
        monitor.ping({'state': final_state, 'message': error_message})
        original_exit(code)

    sys.exit = custom_exit

    async def wrapped_function():
        nonlocal error_occurred, error_message
        try:
            monitor.ping("start")
            await job_function()
        except Exception as e:
            error_occurred = True
            error_message = str(e)
            print(f"❌ Job failed: {error_message}")
        finally:
            end_time = datetime.now()
            print(f"Job execution time: {(end_time - start_time).total_seconds()} seconds")

            if not exit_called:
                custom_exit(0 if not error_occurred else 1)

    return wrapped_function

