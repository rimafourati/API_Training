from pprint import pprint
import pandas as pd
import requests

response_API = 'https://api.github.com/repos/Ayushparikh-code/Web-dev-mini-projects/commits'
data = []
page = 1  # Initialize the page number
per_page = 100  # Number of commits per page, adjust as needed

headers = {
    "Authorization": f"token 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",
    "Accept": "application/vnd.github.v3+json"
}

while True:
    # Set the page and per_page parameters
    params = {
        "page": page,
        "per_page": per_page
    }

    response = requests.get(response_API, headers=headers, params=params)

    if response.status_code == 200:
        commits_data = response.json()
        if not commits_data:
            break  # No more commits to fetch
        data.extend(commits_data)
        page += 1
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        break

commits_data_list = []

for commit_data in data:
    commit_info = commit_data['commit']
    commit_reformatted_dict = {
        'author': commit_info['committer']['name'],
        'author_email': commit_info['committer']['email'],
        'commit_date': commit_info['committer']['date'],
        'commit_message': commit_info['message']
    }
    commits_data_list.append(commit_reformatted_dict)

pprint(commits_data_list)
commits_data_frame = pd.json_normalize(commits_data_list)
print(commits_data_frame.head())
commits_data_frame.to_csv('commits_data_frame.csv')
