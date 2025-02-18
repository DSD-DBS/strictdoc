Release Notes
$$$$$$$$$$$$$

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 0dd2649ec4784c9480eac6f4aef3158b

This document maintains a record of all changes to StrictDoc since November 2023. It serves as a user-friendly version of the changelog, complementing the automatically generated, commit-by-commit changelog available as GitHub releases: `StrictDoc Releases <https://github.com/strictdoc-project/strictdoc/releases>`_.

Unreleased (2024-11-XX)
=======================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - f4e63483a11b442993c47b5d0574e89b

This release introduces language-aware tracing between requirements and C++ source code.

Currently, only C++ functions can be traced using a marker like ``@relation(REQ-1, scope=function)``. The ability to add markers to classes has not yet been implemented.

A new export format has been added to generate a Doxygen tagfile for a documentation tree. When the tagfile is registered in the Doxygen configuration, requirements can be referenced using Doxygen keywords. For example: ``\relation{REQ-1, scope=function}``. Special thanks to @johanenglund for contributing the idea and helping to implement the solution.

Additionally, a minor HTML2PDF formatting issue has been resolved. Previously, RST admonitions were not rendered correctly when spanning across two pages.

0.3.0 (2024-11-21)
==================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - b39a3b3d9f8640e380dad5a2fdb75d79

This release includes an enhancement to the feature for tracing requirements to C source code.

From now on, if a ``@relation`` marker is specified in a C function declaration, StrictDoc will perform its "magic" and automatically connect the referenced requirement to the corresponding C function definition. This allows a ``@relation`` marker to be placed in the main documentation block, typically located above C function declarations, while ensuring the requirement is also linked to the function definition.

0.2.1 (2024-11-10)
==================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 26043bba142a4e739dd206e229829202

This release includes a new feature, a bug fix, and some documentation updates.

- The ``[LINK: ...]`` feature now supports linking to documents by UID. [@haxtibal]
- HTML escaping was fixed on the Diff/Changelog screen. [@haxtibal]

The documentation now includes two new pages:

- The "Feature Map" document provides a high-level overview of the major StrictDoc features from the user's perspective.
- The Troubleshooting document offers advice on clearing the user cache, one of the common solutions to user issues. We plan to expand this section with more tips over time.

0.2.0 (2024-11-04)
==================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 611e8df13d464fd1b22e5026cf3ce531

This release introduces several enhancements to the source code processing introduced in release 0.1.0.

The backend now supports improved function tracing in C, Python, and general parsing code:

- Forward ranges to C functions now include the top comment.
- Each range type is displayed in the output HTML.
- The C source code reader has been updated to support file-level scoping.
- The source code reader now caches parsed objects to disk, improving reading performance.
- Proper handling of functions inside nested Python classes has been implemented, allowing syntax like Foo.Bar.do_baz. Thanks to @haxtibal for contributing this enhancement.

Additionally, caching has been centralized, and the cache directory is now configurable. The project configuration file now supports a ``cache_dir`` option, which can be set to values such as ``./output/build``. This setting can help make caching artifacts visible alongside documentation artifacts.

0.1.0 (2024-11-01)
==================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - e37e230c932448798bd9978d4f27f32c

This backward-compatible release introduces several new features for tracing requirements to source files:

- StrictDoc now integrates with `Tree-sitter <https://tree-sitter.github.io/tree-sitter/>`_, enabling it to parse multiple programming languages. Using AST information, it achieves more precise tracing of requirements to source code.
- Language-specific parsers for Python and C have been added, allowing functions (in C and Python) or classes (in Python) to be linked to requirements.
- Both forward linking of requirements to source files and backward linking of source files to requirements are supported. These features can be used independently or together within the same project.

With this release, we are also transitioning to a more `semantic versioning <https://semver.org>`_-oriented release scheme. From now on, the MAJOR.MINOR.PATCH version components will be maintained according to the recommendations of the semantic versioning specification.

