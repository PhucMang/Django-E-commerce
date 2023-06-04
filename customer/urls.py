from django.urls import path
from .views import SignupPageView, ViewProfile, ViewListCustomer, ViewProfileByID, ViewUpdateProfile, update_profile, ViewOrder, ViewOrderDetail
from django.contrib.auth import views as auth_view
from .forms import MyPasswordChangeFrom, MySetPasswordForm, MyPasswordResetForm

urlpatterns = [
    path('register/', SignupPageView.as_view(), name='register'),
    path('profile/', ViewProfile.as_view(), name='profile'),
    path('list-user/', ViewListCustomer.as_view(), name='list-users'),
    path('profile/<int:pk>', ViewProfileByID.as_view(), name='profile_by_id'),
    path('profile/update-profile/', ViewUpdateProfile.as_view(), name='update-profile'),
    path('profile/update-profile/update', update_profile, name='update'),
    path('order/', ViewOrder.as_view(), name='view-order'),
    path('order-detail/<int:id>', ViewOrderDetail.as_view(), name='order-detail'),
    #change password
    path('passwordchange/',
         auth_view.PasswordChangeView.as_view(template_name='registration/change_password.html',
                                                form_class=MyPasswordChangeFrom,
                                                success_url='/accounts/passwordchangedone'),
                                                name='password-change'),
    path('passwordchangedone/',
         auth_view.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
                                                    name='password-change-done'),
    #reset password
    path('password-reset/',
         auth_view.PasswordResetView.as_view(template_name='registration/password_reset.html',
                                                form_class=MyPasswordResetForm), name='password-reset'),
    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
                                                name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
                                                    form_class=MySetPasswordForm), name='password-reset-confirm'),
    path('password-reset/complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
                                                    name='password-reset-complete'),
]
