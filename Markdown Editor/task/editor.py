def markdown_formatter():
    formatter_options = ["plain", "bold", "italic", "link", "inline-code", "header", "ordered-list", "unordered-list", "line-break"]
    formatter = input("- Choose a formatter: ")

    while formatter != "!done":
        if formatter == "!help":
            print(f"Available formatters: {' '.join(formatter_options)}")
            print("Special commands: !help !done")

        elif formatter not in formatter_options:
            print("Unknown formatting type or command. Please try again")

        formatter = input("- Choose a formatter: ")


markdown_formatter()
