# RescueTheSavvy -- Rock-paper-scissior Fighters 

import random

# ----- constants & rules -----

r = "rock"
p = "paper"
s = "scissors"

BEATS = {
    r: s,
    p: r,
    s: p
}

# ----- shared helpers -----

def ask_yn(prompt):
    # ask a yes/no question; return True for 'y', False for 'n'
    while True:
        ans = input(prompt + " ").strip().lower()
        if ans in ["y", "yes"]:
            return True
        if ans in ["n", "no"]:
            return False
        print("Please answer with Y or N.")

def ask_choice(prompt, options):
    # options: list like ["walk", "uber"]; returns the chosen string
    opts_text = " / ".join(options)
    while True:
        ans = input(prompt + " (" + opts_text + "): ").strip().lower()
        if ans in options:
            return ans
        print("Please choose one of: " + opts_text)

def get_player_move():
    # loops until player enters r/p/s; returns full move "rock"/"paper"/"scissors"
    while True:
        raw = input("Enter r / p / s: ").strip().lower()
        if raw == "r":
            return r
        if raw == "p":
            return p
        if raw == "s":
            return s
        print("Invalid input! Please enter only r, p, or s.")

def judge(p1, p2):
    # return 'draw', 'p1', or 'p2'
    if p1 == p2:
        return "draw"
    elif BEATS[p1] == p2:
        return "p1"
    else:
        return "p2"

def print_round_result(player, opponent, msg):
    print("You chose: " + player + ", Computer chose: " + opponent + " -> " + msg)

# ----- RPS battle modes -----

def play_single():
    # single-round RPS; if draw, repeat until decisive
    print("\n[Battle: Single Round]")
    while True:
        player = get_player_move()
        opponent = random.choice([r, p, s])
        outcome = judge(player, opponent)

        if outcome == "draw":
            print_round_result(player, opponent, "It is a draw. Play again.")
            continue
        elif outcome == "p1":
            print_round_result(player, opponent, "You win.")
            return True
        else:
            print_round_result(player, opponent, "Computer wins.")
            return False

def play_best_of_three():
    # best-of-3; first to 2 wins
    print("\n[Battle: Best of 3]")
    player_score = 0
    computer_score = 0
    round_number = 1

    while player_score < 2 and computer_score < 2:
        print("\nRound " + str(round_number))
        player = get_player_move()
        opponent = random.choice([r, p, s])
        outcome = judge(player, opponent)

        if outcome == "draw":
            print_round_result(player, opponent, "It is a draw.")
        elif outcome == "p1":
            player_score += 1
            print_round_result(player, opponent, "You win this round.")
        else:
            computer_score += 1
            print_round_result(player, opponent, "Computer wins this round.")

        print("Score: You " + str(player_score) + " - " + str(computer_score) + " Computer")
        round_number += 1

    if player_score > computer_score:
        print("\nMatch result: You win the best-of-3.")
        return True
    else:
        print("\nMatch result: Computer wins the best-of-3.")
        return False

def play_streak_coin():
    # need 2 consecutive wins to trigger a coin toss; must get WIN to clear the match
    print("\n[Battle: 2-Win Streak + Press Key + Coin Toss]")
    print("- Get 2 wins in a row to trigger a coin toss.")
    print("- Before the toss, press any key to continue.")
    print("- Coin must land on WIN to win the match; LOSE resets your streak.\n")

    streak = 0
    round_number = 1

    while True:
        print("Round " + str(round_number))
        player = get_player_move()
        opponent = random.choice([r, p, s])
        outcome = judge(player, opponent)

        if outcome == "draw":
            print_round_result(player, opponent, "It is a draw.")
            streak = 0
        elif outcome == "p1":
            streak += 1
            print_round_result(player, opponent, "You win this round.")
        else:
            print_round_result(player, opponent, "Computer wins this round.")
            streak = 0

        print("Current win streak: " + str(streak) + "\n")

        if streak >= 2:
            print("You reached 2 wins in a row.")
            input("Press any key to toss the coin... ")
            coin = random.choice(["WIN", "LOSE"])
            print("Coin result: " + coin)

            if coin == "WIN":
                print("\nYou win the match by coin toss.")
                return True
            else:
                print("Coin says LOSE. Your streak resets.\n")
                streak = 0

        round_number += 1

# ----- story scenes (return next label or 'game_over' / 'campus_store') -----

