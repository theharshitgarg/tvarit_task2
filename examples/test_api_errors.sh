echo "\n\nExample 1 -- Inputs 13 100 \n\n"

curl --location --request POST 'localhost:9000/operations/add' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "num1": 13,
    "num2": 100
}'


echo "\n\nExample 2 - Inputs 13 \n\n"

curl --location --request POST 'localhost:9000/operations/add' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "num1": 13
}'
