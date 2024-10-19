# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from .forms import UserSignupForm, BookingForm
# from .models import Slot, Booking
# import razorpay

# # Initialize Razorpay client with your key id and secret
# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# def index(request):
#     return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('booking')
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('booking')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# @login_required
# def booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.save()

#             # Razorpay payment creation
#             payment_amount = int(booking.price() * 100)  # Razorpay expects amount in paise
#             payment_order = client.order.create({
#                 'amount': payment_amount,
#                 'currency': 'INR',
#                 'payment_capture': 1  # Auto capture payment
#             })

#             # Redirect to Razorpay's payment page
#             return render(request, 'payment.html', {'payment_order': payment_order, 'booking': booking})
#     else:
#         form = BookingForm()
#     return render(request, 'booking.html', {'form': form})

# @login_required
# def payment_success(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)
#     return render(request, 'ticket.html', {'booking': booking})

# def user_logout(request):
#     logout(request)
#     return redirect('index')


# new code and logic startb from here 



# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from .forms import UserSignupForm, BookingForm
# from .models import Slot, Booking
# import razorpay

# # Initialize Razorpay client with your key id and secret
# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# def index(request):
#     return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('booking')
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('booking')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# @login_required
# def booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.save()

#             # Razorpay payment creation
#             payment_amount = int(booking.price() * 100) # Razorpay expects amount in paise
#             payment_order = client.order.create({
#                 'amount': payment_amount,
#                 'currency': 'INR',
#                 'payment_capture': 1 # Auto capture payment
#             })

#             # Redirect to Razorpay's payment page
#             return render(request, 'payment.html', {'payment_order': payment_order, 'booking': booking})
#     else:
#         form = BookingForm()
#     return render(request, 'booking.html', {'form': form})

# # @login_required
# # def payment_success(request, booking_id):
# #     booking = Booking.objects.get(id=booking_id)
# #     return render(request, 'ticket.html', {'booking': booking})

# @login_required
# def payment_success(request, booking_id):
#     try:
#         booking = Booking.objects.get(id=booking_id)
#     except Booking.DoesNotExist:
#         return redirect('error_page')

#     # Optionally check payment status if needed
#     if not booking.is_paid:
#         return redirect('error_page')

#     return render(request, 'ticket.html', {'booking': booking})


# def user_logout(request):
#     logout(request)
#     return redirect('index')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, BookingForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
import razorpay
from django.conf import settings

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('booking')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booking')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            # Create Razorpay order
            payment_amount = int(booking.price() * 100)  # Amount in paise
            payment_order = client.order.create({
                'amount': payment_amount,
                'currency': 'INR',
                'payment_capture': 1
            })

            # Save order id in the booking for future reference
            booking.razorpay_order_id = payment_order['id']
            booking.save()

            # Redirect to payment page with Razorpay order details
            return render(request, 'payment.html', {'payment_order': payment_order, 'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def payment_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'ticket.html', {'booking': booking})

def user_logout(request):
    logout(request)
    return redirect('index')