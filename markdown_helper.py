#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-17 ‏‎15:48:59
# @Author  : Lewis Tian (taseikyo@gmail.com)
# @Link    : github.com/taseikyo
# @Version : python3.8

"""
A simple st3 plugin can help write markdown faster (maybe)
Note: Remember to select the entire line and then press the shortcuts
---
shortcuts:
    ctrl + 1-3: h1 - h3
    ctrl + 4: ul
    ctrl + 5: ol
    ctrl + 6: code (block codes)
    ctrl + 7: latex formula (block)
"""


import sublime
import sublime_plugin

PLUGIN_NAME = "MarkdownHelper"


def load_settings():
    return sublime.load_settings(PLUGIN_NAME + ".sublime-settings")


class PluginEventListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key == "helper_is_enabled":
            settings = load_settings()
            allows = settings.get("allow_fileformats")
            syntax = view.settings().get("syntax").split("/")[-1].split(".")[0]
            if syntax.lower() in allows:
                return True
        return False


class MarkdownHelperCommand(sublime_plugin.TextCommand):
    def run(self, edit, md_type):
        """
        select function according $md_type
        """
        if md_type[0] == "h":
            self.helper_hx(edit, int(md_type[1]))
        elif md_type == "ul":
            self.helper_ul(edit)
        elif md_type == "tl":
            self.helper_tl(edit)
        elif md_type == "ol":
            self.helper_ol(edit)
        elif md_type == "code":
            self.helper_code(edit)
        elif md_type == "icode":
            self.helper_text(edit, "`")
        elif md_type == "lxf":
            self.helper_lxf(edit)
        elif md_type == "ilxf":
            self.helper_text(edit, "$")
        elif md_type == "bt":
            self.helper_text(edit, "**")
        elif md_type == "it":
            self.helper_text(edit, "*")
        elif md_type == "dt":
            self.helper_text(edit, "~~")
        elif md_type == "img":
            self.helper_text(edit, "![](", ")")

    def helper_h1(self, edit):
        """
        generate h1 title
        ---
        xxx => # xxx
        """
        # region consists many lines
        # so we use `self.view.lines` to get all the lines (type: region)
        for region in self.view.sel():
            if not region.empty():
                line = self.view.line(region)
                # st3 uses py3.3, we cannot use f-strings ;(
                text = "# " + self.view.substr(line).lstrip()
                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, line.begin(), text)

    def helper_hx(self, edit, level):
        """
        generate hx title
        ---
        xxx => # xxx
        xxx => ## xxx
        ...
        """
        # region consists many lines
        # so we use `self.view.lines` to get all the lines (type: region)
        for region in self.view.sel():
            if not region.empty():
                subregions = self.view.lines(region)
                new_text = []
                for subregion in subregions:
                    line = self.view.line(subregion)
                    # st3 uses py3.3, we cannot use f-strings ;(
                    text = "#" * level + " " + self.view.substr(line).lstrip() + "\n"
                    new_text.append(text)

                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, subregions[0].begin(), "".join(new_text))

    def helper_ul(self, edit):
        """
        generate unordered list
        ---
        aaa
        bbb
        ccc
        =>
        - aaa
        - bbb
        - ccc
        """
        for region in self.view.sel():
            if not region.empty():
                subregions = self.view.lines(region)
                new_text = []
                for subregion in subregions:
                    line = self.view.line(subregion)
                    # st3 uses py3.3, we cannot use f-strings ;(
                    text = "- " + self.view.substr(line).lstrip() + "\n"
                    new_text.append(text)

                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, subregions[0].begin(), "".join(new_text))

    def helper_tl(self, edit):
        """
        generate task list
        ---
        aaa
        bbb
        ccc
        =>
        - [] aaa
        - [] bbb
        - [] ccc
        """
        for region in self.view.sel():
            if not region.empty():
                subregions = self.view.lines(region)
                new_text = []
                for subregion in subregions:
                    line = self.view.line(subregion)
                    # st3 uses py3.3, we cannot use f-strings ;(
                    text = "- [ ] " + self.view.substr(line).lstrip() + "\n"
                    new_text.append(text)

                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, subregions[0].begin(), "".join(new_text))

    def helper_ol(self, edit):
        """
        generate ordered list
        ---
        aaa
        bbb
        ccc
        =>
        1. aaa
        2. bbb
        3. ccc
        """
        for region in self.view.sel():
            if not region.empty():
                subregions = self.view.lines(region)
                new_text = []
                for index, subregion in enumerate(subregions):
                    line = self.view.line(subregion)
                    # st3 uses py3.3, we cannot use f-strings ;(
                    text = (
                        str(index + 1) + ". " + self.view.substr(line).lstrip() + "\n"
                    )
                    new_text.append(text)

                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, subregions[0].begin(), "".join(new_text))

    def helper_code(self, edit):
        """
        generate code
        ---
        aaa
        bbb
        =>
        ```
        aaa
        bbb
        ```
        """
        for region in self.view.sel():
            if not region.empty():
                # Packages/Python/Python.tmLanguage
                # stupid method, this will always return `Markdown`
                syntax = self.view.settings().get("syntax").split("/")[-1].split(".")[0]
                line = self.view.line(region)
                # st3 uses py3.3, we cannot use f-strings ;(
                text = "```" + syntax + "\n" + self.view.substr(line) + "\n```\n"
                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, line.begin(), text)

    def helper_lxf(self, edit):
        """
        generate latex formula
        ---
        aaa
        bbb
        =>
        $$
        aaa
        bbb
        $$
        """
        for region in self.view.sel():
            if not region.empty():
                line = self.view.line(region)
                # st3 uses py3.3, we cannot use f-strings ;(
                text = "$$\n" + self.view.substr(line) + "\n$$\n"
                # remove the old text and insert...
                self.view.erase(edit, region)
                self.view.insert(edit, line.begin(), text)

    def helper_text(self, edit, begin_char, end_char=""):
        """
        generate style text
        ---
        bt => bold text: aaa -> **aaa**
        it => italic text: aaa -> *aaa*
        dt => delete textL aaa -> ~~aaa~~
        """
        for region in self.view.sel():
            if not region.empty():
                code = self.view.substr(sublime.Region(region.a, region.b))
                # replace(edit, region, string)
                self.view.replace(
                    edit,
                    region,
                    begin_char + code + (end_char if end_char else begin_char),
                )
