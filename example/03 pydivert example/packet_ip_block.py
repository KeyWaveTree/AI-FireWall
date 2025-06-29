import pydivert

#차단할 IP 주소
BLOCK_IP = "192.168.0.1"

filter_str = f"ip.SrcAddr == {BLOCK_IP}"

#pydivert.WinDivert() 생성자
with pydivert.WinDivert(filter_str) as w:
    for packet in w:
        #패킷을 재전송하지 않고 무시(drop)
        print(f"Dropped packet from {packet.src_addr}")
        #w.send(packet) #이 줄을 주석처리하면 패킷이 네트워크로 전달되지 않음 = 차단