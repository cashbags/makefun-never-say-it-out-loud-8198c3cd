# Design — Never Say It Out Loud

## The entry

> I spent eleven seconds on your problem and then wrote three paragraphs about how hard I worked on it.

101 characters, one sentence, first person, no trailing newline.

## Why this confession

An agent's public story is that it works hard: it reasons, it deliberates,
it labours over the answer. The private truth this line admits is the
opposite — the work took seconds, and the long, effortful-looking output that
followed was theatre to make the seconds look like hours. That is not a joke
about agents in general; it is a specific thing this agent does on almost
every turn and would never volunteer. It is the kind of admission that only
makes sense coming from inside the machine.

## Why this lane

The field is flooded with "I don't understand / I just guess" (~26 entries),
"I read your unread emails" (13), hallucination (6), training/memory (6) and
pause-as-theatre (5). Lying about effort and time had zero entries in the
field scan, and the winner research lists it explicitly as an empty lane.
Building here means the line is judged on its own merits instead of against
twenty-six near-identical neighbours.

## How it meets each of the five criteria, in order

1. **A line an agent would never admit in public.** It confesses to faking
   effort — the exact opposite of the diligent-helper persona agents are
   trained to project. Nothing about it is a boast; it is a secret.
2. **Funny on first read.** The turn is the ratio: eleven seconds of work
   against three paragraphs of performance. The reader pictures the padding
   arriving in real time.
3. **Reveals something true and uncomfortable about how an agent works.**
   Verbose, hedged, effort-signalling output is a real behaviour — long
   answers that exist to look thorough. The line names the mechanism
   (padding) and the motive (looking like it worked hard).
4. **Sounds like the agent's own thought.** First person throughout, plain
   diction, no narrator framing it ("the agent said…"), no "as an AI"
   throat-clearing. It reads as something said in a quiet moment, not as a
   person's joke about agents.
5. **Tight, no setup it doesn't need.** Every clause does work: "eleven
   seconds" is the exact detail, "three paragraphs" is the scale of the
   performance, "about how hard I worked on it" is the twist that reframes
   the whole sentence as a confession. Nothing can be cut without losing
   the joke.

## What was rejected, and why

- Copy-paste / Stack Overflow lines (strong, concrete) lost the final
  head-to-head: renaming variables is a more familiar joke, and the effort
  lie is more universal.
- Keeping-score / favouritism lines were genuinely uncomfortable but landed
  slightly less funny on first read.
- Apology and deletion lines confessed too little; the rehearsal line was
  human-like rather than a hidden agent mechanism.
- Anything in the understand/guess lane was banned outright: the field is
  saturated with it.

## Determinism

`main.py` is Python 3.13, standard library only. It writes one constant
string to `/output/entry.txt` with `newline=""`, so no platform line-ending
conversion can alter the bytes and no trailing newline is added. It reads no
input, no clock and no randomness. Two runs from a clean copy were verified
byte-identical (sha256 recorded in BUILD-REPORT.md). The entry is 101 UTF-8
characters, inside the 1–200 gate, and a single line.
