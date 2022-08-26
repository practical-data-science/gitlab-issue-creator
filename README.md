# GitLab Issue Creator

GitLab Issue Creator is a Python package that lets you create issues on a GitLab project. It is a simple wrapper around [Python GitLab](https://python-gitlab.readthedocs.io/en/stable/) with features limited only to the creation of issues. I built it to allow me to create GitLab issues for members of my teams based on the outputs of automated tasks.   

## Installation
To install GitLab Issue Creator enter the following command: 

```python
pip3 install git+https://github.com/practical-data-science/gitlab-issue-creator.git
```

### Authentication
To authenticate with GitLab you need to create a personal access token. You can do this by going to your profile page and clicking on the [Personal Access Tokens](https://gitlab.com/-/profile/personal_access_tokens) tab.

Import the `gitlab_issue_creator` module as `gic` and use the `authenticate()` function to authenticate with GitLab.

```python
import gitlab_issue_creator as gic

gl = gic.authenticate('YOUR-PERSONAL-ACCESS-TOKEN')
```

### Usage
To create an issue you need to call the `create_issue()` function. This takes the following parameters: gl (the GitLab object), project_id (the ID of the project you want to create the issue in), title (the title of the issue), description (the description of the issue), labels (a list of labels to apply to the issue), the milestone_id (the ID of the milestone), and assignee_id (the ID of the user to assign the issue to).

```python
issue = gic.create_issue(gl,
                         project_id=987654321,
                         title='Housekeeping / Fix URLs returning 404s',
                         description='Please fix the below URLs returning 404s:', 
                         assignee_id=54321,
                         milestone_id=123456,
                         labels=['Content'])
```

You can't attach a file to the main issue body in GitLab, so instead we'll create a note and attach the file of data to that. To do this we'll call the `upload_file_to_issue_note()` function. This takes the following parameters: gl (the GitLab object), project_id (the ID of the project you want to create the issue in), issue (the issue object you just created), filename (the name of the file), and filepath (the path and filename of the file).

```python
gic.upload_file_to_issue_note(gl,
                              project_id=987654321,
                              issue=issue,
                              filepath='404s.csv',
                              filename='/data/404s.csv')

```

### Helpers
In order to create an issue you'll require various IDs that aren't exposed in the GitLab interface, such as the `project_id`, `assignee_id`, and `milestone_id`. 

#### Get the project ID
The `get_owned_projects()` function returns a list of projects that the user owns. You'll find the names and IDs of projects in here. 

```python
owned_projects = gic.get_owned_projects(gl)
```

#### Get the milestone ID
The `get_project_milestones()` function returns a list of milestones for a project. You'll find the names and IDs of milestones in here.

```python
milestones = gic.get_project_milestones(gl, 123456789)
```

#### Get the user ID of a username
The `get_user_by_username()` function returns the ID of a GitLab username. 

```python
user = gic.get_user_by_username(gl, 'your-username-here')
```

