from common.casePara import casePara
import unittest

class Validation():

    def get_uniform_valid(self,data,response):
        valid_value = {}
        if isinstance(data,dict):
            for k,v in data.items():
                valid_value['assert'] = k
                valid_value['check'] = v[0]
                valid_value['expect'] = v[1]
                if '.' in valid_value['check']:
                    check_data = valid_value['check'].split('.')
                    for i in check_data:
                        valid_value['check']=response.json()[i]
            return valid_value

    def get_uniform_compare(self,compared):
        self.comparator = compared

        if self.comparator in ["eq", "equals", "equal"]:
            return "equal"
        elif self.comparator in ["lt", "less_than"]:
            return "less_than"
        elif self.comparator in ["le", "less_or_equals"]:
            return "less_or_equals"
        elif self.comparator in ["gt", "greater_than"]:
            return "greater_than"
        elif self.comparator in ["ge", "greater_or_equals"]:
            return "greater_or_equals"
        elif self.comparator in ["ne", "not_equal"]:
            return "not_equal"
        elif self.comparator in ["str_eq", "string_equals"]:
            return "string_equals"
        elif self.comparator in ["len_eq", "length_equal"]:
            return "length_equal"
        elif self.comparator in [
            "len_gt",
            "length_greater_than",
        ]:
            return "length_greater_than"
        elif self.comparator in [
            "len_ge",
            "length_greater_or_equals",
        ]:
            return "length_greater_or_equals"
        elif self.comparator in ["len_lt", "length_less_than"]:
            return "length_less_than"
        elif self.comparator in [
            "len_le",
            "length_less_or_equals",
        ]:
            return "length_less_or_equals"
        else:
            return self.comparator


class AssertType(unittest.TestCase):
    def assert_equal_new(self,assert_data,response_data):
        try:
            unittest.TestCase.assertEqual(assert_data,response_data)
        except AssertionError:
            print('assert断言失败')

    def asset_in_new(self):
        return


if __name__ == '__main__':
    v = Validation()
    vdata = v.get_uniform_valid({'eq': ['status_code', 200]})
    print(vdata)