0.0.60 (2024-10-26)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 65daf4400b464021ba3cb7a06061e651

This is a bugfix release with several fixes:

- Web UI: Add 'TAG' as a supported fieldtype for requirement nodes. Previously, the UI interface would not open an element with a TAG-based field, raising a NotImplementedError. [@mplum]

- Search Screen: Prevent query failure when node is missing requested field [@mplum]

- Project Statistics: Fix generated search URLs for project statistics [@haxtibal]

0.0.59 (2024-10-13)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - e9d5e3f8f6b04647afb95bae6b2f503a

This release includes several important improvements. Thanks to @haxtibal for implementing and testing many of the implemented changes.

- Fixed multiple issues related to the handling of the UID field's format and accepted characters, both on its own and when used as part of LINK and ANCHOR tags. [@haxtibal]

- Implemented a more consistent and unified approach to escaping Jinja templates. With this change, the Jinja templates that StrictDoc uses for rendering content are now automatically escaped, except for a few known edge cases that have been handled separately. For more details, see the "HTML Escaping" section of the Design Document, which describes the rationale and approach taken. [@haxtibal]

- Extended the HTML2PDF feature to support the ``--generate-bundle-document`` option, which allows generating a single PDF document from all documents in an SDoc documentation tree.

- Additionally, a project configuration option was added to specify a custom path to the ChromeDriver used by the HTML2PDF printer. [@haxtibal]

- Enhanced the SDoc-ReqIF-SDoc roundtrip to include relation roles such as Refines, Implements, etc. These roles are now recognized in both directions. This feature was requested by a single user and requires further testing.

- Deprecated the passthrough command. All passthrough functionality has been moved to the export command under the option ``--formats=sdoc``. Users are encouraged to switch to the export command, as using passthrough will now trigger a deprecation warning. [@haxtibal]

- Fixed a bug related to editing custom (non-requirement) nodes and adding links between them, based on a report by @elfman2.

- The Python 3.7 support was removed. The lowest Python baseline will now be 3.8 for some time.

0.0.58 (2024-06-25)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - fd7f4d5b58e54f64aa43349684a675c4

This is a release with a single fix and a minor documentation update.

The ``manage auto-uid`` command is now compatible with grammars that define the ``UID`` field as ``REQUIRED: True``. Previously, StrictDoc would raise a validation message if the ``auto-uid`` command was run against a document with ``UID`` defined as a required field but containing nodes without ``UID``. The new behavior allows the ``auto-uid`` command to operate without validation and correctly creates a new UID for the node. Thanks to @simhein for reporting this issue.

@haxtibal contributed a patch to the User Guide that explains the StrictDoc convention of how the single-line (meta information) fields should be used compared to the multiline fields, such as ``STATEMENT``, ``RATIONALE``, ``COMMENT``, etc. Quoting the key part:

    Each grammar element must have exactly one content field named ``STATEMENT``, ``DESCRIPTION`` or ``CONTENT``. The content field plays a key role in the HTML user interface as well as other export formats.

    All fields before the content field are considered meta information. Meta information fields are assumed to be single-line. The content field and all following fields accept single-line and multiline strings.

See the updated User Guide for more details.

0.0.57 (2024-06-23)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - f99185cb69cf47d4bc6e1bd404b67467

This release contains a significant, non-breaking change that affects the entire StrictDoc codebase and the SDoc data model: the ``FREETEXT-TEXT`` migration.

The description of the migration and the migration paths are described in :ref:`FREETEXT-TEXT migration (June 2024) <SECTION-UG-FREETEXT-TEXT>`.

Other changes in this release:

- The validation messages for the uniqueness of MID fields were improved for the Document, Section and Requirement/Text nodes. Thanks to @bernhard-tuvsud for the improvement suggestion.

- Due to the FREETEXT-TEXT migration, it is now possible to add LINKs to arbitrary nodes, such as REQUIREMENT and TEXT. Previously, LINKs could be added only to SECTION nodes. Thanks to @haxtibal for contributing the initial implementation.

