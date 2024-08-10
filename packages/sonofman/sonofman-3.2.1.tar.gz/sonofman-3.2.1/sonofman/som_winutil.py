#!/usr/bin/env python3
import re
# import sys

import sonofman.som_unicurses as u


class WinUtil:
    """
    Windows utils
    Don't change value of variables, use methods to do it
    """
    def __init__(self, win_ref, win_lines, win_cols, win_top_border_lines, win_bottom_border_lines, colors, color_theme):
        self.win_ref = win_ref
        self.win_lines = win_lines
        self.win_cols = win_cols
        self.win_top_border_lines = win_top_border_lines
        self.win_bottom_border_lines = win_bottom_border_lines
        self.s_line_pos = 0
        self.s_lines_max = 0
        self.s_lst = []
        self.s_dict_expr = {}
        self.s_query_expr = ""
        self.colors = colors
        self.color_theme = color_theme

    @staticmethod
    def get_delimiter_perc():
        return "%"

    """
    Get attributes, code color associated to a color key
    """
    def get_color(self, color_key):
        attr = u.A_NORMAL
        code_color = None

        color_item = self.colors[color_key].split("#")
        if len(color_item) == 2:
            attr = color_item[0]
            if len(attr) > 0:
                attr = attr.replace("A_", "u.A_")
                attr = eval(attr)
            else:
                attr = u.A_NORMAL

            code_color = color_item[1]
            if len(code_color) > 0:
                code_color = code_color.replace("COLOR", "")
                code_color = eval("u.color_pair({0})".format(code_color))
            else:
                code_color = None
        return attr, code_color

    def move(self, step):
        """
        param step: +1, -1, 0=set to 0
        :return True: move possible, False: stop refreshing
        """
        if step == 0:
            self.s_line_pos = 0
        else:
            if step < 0 and self.s_line_pos == 0:
                return False

            new_line_pos = self.s_line_pos + (step * self.win_lines)
            if new_line_pos > self.s_lines_max:
                return False
            elif new_line_pos < 0:
                self.s_line_pos = 0
            else:
                self.s_line_pos = new_line_pos
        return True

    @staticmethod
    def wrap_verse(width, verse, verse_bbname):
        try:
            current_row = []
            lst_word = verse.split(" ")
            lst_wrap = []

            row_size = 0
            for word in lst_word:
                word_size = len(word)
                if (row_size + word_size + 1) <= width:
                    current_row.append(word)
                    current_row.append(" ")
                    row_size = row_size + word_size + 1
                else:
                    lst_wrap.append("".join(str(w) for w in current_row))
                    current_row.clear()

                    current_row.append(word)
                    current_row.append(" ")
                    row_size = word_size + 1

            # Last
            verse_part = "".join(str(w) for w in current_row)
            lst_wrap.append(verse_part)

            current_row.clear()
            lst_word.clear()

            return lst_wrap
        except Exception as ex:
            raise ex

    def wrap_string(self, string, width, query_expr):
        # noinspection PyBroadException
        """
        :return: all rows wrapped and all expr found
        """
        try:
            lst_wrapped = []
            dict_expr = {}
            regex_query_expr = query_expr.replace(self.get_delimiter_perc(), ".*")

            # For all verses
            lst_v_split = []
            lst_v_full_wrap_temp = []
            limit_item = {}
            v = []

            for v in string:
                lst_v_split = v[0].replace("§", "\n").splitlines()
                ref = v[1]
                v_bbname = ref[1]

                lst_v_full_wrap_final = []
                lst_v_full_wrap_limit_final = []
                lst_v_full_wrap_expr_final = []

                # For all verses cleaned
                for v_full in lst_v_split:
                    is_verse_and_expr_not_empty = len(regex_query_expr) > 0 and len(v_full) > 0

                    if v_full == "":
                        jitem = ["", ""]
                        lst_v_full_wrap_final.append(jitem)
                    else:
                        lst_v_full_wrap_temp = self.wrap_verse(width, v_full, v_bbname)
                        bbname = ""

                        # For each parts of a verse: we add ref
                        for j in lst_v_full_wrap_temp:
                            jitem = [j, ref]
                            if ref == ['', '']:
                                if len(j) >= 2:
                                    new_bbname = j[0:2]
                                    if new_bbname in ('k|', 'l|', 'v|', 'd|', 'a|', 'o|', 's|', '2|', '9|', '1|', 'i|', 'y|', 'c|', 'j|', 'r|', 't|', 'b|', 'h|', 'e|', 'u|', 'z|'):
                                        bbname = new_bbname
                                    if bbname in ('k|', 'l|', 'v|', 'd|', 'a|', 'o|', 's|', '2|', '9|', '1|', 'i|', 'y|', 'c|', 'j|', 'r|', 't|', 'b|', 'h|', 'e|', 'u|', 'z|') and not(jitem[0].startswith(bbname)):
                                        jitem[0] = "{0}{1}".format(bbname, jitem[0])

                            # Align
                            """
                            extra_space_bbname = j[0:2]
                            if extra_space_bbname == "y|":
                                extra_space_len = self.win_cols - wcwidth.wcswidth(jitem[0]) - 2
                                if extra_space_len > 0:
                                    jitem[0] = "{0}{1}{2}".format(extra_space_bbname, " " * extra_space_len, jitem[0][2:])
                            """

                            # All verse parts will have ref. bbname is only prefixed in first row
                            lst_v_full_wrap_final.append(jitem)

                    # Find all limits of a verse wrapped
                    limit_item = {}
                    if is_verse_and_expr_not_empty:
                        limit_nr = 0
                        limit_start = 0
                        limit_end = 0

                        for item in lst_v_full_wrap_final:
                            part_len = len(item[0]) 
                            if part_len == 0:
                                continue
                            limit_end += part_len - 1
                            limit_item = {
                                "limit_nr": limit_nr,
                                "limit_start": limit_start,
                                "limit_end": limit_end
                            }

                            lst_v_full_wrap_limit_final.append(limit_item)

                            # Next
                            limit_nr += 1
                            limit_start = limit_end + 1
                            limit_end += 1

                    # Find all regex of actual verse
                    if is_verse_and_expr_not_empty:
                        matches = re.finditer(r"{0}".format(regex_query_expr), v_full, flags=re.I)
                        for match in matches:
                            lst_v_full_wrap_expr_final.append({
                                "start_orig": match.start(),
                                "row_dyn_index": -1,
                                "row_i_index": -1,
                                "start_upd": -1,
                            })
                        matches = None

                    for item in lst_v_full_wrap_final:
                        lst_wrapped.append(item)

                        if not is_verse_and_expr_not_empty:
                            continue

                        row_i_index = len(lst_wrapped) - 1  # Start at 0

                        # For all regex found in actual verse: correct start pos and find row parameters if not done yet
                        for expr in lst_v_full_wrap_expr_final:
                            if expr["row_dyn_index"] == -1:
                                start_in_verse = expr["start_orig"]

                                # Find where start is in the limits
                                limit_start_in_verse_found = False
                                for limit in lst_v_full_wrap_limit_final:
                                    if limit_start_in_verse_found is False and \
                                            limit["limit_start"] <= start_in_verse <= limit["limit_end"]:
                                        limit_start_in_verse_found = True
                                        expr["row_dyn_index"] = limit["limit_nr"]
                                        expr["row_i_index"] = expr["row_dyn_index"] + row_i_index

                                        if expr["row_dyn_index"] == 0:
                                            expr["start_upd"] = start_in_verse - limit["limit_start"] - 2   # 2: extra chars
                                        else:
                                            expr["start_upd"] = start_in_verse - limit["limit_start"]
                                        fut_row_i_index = expr["row_i_index"]

                                        # Add start_upd to lst_expr for row_i_index: dict_expr[0] = lst
                                        if fut_row_i_index not in dict_expr:
                                            dict_expr[fut_row_i_index] = []

                                        lst_expr = dict_expr[fut_row_i_index]
                                        lst_expr.append(expr["start_upd"])

                                        dict_expr[fut_row_i_index] = lst_expr
                                        break

                    # Clear infos of current verse
                    lst_v_full_wrap_final.clear()
                    lst_v_full_wrap_limit_final.clear()
                    lst_v_full_wrap_expr_final.clear()

            string = None
            v.clear()
            lst_v_split.clear()
            lst_v_full_wrap_temp.clear()
            limit_item.clear()

            return lst_wrapped, dict_expr, query_expr
        except Exception as ex:
            pass
            # TODO: was here: print_ex(ex)

    def position_in_list_by_cy(self, cy):
        """
        Screen cursor position (cy) of selection is different of real position in list
        """
        return self.s_line_pos + cy - self.win_top_border_lines

    def fill_window(self, string, from_line_nr, query_expr):
        # noinspection PyBroadException
        try:
            if string is not None:
                self.s_lst, self.s_dict_expr, self.s_query_expr = self.wrap_string(string, self.win_cols, query_expr)
                self.s_lines_max = len(self.s_lst) - 1
                self.s_line_pos = from_line_nr

            if len(self.s_lst) == 0:
                return

            u.wclear(self.win_ref)
            x = y = 0
            to_line_nr = from_line_nr + self.win_lines
            attr_highlight_search, code_color_highlight_search = self.get_color(color_key="HIGHLIGHT_SEARCH")
            # use_attr = True     # was: if len(_tbbName) > 1 else False

            # For each row [i] of display
            ref = []
            text = ""
            for i in range(from_line_nr, to_line_nr):
                text = self.s_lst[i][0]
                # DEBUG: sys.stdout.write("*** {0}".format(text))
                ref = self.s_lst[i][1]
                bbname = ref[1] if len(ref) == 2 else ""
                if bbname == "":
                    if len(text) == 0:
                        pass
                    elif text.startswith("k|"):
                        bbname = "k"
                        text = text[2:]
                    elif text.startswith("v|"):
                        bbname = "v"
                        text = text[2:]
                    elif text.startswith("l|"):
                        bbname = "l"
                        text = text[2:]
                    elif text.startswith("d|"):
                        bbname = "d"
                        text = text[2:]
                    elif text.startswith("a|"):
                        bbname = "a"
                        text = text[2:]
                    elif text.startswith("o|"):
                        bbname = "o"
                        text = text[2:]
                    elif text.startswith("s|"):
                        bbname = "s"
                        text = text[2:]
                    elif text.startswith("2|"):
                        bbname = "2"
                        text = text[2:]
                    elif text.startswith("9|"):
                        bbname = "9"
                        text = text[2:]
                    elif text.startswith("1|"):
                        bbname = "1"
                        text = text[2:]
                    elif text.startswith("i|"):
                        bbname = "i"
                        text = text[2:]
                    elif text.startswith("y|"):
                        bbname = "y"
                        text = text[2:]
                    elif text.startswith("c|"):
                        bbname = "c"
                        text = text[2:]
                    elif text.startswith("j|"):
                        bbname = "j"
                        text = text[2:]
                    elif text.startswith("r|"):
                        bbname = "r"
                        text = text[2:]
                    elif text.startswith("t|"):
                        bbname = "t"
                        text = text[2:]
                    elif text.startswith("b|"):
                        bbname = "b"
                        text = text[2:]
                    elif text.startswith("h|"):
                        bbname = "h"
                        text = text[2:]
                    elif text.startswith("e|"):
                        bbname = "e"
                        text = text[2:]
                    elif text.startswith("u|"):
                        bbname = "u"
                        text = text[2:]
                    elif text.startswith("z|"):
                        bbname = "z"
                        text = text[2:]
                elif text.startswith("{0}|".format(bbname)):
                    text = text[2:]

                attr = u.A_NORMAL
                code_color = None
                if len(text) > 0:
                    # noinspection PyBroadException
                    try:
                        if bbname in ("k", "v", "l", "d", "a", "o", "s", "2", "9", "1", "i", "y", "c", "j", "r", "t", "b", "h", "e", "u", "z"):
                            attr, code_color = self.get_color(color_key=bbname)

                        # TODO: HIGH, add bool to skip check of regex here
                        if text[0] == "#":
                            text = text[1:]
                            attr = u.A_REVERSE
                        elif text[0:4] == "_HB_":
                            text = text[4:]
                            attr = u.A_UNDERLINE + u.A_BOLD
                        elif text[0:2] == "__":
                            attr = u.A_BOLD
                        elif text[0:2] == "~~":
                            self.s_lst[i] = "-" * self.win_cols
                            text = self.s_lst[i]
                    except Exception:
                        attr = u.A_NORMAL

                if bbname in ("i", "y"):
                    code_color = None

                if not(code_color is None):
                    u.mvwaddstr(self.win_ref, y, x, text, attr + code_color)
                    cursor_yx = u.getyx(self.win_ref)
                else:
                    u.mvwaddstr(self.win_ref, y, x, text, attr)
                    cursor_yx = u.getyx(self.win_ref)
                    # DEBUG: sys.stdout.write("### {0}| ({1}, {2}) {3} {4} ".format(bbname, cursor_yx[0], cursor_yx[1], len(text), wcwidth.wcswidth(text)))

                    if bbname in ("i", "y"):
                        for x_tmp in range(0, self.win_cols):
                            u.mvwchgat(self.win_ref, y, x_tmp, 1, attr, attr, None)

                # Highlight search
                if i in self.s_dict_expr:
                    for expr_start in self.s_dict_expr[i]:
                        text_part = text[expr_start:expr_start + len(self.s_query_expr)]

                        if not (code_color_highlight_search is None):
                            u.mvwaddstr(self.win_ref, y, expr_start, text_part, attr_highlight_search + code_color_highlight_search)
                        else:
                            u.mvwaddstr(self.win_ref, y, expr_start, text_part, attr_highlight_search)

                # Alignment
                if bbname == "y":
                    x_tmp = cursor_yx[1]
                    extra_space_len = self.win_cols - x_tmp
                    if extra_space_len > 0:
                        extra_space_len = self.win_cols - x_tmp
                        u.mvwinsstr(self.win_ref, y, 0, " " * extra_space_len, "NO_USE")

                y += 1

            u.wrefresh(self.win_ref)

            string = None
            if isinstance(text, str): text = ""
            if isinstance(ref, list): ref.clear()
        except Exception as ex:
            pass
            # TODO: print_ex(ex) ?
