#!/usr/bin/env python3

import speedtest

def testar_velocidade():
    st = speedtest.Speedtest()
    print("Selecionando melhor servidor...")
    st.get_best_server()
    print("Testando download...")
    download = st.download() / 1_000_000
    print("Testando upload...")
    upload = st.upload() / 1_000_000
    print(f"Velocidade de download: {download:.2f} Mbps")
    print(f"Velocidade de upload: {upload:.2f} Mbps")

if __name__ == "__main__":
    testar_velocidade()