- The UI validations have been added for SingleChoice and MultipleChoice fields. Thanks to @haxtibal for contributing the multiple choice field validation.

- The experimental Graphviz/Dot traceability graph generator has been removed because this feature didn't show much value, mainly due to the static and non-programmable nature of PDF and SVG outputs produced by Graphviz.

0.0.56 (2024-06-02)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 61f17be85ac442a0b70003825d671ced

This is an intermediate bugfix release before the release which will contain major changes.

The following issues have been fixed:

`Composable documents: edge case when a single document path is provided for a document that depends on other documents (#1807) <https://github.com/strictdoc-project/strictdoc/issues/1807>`_

`backend/sdoc: validate grammar from file like a normal grammar (#1831) <https://github.com/strictdoc-project/strictdoc/issues/1831>`_. Thanks to @haxtibal for reporting this.

`backend/reqif: exporting grammar types (#1809) <https://github.com/strictdoc-project/strictdoc/issues/1809>`_. Thanks to ``@PQ`` from Discord for giving feedback about the end-to-end export/import between StrictDoc and Polarion.

`html2pdf: specify UTF-8 encoding when writing HTML file (#1816) <https://github.com/strictdoc-project/strictdoc/issues/1816>`_. Thanks to @npalluat for reporting this based on their experience of running StrictDoc on Windows.

`backend/sdoc: allow using "DESCRIPTION" or "CONTENT" field instead of "STATEMENT" (#1827) <https://github.com/strictdoc-project/strictdoc/issues/1827>`_  Previously only STATEMENT could be used as a reserved statement field. Now StrictDoc will auto-detect two more alternative fields if they are present: ``DESCRIPTION`` or ``CONTENT``. Thanks to @haxtibal for requesting this and explaining the use case.

`pyproject.toml: update python-datauri (#1820) <https://github.com/strictdoc-project/strictdoc/issues/1820>`_ @DomenicP reported an issue to ``python-datauri`` which StrictDoc depends on. They ``ran into an integration issue with the datauri library installing tests to the virtual environment. The library maintainer was kind enough to quickly resolve the issue in fcurella/python-datauri#14.`` Thanks @DomenicP!

0.0.55 (2024-04-28)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 00abb07e55534a75a8cfd50d8cfc5732

The ReqIF export/import feature was extended to support three new command-line options for an improved export/import interfacing with Polarion. See :ref:`ReqIF options <SECTION-UG-ReqIF-options>` for more details.

The Composable Documents feature was extended to support copying assets to the HTML output folder in a redundant way in the case when an included document is stored in a different directory than the parent including document. See https://github.com/strictdoc-project/strictdoc/issues/1777 for the problem definition. Thanks to @Briceus from StrictDoc's Discord channel for reporting this issue.

StrictDoc's caching feature was extended to work around pickling errors when an outdated item is found in a cache. Such issues happen due to the (rare) refactorings in StrictDoc's data model. In this specific case, the previous ``FragmentFromFile`` Python class was renamed to ``DocumentFromFile`` and that caused problems when unpickling outdated cached content on a user machine. Thanks to @nashif for reporting this.

0.0.54 (2024-04-17)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - e5bf489ac0684ea4b626574b5439c7dd

1) Two improvements were made to the Composable Documents feature, when included document's root node is edited in including document:

- If a document is included to another document, now it is possible to edit a title and a free text of the included document.
- It is now possible to add nodes below, above, and inside a root node of an included document. Previously, the UI controls for adding any nodes from the root node were disabled.

2) HTML2PDF feature was updated to support printing UTF8-based documents on Windows.

3) The feature that allows moving TOC (Table of Contents) nodes using drag-and-drop has been enhanced. Now, each TOC element maintains its open or closed state independently of its parent section. Previously, there was some dependency between child and parent TOC nodes, which made quick editing of the TOC more challenging.

