#!/usr/bin/env bash
steps=$3;
step=$4;
arg=0;
echo "Iterations Time Unit"> $2"_tit".res;
for ((i = 1; i <= $steps; i++))
    do
        let arg=$i*$step;
        echo step ${i} arg ${arg}
        echo -n "$arg ">> $2"_tit".res;
        python3.6 -m timeit -n 10 -s "import $1" "$1.$2($arg)" | cut -f 6,7 -d " " >> $2"_tit".res;
    done