import sys
from pathlib import Path

# from collections import namedtuple
from typing import Any, List, Optional

import click

# from beepy import beep
from click import ClickException
from rich import print
from rich.pretty import pprint

from . import __version__
from .build_doc import DocBuilder
from .build_html import HTMLBuilder
from .core import Core
from .pandoc import print_pandoc_info

# from .build_latex import build_latex
from .report import Report
from .setup import setup_github_action


def logo(version: str) -> str:
    return (
        R""" ___ __  __ ____ ____ ____ __  __   __   ____ _  _
/ __|  )(  |  _ ( ___|  _ (  \/  ) /__\ (  _ ( )/ )
\__ \)(__)( )___/)__) )   /)    ( /(__)\ )   /)  (
(___(______|__) (____|_)\_|_/\/\_|__)(__|_)\_|_)\_) """
        + version
    )


def logo_2(version: str) -> str:
    return """[bold]SUPERMARK[/bold] """ + version


@click.version_option(version=__version__)
@click.group()
# @click.version_option(__version__)
def supermark():
    ...


# PathSetup = namedtuple('input', 'output', "template")


class PathSetup:
    def __init__(self, base: Path, input: Path, output: Path, template: Path) -> None:
        self.base = base
        self.input = input
        self.output = output
        self.template = template


def ensure_path(path: Any) -> Optional[Path]:
    if path is None:
        return None
    elif isinstance(path, Path):
        return path
    elif isinstance(path, bytes):
        return Path(path.decode("utf-8"))
    elif isinstance(path, str):
        return Path(path)
    else:
        raise ValueError()


def setup_paths(
    path: Optional[Path],
    input: Optional[Path],
    output: Optional[Path],
    template: Optional[Path],
    core: Core,
) -> PathSetup:
    base_path = path or Path.cwd()
    input_path = None
    output_path = None
    template_path = None

    if core.config.has_config("input") and input is None:
        input_path = base_path / core.config.get("input")
    if core.config.has_config("output") and output is None:
        output_path = base_path / core.config.get("output")
    if core.config.has_config("template") and template is None:
        template_path = base_path / core.config.get("template")

    if input_path is None:
        input_path = base_path / "pages"
    if output_path is None:
        output_path = output or Path.cwd()
    if template_path is None:
        template_path = template or (base_path / "templates/page.html")
    return PathSetup(base_path, input_path, output_path, template_path)


@supermark.command(help="Build a project, site or document.")
@click.option(
    "-a",
    "--all",
    is_flag=True,
    default=False,
    help="Rebuild all pages, not only modified ones.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    help="Provide more feedback on what is happening.",
)
@click.option(
    "-d",
    "--draft",
    is_flag=True,
    default=False,
    help="Also print draft parts of the documents.",
)
@click.option(
    "-c",
    "--continuous",
    is_flag=True,
    default=False,
    help="Observe the source directory and run continuously.",
)
@click.option(
    "-p",
    "--path",
    "path",
    type=click.Path(exists=True, readable=True, path_type=Path),
    help="Base path pointing to the folder that contains input, template, output path and an optional config file.",
)
@click.option(
    "-i",
    "--input",
    "input",
    type=click.Path(exists=True, readable=True, path_type=Path),
    help="Input directory containing the source files.",
)
@click.option(
    "-o",
    "--output",
    "output",
    type=click.Path(exists=True, writable=True, path_type=Path),
    help="Output directory.",
)
@click.option(
    "-t",
    "--template",
    "template",
    type=click.File("rb"),
    help="Template file for the transformation.",
)
@click.option(
    "-r",
    "--reformat",
    is_flag=True,
    default=False,
    help="Reformat the input file.",
)
@click.option(
    "-l",
    "--log",
    is_flag=True,
    default=False,
    help="Write messages to a log file instead of standard output.",
)
@click.option(
    "-u",
    "--urls",
    is_flag=True,
    default=False,
    help="Check external URLs for reachability.",
)
def build(
    all: bool,
    verbose: bool,
    draft: bool,
    continuous: bool,
    path: Optional[Path] = None,
    input: Optional[Path] = None,
    output: Optional[Path] = None,
    template: Optional[Path] = None,
    reformat: bool = False,
    log: bool = False,
    urls: bool = False,
):
    report = Report(verbose=verbose)
    core = Core(report=report, check_external_urls=urls)
    print(logo_2(__version__))
    print_pandoc_info(report)
    report.info(f"Installed Python version: {sys.version}")

    path_setup = setup_paths(path, input, output, template, core)

    builder = HTMLBuilder(
        path_setup.input,
        path_setup.output,
        path_setup.base,
        path_setup.template,
        report,
        rebuild_all_pages=all,
        abort_draft=not draft,
        verbose=verbose,
        reformat=reformat,
    )
    builder.set_core(core)
    builder.build()

    core.url_checker.check(path_setup.input)

    builder.copy_resources()

    report.print()
    if log:
        report.print_to_file(path_setup.base / "supermark.log")
    else:
        if report.has_error():
            # beep(3)  # sad error
            ex = ClickException("Something is wrong.")
            ex.exit_code = 1
            raise ex
    # else:
    # beep(5)


