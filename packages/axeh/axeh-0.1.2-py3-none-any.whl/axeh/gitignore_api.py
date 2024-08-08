from urllib import request

headers = {"User-Agent": "axe"}


def get_template_list():
    response = (
        request.urlopen(
            request.Request(url="https://www.gitignore.io/api/list", headers=headers)
        )
        .read()
        .decode("utf-8")
    )

    template_list = []
    for line in map(str, response.split("\n")):
        template_list.extend(line.split(","))

    return template_list


def get_gitignore(gi_stack):
    template_list = get_template_list()

    for tech in gi_stack:
        if tech.lower() not in template_list:
            raise ValueError(tech)  # Reports iffy item in the list

    comma_delimited = ",".join(gi_stack)
    response = (
        request.urlopen(
            request.Request(
                f"https://www.gitignore.io/api/{comma_delimited}", headers=headers
            )
        )
        .read()
        .decode("utf-8")
    )

    return response
