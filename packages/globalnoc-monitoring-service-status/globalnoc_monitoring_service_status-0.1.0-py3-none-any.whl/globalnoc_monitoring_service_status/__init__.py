import time
import json
import shutil

def write_service_status(error, error_text, path='', service='', filename='status.txt', timestamp=str(int(time.time()))):

    log_dict = {
        'timestamp': timestamp,
        'error_text': error_text,
        'error': error
    }

    if path is not '':
        status_file = path + filename
        tmp_status_file = path + filename + '.tmp'
    elif service is not '':
        status_file = f'/var/lib/grnoc/{service}/{filename}'
        tmp_status_file = f'/var/lib/grnoc/{service}/{filename}.tmp'
    else:
        return 0

    try:
        with open(tmp_status_file, 'w') as tmp_log_file:
            json.dump(log_dict, tmp_log_file)
            tmp_log_file.write('\n')

        shutil.move(tmp_status_file, status_file)
        return 1
    except Exception as error:
        print(error)
        return 0

