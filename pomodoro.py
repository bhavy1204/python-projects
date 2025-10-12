#!/usr/bin/env python3
import time
import argparse
import sys

def countdown(minutes, label):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"{label}: {mins:02d}:{secs:02d}"
        print(time_str, end='\r')
        time.sleep(1)
    print(f"\n⏰ {label} session over! Take a break!\n")

def pomodoro(work, short_break, long_break, cycles):
    for cycle in range(1, cycles + 1):
        print(f"\n🍅 Pomodoro {cycle}/{cycles} started. Focus!\n")
        countdown(work, "Work")
        if cycle < cycles:
            if cycle % 4 == 0:
                print("\n🌴 Time for a long break!\n")
                countdown(long_break, "Long Break")
            else:
                print("\n☕ Short break time!\n")
                countdown(short_break, "Short Break")
    print("🎉 All pomodoros done! You're a focus machine!\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI Pomodoro Timer")
    parser.add_argument("--work", type=int, default=25, help="Work duration in minutes (default: 25)")
    parser.add_argument("--short", type=int, default=5, help="Short break duration in minutes (default: 5)")
    parser.add_argument("--long", type=int, default=15, help="Long break duration in minutes (default: 15)")
    parser.add_argument("--cycles", type=int, default=4, help="Number of Pomodoros (default: 4)")
    args = parser.parse_args()

    try:
        pomodoro(args.work, args.short, args.long, args.cycles)
    except KeyboardInterrupt:
        sys.exit("\n🛑 Pomodoro interrupted. See you next time!\n")
