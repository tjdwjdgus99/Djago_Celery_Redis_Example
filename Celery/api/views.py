# api/views.py

from django.http import JsonResponse
from .tasks import process_number

def process_number_view(request):
    number = 10  # 예시로 10개의 숫자를 처리하도록 설정
    task = process_number.apply_async(args=(number,))
    
    return JsonResponse({'task_id': task.id}, status=202)
