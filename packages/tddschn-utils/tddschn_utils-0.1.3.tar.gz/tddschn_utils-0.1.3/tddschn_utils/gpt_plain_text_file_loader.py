#!/usr/bin/env python3

import io
import os
import fnmatch
import argparse
from pathlib import Path
import sys
from typing import Iterable

DEFAULT_PREAMBLE_GIT_REPO = "The following text is a Git repository with code. The structure of the text are sections that begin with ----, followed by a single line containing the file path and file name, followed by a variable amount of lines containing the file contents. The text representing the Git repository ends when the symbols --END-- are encounted. Any further text beyond --END-- are meant to be interpreted as instructions using the aforementioned Git repository as context."
DEFAULT_PREAMBLE_FILE_COLLECTION = "The following text is a collection of files. The structure of the text are sections that begin with ----, followed by a single line containing the file path and file name, followed by a variable amount of lines containing the file contents."

DEFAULT_EPILOGUE = """reply 'ok' and only 'ok' if you read."""


def get_args():
    parser = argparse.ArgumentParser(
        description="Process a Git repository into a text file"
    )
    parser.add_argument(
        "repo_path",
        help="Path to the Git repository, defaults to CWD.",
        nargs="?",
        default=Path("."),
    )
    parser.add_argument("-p", "--preamble", help="Preamble text", default=None)
    parser.add_argument(
        "-f", "--preamble-file", help="Path to preamble text file", default=None
    )
    # epilogue
    parser.add_argument("-e", "--epilogue", help="Epilogue text", default=None)
    parser.add_argument(
        "-F", "--epilogue-file", help="Path to epilogue text file", default=None
    )
    # -E
    parser.add_argument(
        "-E",
        "--no-epilogue",
        help="Do not include epilogue text",
        action="store_true",
    )
    parser.add_argument(
        "-o", "--output", help="Path to output text file", default="output.txt"
    )

    # -c, copy
    parser.add_argument(
        "-c",
        "--copy",
        help="Copy the output to the clipboard",
        action="store_true",
    )

    parser.add_argument(
        "-G",
        "--no-ignore-git",
        help="Do not ignore .git directory",
        action="store_true",
    )
    parser.add_argument(
        "-Z",
        "--no-ignore-gitignore-and-gitattributes",
        help="Do not ignore .gitignore and .gitattributes files",
        action="store_true",
    )
    # cSpell:disable
    parser.add_argument(
        "-i",
        "--gptignore",
        help="Path to .gptignore file, repo_path/.gptignore by default",
    )
    parser.add_argument(
        "-I", "--no-gptignore", help="Do not use .gptignore file", action="store_true"
    )
    # cSpell:enable

    parser.add_argument(
        "-l",
        "--file-list",
        help="List of files to include in the output",
        nargs="+",
        default=None,
    )
    parser.add_argument(
        "-L",
        "--file-list-file",
        help="Path to file list file. Only files paths listed will be included in that order. Pass `-` to read from stdin",
        default=None,
        type=Path,
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        "--list-files-would-be-included",
        help="List files that would be included in the output (Only this will be written to stderr)",
        action="store_true",
    )
    return parser.parse_args()


def get_ignore_list(ignore_file_path: os.PathLike) -> list[str]:
    ignore_list = []
    with open(ignore_file_path, "r") as ignore_file:
        for line in ignore_file:
            if os.name == "nt":
                line = line.replace("/", "\\")
            ignore_list.append(line.strip())
    return ignore_list


def should_ignore(file_path: str, ignore_list: Iterable[str]) -> bool:
    for pattern in ignore_list:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False


def get_included_files(
    repo_path: os.PathLike,
    ignore_list: Iterable[str] = [],
    file_list: list[str] | None = None,
) -> list[Path]:
    included_files = []
    if file_list:
        for file_path in file_list:
            relative_file_path = os.path.relpath(file_path, repo_path)
            if not should_ignore(relative_file_path, ignore_list):
                included_files.append(Path(file_path))
    else:
        for root, _, files in os.walk(repo_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_file_path = os.path.relpath(file_path, repo_path)
                if not should_ignore(relative_file_path, ignore_list):
                    included_files.append(Path(file_path))
    return included_files


def write_files_to_output(file_paths: list[Path], output_file):
    for file_path in file_paths:
        with open(file_path, "r", errors="ignore") as file:
            contents = file.read()
        output_file.write("-" * 4 + "\n")
        output_file.write(f"{file_path}\n")
        output_file.write(f"{contents}\n")


def main() -> None:
    args = get_args()

    repo_path = args.repo_path
    if not args.file_list and args.file_list_file == Path("-"):
        args.file_list = [line.strip() for line in sys.stdin.readlines()]
    if not args.file_list and args.file_list_file and args.file_list_file.exists():
        args.file_list = args.file_list_file.read_text().splitlines()  # noqa
    # cSpell:disable
    if args.gptignore:
        ignore_file_path = args.gptignore
    else:
        ignore_file_path = os.path.join(repo_path, ".gptignore")

    if args.no_gptignore:
        ignore_list = []
    else:
        ignore_list = (
            get_ignore_list(ignore_file_path)  # type: ignore
            if os.path.exists(ignore_file_path)
            else []
        )  # type: ignore
    # cSpell:enable
    if not args.no_ignore_git:
        ignore_list.append(".git/*")
    if not args.no_ignore_gitignore_and_gitattributes:
        ignore_list.append(".gitignore")
        ignore_list.append(".gitattributes")
    print(f"Ignore list: {ignore_list}")

    included_files = get_included_files(repo_path, ignore_list, args.file_list)
    if args.dry_run:
        for file in included_files:
            print(file, file=sys.stderr)
        return

    output_file_path = args.output
    if args.copy:
        # set output to stringIO
        output_file = io.StringIO()
    else:
        output_file = open(output_file_path, "w")

    with output_file:
        if args.preamble:
            preamble = args.preamble
        elif args.preamble_file:
            with open(args.preamble_file, "r") as pf:
                preamble = pf.read()
        else:
            preamble = DEFAULT_PREAMBLE_GIT_REPO
        output_file.write(f"{preamble}\n")

        # process_repository(repo_path, output_file, ignore_list, args.file_list)
        write_files_to_output(included_files, output_file)

        output_file.write("--END--")

        if not args.no_epilogue:
            if args.epilogue:
                epilogue = args.epilogue
            elif args.epilogue_file:
                with open(args.epilogue_file, "r") as ef:
                    epilogue = ef.read()
            else:
                epilogue = DEFAULT_EPILOGUE
            output_file.write(f"\n\n{epilogue}\n")

        if args.copy:
            import pyperclip

            pyperclip.copy(content := output_file.getvalue())  # type: ignore
            print(f"Prompt copied to clipboard. Total chars: {len(content)}")
        else:
            print(
                f"Repository contents written to {output_file_path}. Total chars: {output_file.tell()}"
            )


if __name__ == "__main__":
    main()
