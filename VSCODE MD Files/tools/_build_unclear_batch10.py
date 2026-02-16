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
        ("Interpret level as Sequence level difference.", "Interpret level as character tier difference.", "GM decides."),
        ("Opposed check: your Inspiration vs their divination check.", "Fixed DV 20 for the anti-divination check.", "GM decides."),
        ("Full Physical Defense applies to firearms; light/lightning bypass it.", "Full Physical Defense applies to light/lightning instead of firearms.", "GM decides."),
        ("Treat the listed bonuses as fixed effects.", "Treat the listed bonuses as examples; GM sets exact values.", "GM decides."),
        ("Penalty stacks up to -2 while madness lasts.", "Penalty applies once per madness episode (no stacking).", "GM decides."),
        ("1d3 for minor splits, 1d6 for major splits.", "Apply both 1d3 and 1d6 Sanity checks.", "GM decides."),
        ("Refers to Sequence 1 of the same Pathway; it can regenerate after a day.", "Remove this clause as unclear.", "GM decides."),
        ("Removes the target’s Spirit costs while under your gaze.", "Removes Spirit costs you pay to affect the target.", "GM decides."),
        ("Narrative effect only; no mechanical changes.", "Treat as a world-scale effect in the region (GM-defined).", "GM decides."),
        ("Treat Charm as numeric here; gain +4 to Charm-related checks.", "Treat +4 as Advantage on Charm-related checks.", "GM decides."),
        ("Same personality = same Personality stat value; disadvantages are -2.", "Same personality = same Pathway/Sequence; disadvantages are -4.", "GM decides."),
        ("Life grant = one use/charge of full activation.", "Life grant = one round of the full activation effect.", "GM decides."),
        ("One extra limb per 5 points above the DV (15).", "One extra limb per 5 points above the target’s Constitution.", "GM decides."),
        ("Trigger at max difficulty (25); +1 per Moon Knowledge level.", "Trigger at 20+; +1 per Moon Knowledge level.", "GM decides."),
        ("Refers to the second Lucky Appraisal result.", "Refers to the original difficulty value.", "GM decides."),
        ("Gate gains the same restraint bonuses against undead as the summoner.", "Undead restraint bonuses apply against the gate itself.", "GM decides."),
        ("You can carry 1 training-only figurine in addition to active ones.", "Only 1 figurine can be designated for training at a time.", "GM decides."),
        ("Keep the phrase; it means area damage can consume multiple Stand-ins.", "Ignore the phrase and follow the explicit area-damage rules below.", "GM decides."),
        ("Substitute state and avatar state are the same.", "Avatar state is a stronger variant of substitute state.", "GM decides."),
        ("“Your damage” means your normal attack damage.", "“Your damage” refers to this ability’s base damage only.", "GM decides."),
        ("Immune to Hard Damage while in bat swarm.", "Hard Damage applies but only to the swarm’s total HP.", "GM decides."),
        ("Base +1 from moonlight plus +1 per Moon Knowledge level; “in train” = Trained.", "Only +1 total; no additional stacking.", "GM decides."),
        ("Add Moon Knowledge level to the extra spirituality bonus.", "Add +1 per Moon Knowledge level (flat).", "GM decides."),
        ("Heart-hit disadvantage means attackers have disadvantage; holy attacks <=1 character above still allow reorg.", "Treat this clause as flavor only.", "GM decides."),
        ("Free actions only; no attack/casting actions.", "No actions except movement actions.", "GM decides."),
        ("Applies if attacker is 1 character or 2 Sequence levels below you (either).", "Applies only if both conditions are met.", "GM decides."),
        ("Cannot avoid light/lightning; must flash out of ranged attack range.", "Light/lightning still hits unless you exit line of sight.", "GM decides."),
        ("Apply Sequence/character multipliers on top of Trained/Proficient/Advanced multipliers.", "Replace base multipliers with Sequence/character multipliers.", "GM decides."),
        ("Stealth Potion refers to the Invisibility Potion.", "Add a distinct Stealth Potion (GM-defined).", "GM decides."),
        ("Two courses are required to exceed the drug maker’s level (Sequence/skill).", "Two courses are required to exceed the drug maker’s Constitution/resistance.", "GM decides."),
        ("“Blood adult” means an adult blood-race specimen.", "“Blood adult” means a mature bloodline stage.", "GM decides."),
        ("Bloodline legacy = a bloodline relic/replacement material.", "Bloodline legacy = a living descendant’s blood.", "GM decides."),
        ("Use Sequence 9 rapid growth rules; cap at Proficient; 2/3/4 growths.", "Treat as flavor only (no mechanical change).", "GM decides."),
        ("Full Physical Defense vs firearms; light/lightning bypass it.", "Full Physical Defense vs light/lightning instead of firearms.", "GM decides."),
        ("Light/lightning cannot be avoided by this ability.", "Light/lightning can be avoided by leaving the area.", "GM decides."),
        ("Moribund due to lack of health = at 0 HP.", "Moribund due to lack of health = below 10% HP.", "GM decides."),
        ("Refers to skipping a promotion check with a successful identification.", "Refers to a special jump-path ritual check.", "GM decides."),
        ("Remove the fragment as uninterpretable.", "Treat as referring to the ritual object responsible.", "GM decides."),
        ("Follow the target player’s wishes.", "Follow the summoner’s wishes.", "GM decides."),
        ("Use Sequence 9 rapid growth; cap at Proficient; each non-repeat tame = 1 growth.", "Treat as flavor only.", "GM decides."),
        ("Maintain inspired animals equal to your Inspiration; they share senses.", "Maintain inspired animals equal to your Sequence level.", "GM decides."),
        ("Grant +4 benefit to Sanity Loss Identification as if Sequence 9.", "Apply a -4 penalty to the target’s sanity checks.", "GM decides."),
        ("The animal receives the -2 benefit on promotion.", "You receive the -2 benefit when promoting the animal.", "GM decides."),
        ("“1 character larger” means size category larger by 1.", "“1 character larger” means Sequence higher by 1.", "GM decides."),
        ("At character creation for higher Sequences, double potion Inspiration for growth skills.", "Only applies when creating higher-Sequence characters at start.", "GM decides."),
        ("“Mod” refers to the current module/adventure.", "“Mod” refers to the broader campaign setting.", "GM decides."),
        ("“Negligible” means no effective cap (remove the limit).", "Set a high cap (e.g., 100) instead of removing it.", "GM decides."),
        ("Credit appraisal = a Reputation/Credit check.", "Credit appraisal = an Inspiration appraisal.", "GM decides."),
        ("Uncertainty madness = indeterminate madness; restore sleep benefit once.", "Remove this clause as unclear.", "GM decides."),
        ("After 3 injections, effectiveness is reduced by Constitution/2.", "After 3 injections, required dose increases by Constitution/2.", "GM decides."),
    ]

    out_lines = []
    out_lines.append("# UNCLEAR Review Queue (Batch 10 of 50)")
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