0.0.53 (2024-04-01)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 2ac296f6326b4481beb7d67b95dbb23c

The JSON export algorithm was extended to support composable documents. By default, the included documents are exported only as part of their including documents. To export both the including documents and included documents' standalone SDoc content, the option ``--included-documents`` option has to be specified with the ``export`` command.

All code related to pybtex/BibTeX bibliographies has been removed from the StrictDoc project tree. This work was left unfinished for a long time and became unused legacy code over time. See the PR: `Remove all BibTeX bibliography-related code and pybtex dependency <https://github.com/strictdoc-project/strictdoc/pull/1744>`_ for more explanation.

0.0.52 (2024-03-25)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 72d6e38e89cc471b8d3f46ae5654e0e6

The **Grammar from File** feature has been implemented. Now it is possible to declare a usual StrictDoc ``[GRAMMAR]`` in a dedicated file with an ``.sgra`` extension. When a grammar is declared in a separate file, it is possible to share this grammar between several documents. Editing of the grammars defined in ``.sgra`` files can be only done with a text editor, it is not implemented yet in the editable web interface.

0.0.51 (2024-03-20)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - e81c4206bcb148979762ee3f2aa5c9ba

This is a bugfix release with only one change.

A regression was introduced during recent internal refactoring, resulting in malfunctions on the Search screen when opening search links like "Find all requirements" or "Find all sections." This release fixes the introduced regression.

0.0.50 (2024-03-19)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - a9d7c449d1a7400496504926c744e500

**Breaking change:** The "Fragments" feature has been replaced by the "Composable documents" feature:

- The command ``[FRAGMENT_FROM_FILE]`` has been renamed to ``[DOCUMENT_FROM_FILE]``.
- Rather than importing section-like fragments, standard SDoc documents can now be included within other SDoc documents.
- The web interface has been updated to support viewing and editing documents both as standalone items and when they are included in other documents.
- Not everything related to the composable documents has been implemented. For example, the ability to drag and drop TOC (Table of Contents) nodes in documents that include other documents. Currently, moving the TOC in documents that include other documents is disabled.
- Further work for the editable web interface can be found here: https://github.com/strictdoc-project/strictdoc/issues/1698.

----

**Other changes:**

- The functionality of the HTML2PDF script on Windows has been corrected for scenarios where StrictDoc is operated within a virtual environment. Special thanks to @Timotheous for highlighting this issue.

0.0.49 (2024-03-11)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 0b8c8f40923744b089845afeb44223e9

The web interface code has been extended to allow editing arbitrary nodes. Previously, only editing the REQUIREMENT type was possible. From now on, it is possible to use the web interface to create custom grammar elements and nodes of corresponding grammar element types.

A basic JSON export feature has been added. Now it is possible to export a StrictDoc project tree to a single JSON file with a structure that mirrors the structure of the SDoc grammar.

Thanks to the work by @dahbar, the SDoc grammar and the web interface have been extended to allow assigning a human title to each field of a grammar element. For example, the ``UID`` field can be now displayed as ``Unique identifier`` in the web interface and the static HTML export.

The layout of the PDF document generated by the HTML2PDF conversion process has been improved. Several edge cases, such as the breaks between sentences, have been fixed.

The source file identification mechanism of the requirement-to-source traceability feature has been expanded to locate all source files present in a given source input directory. Previously, it was limited to finding files with specific extensions such as .c, .py, .sdoc, .rst, among others. This restriction, originally implemented for historical reasons, has now been removed. Moreover, StrictDoc has now integrated the ``get_lexer_by_name()`` function to automatically identify a lexer based on a source file's extension. This enhancement help StrictDoc to offer syntax highlighting tailored specifically to the format of each source file. Previously, StrictDoc's code directly hardcoded only a limited selection of Pygments' lexers. Thanks to @KlfJoat for helping us to prioritize and fix this issue sooner.

