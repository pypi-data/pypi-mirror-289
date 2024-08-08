import os

from sonarcloud_report.client import query_sonarcloud_project_report
from sonarcloud_report.logger_manager import log_error, log_info
from sonarcloud_report.template_manager import get_local_template


def generate_sonarcloud_project_report_file(
    project_name: str, commit_id: str, sonar_token: str
):
    if not project_name:
        log_error("Project name is missing, please define CI_PROJECT_NAME")
    else:
        log_info(f"Project name is '{project_name}'")

    if not sonar_token:
        log_error("SonarCloud token is missing")

    if not commit_id:
        log_error("Current commit ID is missing, please define CI_COMMIT_SHA")
    else:
        log_info(f"Git commit ID is '{commit_id}'")

    branch_name = os.environ.get("CI_COMMIT_BRANCH")
    tag_name = os.environ.get("CI_COMMIT_TAG")
    if not branch_name:
        if tag_name:
            log_info(f"Current build is for tag '{tag_name}'")
        else:
            log_error(
                "Current build branch or tag name is missing, please define CI_COMMIT_BRANCH or CI_COMMIT_TAG"
            )
    elif branch_name != "main":
        log_error(
            f"Current build branch must be 'main' or a tag, found '{branch_name}'"
        )
    else:
        log_info(f"Current build branch is '{branch_name}'")

    project_report = query_sonarcloud_project_report(
        project_name=project_name, token=sonar_token
    )

    if project_report.last_analysis_commit_id != commit_id:
        log_error(
            (
                f"Current commit ID '{commit_id}' does not match the last analysis commit ID "
                f"'{project_report.last_analysis_commit_id}'"
            )
        )

    log_info("Generating output from report template")
    j2_template = get_local_template()
    report_vars = vars(project_report)
    report_vars["branch_name"] = branch_name
    report_vars["tag_name"] = tag_name
    rendered_text = j2_template.render(report_vars)

    output_file_name = "sonarcloud-report.md"
    log_info(f"Saving output to file '{output_file_name}'")
    with open(output_file_name, "w") as f:
        f.write(rendered_text)


if __name__ == "__main__":
    project_name = os.environ.get("CI_PROJECT_NAME")
    commit_id = os.environ.get("CI_COMMIT_SHA")
    sonar_token = os.environ.get("SONAR_TOKEN")
    generate_sonarcloud_project_report_file(project_name, commit_id, sonar_token)
