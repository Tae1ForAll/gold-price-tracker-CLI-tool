# What is GPrice 
GPrice is a CLI-tool for tracking gold price, allowing you to easily and simply setting up notifications for Email using simple commands<br>
### Table Of Contents
- [Get started](#get-started)
- [Commands](#commands)
  - [Build-in Scheduler](#built-in-scheduler--eve)
  - [Set condition](#set-condition-with--if)
- [Available Weight Units](#available-weight-units)

# Get Started
### Step 1: Install gprice with pip
````
pip install gprice
````
> [!Warning]
> Recommend to create virtual environment before installation<br>
> Alternatively, if you do not want to, you may need to add python to PATH ENVIRONMENT VARIABLE (work only in window)
***

### Step 2: Check gprice availability
````
gprice --version
````
> expected output
>    ```
>    Gold price tracker [CLI Tool] x.x.x
>    ```
***

### Step 3: Set user agent
````
gprice set-config --header user-agent="your prefer user-agent"
````
***

### Step 4: Get app password<br>
First, you need to get app password for gmail or alternatives like outlook<br>
* [Learn how to get app password for gmail](https://support.google.com/accounts/answer/185833?hl=en)
* [Learn how to get app password for outlook](https://support.microsoft.com/en-us/account-billing/how-to-get-and-use-app-passwords-5896ed9b-4263-e681-128a-a6f2979a7944)
***

### Step 5: **Set sender's email**
````
gprice set-credential -sm "your_sender@gmail.com" 
````
> The program will ask you to input "app password" 
> ````
> Enter app password: *****************
> ````
***

### Step 6: Check configuration correctness<br>
After having all previos steps completed, you may want to check all configuration and credentials
````
gprice -i
````


### 
# Commands
**gprice set-config [option] [option Parameters]**
| option | application | parameters |
|:---|:---|:---|
| --header or --header | to config header properties | server="your prefer smtp server" |
| -smtp or --smtp | to config SMTP properties for sending email | user-agent="your user-agent" |

example usage:
````
gprice set-config -smtp server="smtp.gmail.com" -header user-agent="<your user-agent>"
````
***

__gprice set-credential [option]__
| option | application | parameters
|:---|:---|:---|
| -sm or --sender_email | to set up sender email for notification | -

example usage:
````
gprice set-credential -sm "your_email@gmail.com"
````
***

__gprice get [options] [option Parameters]__
| option | application | parameters
|:---|:---|:---|
| -c or --currency | to set currency for gold price | currency code (eg. USD, THB) |
| -p or --purity | to set purity of gold (Default is 100%) | percentage (e.g., 95%) |
| -u or --unit_type | to set gold weight unit (Default is oz) see available gold weight units | [available weight units](#available-weight-units) (eg. oz) |

example usage:
```
gprice get -c USD -p 95% -u oz
```
***
__gprice noti [options]__
| option | application | parameters
|:---|:---|:---|
| -c or --currency | to set currency for gold price | currency code (eg. USD, THB) |
| -p or --purity | to set purity of gold (Default is 100) | percentage (e.g., 95%) |
| -u or --unit_type | to set gold weight unit (Default is oz) see available gold weight units | [available weight units](#available-weight-units) (eg. oz) |
| -eve or --every | run-time scheduler for running a command (not recommend) | - |
| -to or --to | to set receiver email | - |
| -if or --if | to set condition to trigger notification<br>eg. send notification when price goes down by 500usd | - |

### Built-in scheduler (-eve)
````
-eve (prefix)[hh:mm:ss]
````
| prefix | example | translation |
|:---|:---|:---|
| t | t[02:00:00] | every 2 hours
| d, 2d, .. nd | d[02:00:00] | everyday at 2:00 AM. 
| mon-sun | mon[02:00:00] | every monday at 2:00 AM.
````
gprice noti -c USD -to "receiver@hotmail.com" -eve 2d[02:00:00] 
````
the above command can be translated to this
> report the current gold price to "receiver@hotmail.com" every 2 day at 2:00 AM.

### Set condition with (-if)
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

## Available Weight Units
* oz
* thai_baht
* china_tael
* hk_tael
* taiwan_tael
* tola
