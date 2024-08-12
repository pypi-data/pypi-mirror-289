import os
from typing import List, Optional
from cururo.util.publisher import Publisher
from github import Github, Auth, GithubException

class GitIssuePublisher(Publisher):
    """
    A class to publish and manage GitHub issues with branch-specific threading and graph updates.
    """

    def __init__(self, _api_key: str, repo: str, branch: str, sha: str):
        """
        Initializes the GitIssuePublisher with authentication, repository, and branch details.

        :param _api_key: The GitHub API key for authentication.
        :param repo: The name of the GitHub repository.
        :param branch: The name of the branch related to the issue.
        :param sha: The commit SHA related to the issue.
        """
        super().__init__()

        try:
            _auth = Auth.Token(_api_key)
            self.github = Github(auth=_auth)
            self.repo = repo
            self.branch = branch
            self.sha = sha
            self.user = self.github.get_user().login
        except GithubException as e:
            print(f"Error initializing GitHub client: {e}")
            raise

    def __get_repo(self):
        """
        Retrieves the GitHub repository object.

        :return: The GitHub repository object.
        """
        try:
            return self.github.get_repo(self.repo)
        except GithubException as e:
            print(f"Error retrieving repository {self.repo}: {e}")
            raise


    def publish(self, body: str):
        """
        Publishes or updates an issue with the graph and body content.

        :param body: The body text for the issue.
        :param values: A list of integer values to include in the graph.
        :return: The existing or newly created issue.
        """
        try:
            title = f"Automated Issue on branch {self.branch}"
            repo = self.__get_repo()
            existing_issue = self.thread(title)

            repo.create_issue_comment(existing_issue.number, body)

            return existing_issue
        except GithubException as e:
            print(f"Error publishing issue: {e}")
            raise
 
    def thread(self, title: str, body: Optional[str] = ''):
        """
        Searches for an issue by title and creates or reopens it if necessary.

        :param title: The title of the issue to search or create.
        :param body: The body text for a new issue.
        :return: The existing or newly created issue.
        """
        try:
            repo = self.__get_repo()
            issues = repo.get_issues(state='all')  # Fetch all issues (open and closed)

            # Search for the issue by title
            existing_issue = None
            for issue in issues:
                if issue.title == title:
                    existing_issue = issue
                    break

            # Check if the issue is found
            if existing_issue:
                if existing_issue.state != 'open':
                    existing_issue.edit(state='open')
                existing_issue.edit(assignee=self.user)
                return existing_issue

            # If no issue is found, create a new one
            new_issue = repo.create_issue(title=title, body=body, assignee=self.user)
            return new_issue

        except GithubException as e:
            print(f"Error threading issue: {e}")
            raise

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


if __name__ == "__main__":
    repo = 'agustin-rios/code-diff-review'
    token = ''
    sha = 'azwexrshnuijmk'
    git_publisher = GitIssuePublisher(token, repo, sha)
    git_publisher.publish('hola')
    