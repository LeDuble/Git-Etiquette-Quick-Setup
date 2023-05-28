import time

def loading(file_loaded, reason_to_wait, end_message):
    dots = ""
    while not reason_to_wait:

        if len(dots) == 3:
            for i in range(0, len(dots)):
                dots = dots.replace(".", "", 1)
                print(f"{file_loaded} is loading{dots}")
                time.sleep(0.1)

        else:
            dots += "."
            print(f"{file_loaded} is loading{dots}")
        time.sleep(0.1)
    return end_message