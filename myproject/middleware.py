# myapp/middleware.py

from django.shortcuts import redirect

class PreventBackwardLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ตรวจสอบสถานะการล็อกอินของผู้ใช้
        if not request.user.is_authenticated:
            # หากไม่ได้ล็อกอิน ให้ทำการ redirect ไปยังหน้าล็อกอินหรือหน้าหลักตามที่คุณต้องการ
            return redirect('login.html')  # แทน 'login' ด้วย URL ของหน้าล็อกอินของคุณ

        response = self.get_response(request)
        return response
