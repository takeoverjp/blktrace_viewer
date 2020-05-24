#!/bin/bash -e

if [ $# != 3 ]; then
    echo "[USAGE] $0 BLKRAW PREFIX DEVNO"
    exit
fi

BLKRAW=$1
PREFIX=$2
DEVNO=$3

btt -i ${BLKRAW} -l ${PREFIX} -q ${PREFIX} -z ${PREFIX} > ${PREFIX}.btt
for TYPE in "q2c" "q2d" "d2c"; do
    BASE="${PREFIX}_${DEVNO}_${TYPE}"
    python ../blktrace_viewer/main.py -t ${TYPE} -o "${BASE}.dat" "${BASE}.png"
done
