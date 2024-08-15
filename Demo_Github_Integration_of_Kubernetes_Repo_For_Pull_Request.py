# Program to demonstrate integration with Github to fetch the details of Users who
# created Pull Requests(Active) on Kubernetes Github Repo

# pip install requests
import requests

# URL to fetch pull requests from the Github API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

#Make a GET request to fetch pull requests data from the GITHUB Api
response = requests.get(url) # Add headers = headers inside get() for authentication

# Only if response is successful 
if response.status_code == 200: 

#Convert the JSON response to a directory 
    pull_requests = response.json()

# Create an empty directory to store PR creators and their counts
    pr_creators = {}

# Iterate through each pull requests and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator]+=1
        else:
            pr_creators[creator] = 1

# Display the directory of PR creators and their counts
    print("PR Creators and Counts: ")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")        

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Demo_Github_Integration_of_Kubernetes_Repo_For_Pull_Request.py"
PR Creators and Counts: 
BenTheElder: 1 PR(s)
2uasimojo: 1 PR(s)
fedebongio: 1 PR(s)
Huang-Wei: 4 PR(s)
wedaly: 4 PR(s)
googs1025: 1 PR(s)
enj: 1 PR(s)
aojea: 1 PR(s)
macsko: 1 PR(s)
light-smile: 1 PR(s)
soltysh: 1 PR(s)
xovoxy: 1 PR(s)
fusida: 1 PR(s)
liggitt: 1 PR(s)
bouaouda-achraf: 1 PR(s)
thockin: 2 PR(s)
impact-maker: 2 PR(s)
tklauser: 1 PR(s)
jdcloudconformance: 1 PR(s)
zhifei92: 1 PR(s)
ardaguclu: 1 PR(s)
omerap12: 1 PR(s)
"""