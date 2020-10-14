#!/bin/bash

read -p "Enter parameters: " ARG

#cmake-build-debug/kp.exe ${ARG/\//\/\/} optional silent mode
cmake-build-debug/kp.exe "//s" "${ARG}"

case "$?" in
	11) echo "Brak parametrów" ;;
	12) echo "Parameter" "$ARG" "nie jest cyfrą" ;;
	13) echo "Niewłaściwa wartość parametru" "$ARG" ;;
	*) echo 'Przekazano:' "$ARG" ;;
esac

exit 0