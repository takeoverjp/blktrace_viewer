#!/bin/bash -e

btt -i sample.blktrace.0 -l sample -q sample -z sample > /dev/null
for TYPE in "q2c" "q2d" "d2c"; do
    python ../blktrace_viewer/main.py -t ${TYPE} -o "sample_259,0_${TYPE}.dat" "sample_259,0_${TYPE}.png"
done
