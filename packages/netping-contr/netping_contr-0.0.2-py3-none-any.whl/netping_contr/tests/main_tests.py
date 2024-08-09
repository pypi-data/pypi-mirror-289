from netping_contr.main import NetPingDevice
from netping_contr import mixins
import unittest


class TestCase(unittest.TestCase):
    inst = NetPingDevice("192.168.0.100")

    @unittest.SkipTest
    def test_get_io_info(self):
        response = self.inst.get_di_status(1)
        response = self.inst.parse_line_request(response)
        print(response)
        return response

    @unittest.SkipTest
    def test_change_relay(self):
        res = self.inst.change_relay_status(1, 0)
        res = self.inst.parse_relay_change(res)
        print(res)

    def test_get_all_io_info(self):
        response = self.inst.get_all_di_status()
        states = self.inst.parse_all_lines_request(response)
        print(states)


if __name__ == "__main__":
    unittest.main()
