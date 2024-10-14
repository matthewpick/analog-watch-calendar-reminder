# analog-watch-calendar-reminder

Programatically generate a "subscribable" ICS calendar for custom calendar notifications. Hosted via Vercel.

This particular calendar reminder is related to 31-day calendar wristwatches, 
you must manually set the date after a "short" month.

## Purpose

Most calendar systems (Apple, Google, Microsoft) do not support logic for custom date logic,
other than "last day of month" or "first Wednesday of the month."

By generating a subscribable calendar link, you can create any calendar you like!

## Usage

Subscribe to the following URL with your calendar app of choice (Apple Calendar, Outlook, etc.):  
`https://analog-watch-calendar-reminder.vercel.app/`

The calendar URL can be previewed via this website too: https://icscalendar.com/preview

## Development

```
pip install -r requirements.txt

python3 generate_calendar.py  # test end-of-month date calculation
python3 app.py  # run FastAPI service locally via uvicorn
```
