# tests/test_monitor.py
import sys
import os
import asyncio
import requests
# Add the cronpulse directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cronpulse')))

from monitor import Monitor, wrap  # Now directly importing from monitor.py

# Example job function that succeeds
async def successful_job():
    print("Job is running successfully...")
    await asyncio.sleep(2)  # Simulate a job that takes 2 seconds
    print("Job completed successfully.")

# Example job function that fails
async def failing_job():
    print("Job is running but will fail...")
    await asyncio.sleep(1)  # Simulate a job that takes 1 second
    raise Exception("wtf!")  # Raise an exception to simulate failure

# Monitor example with success
def test_monitor_success():
    print("Testing monitor for success...")
    job_key = "ft1joc4eo"  # Replace with a valid job key
    monitor = Monitor(job_key)

    # Test the different states for a successful job
    monitor.ping("start")
    asyncio.run(successful_job())
    monitor.ping("success")

# Monitor example with failure
def test_monitor_failure():
    job_key = "ft1joc4eo"  # Replace with a valid job key
    monitor = Monitor(job_key)

    # Test the different states for a failing job
    try:
        monitor.ping("start")
        asyncio.run(failing_job())
        monitor.ping("success")  # This should not be called if the job fails
    except Exception as e:
        monitor.ping({'state': 'fail', 'message': str(e)})

# Test the wrap function for success
# Test the wrap function for success with error handling
def test_wrap_success():
    print("Testing wrap function for success...")
    job_key = "ft1joc4eo"  # Replace with a valid job key
    wrapped_job = wrap(job_key, successful_job)
    
    try:
        asyncio.run(wrapped_job())
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error occurred: {e}")
        print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

# Test the wrap function for failure
def test_wrap_failure():
    job_key = "ft1joc4eo"  # Replace with a valid job key
    wrapped_job = wrap(job_key, failing_job)
    asyncio.run(wrapped_job())

if __name__ == "__main__":
    # print("Testing success scenario...")
    # test_monitor_success()
    # test_wrap_success()
    
    print("\nTesting failure scenario...")
    # test_monitor_failure()
    test_wrap_failure()
