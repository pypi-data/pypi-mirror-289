import logging

from jinja2 import (
    Environment,
    PackageLoader,
    select_autoescape,
    Template,
    TemplateError,
    TemplateNotFound,
    TemplateRuntimeError,
)

from sonarcloud_report.client import query_sonarcloud_project_report


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler()],
)


def get_local_template() -> Template:
    template_name = "sonarcloud_report.j2"
    try:
        env = Environment(
            loader=PackageLoader("sonarcloud_report", "templates"),
            autoescape=select_autoescape(),
        )
        return env.get_template(template_name)
    except TemplateNotFound as e:
        raise TemplateError(f"Template not found: {template_name}") from e
    except TemplateRuntimeError as e:
        raise TemplateError(f"Template runtime error: {template_name}") from e
    except Exception as e:
        raise TemplateError(f"Template error: {template_name}") from e


def generate_sonarcloud_project_report_file(project_name: str, sonar_token: str):
    if not project_name:
        logging.critical("Project name is missing, please define CI_PROJECT_NAME")
        exit(1)
    else:
        logging.info(f"Project name is '{project_name}'")

    if not sonar_token:
        logging.critical("SonarCloud token is missing")
        exit(1)

    # if not commit_id:
    #    logging.critical("Current commit ID is missing, please define CI_COMMIT_SHA")
    #    exit(1)
    # else:
    #    logging.info(f"Git commit ID is '{commit_id}'")
    #
    # branch_name = os.environ.get("CI_COMMIT_BRANCH")
    # tag_name = os.environ.get("CI_COMMIT_TAG")
    # if not branch_name:
    #    if tag_name:
    #        logging.info(f"Current build is for tag '{tag_name}'")
    #    else:
    #        logging.critical("Current build branch or tag name is missing, please define CI_COMMIT_BRANCH or CI_COMMIT_TAG")
    #        exit(1)
    # elif branch_name != "main":
    #    logging.critical(f"Current build branch must be 'main' or a tag, found '{branch_name}'")
    #    exit(1)
    # else:
    #    logging.info(f"Current build branch is '{branch_name}'")

    # TODO: pass tag name, and commit id?

    project_report = query_sonarcloud_project_report(
        project_name=project_name, token=sonar_token
    )

    logging.info("Generating output from report template")
    j2_template = get_local_template()
    rendered_text = j2_template.render(vars(project_report))

    output_file_name = "sonarcloud-report.md"
    logging.info(f"Saving output to file '{output_file_name}'")
    with open(output_file_name, "w") as f:
        f.write(rendered_text)
