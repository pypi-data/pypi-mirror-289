from functools import reduce
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.runners import list_of_runners

prefix = "https://kamangir-public.s3.ca-central-1.amazonaws.com"

items = (
    ["📜"]
    + [
        "[`{}`](./patterns/{}.dot)".format(
            pattern,
            pattern,
        )
        for pattern in list_of_patterns()
    ]
    + reduce(
        lambda x, y: x + y,
        [
            (
                [f"[{runner_type}](./runners/{runner_type}.py)"]
                + [
                    f"[![image]({url})]({url})"
                    for url in [
                        "{}/{}-{}/workflow.gif?raw=true".format(
                            prefix,
                            runner_type,
                            pattern,
                        )
                        for pattern in list_of_patterns()
                    ]
                ]
            )
            for runner_type in list_of_runners()
        ],
        [],
    )
)
