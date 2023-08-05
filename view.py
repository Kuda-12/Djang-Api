from django.http import JsonResponse

def my_app(request):
    if request.method == 'GET':
        data = {
            'message': 'This is a sample GET request response.',
            'data': [1, 2, 3, 4, 5]
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        # Assuming you expect some data in the POST request body
        received_data = request.POST.get('data', None)
        data = {
            'message': 'This is a sample POST request response.',
            'received_data': received_data
        }
        return JsonResponse(data)

    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
