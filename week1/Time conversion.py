def timeConversion(s):
    timeSplit = s.split(':')
    hours = timeSplit[0]
    mins = timeSplit[1]
    secs = timeSplit[2][:-2]
    if 'AM' in s:
        if hours == '12':
            hours = '00'
    else:
        if '12' not in hours:
            hours = str(int(hours) + 12)
            
    return (hours + ':' + mins + ':' + secs)