The Excel export algorithm was extended to support generating multiple Excel files for documentation tree with requirements that link to each other across documents. The issue manifested itself as ``KeyError``. Thanks to @Dynteq for reporting this.

0.0.48 (2024-01-24)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - 6cff333594d6430886053b59b265e806

The requirement-to-source traceability feature was extended to support linking requirements to the RST files.

One more input scenario was handled for the Create Document workflow. When a project config has ``include_doc_paths`` or ``exclude_doc_paths`` filters specified, and an input document path contradicts to the provided filters, a validation message is shown.

The Project Statistics screen was extended with the **"Sections without any text" metric**. Now it is possible to visualize which sections are still missing any introduction or description (free text).

**The new Machine Identifier (MID)** field has been added to StrictDoc's grammar. The automatic generation of MIDs can be activated per-document using the ``ENABLE_MID: True`` document-level config option. The main driver for this feature is the need of accurate Diff/Changelog results. The new section of the User Guide explains the rationale and the configuration details: :ref:`Machine identifiers (MID) <SECTION-UG-Machine-identifiers-MID>`.

**The Diff and Changelog screens** have been introduced to facilitate a historical comparison of documentation trees. The Diff screen aids in focusing on which document nodes have been altered, while the Changelog functions as a sequential table where changes are displayed as table cells and each cell emphasizes specific details of a particular change.

The Requirements Coverage has been transformed into **the Traceability Matrix** screen. This matrix screen lists all nodes of a documentation graph, along with all their interrelations. The currently generated screen is entirely static. However, future enhancements are planned to include filtering capabilities for the content. The Traceability Matrix feature is disabled by default and has to be activated as ``TRACEABILITY_MATRIX_SCREEN`` in the strictdoc.toml project config file.

**The HTML2PDF feature** has now entered the alpha testing phase. This feature enables printing of documents directly from a browser, which can be done either through the "PDF" screen view or by utilizing the "Export to PDF" button. By default, the HTML2PDF feature is disabled. To activate it, you need to indicate the ``HTML2PDF`` feature in the strictdoc.toml project configuration file.

0.0.47 (2023-11-20)
===================

.. list-table::
    :align: left
    :header-rows: 0

    * - **MID:**
      - c422af340d5b45c48bfe89130e1bba52

A **query search engine** is introduced which allows filtering a documentation tree by queries like ``(node.is_requirement and "System" in node["TITLE"])``.
Building on the search engine capability, the "Search" screen is introduced in the web interface. Additionally, it is now possible to specify ``--filter-requirements <query>`` and ``filter-sections <query>`` when running ``export`` and ``passthrough`` commands. The visual design of the project statistics was improved as well as the new design for the search screen has already landed.

The **document option** ``ROOT: True/False`` was introduced to indicate the root documents in the traceability graph. Currently, this option is only used when printing requirement statistics, where the root nodes are skipped when the metric "requirements without parents" is calculated. The root-level requirements by definition have no parent requirements, they can only be parents to other requirements.

When editing Section, **it is now possible to auto-generate a section UID with a corresponding button** which makes the management of section UIDs much easier.

The **stability and the execution time of the CI end-2-end tests for the web interface has been increased**. The sharding of the end-2-end tests was introduced for all systems: macOS, Linux, and Windows. At the same time, the number of Python versions that are tested by each platform's jobs was reduced to maintain a reasonable total number of build jobs.

The requirement-to-source traceability feature was extended with the so-called **single-line markers**. Now it is possible to reference just a single line in a file by using the ``@sdoc(REQ-001)`` marker.

Python 3.12 support has been added to the GitHub CI jobs.

The second generation of StrictDoc's requirements received many updates. The new requirements set will be incorporated to the main documentation very soon (estimated time is until the end of 2023). These requirements are maintained in the ``drafts/requirements`` folder.

The User Guide has been updated to include the **"Security Considerations" chapter**, which provides a warning about unsafe use of StrictDoc if it is deployed to a server on a public network.
