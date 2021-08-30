FROM tronprotocol/java-tron

ENV CONFIG=mainnet.conf

RUN mkdir -p /data

VOLUME [ "/data" ]