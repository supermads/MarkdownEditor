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


def format_list(list_type):
    formatted_list = ""
    num_rows = int(input("- Number of rows: "))

    while num_rows <= 0:
        print("The number of rows should be greater than zero")
        num_rows = int(input("- Number of rows: "))

    for i in range(1, num_rows + 1):
        row_text = input(f"- Row #{i}: ")
        if list_type == "ordered":
            formatted_list += f"{i}. {row_text}\n"
        else:
            formatted_list += f"* {row_text}\n"

    return formatted_list


def markdown_formatter():
    formatter_funcs = {
        "plain": format_plain,
        "bold": format_bold,
        "italic": format_italic,
        "link": format_link,
        "inline-code": format_inline,
        "header": format_header,
        "new-line": format_new_line,
        "ordered-list": format_list,
        "unordered-list": format_list
    }
    formatter = input("- Choose a formatter: ")
    markdown_string = ""

    while formatter != "!done":
        if formatter == "!help":
            print(f"Available formatters: {' '.join(formatter_funcs.keys())}")
            print("Special commands: !help !done")

        elif formatter not in formatter_funcs:
            print("Unknown formatter or command. Please try again.")

        elif "list" in formatter:
            if formatter[0] == "o":
                markdown_string += format_list("ordered")
            else:
                markdown_string += format_list("unordered")

        else:
            markdown_string += formatter_funcs[formatter]()

        print(markdown_string)

        formatter = input("- Choose a formatter: ")

    with open("output.md", "w") as f:
        f.write(markdown_string)


markdown_formatter()
