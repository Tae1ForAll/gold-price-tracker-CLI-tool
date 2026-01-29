from model import InputArgs
import schedule

def set_handler(args: InputArgs):
    if args.sender_email == None and args.user_agent == None:
        print("input 'gprice set -h' to how to use")
        
    if args.sender_email:
        print("implement set sender-email")
    
    if args.user_agent:
        print("implement setting user-agent")
        
    
import schedule
import time
import re

def handle_noti():
    pass

def _parse_every(eve: str):
    eve = eve.strip()

    m = re.fullmatch(r"(t|\d*d|mon|tue|wed|thu|fri|sat|sun)\[(\d{2}:\d{2}:\d{2})\]", eve, flags=re.IGNORECASE)
    if not m: raise ValueError("Wrong Format")
    
    mode, detail = m.group(1), m.group(2)
    return mode, detail

def _parse_days(mode: str) -> int:
    s = mode.strip().lower()
    if s == 'd': return 1
    
    m = re.fullmatch(r"(\d+)d", s)
    if not m:
        raise ValueError(f"Invalid day format: {mode!r} (expected 'Nd', e.g. '1d')")
    
    days = int(m.group(1))
    if days <= 0:
        raise ValueError("Days must be greater than 0")

    return days

def _parse_detail(detail: str):
    _HHMMSS_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2})$")
    detail = detail.strip()
    m_detail = _HHMMSS_RE.fullmatch(detail)
    
    if not m_detail:
        raise ValueError(f"Invalid time format: {detail!r}. Expected 'HH:MM:SS' (e.g. 00:05:00)")
    
    hh,mm,ss = int(m_detail.group(1)), int(m_detail.group(2)), int(m_detail.group(3))

    if not (0 <= hh <= 23):
        raise ValueError(f"Hour must be 00-23: {detail!r}")
    if not (0 <= mm <= 59):
        raise ValueError(f"Minute must be 00-59: {detail!r}")
    if not (0 <= ss <= 59):
        raise ValueError(f"Second must be 00-59: {detail!r}")

    total = hh * 3600 + mm * 60 + ss
    
    return hh, mm, ss, total
    
def schedule_handler(args: InputArgs):
    # -evr t[00:05:00] = every 1 min 2 seconds
    # -evr 1h:20:20
    # -evr 2d:10:10 = every 2 day at 10 hours
    def job():
        print("=== Test job ===")
        pass
    
    try:
        if not args.every:
            raise ValueError("schedule value is missing")        
        
        # extact mode and detail
        raw = args.every.strip()
        mode, detail = _parse_every(raw)
        
        # extract detail
        hh, mm, ss, total = _parse_detail(detail)
        
        # time mode
        if mode == "t": 
            schedule.every(total).seconds.do(job)
            print(f"Job execute every {detail}")
            
        # number of day mode        
        elif mode.endswith("d"): 
            days = _parse_days(mode)
            schedule.every(days).days.at(detail)
            if days == 1:
                print(f"Job execute everyday at {detail}")
            else:
                print(f"Job execute every {days} days at {detail}")

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
                    raise ValueError(f"Unexpected error wrong format {args.every!r}")            
            print(f"Job execute every {mode.upper()} at {detail}")
            
        run_schedule() 
            
    except Exception as e:
        raise(e)    
    

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)