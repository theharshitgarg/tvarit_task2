echo "Success examples ......\n"
echo "\n\nExample 1 - Inputs  13 100 200 \n"

curl --location --request POST 'localhost:9000/operations/add' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "num1": 13,
    "num2": 100,
    "num3": 200
}'

echo "\n\nExample 2 - Inputs 15 100 20 \n"

curl --location --request POST 'localhost:9000/operations/add' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "num1": 15,
    "num2": 100,
    "num3": 20
}'


echo "\n\nExample 3 - Inputs 10 10 10 \n"
curl --location --request POST 'localhost:9000/operations/add' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "num1": 10,
    "num2": 10,
    "num3": 10
}'
