import re
import pathlib
import subprocess


def main() -> None:
    rg_cmd = ["rg", "-n", r"\[\[UNCLEAR", "VSCODE MD Files/draft"]
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
        ("Cap is Mastery; you can learn quickly up to Mastery.", "Cap is Proficient; you cannot advance further.", "GM decides."),
        ("At character creation, double growth points from potion Inspiration.", "Use normal Inspiration growth points (no doubling).", "GM decides."),
        ("Interpret as Sequence higher than you by 1+.", "Interpret as multiple targets (more than one).", "GM decides."),
        ("Levels refer to Sequence levels.", "Levels refer to Difficulty Value tiers.", "GM decides."),
        ("Your Inspiration roll sets the anti-divination DV.", "Opposed roll: your Inspiration vs their check.", "GM decides."),
        ("Against firearms, retain full Physical Defense; light/lightning unaffected.", "Swap: firearms use full defense, light/lightning use normal.", "GM decides."),
        ("Blocks attacks made by the true god.", "Blocks attacks targeting the true god.", "GM decides."),
        ("Set Pathway to Earth (Mother/Desolation).", "Leave Pathway as TBD.", "GM decides."),
        ("Treat as numeric modifiers to checks.", "Treat as changes to Luck/Disadvantage resources.", "GM decides."),
        ("Set Pathway to Earth (Pallbearers).", "Leave Pathway as TBD.", "GM decides."),
        ("Choose a Doom check from the Doom table.", "Choose any check affected by Doom to double penalties.", "GM decides."),
        ("Lucky numbers modify a roll you choose (treat as lucky).", "Lucky numbers are flavor only (no mechanical effect).", "GM decides."),
        ("Treat as a standard calamity effect for 61–80 (replace garble).", "Remove this clause entirely.", "GM decides."),
        ("10 Spirituality is a stronger once/day suppression; Remove Doom still exists.", "Treat as an alternative to Remove Doom (choose one).", "GM decides."),
        ("Suffer three backlash instances immediately.", "Suffer three doom level increases.", "GM decides."),
        ("10 charges of DR that are consumed per hit.", "10 points of DR that refresh each round.", "GM decides."),
        ("Graeme is a named example creature; keep as example.", "Remove the name and generalize the sentence.", "GM decides."),
        ("Use 30% as the threshold.", "Any Sanity loss (less than 100%) triggers it.", "GM decides."),
        ("Foresee time only.", "Foresee time and location.", "GM decides."),
        ("For each target higher than you by 1+, halve Luck checks.", "For each additional target, halve Luck checks once.", "GM decides."),
        ("Use the Disaster list; GM chooses the common disaster.", "Use a fixed default disaster.", "GM decides."),
        ("Treat as the same ability (Spiritual Storm).", "Treat as a separate Mental Storm effect.", "GM decides."),
        ("Reorder as a poetic name only (no mechanical effect).", "Remove this clause entirely.", "GM decides."),
        ("Can trigger multiple times per round without a cap.", "Limit to once per round.", "GM decides."),
        ("1d4 for ordinary targets; 1d6+1 for stronger targets.", "Always use 1d6+1.", "GM decides."),
        ("Rebuke/negotiation vs Will Defense on success applies the effect.", "Require both rebuke and negotiation to succeed.", "GM decides."),
        ("3 minutes required for demigods; lower targets are faster.", "3 minutes required for non-demigods; demigods are immune.", "GM decides."),
        ("Sequence lower by 1 uses two -4 checks; duration while undead.", "Remove this clause entirely.", "GM decides."),
        ("Biology +1 skill rank.", "Biology +1 attribute level.", "GM decides."),
        ("Reduced training to reach Mastery.", "Immediate Mastery on gain.", "GM decides."),
        ("Touch a point within 10 meters (10m range).", "Touch yourself; affect soil at least 10 meters away.", "GM decides."),
        ("+4 to your Stealth.", "+4 to the opponent's Scouting.", "GM decides."),
        ("Target makes a lightning attack roll against you.", "You make a resistance check against lightning.", "GM decides."),
        ("Ends underground stealth and hiding.", "Ends hiding only; remains underground.", "GM decides."),
        ("Treat biological defense as a defined stat from core rules.", "Treat as Constitution-based defense.", "GM decides."),
        ("Add half Strength as a flat bonus (round down).", "Add half Strength as damage dice (round down).", "GM decides."),
        ("Damaged vine ends the effect.", "Damaged vine halves its effectiveness.", "GM decides."),
        ("50m cone in front of you.", "50m line in front of you.", "GM decides."),
        ("Invalid for targets Sequence higher by 1+.", "Invalid for targets larger than you.", "GM decides."),
        ("Spirit points = Spirituality points.", "Spirit points are a separate resource.", "GM decides."),
        ("Suffer 1d6 fire damage on transformation.", "Suffer 1d6 fire damage per round while transformed.", "GM decides."),
        ("Flight speed equals your Mobility.", "Flight speed equals half your Mobility.", "GM decides."),
        ("Maximum spotting distance becomes 1 km.", "Ability range for vision effects becomes 1 km.", "GM decides."),
        ("Special breeds are GM-approved templates.", "Special breeds are any extraordinary breeds.", "GM decides."),
        ("Use 1 for minor cases and 1d3 for severe cases.", "Always use 1d3.", "GM decides."),
        ("Immune to grapple/tackle except Clown precise control.", "Immune to forced movement except Clown precise control.", "GM decides."),
        ("Treat as a +4 bonus.", "Treat as Advantage.", "GM decides."),
        ("GM-approved creature templates; data = stat block written in advance.", "Remove clause; use standard creature stats.", "GM decides."),
        ("High-Sequence means Sequence 4+; cap equals Inspiration.", "High-Sequence means Sequence 3+; cap equals Inspiration.", "GM decides."),
        ("Use 1 meter for precise targets, 50 meters for area use.", "Always use 50 meters as the range.", "GM decides."),
    ]

    out_lines = []
    out_lines.append("# UNCLEAR Review Queue (Batch 8 of 50)")
    out_lines.append("")
    out_lines.append("Resolved in this batch:")
    out_lines.append("- Auto-fixed: `draft/sequences/fate/seq-08.md` training ladder clarified to cap at Proficient.")
    out_lines.append("- Auto-fixed: `draft/sequences/fate/seq-08.md` \"higher than 1 person\" -> Sequence higher by 1+.")
    out_lines.append("- Auto-fixed: `draft/sequences/mutant/seq-08.md` \"rd20s\" -> \"d20 rolls\".")
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
