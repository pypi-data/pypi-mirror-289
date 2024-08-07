#!/usr/bin/env python3
"""
SPDX-License-Identifier: Apache-2.0
Copyright Contributors to the ODPi Egeria project.

A simple viewer for collections - provide the root and we display the hierarchy

"""

import argparse
import os
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.tree import Tree
from rich.markdown import Markdown
from rich.console import Console

from pyegeria import (ProjectManager, MyProfile, UserNotAuthorizedException, PropertyServerException,
                      InvalidParameterException)
from pyegeria._exceptions import (
    print_exception_response,
)

disable_ssl_warnings = True
EGERIA_METADATA_STORE = os.environ.get("EGERIA_METADATA_STORE", "active-metadata-store")
EGERIA_KAFKA_ENDPOINT = os.environ.get('KAFKA_ENDPOINT', 'localhost:9092')
EGERIA_PLATFORM_URL = os.environ.get('EGERIA_PLATFORM_URL', 'https://localhost:9443')
EGERIA_VIEW_SERVER = os.environ.get('VIEW_SERVER', 'view-server')
EGERIA_VIEW_SERVER_URL = os.environ.get('EGERIA_VIEW_SERVER_URL', 'https://localhost:9443')
EGERIA_INTEGRATION_DAEMON = os.environ.get('INTEGRATION_DAEMON', 'integration-daemon')
EGERIA_ADMIN_USER = os.environ.get('ADMIN_USER', 'garygeeke')
EGERIA_ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'secret')
EGERIA_USER = os.environ.get('EGERIA_USER', 'erinoverview')
EGERIA_USER_PASSWORD = os.environ.get('EGERIA_USER_PASSWORD', 'secret')
EGERIA_JUPYTER = bool(os.environ.get('EGERIA_JUPYTER', 'False'))
EGERIA_WIDTH = int(os.environ.get('EGERIA_WIDTH', '200'))

def project_structure_viewer(root: str, server_name: str, platform_url: str, user: str, user_password: str,
                      jupyter:bool=EGERIA_JUPYTER, width:int = EGERIA_WIDTH):
    """ A simple collection viewer"""
    def walk_project_hierarchy(project_client: ProjectManager, project_name: str, tree: Tree, root:bool = False) -> None:
        """Recursively build a Tree with collection contents."""
        t = None
        style = "bright_white on black"

        project = project_client.get_projects_by_name(project_name)
        if type(project) is list:
            proj_guid = project[0]['elementHeader']['guid']
            proj_props = project[0]['properties']

            proj_type = proj_props.get('typeName','---')
            proj_unique = proj_props.get('qualifiedName', '---')
            proj_identifier = proj_props.get('identifier', '---')
            proj_name = proj_props.get('name','---')
            proj_desc = proj_props.get('description','---')
            proj_status = proj_props.get('projectStatus','---')
            proj_priority = proj_props.get('priority', '---')
            proj_start = proj_props.get('startDate', '---')[:-10]
            proj_props_md = (f"* Name: {proj_name}\n"
                             f"* Identifier: {proj_identifier}\n"
                             f"* Type: {proj_type}\n"
                             f"* Status: {proj_status}\n"
                             f"* priority: {proj_priority}\n"
                             f"* Start:    {proj_start}\n"
                             f"* Description: {proj_desc}\n"
                             f"* GUID: {proj_guid}")
        else:
            return

        team = project_client.get_project_team(proj_guid)
        member_md = ""
        if type(team) is list:
            for member in team:
                member_guid = member['member']['guid']
                member_unique = member['member']['uniqueName']
                member_md += f"* Member Unique Name: {member_unique}\n* Member GUID: {member_guid}"
            proj_props_md += f"\n### Team Members\n {member_md}"

        proj_props_out = Markdown(proj_props_md)
        p = Panel(proj_props_out, style = style, title=project_name)
        t = tree.add(p)


        linked_projects = project_client.get_linked_projects(proj_guid)
        if type(linked_projects) is list:
            for proj in linked_projects:
                child_md = ""
                child_guid = proj['elementHeader']['guid']
                child_name = proj['properties']['name']
                # child_props = proj['properties']
                # for key in child_props.keys():
                #     child_md += f"* {key}: {child_props[key]}\n"
                # child_md += f"* GUID: {child_guid}"
                walk_project_hierarchy(project_client, child_name, t)

        else:
            return t
        #     tt= tree.add(f"[bold magenta on black]No projects match {root_project_name}")

            #
            # branch = tt.add(f"[bold magenta on black]Members", style=style, guide_style=style)
            # walk_collection_hierarchy(collection_client, member['qualifiedName'], branch),

        # members = project_client.get_member_list(root_project_name)
        # if members:
        #     for member in members:
        #         style = "bold white on black"
        #         text_collection_name = Text(f"[bold white on black]Name: {member['name']}", style=style)
        #         text_qualified_name = Text(f"* QualifiedName: {member['qualifiedName']}")
        #         text_guid = Text(f"* GUID: {member['guid']}", "green")
        #         text_collection_type = Text(f"* Collection Type: {member['collectionType']}")
        #         text_description = Text(f"* Description: {member['description']}")
        #         p = Panel.fit(f"{text_collection_name}[green]\n{text_qualified_name}\n{text_guid}\n"
        #                       f"{text_collection_type}\n{text_description}")
        #         tt = tree.add(p, style=style)
        #
        #
        #         linked_projects = project_client.get_linked_projects()
        #         if type(children) is list:
        #             branch = tt.add(f"[bold magenta on black]Members", style=style, guide_style=style)
        #             walk_collection_hierarchy(collection_client, member['qualifiedName'], branch),
        # else:
        #     tt = tree.add(f"[bold magenta on black]No collections match {root_collection_name}")
    try:
        console = Console(width=EGERIA_WIDTH)
        tree = Tree(f"[bold bright green on black]{root}",guide_style="bold bright_blue")
        p_client = ProjectManager(server_name, platform_url,
                                     user_id=user)

        token1= p_client.create_egeria_bearer_token(user, user_password)

        walk_project_hierarchy(p_client,root, tree, root = True)
        print(tree)

    except (
        InvalidParameterException,
        PropertyServerException,
        UserNotAuthorizedException
    ) as e:
        print_exception_response(e)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--server", help="Name of the server to display status for")
    parser.add_argument("--url", help="URL Platform to connect to")
    parser.add_argument("--userid", help="User Id")
    parser.add_argument("--password", help="User Password")
    args = parser.parse_args()

    server = args.server if args.server is not None else EGERIA_VIEW_SERVER
    url = args.url if args.url is not None else EGERIA_PLATFORM_URL
    userid = args.userid if args.userid is not None else EGERIA_USER
    user_pass = args.password if args.password is not None else EGERIA_USER_PASSWORD

    try:
        root_project = Prompt.ask("Enter the Root Project to start from:", default="Sustainability Campaign")
        project_structure_viewer(root_project, server, url, userid, user_pass)
    except (KeyboardInterrupt):
        pass
if __name__ == "__main__":
    main()