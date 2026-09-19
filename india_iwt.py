from data_loader import get_india_projects
from domain_views import india_design_table
def projects():
    return get_india_projects()
def technical_issues():
    return india_design_table()
