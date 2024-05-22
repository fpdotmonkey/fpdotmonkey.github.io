import html
import os
from typing import Dict, List, Optional

import bibtexparser

PAGE_TEMPLATE = """
+++
title = "Publications"
author = ["Fletcher Porter"]
draft = false
+++
<div>
    <style>
 :target {{
     background: AntiqueWhite;
 }}

 label {{
     cursor: pointer;
     color: #5E0703;
     text-decoration: underline;
 }}

 .bib-artifact-container {{
     margin: -10px 0 10px 0;
 }}

 .bib-artifact {{
     font-family: monospace;
     font-size: 12pt;
     user-select: none;
 }}

 textarea {{
     -webkit-user-select: all;
     user-select: all;
     width: 300px;
 }}

 input[type=checkbox] {{
     display: none;
 }}

 .bib-check:checked ~ .bib-src {{
     display: none;
 }}

 .abstract-check:checked ~ .abstract-src {{
     display: none;
 }}
    </style>
    {entries}
</div>

"""

ENTRY_TEMPLATE = """
<div id="{key}">
    {reference}
    <div class="bib-artifact-container">
	{abstract_control}
	{pdf}
	{doi}
	<input type="checkbox" class="bib-check" id="{key}bib" checked="">
	<label class="bib-artifact" for="{key}bib"> [bib]</label>
	<div class="bib-src">
	    <textarea readonly="true">{bib}</textarea>
        </div>
	{abstract}
    </div>
</div>
"""

PDF_TEMPLATE = '<a class="bib-artifact" href="{pdf}">[pdf]</a>'
DOI_TEMPLATE = '<a class="bib-artifact" href="https://doi.org/{doi}">[doi]</a>'
ABSTRACT_CONTROL_TEMPLATE = '<input type="checkbox" class="abstract-check" id="{key}abs" checked="">\n<label class="bib-artifact" for="{key}abs">[abstract]</label>'
ABSTRACT_TEMPLATE = '<blockquote class="abstract-src">{abstract}</blockquote>'


def main():
    library = bibtexparser.parse_file("publications.bib")
    publications = [Publication(entry) for entry in library.entries]
    print(
        PAGE_TEMPLATE.format(
            entries="\n".join(
                (
                    publication.format()
                    for publication in sorted(publications)
                )
            )
        )
    )


class Publication:
    _bib: str
    _key: str
    _reference_data: dict
    _doi: Optional[str]
    _abstract: Optional[str]
    _pdf: Optional[str]

    def __init__(self, entry) -> None:
        self._key = entry.key
        self._reference_data = entry.fields_dict
        self._abstract = self._reference_data.get("abstract")
        if self._abstract is not None:
            self._abstract = (
                "<p>"
                + str(
                    html.escape(self._abstract.value).replace("\n", "</p><p>")
                )
                + "</p>"
            )
        self._pdf = self._reference_data.get("file")
        if self._pdf is not None:
            self._pdf = str(self._pdf.value)
        self._doi = self._reference_data.get("doi")
        if self._doi is not None:
            self._doi = str(self._doi.value)
        self._bib = entry.raw

    def format(self) -> str:
        return ENTRY_TEMPLATE.format(
            reference=self.reference(),
            key=html.escape(self._key),
            bib=html.escape(self._bib),
            abstract_control=(
                ABSTRACT_CONTROL_TEMPLATE.format(key=self._key)
                if self._abstract is not None
                else ""
            ),
            abstract=(
                ABSTRACT_TEMPLATE.format(abstract=self._abstract)
                if self._abstract is not None
                else ""
            ),
            pdf=(
                PDF_TEMPLATE.format(pdf=self._pdf)
                if self._pdf is not None
                else ""
            ),
            doi=(
                DOI_TEMPLATE.format(doi=self._doi)
                if self._doi is not None
                else ""
            ),
        )

    def reference(self) -> str:
        authors = self._reference_data.get("author").value.split(" and ")
        author_line = None
        display_authors = []
        for author in authors:
            if "," in author:
                # last name is first
                display_authors.append(
                    " ".join(reversed(author.split(",", maxsplit=1))).strip()
                )
            else:
                # first name is first
                display_authors.append(author)
        if len(display_authors) <= 2:
            author_line = " and ".join(display_authors)
        else:
            author_line = (
                ", ".join(display_authors[:-1])
                + ", and "
                + display_authors[-1]
            )
        author_line += ".  "

        title = self._reference_data.get("title").value.translate(
            str.maketrans("", "", "}{")
        )
        booktitle = self._reference_data.get("booktitle").value.translate(
            str.maketrans("", "", "}{")
        )

        title_line = '"' + title + '", '
        book_title_line = (
            "<i>"
            + booktitle
            + "</i>, "
            + self._reference_data.get("year").value
            + "."
        )

        return author_line + title_line + book_title_line

    def __lt__(self, other) -> bool:
        if (
            self._reference_data.get("year").value
            < other._reference_data.get("year").value
        ):
            return True

        authors = self._reference_data.get("author").value.split(" and ")
        o_authors = other._reference_data.get("author").value.split(" and ")
        for i in range(min(len(authors), len(o_authors))):
            sort_author = None
            sort_o_author = None
            if "," in authors[i]:
                # last name is first
                sort_author = authors[i]
            else:
                # first name is first
                sort_author = ", ".join(
                    reversed(authors[i].split(" ", maxsplit=1))
                ).strip()
            if "," in o_authors[i]:
                sort_o_author = o_authors[i]
            else:
                sort_o_author = ", ".join(
                    reversed(o_authors[i].split(" ", maxsplit=1))
                ).strip()
            if sort_author < sort_o_author:
                return True
        return False


if __name__ == "__main__":
    main()
