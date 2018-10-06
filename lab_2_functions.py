"""
This program does important stuff
And is written by me
"""


# the function takes a named argument of dict which defaults to an empty dictionary
# it prints out keys and corresponding values if dictionary is not empty

def dict_processing(dict="placeholder"):
    # output "empty dictionary" if it is empty
    if bool(dict == "placeholder"):
        print("empty dictionary")

    # output the keys and values of the dictionary if it is not empty
    else:
        for key, value in dict.items():
            print("key:", key, " value:", value)

    # output a blank line
    return print()


# the function takes a **kwarg as its input argument and prints out each passed in parameter
# value and data type

def var_args(**kwargs):
    # output the keys and values of the kwargs
    if kwargs is not None:
        for key, value in kwargs.items():
            print("key:", key, " value:", value)
    # output a blank line
    return print()


# main

if __name__ == "__main__":
    # some dictionaries: books, languages, placeholder(empty), soEmpty(empty)

    books = {
        "Odyssey": "Homer",
        "War and Peace": "Tolstoy",
        "Pride and Prejudice": "Austin",
        "Grapes of Wrath": "Steinbeck"
    }

    languages = {
        "Java": 1995,
        "Python": 1990,
        "C++": 1985
    }

    people = {
        "Kimmel": "Jimmy",
        "Carter": "Jimmy",
        "Fallon": "Jimmy",
        "Jimmy": "Jimmy"
    }

    placeholder = {}

    soEmpty = {}

    hamilton = {
        "Alexander Hamilton": 916,
        "Aaron Burr": 665,
        "Eliza Hamilton": 324,
        "George Washington": 300,
        "Angelica Schuyler": 246,
        "Thomas Jefferson": 234,
        "John Laurens": 163,
        "Marquis de Lafayette": 129,
        "Hercules Mulligan": 115,
        "James Madison": 112,
        "King George": 100,
        "Philip Hamilton": 85,
        "Peggy Schuyler": 42,
    }

    print()

    # test the output of dictionaries with dict_processing(dict="placeholder")

    print("Test dictionary books with dict_processing():")
    dict_processing(books)

    print("Test dictionary languages with dict_processing():")
    dict_processing(languages)

    print("Test dictionary placeholder with dict_processing():")
    dict_processing()

    # test the output of dictionaries with var_args(**kwargs)

    print("Test dictionary books with var_args():")
    var_args(**books)

    print("Test dictionary languages with var_args():")
    var_args(**languages)

    print("Test dictionary soEmpty with var_args():")
    var_args(**soEmpty)

    print("Test dictionary people with var_args():")
    var_args(**people)

    print("Test dictionary placeholder with var_args():")
    var_args(**placeholder)

    print("Test dictionary hamilton with var_args():")
    var_args(**hamilton)