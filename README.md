# What is GPrice
GPrice is a CLI-tool for tracking gold price, allowing you to easily and simply setting up notifications for Email using simple commands 

# Setup for email notificaton
GPrice Installation
````
pip install gprice

````
> note: you may need to install pip before if don't have

check gprice avalability
````
gprice --version
````
It should show somthing like this
````

````

Set up sender email
````
gprice set -se "your_sender@gmail.com" 
````

The program will prompt you to input "app password" 
````
Enter password for your_sender@gmail.com: *****************
````

# Commands
__gprice set [Option]__
| option | full-text option | application |
|:---:|:---:|:---:|
| -se | --sender-email | to determine sender email |
| -smtph | --smtp-host | to determine host server for sending email |
| -ug | --user-agent | to determine user agent |

__gprice show [options]__
| option | full-text option | application |
|:---:|:---:|:---:|
| -c | --currency | show gold price in the specified currency | 
| -i | --info | show infomation about the configuration<br>such as sender email, host server, and so on |

__gprice noti [options]__
| option | full-text option | application |
|:---:|:---:|:---:|
| -c | --currency | get gold price in the specified currency |
| -eve | --every | run-time scheduler for running a command (not recommend) | 
| -to | --to | set receiver email |
| -if | --if | set condition to trigger notification<br>eg. send notification when price goes down by 500usd

# Built-in scheduler (-eve)
````
-eve (prefix)[hh:mm:ss]
````
| prefix | example | translation |
|:---:|:---:|:---:|
| t | t[02:00:00] | every 2 hours
| d, 2d, .. nd | d[02:00:00] | everyday at 2:00 AM. 
| mon-sun | mon[02:00:00] | every monday at 2:00 AM.
````
gprice noti -c USD -to "receiver@hotmail.com" -eve 2d[02:00:00] 
````
the above command can be translated to this
> report the current gold price to "receiver@hotmail.com" every 2 day at 2:00 AM.

# Make condition with (-if)
up[x] = when price goes up to x \
down[x] = when price goes down to x

example usage:
````
gprice noti -c USD -to "receiver@hotmail.com" -eve t[00:05:00] -if up[500] down[500]
````
the above command can be translated to this
> the gold price (USD) is checked every 5 mins and 
> if the price goes up or goes down by 500USD,
> the notification is sent to the receiver mail.
