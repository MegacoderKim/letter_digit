from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import possible_lower_and_upper_case_variations


@api_view(["POST"])
def string_variations_list(request):
    """
    Post string as {"word":"a2B"}
    """
    word = request.data.get("word")
    if word:
        variations = possible_lower_and_upper_case_variations(word)

        return Response({"variations": variations}, status=status.HTTP_200_OK)
    return Response(
        {"error": "Invalid data received"}, status=status.HTTP_400_BAD_REQUEST
    )
