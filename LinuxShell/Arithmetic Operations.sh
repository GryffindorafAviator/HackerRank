read expression

result=$(echo "scale = 4; $expression"| bc)
printf "%.3f\n" "$result"
