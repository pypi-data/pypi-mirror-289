import os
from typing import List, Optional, Dict, Any
from cururo.util.publisher import Publisher
from github import Github, Auth, GithubException
from github.Issue import Issue

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
            self.__github = Github(auth=_auth)
            self.repo = repo
            self.branch = branch
            self.sha = sha
            self.user = self.__github.get_user().login
        except GithubException as e:
            raise Exception(f"Error initializing GitHub client: {e}")

    def __get_repo(self):
        """
        Retrieves the GitHub repository object.

        :return: The GitHub repository object.
        """
        try:
            return self.__github.get_repo(self.repo)
        except GithubException as e:
            raise Exception(f"Error retrieving repository {self.repo}: {e}")


    def publish(self, data):
        """
        Publishes or updates an issue with the graph and body content.

        :param data: The body for the issue.
        :return: None
        """
        try:
            title = f"Automated Issue on branch {self.branch}"
            print(1)
            existing_issue = self.get_thread(title)

            # main_comment = existing_issue.get_comments()[0]
            print(2)
            updated_body = self.append_data_to_comment(existing_issue.body or '', data['message']['adherence'])
            print(3)
            existing_issue.edit(body=updated_body)
            print(4)
            existing_issue.create_comment(self.generate_report(data))

            return 
        except GithubException as e:
            raise Exception(f"Error publishing issue: {e}")
 
    def get_thread(self, title: str, body: Optional[str] = ''):
        """
        Searches for an issue by title and creates or reopens it if necessary.

        :param title: The title of the issue to search or create.
        :param body: The body text for a new issue.
        :return: The existing or newly created issue.
        """
        try:
            repo = self.__get_repo()

            ############################################################################
            # Search for the issue by title
            # Esta parte del codigo es la mas costosa... investigar como optimizar
            issues = repo.get_issues(state='all')  # Fetch all issues (open and closed)
            existing_issue = next((issue for issue in issues if issue.title == title), None)
            ############################################################################

            # Check if the issue is found
            if existing_issue:
                if existing_issue.state != 'open':
                    existing_issue.edit(state='open')
                existing_issue.add_to_assignees(self.user)
                return existing_issue

            # If no issue is found, create a new one
            # This creates the first comment... this is where we are going to have the summary built with markdown
            new_issue = repo.create_issue(title=title, body=body, assignee=self.user)
            return new_issue

        except GithubException as e:
            raise Exception(f"Error threading issue: {e}")

    def generate_report(self, data):
        report = [
            f"### Commit Review Summary [{self.sha}]\n",
            f"**Author:** {self.user}\n",
            f"**Message:**\n",
            f"- **Provided:** {data['message']['provided']}",
            f"- **Generated:** {data['message']['generated']}\n",
            f"- **Adherence Score:** {data['message']['adherence']['score']} {data['message']['adherence']['emoji']}",
            f"  *{data['message']['adherence']['comment']}*\n",
            "\n**Code Complexity:**\n",
            f"- **Comment:** {data['codeComplexity']['comment']}\n",
            "\n**Code Vulnerability:**\n",
            f"- **Score:** {data['codeVulnerability']['score']} {data['codeVulnerability']['emoji']}",
            f"  *{data['codeVulnerability']['comment']}*\n",
            "\n**SOLID Principles Analysis:**\n",
            "| Principle | Score | Comment |\n",
            "|-----------|-------|---------|"
        ]

        for principle, details in data['codeSOLID'].items():
            principle_name = principle.replace('_', ' ').title()
            score_emoji = f"{details['score']} {details['emoji']}"
            comment = details['comment']
            # Ensure proper Markdown escaping to handle special characters in comments
            comment = comment.replace('|', '\\|').replace('\n', ' ')
            report.append(f"| {principle_name} | {score_emoji} | {comment} |\n")


        return '\n'.join(report)

    def append_data_to_comment(self, existing_body: str, adherence: Dict[str, Any]) -> str:
        """
        Appends adherence data to the existing comment body using an XY diagram with emojis.

        :param existing_body: The existing comment body.
        :param adherence: A dictionary with adherence score details.
        :return: The updated comment body.
        """
        # Extract existing data points from the comment
        data_points = self.extract_data_points(existing_body)
        data_points.append((self.sha[:7], adherence['score'], adherence['emoji']))

        # Generate the new XY diagram
        xy_diagram = self.generate_xy_diagram(data_points)

        # Update the comment with the new diagram
        updated_body = existing_body.split("\n**Adherence Scores History:**")[0]
        updated_body += "\n**Adherence Scores History:**\n" + xy_diagram
        return updated_body

    def generate_xy_diagram(self, data_points: List[tuple]) -> str:
        """
        Generates a simple XY diagram using emojis as data points.

        :param data_points: A list of tuples containing commit SHAs, scores, and emojis.
        :return: A string representing the XY diagram.
        """
        max_score = max(score for _, score, _ in data_points)
        diagram = ["```\n    +---+---+---+---+---+---+---+---+---+---+---+ (Score)"]
        for i in range(max_score, 0, -1):
            line = f"{str(i).rjust(2)} | " + ''.join(
                data_point[2] if data_point[1] >= i else '   '
                for data_point in sorted(data_points, key=lambda x: x[1])
            )
            diagram.append(line)
        diagram.append("    +---+---+---+---+---+---+---+---+---+---+---+\n")
        diagram.append("       " + "   ".join(dp[0] for dp in sorted(data_points, key=lambda x: x[1])) + " (SHA)")
        diagram.append("```")
        return '\n'.join(diagram)

    def extract_data_points(self, body: str) -> List[tuple]:
        """
        Extracts data points from the comment body.

        :param body: The comment body.
        :return: A list of tuples with commit SHAs, scores, and emojis.
        """
        lines = body.split("\n")
        data_points = []
        start_extracting = False
        for line in lines:
            if line.strip().startswith("+---"):  # Start of the diagram
                start_extracting = True
                continue
            if start_extracting:
                if line.strip().startswith("```"):  # End of the diagram
                    break
                parts = line.split('|')
                if len(parts) > 2:  # Data point lines
                    sha_part = parts[0].strip()
                    for idx, part in enumerate(parts[1:], 1):
                        if part.strip():  # Contains an emoji
                            data_points.append((sha_part, idx, part.strip()))
        return data_points
    

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
    