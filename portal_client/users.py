import json
from argparse import ArgumentParser
from urllib.parse import urljoin

import requests

from portal_client.defaults import PORTAL_BACKEND_ENDPOINT
from portal_client.pagination import pagination_parser
from portal_client.utils import get_authorization_header


def list_users(**filters):
    users_url = urljoin(PORTAL_BACKEND_ENDPOINT, "/api/users/")
    response = requests.get(
        users_url,
        headers={"Authorization": get_authorization_header()},
        params=filters,
    )
    return response.json()


def list_users_cli(args):
    users_response = list_users(
        organization=args.organization,
        groups=args.user_groups,
        page=args.page,
        page_size=args.page_size,
        search=args.search,
    )

    print(json.dumps(users_response))


def configure_users_parser(parser: ArgumentParser):
    users_parser = parser.add_subparsers(
        description="List and manage user accounts on Portal"
    )

    users_list_parser = users_parser.add_parser(
        "list",
        help="Returns a paginated list of users on Portal",
        parents=[pagination_parser],
    )

    filters_group = users_list_parser.add_argument_group("filters", "Filtering Users")
    filters_group.add_argument(
        "--user-groups",
        metavar="GROUP_ID",
        type=int,
        default=[],
        nargs="+",
        help="Only return users within the given groups (ids)",
    )
    filters_group.add_argument(
        "--organization",
        type=int,
        help="Only return users from the given organization (id)",
    )
    filters_group.add_argument(
        "--search",
        help="A search term (e.g. email address, user name) to filter results by",
    )

    users_list_parser.set_defaults(func=list_users_cli)