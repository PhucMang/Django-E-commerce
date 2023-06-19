
class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kargs):
        # Khởi tạo và gán giá trị cho request.role = None
        request.role = None
        # Xác thực request user
        if request.user.is_authenticated:
            # lấy ra group của user
            groups = request.user.groups.all()
            # kiểm tra groups có giá trị hay không
            if groups:
                # gán giá trị tên của group cho request.role
                request.role = groups[0].name
        # nếu request user không xác thực hoặc qroups không có giá trị thì request.role = None
