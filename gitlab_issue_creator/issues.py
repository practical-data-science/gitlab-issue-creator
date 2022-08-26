"""
GitLab Issue Creator
"""

import gitlab


def authenticate(personal_access_token):
    """Authenticates to GitLab.

    Args:
        personal_access_token (str): The PERSONAL_ACCESS_TOKEN URL.
    """

    gl = gitlab.Gitlab(private_token=personal_access_token)
    gl.auth()

    return gl


def get_owned_projects(gl):
    """Gets the owned projects.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
    """

    owned_projects = gl.projects.list(owned=True, archived=0)
    return owned_projects


def get_project_by_id(gl, project_id):
    """Gets the project by ID.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        project_id (int): The project ID.
    """

    project = gl.projects.get(project_id)
    return project


def get_project_milestones(gl, project_id):
    """Gets the project milestones.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        project_id (int): The project ID.
    """

    project = gl.projects.get(project_id)
    milestones = project.milestones.list(state='active')
    return milestones


def get_user_by_username(gl, username):
    """Gets the user by username.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        username (str): The username.
    """

    user = gl.users.list(search=username)
    return user


def create_issue(gl, project_id, title, description, assignee_id, milestone_id, labels: list):
    """
    Create an issue.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        project_id (int): The project ID.
        title (str): The issue title.
        description (str): The issue description.
        assignee_id (int): The assignee ID.
        milestone_id (int): The milestone ID.
        labels (list): The labels.
    """

    project = gl.projects.get(project_id)
    issue = project.issues.create({'title': title,
                                   'description': description,
                                   'assignee_id': assignee_id,
                                   'milestone_id': milestone_id,
                                   'labels': labels})
    return issue


def add_note_to_issue(gl, project_id, issue, note):
    """
    Add a note to an issue.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        project_id (int): The project ID.
        issue (int): The issue object.
        note (str): The note.
    """

    project = gl.projects.get(project_id)
    issue.notes.create({'body': note})
    return issue


def upload_file_to_issue_note(gl, project_id, issue, filepath, filename):
    """
    Upload a file to an issue note.

    Args:
        gl (gitlab.Gitlab): The GitLab object.
        project_id (int): The project ID.
        issue (int): The issue object.
        filepath (str): The file path.
        filename (str): The file name.
    """

    project = gl.projects.get(project_id)
    uploaded_file = project.upload(filename, filepath=filepath)
    issue.notes.create({
        "body": "See the [attached file]({})".format(uploaded_file["url"])
    })

    return issue