def scene_intro():
    print("\n=== Prologue ===")
    print("Savvy, the SVA mascot, has been taken.")
    print("A note says: 'If you want her back, come to the 21st St campus store.'")
    start = ask_yn("Do you want to start the rescue game? (Y/N)")
    if not start:
        print('Savvy cries: "You will have nightmares!"')
        return "game_over"
    return "next"

def scene_21st_street():
    print("\n[21st Street Entrance]")
    print("You encounter Physical Computing instructor, Dianel.")
    print('D: "Today we have 3 labs and 2 projects. Submit your blog on Monday night.')
    print('    Or play Rock-Paper-Scissors with me and skip them."')

    while True:
        print("\nSystem: Start single-round RPS.")
        win = play_single()

        if win:
            print('D: "You beat me. There is still a midterm, though. Go save Savvy."')
            move = ask_choice("Choose your way", ["walk", "uber"])
            if move == "walk":
                return "eataly"
            else:
                return "campus_store"
        else:
            print("System: You are sent back to 3F to do homework.")
            retry = ask_yn("Do you want to challenge Dianel again? (Y/N)")
            if not retry:
                return "game_over"
            # else loop to retry single-round with Dianel

def scene_eataly():
    print("\n[Eataly Entrance]")
    print("You encounter the M & M instructors.")
    print('M&M: "Can you use Service Seeing to read our moves?"')
    print("System: Best-of-3 match.")

    while True:
        win = play_best_of_three()
        if win:
            print('M&M: "You have grasped the secret of Service Design. Proceed, and good luck."')
            move = ask_choice("Choose your way", ["walk", "uber"])
            if move == "walk":
                return "madison_park"
            else:
                return "campus_store"
        else:
            print('M&M: "Your Service Seeing eye is clouded. Go study Design the Invisible."')
            retry = ask_yn("Do you want to challenge M & M again? (Y/N)")
            if not retry:
                return "game_over"
            # else loop and retry best-of-3

def scene_madison():
    print("\n[Madison Square Park]")
    print("System: You are close to the Campus Store. Victory is near.")
    print('Mysterious Person: "Can you resist assignments?')
    print('Design five things. I will not tell you why. Then five more until the course ends."')

    do_five = ask_yn("Do you accept the five-design task? (Y/N)")
    if do_five:
        print("System: You return to 21st St and keep designing. The journey ends here.")
        return "game_over"
    else:
        print('You shout: "Let us settle this with Rock-Paper-Scissors."')
        print("System: Entering 2-win streak + coin toss challenge.")
        win = play_streak_coin()
        if win:
            print("Mysterious Person: You shattered my infinite design challenge. Proceed to the Campus Store.")
            return "campus_store"
        else:
            print("Mysterious Person: Five designs are not enough. Do ten and present in one minute.")
            retry = ask_yn("Do you want to challenge the mysterious person again? (Y/N)")
            if retry:
                return "madison_park"
            else:
                return "game_over"

def scene_campus_store():
    print("\n[Campus Store Entrance]")
    open_door = ask_yn("Do you choose to open the door? (Y/N)")
    if not open_door:
        print("System: Why choose No now? You are almost there.")
        input("Press any key to confirm opening the door... ")
        # fallthrough to opening the door

    print('You open the door and see: "Hello World".')
    print("C & B: Congratulations on reaching this place. Have you learned the essence of Hello World?")
    print("C & B: We grant you the Power of Python.")
    print("System: You acquired the Power of Python.")
    print('As for Savvy... she is a pigeon. No one ever captured her.')
    print("System: The journey ends.")
    return "finished"

# ----- one full run (no exit; returns True if finished, False if game over) -----

def run_game_once():
    nxt = scene_intro()
    if nxt == "game_over":
        return False

    nxt = scene_21st_street()
    if nxt == "game_over":
        return False

    if nxt == "eataly":
        nxt = scene_eataly()
        if nxt == "game_over":
            return False

    if nxt == "madison_park":
        nxt = scene_madison()
        if nxt == "game_over":
            return False

    # at this point nxt should be "campus_store" (from 21st/eataly/madison paths)
    if nxt == "campus_store":
        end = scene_campus_store()
        return end == "finished"

    # fallback: if flow is inconsistent, treat as game over
    return False

# ----- main loop: allow restarting after any failure -----

def main():
    print("=== DeepForst: Rescue Savvy ===")
    while True:
        finished = run_game_once()
        # regardless of finish or game over, ask if the player wants to restart
        again = ask_yn("\nDo you want to start a new game? (Y/N)")
        if not again:
            print("Thanks for playing. Goodbye.")
            break

if __name__ == "__main__":
    main()