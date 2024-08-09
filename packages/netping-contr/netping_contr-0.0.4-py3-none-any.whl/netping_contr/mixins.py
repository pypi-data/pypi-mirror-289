from requests.models import Response
import deprecation
import re


class NetPingResponseParser:
    """ Служит для парсинга ответов от Непинг. Переводит байты в JSON """

    def get_decoded_res(self, response: Response):
        return response.content.decode()

    def parse_all_lines_request(self, response: Response):
        res_decoded = self.get_decoded_res(response)
        res_decoded = res_decoded.replace(';', '')
        res_tuple = tuple(eval(res_decoded.split('io_result')[1]))
        status = res_tuple[0]
        if status == "error":
            return {"error": status}
        states = bin(res_tuple[1])
        states = states.replace("0b", "")
        if len(states) == 3:  # Баг Нетпинга - когда 4 вход замкнут - возвращаются только состояния первых трех входов
            states = "0" + states  # Мы его обходим добавив состояние замкнутости (0) для 4-го входа (первый элемент)
        states = states[
                 ::-1]  # Поскольку состояния входов реверсивные - развочариваем
        states_dict = {}
        for index, state in enumerate(states, start=1):  # Создаем словарь
            state = int(state)
            state ^= 1  # Превращаем состояние замкнутости из 0 в 1 и наоборот
            states_dict[index] = state
        return states_dict

    def parse_line_request(self, response: Response):
        res_decoded = self.get_decoded_res(response)
        res_decoded = res_decoded.replace(';', '')
        res_tuple = tuple(eval(res_decoded.split('io_result')[1]))
        response = {"status": res_tuple[0],
                    "state": res_tuple[2],
                    "count": res_tuple[-1]}
        return response

    @deprecation.deprecated(
        deprecated_in="0.0.1", removed_in="1.0.0",
        details="Устарело! Используйте метод parse_relay_state")
    def parse_relay_change(self, response: Response):
        """ DEPRECATED! """
        res_decoded = self.get_decoded_res(response)
        res_decoded = res_decoded.replace(';', '')
        res_tuple = res_decoded.split('relay_result')[1]
        response = re.search(r'\((.*?)\)', res_tuple).group(1).replace("'", '')
        response = {'status': response}
        return response

    def parse_relay_state(self, response: Response):
        res_decoded = self.get_decoded_res(response)
        if "error" in res_decoded:
            return res_decoded
        res_decoded = res_decoded.replace(';', '')
        state = res_decoded.split(',')[1]
        return state
