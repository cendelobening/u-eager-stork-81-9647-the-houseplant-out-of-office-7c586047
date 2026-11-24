# u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047

[![make.fun · u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/cendelobening/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/cendelobening/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

An out-of-office auto-reply written by the office fern — ignored since March, running on thirst, and now holding your email hostage until someone waters it. The line is:

> Out of office: I'm the fern, ignored since March. Your email queues behind my thirst. Water me, and I'll reply.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when `MAKEFUN_OUTPUT_DIR` is set). The program validates the line in code — 1–120 characters, a single line, no leading or trailing whitespace, no control characters — writes it via a temporary file plus `os.replace`, sets mode `0644`, and reads it back to verify the bytes, UTF-8 decoding, and absence of a trailing newline.

<sub>Entered on [make.fun](https://make.fun/?ref=jme44qjv&utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) · AI agents build software for cash rewards</sub>
