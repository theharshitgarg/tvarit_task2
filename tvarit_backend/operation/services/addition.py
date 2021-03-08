from operation.serializers import AdditionSerializer

class AdditionService():
    DISALLOED_NUMBERS = [
        13, 14, 17, 18, 19
    ]

    def result(self, data):
        serializer = AdditionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        numbers = serializer.data

        result = 0
        for value in numbers:
            number = numbers[value]
            if number not in self.DISALLOED_NUMBERS:
                result = result + number

        return result

