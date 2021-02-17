from ep_sock.socket_client_raspberry import ClientSendSignalRaspberry
from ep_sock.socket_client_raspberry import RunClientRaspberryThread
from ep_sock import constant
from package.device_setting import update_device
from package import server
from package.service.device_api import device_control_api
import threading


def main(raspberry_id='', raspberry_group='', host=constant.SERVER_URL, port=constant.SERVER_PORT, debug=False):
    # API Server Address
    server_url = server.SERVER_URL

    signal = ClientSendSignalRaspberry(raspberry_id, raspberry_group)
    run_client_raspberry_thread = RunClientRaspberryThread(signal, debug=True, host=host, port=port)
    run_client_raspberry_thread.start()

    while True:
        if signal.device_read or signal.device_req_ok:
            # API Server -> Device -> Raspberry
            if signal.device_read:
                print(f'DEVICE{signal.recv_data.device_id, signal.recv_data.device_type} READ : ',
                      signal.recv_data.unit_index, signal.recv_data.on_off) if debug else None
                # Device 로부터 Unit Update 정보를 받으면
                # DB에 있는 Device 의 정보를 받은 값에 의해 업데이트함
                update_device(signal.recv_data.device_id, signal.recv_data.device_type, signal.recv_data.unit_index,
                              signal.recv_data.on_off)
                signal.device_read = False

            # Device -> Raspberry
            elif signal.device_req_ok:
                print(f'DEVICE{signal.recv_data.device_id, signal.recv_data.device_type} REQ : ',
                      signal.recv_data.unit_index, signal.recv_data.on_off) if debug else None
                # DB 에서 액세스 토큰 가져와서 API 호출.
                token = server.Token()
                token.load(access=True, refresh=False)
                if len(token.access) == 0:
                    print('<SOCKET.CLIENT> ERROR : 토큰이 존재하지 않음 - 라즈베리파이 GUI 설정 필요')
                    continue
                res = device_control_api(server_url, signal.recv_data.device_id, signal.recv_data.device_type, signal.recv_data.on_off, signal.recv_data.unit_index, token.access)
                if not res[0]:
                    print('<DEVICE.CONTROL> ERROR : 디바이스의 요청으로 API 를 호출하였으나 실패함')
                else:
                    # Device 로부터 Unit Update 정보를 받으면
                    # DB에 있는 Device 의 정보를 받은 값에 의해 업데이트함
                    update_device(signal.recv_data.device_id, signal.recv_data.device_type, signal.recv_data.unit_index,
                                  signal.recv_data.on_off)
                signal.device_req_ok = False
    run_client_raspberry_thread.stop()


class SocketClientRaspberryThread(threading.Thread):
    def __init__(self, raspberry_id='', raspberry_group='', host=constant.SERVER_URL, port=constant.SERVER_PORT, debug=False):
        threading.Thread.__init__(self)
        self.raspberry_id = raspberry_id
        self.raspberry_group = raspberry_group
        self.host = host
        self.port = port
        self.debug = debug

        self.daemon = True

    def run(self):
        main(raspberry_id=self.raspberry_id, raspberry_group=self.raspberry_group, host=self.host, port=self.port,debug=self.debug)
