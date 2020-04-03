#!/bin/bash

echo "Este Proceso podria tardar media hora en un SSD, los archivos descomprimidos ocuparán cerca de 25gb "
if md5sum --check hash_partes.txt; then
    echo "Los archivos estan OK"
else
    echo "Algun archivo esta Danado"
    exit 1
fi

echo "Uniendo archivos esto podria tardar"
cat iemocapsinvideo.tar.gz.parta* > iemocapjoined.tar.gz.joined

if md5sum --check hash_join.txt; then
    echo "El archivo esta OK"
else
    echo "Algo salio mal"
    exit 1
fi

tar -xvf iemocapjoined.tar.gz.joined
