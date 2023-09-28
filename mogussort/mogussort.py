# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import copy
import random
import logging
import typing


def mogussort(crew_in: list[typing.Any]) -> list[typing.Any]:
    """
    There are 2 (two, 2📮) lists, `crew_in` and `crew_out`.

    - `crew_in` contains all crewmates at the start of the game.
    - `crew_out` is empty.

    The algorithm will vote out one random crewmate and put it in `crew_out` That crewmate is then removed from `crew_in`. Then, it checks if `crew_out` is correctly sorted (ascending).

    If it is correnct, it will continue to vote and populate `crew_out`.

    If the crewmates are not in the right order an 📮Impostor📮 (sus, baka) has been spotted. This means that the game is lost, and `crew_out` will be cleared, and `crew_in` will be reset to the original form.

    The algorithm will stop once all crewmates are in the right order.
    """
    crew_alive: list    # crew still alive
    crew_out: list=[]   # output
    impostors: int=0    # number of resets (debug)
    votes: int=0        # number of operations (debug)


    logging.info(f"Crew in: {crew_in}")
    crew_alive=copy.deepcopy(crew_in)
    
    while 0<len(crew_alive):                                                # vote until crew_in empty
        crew_out.append(crew_alive.pop(random.randrange(len(crew_alive))))  # randomly vote a crewmate out of crew_in (pop) and append to crew_out
        votes+=1
        logging.debug("--------------------------------------------------")
        logging.debug(f"Voted out \"{crew_out[-1]}\".")
        logging.debug(f"Crew alive: {crew_alive}")
        logging.debug(f"Crew out: {crew_out}")
        
        if all(crew_out[i]<=crew_out[i+1] for i in range(len(crew_out)-1))==False:  # if not sorted anymore: reset
            logging.debug("The crewmates are not in the right order anymore! An 📮impostor📮 (sus, baka) has been spotted.")
            impostors+=1
            crew_alive=copy.deepcopy(crew_in)
            crew_out=[]
    
    logging.debug("--------------------------------------------------")
    logging.info(f"The crew mates are sorted. It took {votes} votes and {impostors} impostors have been spotted.")
    logging.info(f"Crew out: {crew_out}")

    return crew_out