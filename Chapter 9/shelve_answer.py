# Write your code here :-)
import shelve
import sys

def save_clipboard(shelf, keyword, text):
    shelf[keyword] = text

def delete_clipboard(shelf, keyword):
    if keyword in shelf:
        del shelf[keyword]
        print(f"Keyword '{keyword}' deleted successfully.")
    else:
        print(f"Keyword '{keyword}' not found.")

def delete_all_clipboards(shelf):
    shelf.clear()
    print("All keywords deleted successfully.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python multi_clipboard.py <keyword> - save text to clipboard")
        print("       python multi_clipboard.py <keyword> - get text from clipboard")
        print("       python multi_clipboard.py delete <keyword> - delete a specific keyword")
        print("       python multi_clipboard.py delete - delete all keywords")
        sys.exit()

    shelf = shelve.open('mcb')

    if sys.argv[1].lower() == 'delete':
        if len(sys.argv) == 2:
            delete_all_clipboards(shelf)
        else:
            delete_clipboard(shelf, sys.argv[2])
    elif len(sys.argv) == 3:
        if sys.argv[1] in ('save', 'get'):
            keyword = sys.argv[2]
            if sys.argv[1] == 'save':
                text = input("Enter text to save: ")
                save_clipboard(shelf, keyword, text)
                print(f"Text saved for keyword '{keyword}'.")
            elif sys.argv[1] == 'get':
                if keyword in shelf:
                    print(f"Clipboard for '{keyword}':")
                    print(shelf[keyword])
                else:
                    print(f"No text found for keyword '{keyword}'.")
        else:
            print("Invalid command.")
    else:
        print("Invalid number of arguments.")

    shelf.close()

if __name__ == "__main__":
    main()