@supermark.command(help="Show info about a project and installation.")
def info():
    report = Report()
    core = Core(report=report)
    core.info()


@supermark.command(help="Add documentation pages.")
@click.option(
    "-i",
    "--input",
    "input",
    type=click.Path(exists=True, readable=True, path_type=Path),
    help="Input directory containing the source files.",
)
def doc(
    input: Optional[Path] = None,
):
    report = Report()
    core = Core(report=report)
    path_setup = setup_paths(None, input, None, None, core)
    builder = DocBuilder(
        path_setup.input,
        path_setup.output,
        path_setup.base,
        path_setup.template,
        report,
        verbose=True,
    )
    builder.set_core(core)
    builder.build()

    # pm = PageMapper(path_setup.input, core, report)
    # print(pm.get_html())
    #     # build the page map
    # pm = PageMapper(self.input_path, self.core, self.report)
    # target_file_path = self.output_path / "pagemap.html"
    # html: List[str] = []
    # indent = ""
    # if pm.root.index_path is not None:
    #     target = get_relative_path(
    #         target_file_path, self.get_target_file(pm.root.index_path)
    #     )
    #     html.append(indent + f'<a href="{target}">{pm.root.title}</a>')
    # else:
    #     html.append(indent + f'<a href="#">{pm.root.title}</a>')
    # self._get_html_folder(pm.root, target_file_path, html)
    # write_file("\n".join(html), target_file_path, self.report)

    # # build the breadcrumbs
    # # print(yaml.dump(pm.root.get_list(self.input_path)))

    # # for folder in pm.get_all_folders_with_index_paths():
    # #    self._write_links(folder)


@supermark.command(help="Setup a project.")
@click.option(
    "-g",
    "--githubaction",
    "githubaction",
    is_flag=True,
    default=False,
    help="Add a Github action so that projects are built after each commit.",
)
@click.option(
    "-p",
    "--path",
    "path",
    type=click.Path(exists=True, readable=True, path_type=Path),
    help="Base path containing the source files. Current working directory is default.",
)
def setup(
    githubaction: bool = False,
    path: Optional[Path] = None,
):
    base_path = path or Path.cwd()
    if githubaction:
        setup_github_action(base_path)


@supermark.command(help="Perform some cleanup tasks.")
@click.option(
    "-h",
    "--html",
    "html",
    is_flag=True,
    default=False,
    help="Remove *.html files that do not have corresponding source files.",
)
def clean(
    html: bool = False,
):
    report = Report()
    core = Core(report=report)

    path_setup = setup_paths(None, None, None, None, core)

    if html:
        html_files: List[Path] = []
        files = list(path_setup.input.glob("*.md"))
        for source_file_path in files:
            html_files.append(path_setup.output / (source_file_path.stem + ".html"))
        files = list(path_setup.output.glob("*.html"))
        html_files_to_delete: List[Path] = []
        for output_file_path in files:
            if output_file_path not in html_files:
                html_files_to_delete.append(output_file_path)
        if len(html_files_to_delete) > 0:
            pprint(
                f"This would delete the following files from folder {path_setup.output}"
            )
            pprint(
                [
                    file.relative_to(path_setup.output).name
                    for file in html_files_to_delete
                ]
            )
            if click.confirm("Do you want to delete these files?"):
                for html_file in html_files_to_delete:
                    html_file.unlink(missing_ok=True)
        else:
            pprint("No files found to delete.")
