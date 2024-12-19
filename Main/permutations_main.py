"""This Code imports json, product from itertools and \
      pandas to find the all probbilities of the state"""

import json
from itertools import product
import pandas as pd


def permutation() -> tuple:
    """
    Summary: Identifies all the probabilities of the different states like \
          door, smoke, temperature, humidity, ldr, camera, rtc_time ,all_states

    Return:
     tuple: all_states , length(all_states), data_table 

    """
    door = ("on", "off", "on_fail", "off_fail", "fluctuate")
    smoke = ("on", "off")
    keypad = ("auth", "non_auth", "none")
    temperature = ("increasing", "decreasing", "stable", "fluctuate")
    humidity = ("increasing", "decreasing", "stable", "fluctuate")
    ldr = ("increasing", "decreasing", "stable", "fluctuate")
    camera = ("1", "2", "3", "4", " 5")
    rtc_time = ("dawn", "day", "noon", "evening", "dusk", "night")
    all_states = []
    for (
        door_state,
        smoke_state,
        keypad_state,
        temperature_state,
        humidity_state,
        ldr_state,
        camera_state,
        rtc_time_state,
    ) in product(door, smoke, keypad, temperature, humidity, ldr, camera, rtc_time):
        state_manager = {
            "door_state": door_state,
            "smoke_state": smoke_state,
            "keypad_state": keypad_state,
            "temperature_state": temperature_state,
            "humidity_state": humidity_state,
            "ldr_state": ldr_state,
            "camera_state": camera_state,
            "rtc_time_state": rtc_time_state,
        }
        all_states.append(state_manager)
    all_state_json = json.dumps(all_states)
    data_table = pd.DataFrame.from_records(all_states)
    print(data_table)
    data_table.to_csv("data_table.csv")
    return (all_state_json, len(all_state_json), data_table)


if __name__ == "__main__":
    print(permutation())
