import re
import pathlib
import subprocess


def main() -> None:
    rg_cmd = ["rg", "--sort", "path", "-n", r"\[\[UNCLEAR", "VSCODE MD Files/draft"]
    result = subprocess.check_output(rg_cmd, text=True, encoding="utf-8", errors="replace")
    lines = [line for line in result.splitlines() if line.strip()][:50]

    items = []
    for line in lines:
        path_str, lineno_str, content = line.split(":", 2)
        path = pathlib.Path(path_str)
        lineno = int(lineno_str)
        text = path.read_text(encoding="utf-8", errors="replace").splitlines()
        idx = lineno - 1
        m = re.search(r"\[\[UNCLEAR:\s*(.*?)\]\]", content)
        unclear = m.group(1) if m else ""
        line_text = text[idx] if 0 <= idx < len(text) else content
        cleaned = re.sub(r"\s*\[\[UNCLEAR:.*?\]\]", "", line_text).strip()
        if cleaned and cleaned != line_text.strip():
            excerpt = cleaned
        else:
            excerpt = ""
            for j in range(idx - 1, -1, -1):
                prior = text[j].rstrip()
                if not prior.strip():
                    continue
                if "[[UNCLEAR:" in prior:
                    continue
                excerpt = prior
                break
            if not excerpt:
                excerpt = cleaned if cleaned else content.strip()
        items.append((path_str.replace("VSCODE MD Files/", ""), lineno, unclear, excerpt))

    options = [
        ("Deathmark is the only mark at Sequence 0.", "Deathmark is the only mark in the Death Pathway.", "GM decides."),
        ("Treat the naming phrase as poetic flavor only.", "Remove the naming phrase entirely.", "GM decides."),
        ("No per-round cap on how many times peripheral damage can apply to a target.", "No per-round cap on how many targets can take peripheral damage.", "GM decides."),
        ("1d4 for ordinary targets; 1d6+1 for stronger targets.", "Always use 1d6+1.", "GM decides."),
        ("If rebuke/negotiation succeeds vs Will Defense, it enables the easy-to-crazy effect.", "Rebuke/negotiation replaces the sanity test.", "GM decides."),
        ("3 minutes required for non-demigods; demigods are immune.", "3 minutes required for demigods/higher; lower targets are faster.", "GM decides."),
        ("Two -4 checks must succeed in the same round.", "Two -4 checks can succeed over consecutive rounds.", "GM decides."),
        ("Door/core description is cosmetic only.", "Grant a minor bonus (e.g., +2) to related checks.", "GM decides."),
        ("Spend 1 Inspiration as a cost, then roll Knowledge of the Dead.", "Add Inspiration as a modifier to the Knowledge of the Dead roll.", "GM decides."),
        ("Nether revenant refers to the Ghosts of the Underworld effect.", "Nether revenant is a separate summoned entity.", "GM decides."),
        ("Gate gets the summoner's current HP as its own pool.", "Gate gets the summoner's max HP as its own pool.", "GM decides."),
        ("Remove the incomplete sentence.", "Treat the sentence as flavor only.", "GM decides."),
        ("\"Within a certain period\" means 1 minute after the wave ends; additions during this time need no new action.", "Each additional creature requires a new full-round action after the wave ends.", "GM decides."),
        ("Owner is at least 1 rank/Sequence lower than you.", "Owner is at least 1 size category lower than you.", "GM decides."),
        ("Halve forced movement (round up) on first use; remove after second.", "Remove forced movement immediately.", "GM decides."),
        ("Spend a swift action to convert one action into two swift actions.", "Spend a swift action to convert two actions into one action type.", "GM decides."),
        ("Bonus = base bonus / (number of species * 2).", "Bonus = (base bonus / number of species) then /2 for rounding.", "GM decides."),
        ("Offsets advantage/disadvantage only for targets higher than you by 1+ Sequence.", "Offsets advantage/disadvantage only when facing multiple attackers.", "GM decides."),
        ("Refers to real-world/setting events that already occurred (narrative requirement).", "Treat as flavor only; no mechanical effect.", "GM decides."),
        ("Doctor's Physical must be 20+ to prevent spread.", "Patient's Physical must be 20+ to prevent spread.", "GM decides."),
        ("Below Sequence 8 start at Infection Level 1 unless directly exposed; otherwise Level 2.", "Below Sequence 8 always start at Infection Level 1.", "GM decides."),
        ("Each round increases the target's charm level against you.", "Each round increases your charm level for the contest.", "GM decides."),
        ("Remote image is purely sensory; no interaction beyond illusion.", "Remote image can also deliver your voice/abilities there.", "GM decides."),
        ("If the target is in a mirrored environment, the illusion is indistinguishable.", "If you are in a mirrored environment, the illusion is indistinguishable.", "GM decides."),
        ("Blocks attacks made by a true god.", "Blocks attacks targeting a true god.", "GM decides."),
        ("10 points of DR are consumed per hit and do not refresh.", "10 points of DR refresh each round.", "GM decides."),
        ("Lightning identification is the lightning attack roll; if it hits, you take half damage.", "You make a resistance check to halve the damage.", "GM decides."),
        ("Take 1d6 fire damage on transformation (once).", "Take 1d6 fire damage each round while transformed.", "GM decides."),
        ("Lose 1 Sanity for minor incarnations, 1d3 for major.", "Always lose 1d3 Sanity.", "GM decides."),
        ("High-Sequence means Sequence 4+.", "High-Sequence means Sequence 3+.", "GM decides."),
        ("1 meter for single-target use; 50 meters for area use.", "Always use 50 meters as the range.", "GM decides."),
        ("Replace “price” with “rate” (growth/metabolic rate).", "Replace “price” with “pace” (narrative only).", "GM decides."),
        ("Recover half Constitution if untreated; full Constitution if treated.", "Recover half Constitution regardless of treatment.", "GM decides."),
        ("Use existing progress tracks; allow an immediate extra test to deepen progress.", "Treat as flavor only; no extra test.", "GM decides."),
        ("Trigger when a plant is created/activated.", "Trigger when a plant is attacked/damaged.", "GM decides."),
        ("Choose how many 1d3 dice to roll (up to available seeds).", "Choose a single 1d3 result instead of rolling.", "GM decides."),
        ("Wither after 3 yield reductions or 48 hours without nursing (whichever comes first).", "Wither only after both 3 reductions and 48 hours without nursing.", "GM decides."),
        ("Choose a Doom check from the Doom table.", "Choose any check affected by Doom to double penalties.", "GM decides."),
        ("Lucky numbers modify a roll you choose (treat as lucky).", "Lucky numbers are flavor only (no mechanical effect).", "GM decides."),
        ("Replace with a standard calamity effect for 61–80.", "Remove the garbled clause entirely.", "GM decides."),
        ("10 Spirituality is a stronger once/day suppression; Remove Doom still exists.", "Treat as an alternative to Remove Doom (choose one).", "GM decides."),
        ("Suffer three backlash instances immediately.", "Suffer three doom level increases.", "GM decides."),
        ("Foresee time only.", "Foresee time and location.", "GM decides."),
        ("For each target higher than you by 1+ Sequence, halve Luck checks.", "For each additional target, halve Luck checks once.", "GM decides."),
        ("Use the Disaster list; GM chooses the common disaster.", "Use a fixed default disaster.", "GM decides."),
        ("Treat as the same ability (Spiritual Storm).", "Treat as a separate Mental Storm effect.", "GM decides."),
        ("Treat as numeric modifiers to checks.", "Treat as changes to Luck/Disadvantage resources.", "GM decides."),
        ("Cap is Mastery.", "Cap is Proficient.", "GM decides."),
        ("At character creation, double growth points from potion Inspiration.", "Use normal Inspiration growth points (no doubling).", "GM decides."),
        ("Target higher than you by 1+ Sequence.", "Target larger than you by 1+ size category.", "GM decides."),
    ]

    out_lines = []
    out_lines.append("# UNCLEAR Review Queue (Batch 9 of 50)")
    out_lines.append("")
    out_lines.append("Pending manual review (50):")
    out_lines.append("")

    for i, (path, lineno, unclear, excerpt) in enumerate(items, 1):
        out_lines.append(f"{i}. Location: `{path}:{lineno}`")
        out_lines.append(f"UNCLEAR: {unclear}")
        out_lines.append("Excerpt:")
        out_lines.append(f"> {excerpt}")
        out_lines.append("Proposed options:")
        opt = options[i - 1] if i - 1 < len(options) else ("[TBD]", "[TBD]", "[TBD]")
        out_lines.append("Option 1: " + opt[0])
        out_lines.append("Option 2: " + opt[1])
        out_lines.append("Option 3: " + opt[2])
        out_lines.append("")

    path_out = pathlib.Path("VSCODE MD Files/unclear_review_queue.md")
    path_out.write_text("\n".join(out_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
