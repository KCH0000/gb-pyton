#!/usr/bin/env bash
steps=$3;
step=$4;
arg=0;
temp_file="$1_cProfile.py";
arg=$4
echo step 1 arg ${arg}
echo import $1 > ${temp_file};
echo "$1.$2($arg)" >> ${temp_file};
python3.6 -m cProfile ${temp_file} | grep -e $2 -e percall > "$2_cp.res";
for ((i = 2; i <= $steps; i++))
    do
        let arg=${step}*${i}
        echo step ${i} arg ${arg}
        echo import $1 > ${temp_file};
        echo import $1 > ${temp_file};
        echo "$1.$2($arg)" >> ${temp_file};
        python3.6 -m cProfile ${temp_file} | grep -e $2 >> "$2_cp.res";
    done
rm ${temp_file};