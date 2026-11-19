# CS 1500 advice collector

A CS 1500 shell exercise. `advice_collector.sh` fetches one advice slip from the public adviceslip.com API with `curl` and `jq` and appends it, timestamped, to `Drew.Trigg.advices`.

## Rules

- The script's log path is relative to the folder above the repo; run it from there or update the path deliberately, never by accident.
- Keep it plain Bash with only `curl` and `jq`; check with `bash -n advice_collector.sh` after edits.
- Never rewrite or reorder existing lines in `Drew.Trigg.advices`; it is an append-only log.

## How this file improves itself

Run `/lessons` at the end of a session. It reviews the session for corrections and mistakes, proposes short rules, and adds only the ones Drew approves to the Lessons section below. Keep this file under about 150 lines; move topic-specific rules into `.claude/rules/`.

## Lessons

<!-- Approved by /lessons. One line each: - YYYY-MM-DD: rule -->
