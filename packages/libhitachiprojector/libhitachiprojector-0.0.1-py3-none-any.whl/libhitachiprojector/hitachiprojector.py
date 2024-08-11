import argparse
from enum import Enum
import logging
import os
import secrets
import socket

PORT = 9715

logger = logging.getLogger(__name__)


class PowerStatus(Enum):
    Off = 0
    On = 1
    CoolDown = 2


class Command(Enum):
    AutoEcoModeOn = "auto_eco_mode_on"
    AutoEcoModeOff = "auto_eco_mode_off"
    EcoModeEco = "eco_mode_eco"
    EcoModeNormal = "eco_mode_normal"
    PowerTurnOn = "power_turn_on"
    PowerTurnOff = "power_turn_off"
    PowerGet = "power_get"


commands = {
    Command.AutoEcoModeOff: bytes.fromhex("BE EF 03 06 00 FB 27 01 00 10 33 00 00"),
    Command.AutoEcoModeOn: bytes.fromhex("BE EF 03 06 00 6B 26 01 00 10 33 01 00"),
    Command.EcoModeEco: bytes.fromhex("BE EF 03 06 00 AB 22 01 00 00 33 01 00"),
    Command.EcoModeNormal: bytes.fromhex("BE EF 03 06 00 3B 23 01 00 00 33 00 00"),
    Command.PowerTurnOff: bytes.fromhex("BE EF 03 06 00 2A D3 01 00 00 60 00 00"),
    Command.PowerTurnOn: bytes.fromhex("BE EF 03 06 00 BA D2 01 00 00 60 01 00"),
    Command.PowerGet: bytes.fromhex("BE EF 03 06 00 19 D3 02 00 00 60 00 00"),
}


def make_packet(cmd):
    HEADER = 0x02
    DATA_LENGTH = 0x0D

    packet = bytearray([HEADER, DATA_LENGTH])
    packet.extend(cmd)

    checksum = (255 - ((packet[0] + packet[1] + packet[-1]) & 0xFF)).to_bytes(1)
    packet.extend(checksum)

    connection_id = secrets.randbelow(256)
    packet.append(connection_id)

    logger.debug(
        f"checksum={checksum},connection_id={connection_id},packet={packet.hex()}"
    )
    return (packet, connection_id)


class ReplyType(Enum):
    ACK = 0x06
    NACK = 0x15
    ERROR = 0x1C
    DATA = 0x1D
    BUSY = 0x1F


class HitachiProjectorConnection:
    def __init__(self, host):
        self.host = host

    def send_cmd(self, cmd):
        (packet, connection_id) = make_packet(cmd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logger.debug("connecting")
            s.connect((self.host, PORT))

            logger.debug("sending")
            s.sendall(packet)
            logger.debug("sent")

            reply = s.recv(256)
            logger.debug(f"data=f{reply.hex()}")
            reply_type = ReplyType(reply[0])

            this_connection = connection_id == reply[-1]
            if not this_connection:
                logger.debug("Received reply for other connection")
                return (False, None)

            match reply_type:
                case ReplyType.ACK:
                    logger.debug("Command ACKed")
                    return (ReplyType.ACK, None)

                case ReplyType.NACK:
                    logger.debug("Command NACKed")
                    return (ReplyType.NACK, None)

                case ReplyType.ERROR:
                    error_code = reply[1:3]
                    logger.debug(f"Command errored: {error_code.hex()}")
                    return (ReplyType.ERROR, error_code)

                case ReplyType.DATA:
                    data = reply[1:3]
                    logger.debug(f"Command response: {data.hex()}")
                    return (ReplyType.DATA, data)

                case ReplyType.BUSY:
                    status = reply[1:3]
                    logger.debug(f"Command busy: {status.hex()}")
                    return (ReplyType.BUSY, status)


if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOG", logging.INFO))

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument(
        "command", choices=list(map(lambda key: key.value, commands.keys()))
    )
    args = parser.parse_args()
    command = Command(args.command)

    con = HitachiProjectorConnection(host=args.host)

    print(f"Sending cmd: {command}")

    (reply_type, data) = con.send_cmd(commands[command])
    match reply_type:
        case ReplyType.ACK:
            pass

        case ReplyType.DATA:
            assert data is not None
            match command:
                case Command.PowerGet:
                    status = PowerStatus(int.from_bytes(data, byteorder="little"))
                    print(f"Power status: {status}")

        case _:
            print(f"bad response: {reply_type}, {data}")
            raise RuntimeError("bad response")

    print("Done")
