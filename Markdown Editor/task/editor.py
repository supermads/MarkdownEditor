def get_text():
    return input("- Text: ")


def format_plain():
    return get_text()


def format_bold():
    return f"**{get_text()}**"


def format_italic():
    return f"*{get_text()}*"


def format_inline():
    return f"`{get_text()}`"


def format_link():
    label = input("- Label: ")
    url = input("- URL: ")
    return f"[{label}]({url})"


def format_header():
    level = int(input("- Level: "))
    if 1 <= level <= 6:
        return f"{'#' * level} {get_text()}\n"
    else:
        return "The level should be within the range of 1 to 6"


def format_new_line():
    return "\n"


def markdown_formatter():
    # Ordered and unordered lists not added yet
    formatter_funcs = {"plain": format_plain,
                       "bold": format_bold,
                       "italic": format_italic,
                       "link": format_link,
                       "inline-code": format_inline,
                       "header":format_header,
                       "new-line": format_new_line}
    formatter = input("- Choose a formatter: ")
    markdown_string = ""

    while formatter != "!done":
        if formatter == "!help":
            print(f"Available formatters: {' '.join(formatter_funcs.keys())}")
            print("Special commands: !help !done")

        elif formatter not in formatter_funcs:
            print("Unknown formatter or command. Please try again.")

        else:
            markdown_string += formatter_funcs[formatter]()

        print(markdown_string)

        formatter = input("- Choose a formatter: ")


markdown_formatter()
