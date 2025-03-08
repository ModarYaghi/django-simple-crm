from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import AddRecordForm, SignUpForm
from .models import Record

# Create your views here.


def home(request):
    """home view"""

    # Grap all records from Record
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Hello, {username}. You Have Been Logged In")
            return redirect("home")

        messages.success(request, "There Was an Error Logging In, Please Try Again...")
        return redirect("home")

    return render(request, "home.html", {"records": records})


# def login_user(request):
# """In case we want to make a separate login page"""
# pass


def logout_user(request):
    """For logging out in separate page"""
    username = (
        request.user.username
    )  # Store username before logging out. This let me access the username before logging out, so I can say goodbye.
    logout(request)
    messages.success(request, f"Good Bye, {username}")
    return redirect("home")


def register_user(request):
    """To register a new user"""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():  # NOTE: How Django evaluate form validation?
            form.save()
            # If form is valid and saved. Poeple want to login in and start using our website.
            # Lets let them in by Authenticate and login
            # NOTE: What is .cleaned_data["..."] is?
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, f"You Have Successfully Registered! Welcome {username}!"
            )
            return redirect("home")
    # If user did not enter information we want for registeration,
    # we need to redirect them to the register page to fill information needed.
    else:
        form = SignUpForm()  # there is no request.POST here.
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def get_customer_record(request, pk):
    """Get a customer record based on costomer id"""
    # Check if user is logged in:
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})

    messages.success(request, "You Must Be Logged In To View That Page...")
    return redirect("home")


def delete_record(request, pk):
    """Delete a costomer record"""
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect("home")

    messages.success(request, "You Must Be Logged In To Do That...")
    return redirect("home")


def add_record(request):
    """Add new record"""
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect("home")

        return render(request, "add_record.html", {"form": form})

    messages.success(request, "You Must Be Logged In To Add Records...")
    return redirect("home")


def update_record(request, pk):
    """Update un existed record"""
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has Been updated!")
            return redirect("home")

        return render(request, "update_record.html", {"form": form})
    messages.success(request, "You Must Be Logged In To Update Records...")
    return redirect("home")
