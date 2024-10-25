from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import BloodPressureRecord
from .forms import BloodPressureForm

@login_required
def create_record(request):
    if request.method == 'POST':
        form = BloodPressureForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('last_record')
    else:
        form = BloodPressureForm()
    return render(request, 'tracker/create_record.html', {'form': form})

@login_required
def last_record(request):
    record = BloodPressureRecord.objects.filter(user=request.user).order_by('-date').first()
    return render(request, 'tracker/last_record.html', {'record': record})

@login_required
def statistics(request):
    period = request.GET.get('period', 'day')
    if period == 'day':
        start_date = timezone.now() - timedelta(days=1)
    elif period == 'month':
        start_date = timezone.now() - timedelta(days=30)
    else:
        start_date = timezone.now() - timedelta(days=1)

    records = BloodPressureRecord.objects.filter(user=request.user, date__gte=start_date).order_by('date')
    return render(request, 'tracker/statistics.html', {'records': records, 'period': period})