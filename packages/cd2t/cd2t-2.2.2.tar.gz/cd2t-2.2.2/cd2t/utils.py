"""
cd2t utils
classes and functions
"""

import copy
import re


def _re_fullmatch(regex_string, test_string):
    return re.fullmatch(regex_string, test_string)


def _re_fullmatch_multi(regex_string, test_string):
    return re.fullmatch(regex_string, test_string, re.MULTILINE)


def _re_search(regex_string, test_string):
    return re.search(regex_string, test_string)


def _re_search_multi(regex_string, test_string):
    return re.search(regex_string, test_string, re.MULTILINE)


def get_match_function(multiline: bool, full_match: bool):
    if full_match:
        if multiline:
            return _re_fullmatch_multi
        return _re_fullmatch
    if multiline:
        return _re_search_multi
    return _re_search


def string_matches_regex_list(
    string: str, regex_list: list, multiline=False, full_match=False
):
    match_fct = get_match_function(multiline, full_match)
    for regex in regex_list:
        match = match_fct(regex, string)
        if match:
            return regex
    return None


def any_string_matches_regex_list(
    strings: list, regex_list: list, multiline=False, full_match=False
):
    for string in strings:
        match = string_matches_regex_list(string, regex_list, multiline, full_match)
        if match:
            return string, match
    return None


def regex_matches_in_string_list(
    regex: str, strings: list, multiline=False, full_match=False
):
    match_fct = get_match_function(multiline, full_match)
    for string in strings:
        match = match_fct(regex, string)
        if match:
            return string
    return None


def merge_lists(left: list, right: list, list_merge: str = "append_rp") -> list:
    if not isinstance(left, list):
        raise ValueError("'left' is not a list")
    if not isinstance(right, list):
        raise ValueError("'right' is not a list")
    _left = copy.deepcopy(left)
    if list_merge == "replace":
        return copy.deepcopy(right)
    if list_merge == "append":
        return _left + copy.deepcopy(right)
    if list_merge == "prepend":
        return copy.deepcopy(right) + _left
    if list_merge in ["append_rp", "prepend_rp"]:
        append = list_merge == "append_rp"
        for element in right:
            if element not in _left:
                if append:
                    _left.append(copy.deepcopy(element))
                else:
                    _left.insert(0, copy.deepcopy(element))
        return _left
    raise ValueError(f"'list_merge' option {list_merge} is not known")


def merge_dictionaries(
    left: dict, right: dict, recursive: bool = True, list_merge: str = "append_rp"
) -> dict:
    if not isinstance(left, dict):
        raise ValueError("'left' is not a dictionary")
    if not isinstance(right, dict):
        raise ValueError("'right' is not a dictionary")
    _left = copy.deepcopy(left)
    for key, r_value in right.items():
        if key not in _left or not isinstance(r_value, type(_left[key])):
            # right element not in left or mismatching types => Just copy right to left
            _left[key] = copy.deepcopy(r_value)
        else:
            # left value is same type as right value
            if isinstance(r_value, list):
                # Merge left list with right list
                _left[key] = merge_lists(
                    left=_left[key], right=right[key], list_merge=list_merge
                )
            elif isinstance(r_value, dict):
                if recursive:
                    # Merge left dict with right dict
                    _left[key] = merge_dictionaries(
                        left=_left[key],
                        right=right[key],
                        recursive=recursive,
                        list_merge=list_merge,
                    )
                else:
                    # Overwrite left with right value
                    _left[key] = copy.deepcopy(r_value)
            else:
                # Something like integer or string and just copy right to left
                _left[key] = copy.deepcopy(r_value)
    return _left


def merge_template_data(
    template_data: dict,
    additional_data: dict,
    recursive: bool = True,
    list_merge: str = "append_rp",
) -> dict:
    template_data = template_data.copy()
    template_data_keys = set(list(template_data.keys()))
    additional_data_keys = set(list(additional_data.keys()))
    return_dict = template_data
    for key in template_data_keys.intersection(additional_data_keys):
        if isinstance(additional_data[key], list):
            if isinstance(template_data[key], list):
                return_dict[key] = merge_lists(
                    left=template_data[key],
                    right=additional_data[key],
                    list_merge=list_merge,
                )
            else:
                return_dict[key] = additional_data[key]
        elif not isinstance(additional_data[key], dict) or not isinstance(
            template_data[key], dict
        ):
            return_dict[key] = additional_data[key]
        else:
            return_dict[key] = merge_dictionaries(
                left=template_data[key],
                right=additional_data[key],
                recursive=recursive,
                list_merge=list_merge,
            )
    for key in additional_data_keys - template_data_keys:
        return_dict[key] = additional_data[key]
    return return_dict
