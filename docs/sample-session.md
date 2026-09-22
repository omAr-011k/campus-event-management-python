# Sample Session — Administrator Module

Three short runs of `Administrator.py`, the module I wrote. Lines marked `>` are what the user types.

## 1. Login and system statistics

```text
write your name please ('only admin') ...  > Omar
please Enter your password ...             > 333
welcome back Mr Omar your password 333

=====  administrator menu  =====

1. Approving or rejecting proposals .
2. Viewing system statistics (total events, most popular event, number of users).
3. Generating reports  of event data.
4. Manage user roles (promote participant to organizer, etc.) .
5. Exit .

 Write your chose's number ---> > 2

=== System Statistics ===
Total Approved Events: 3
Total Registered Participants: 6
Most Popular Event: 'science fair' with 2 participants
```

## 2. Generating a report

```text
 Write your chose's number ---> > 3

=== Generate Reports ===
1. Events Report
2. Participants Report
3. Organizers Report
4. Back to Main Menu
Select report type (1-4): > 1
Events report generated successfully as 'events_report.txt'
```

The generated `events_report.txt`:

```text
=== EVENTS REPORT ===
Total Events: 3

Event Details:
----------------
LaunchPad Expo
The Growth Forum
Innovate or Die
```

## 3. Failed login attempts

Wrong password:

```text
write your name please ('only admin') ...  > Omar
please Enter your password ...             > 999
wrong .. can not find your password.
do you want to reset your password? (Y/N): > no
Goodbye!
```

Unknown user:

```text
write your name please ('only admin') ...  > someone

Access denied. You are not an authorized admin.
Please contact the system administrator if you believe this is an error.
```
