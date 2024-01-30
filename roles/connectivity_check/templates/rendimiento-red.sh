#!/bin/bash 

echo -e "${YELLOW}PRUEBAS IPERF${PLAIN}"
echo -e "${YELLOW}Si alguno fallara y te interesa debes acceder al mismo por SSH (En GO estÃƒÂ¡ toda la informaciÃƒÂ³n) y ejecutar: iperf3 -D -s${PLAIN}"
sleep 4
echo ""
echo -e "${YELLOW}Chile subida:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 138.121.169.14 -R${PLAIN}"

iperf3 -c 138.121.169.14 -R
echo ""
echo -e "${YELLOW}Chile descarga:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 138.121.169.14${PLAIN}"

iperf3 -c 138.121.169.14
echo ""
echo -e "${YELLOW}Miami subida:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 199.89.55.86 -R${PLAIN}"

iperf3 -c 199.89.55.86 -R
echo ""
echo -e "${YELLOW}Miami descarga:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 199.89.55.86${PLAIN}"

iperf3 -c 199.89.55.86 
echo ""
echo -e "${YELLOW}Madrid subida:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 195.114.216.47 -R${PLAIN}"

iperf3 -c 195.114.216.47 -R
echo ""
echo -e "${YELLOW}Madrid descarga:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 195.114.216.47${PLAIN}"

iperf3 -c 195.114.216.47 
echo ""
echo -e "${YELLOW}Colombia subida:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 170.239.154.28 -R${PLAIN}"

iperf3 -c 170.239.154.28 -R
echo ""
echo -e "${YELLOW}Colombia descarga:${PLAIN}"
echo -e "${YELLOW}iperf3 -c 170.239.154.28${PLAIN}"

iperf3 -c 170.239.154.28 
echo ""


   # pause
