import os
import requests
from typing import Dict, Any
from cururo.util.publisher import Publisher
from github import Github, Auth

class GitIssuePublisher(Publisher):

    def __init__(self, repo:str, _api_key:str, sha:str, user:str = None):
        super().__init__()
        _auth = Auth.Token(_api_key)
        self.github = Github(auth=_auth)
        self.repo = repo
        self.sha = sha
        self.user = user

    def __get_repo(self):
        return self.github.get_repo(self.repo)
    
    def publish(self, body: str):
        title = f"Automated Issue for {self.user};\n [commit {self.sha}]"
        return self.__get_repo().create_issue(title, body=body) # assignee=self.user)
    
    def generate_report(self, data):
        report = [
            "### Commit Review Summary\n",
            f"**Commit SHA:** {self.sha}\n",
            f"**Message:**\n",
            f"- **Provided:** {data['message']['provided']}",
            f"- **Generated:** {data['message']['generated']}\n",
            f"- **Adherence Score:** {data['message']['adherence']['score']} {data['message']['adherence']['emoji']}",
            f"  *{data['message']['adherence']['comment']}*\n"
        ]

        # Code complexity section
        report.append("**Code Complexity:**\n")
        report.append(f"- **Comment:** {data['codeComplexity']['comment']}\n")

        # SOLID principles section
        report.append("**SOLID Principles Analysis:**\n")
        for principle, details in data['codeSOLID'].items():
            report.append(f"- **{principle.replace('_', ' ').title()}**")
            report.append(f"  - **Score:** {details['score']} {details['emoji']}")
            report.append(f"  *{details['comment']}*\n")

        # Vulnerability section
        report.append("**Code Vulnerability:**\n")
        report.append(f"- **Score:** {data['codeVulnerability']['score']} {data['codeVulnerability']['emoji']}")
        report.append(f"  *{data['codeVulnerability']['comment']}*\n")

        return '\n'.join(report)

    

class WebPublisher(Publisher):

    def __init__(self, url:str, secret:str):
        super().__init__()
        self.url = url
        self.secret = secret

    def publish(self, data):
        return self.__send_request(data)

    def __send_request(self, data):
        headers = { 'Content-Type': 'application/json' }
        data['secret'] = self.secret
        res = requests.post(self.url, headers=headers, json=data)
        res.raise_for_status()
        return res

    def sort_data(self, data: Dict[str, Any], others: Dict[str, Any] = None) -> Dict[str, Any]:
        if others is None:
            others = {}
        sorted_data = {
            'message': data['message'].get('message', ''),
            'suggested': data['message'].get('suggested', ''),
            'adherence': data['message'].get('adherence', ''),
            'completeness': data['message'].get('completeness', ''),
            'atomicity': data['code']['acid_score'].get('a', ''),
            'consistency': data['code']['acid_score'].get('c', ''),
            'isolation': data['code']['acid_score'].get('i', ''),
            'durability': data['code']['acid_score'].get('d', ''),
            'vulnerability': data['code']['vulnerable_code'].get('score', ''),
        }
        sorted_data.update(others)
        return sorted_data
    