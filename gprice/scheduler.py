import schedule
import re
import time
import gprice.custom_printer as printer
import gprice.error as error

# scheduler message
SCHD_DEFAULT_ERROR_MESSAGE = "Schedule operation failed, please follow the option rule (Enter: [gprice noti -eve -h] to learn more)"
DAY_LESS_EQ_ZERO = "Day must be greater than 0 (d, 2d..), Enter: [gprice noti -eve] to learn more"

INVALID_TIME_FORMAT = "Invalid time format expected [hh:mm:ss]"
INVALID_DAY_FORMAT = "Invalid day format expected (d, 2d, .. nd)"
HOUR_OUT_OF_RANGE = "Hours must be 00-23"
MINUTE_OUT_OF_RANGE = "Minutes must be 00-59"
SECOND_OUT_OF_RANGE = "Seconds must be 00-59"

# public function
def run_schedule(every: str, job):
    try:        
        # extact mode and detail
        raw = every.strip()
        mode, detail = _parse_every(raw)
        
        # extract detail
        hh, mm, ss, total = _parse_detail(detail)
        
        # time mode
        if mode == "t": 
            schedule.every(total).seconds.do(job)
            printer.print_auto(f"Job execute every {detail}")
            
        # number of day mode        
        elif mode.endswith("d"): 
            days = _parse_days(mode)
            schedule.every(days).days.at(detail)
            if days == 1:
                printer.print_auto(f"Job execute everyday at {detail}")
            else:
                printer.print_auto(f"Job execute every {days} days at {detail}")

        # days mode (mon-sun)
        else:
            match mode:
                case "mon": schedule.every().monday.at(detail).do(job)
                case "tue": schedule.every().tuesday.at(detail).do(job)
                case "wed": schedule.every().wednesday.at(detail).do(job)
                case "thu": schedule.every().thursday.at(detail).do(job)
                case "fri": schedule.every().friday.at(detail).do(job)
                case "sat": schedule.every().saturday.at(detail).do(job)
                case "sun": schedule.every().sunday.at(detail).do(job)
                case __:
                    raise ValueError(SCHD_DEFAULT_ERROR_MESSAGE)            
            printer.print_auto(f"Job execute every {mode.upper()} at {detail}")
        

        while True:
            schedule.run_pending()
            time.sleep(1) 
            
    except error.SchedulerError as e:
        printer.print_error(str(e))
    except Exception as e:
        printer.print_error(str(e))
 
# internal functions
def _parse_every(eve: str):
    eve = eve.strip()

    m = re.fullmatch(r"(t|\d*d|mon|tue|wed|thu|fri|sat|sun)\[(\d{2}:\d{2}:\d{2})\]", eve, flags=re.IGNORECASE)
    if not m: raise error.SchedulerError(SCHD_DEFAULT_ERROR_MESSAGE)
    
    mode, detail = m.group(1), m.group(2)
    return mode, detail

def _parse_days(mode: str) -> int:
    s = mode.strip().lower()
    if s == 'd': return 1
    
    m = re.fullmatch(r"(\d+)d", s)
    if not m:
        raise error.SchedulerError(INVALID_TIME_FORMAT)
    
    days = int(m.group(1))
    if days <= 0:
        raise error.SchedulerError(DAY_LESS_EQ_ZERO)

    return days

def _parse_detail(detail: str):
    _HHMMSS_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2})$")
    detail = detail.strip()
    m_detail = _HHMMSS_RE.fullmatch(detail)
    
    if not m_detail:
        raise error.SchedulerError(INVALID_TIME_FORMAT)
    
    hh,mm,ss = int(m_detail.group(1)), int(m_detail.group(2)), int(m_detail.group(3))

    if not (0 <= hh <= 23):
        raise error.SchedulerError(HOUR_OUT_OF_RANGE)
    if not (0 <= mm <= 59):
        raise error.SchedulerError(MINUTE_OUT_OF_RANGE)
    if not (0 <= ss <= 59):
        raise error.SchedulerError(SECOND_OUT_OF_RANGE)

    total = hh * 3600 + mm * 60 + ss
    
    return hh, mm, ss, total
