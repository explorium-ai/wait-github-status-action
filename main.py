import json
import os
import requests
import time
import sys

git_api = os.environ["GITHUB_API_URL"]
repo = os.environ["GITHUB_ACTION_REPOSITORY"]
sha = os.environ["GITHUB_SHA"]
token = os.environ["INPUT_TOKEN"]
name = os.environ["INPUT_NAME"]
strict = (True if (os.environ["INPUT_STRICT"] == "true") else False)
timeout = (0 if (os.environ["INPUT_TIMEOUT"] == "") else int(os.environ["INPUT_TIMEOUT"]))

statuses_url = f"{git_api}/repos/{repo}/commits/{sha}/status"
checks_url = f"{git_api}/repos/{repo}/commits/{sha}/check-runs"
passed = 0

def main():
    print(statuses_url,checks_url)
    statuses = get_data(statuses_url)
    checks = get_data(checks_url)
    isStat = False
    isCheck = False
    for stat in statuses:
        if stat["context"] == name:
            isStat = True
    for check in checks:
        if check["name"] == name:
            isCheck = True
    if isStat:
        status_code = "pending"
        while status_code not in {'success', 'failed'}:
            status_code = getStatStatus()
            time.sleep(1)
            passed = passed + 1
            if timeout == passed:
                sys.exit("Timeout Reached")            
        if status_code != "success":
            print(f"::set-output name=result::Failed")
            if strict is True:
                sys.exit("Dag Failed")
        else:
            print(f"::set-output name=result::Success")
            sys.exit(0)
    if isCheck:
        status_code = "in_progress"
        while status_code not in {'success', 'failed'}:
            status_code = getStatStatus()
            time.sleep(1)
            passed = passed + 1
            if timeout == passed:
                sys.exit("Timeout Reached")
        if status_code != "success":
            print(f"::set-output name=result::Failed")
            if strict is True:
                sys.exit("Dag Failed")
        else:
            print(f"::set-output name=result::Success")
            sys.exit(0)       

def getStatStatus():
    temp_statuses = get_data(statuses_url)
    for stat in temp_statuses:
        if stat["context"] == name:
            return stat["state"]

def getCheckStatus():
    temp_checks = get_data(checks_url)
    for check in temp_checks:
        if check["name"] == name:
            return check["state"]

def get_data(url):
    resp = requests.request(
        "GET",
        url,
        headers={"Authorization": "Bearer " + token},
    )    
    if resp.status_code != 200:
        raise Exception(
            "Bad response from application: " + str(resp.status_code) + " / " + str(resp.headers) + " / " + str(resp.text)
        )
    else:
        data = json.loads(str(resp.text).replace("'", ""))
        return data

if __name__ == "__main__":
    main()