(function(){
  "use strict";

  const STORAGE_KEY = "lotm_char_v1";
  const NAV_STATE_KEY = "rv_nav_open";
  const SIDEBAR_COLLAPSE_KEY = "rv_sidebar_collapsed";
  const SAVE_DEBOUNCE_MS = 220;
  const ROLL_LOG_MAX = 50;
  const COMPENDIUM_URL = "/assets/compendium.json";

  const ATTR_KEYS = ["str","dex","con","wil","int","edu","cha","luk"];
  const ATTR_LABELS = {
    str: "Strength (STR)",
    dex: "Agility (DEX)",
    con: "Constitution (CON)",
    wil: "Willpower (WIL)",
    int: "Intuition (INT)",
    edu: "Education (EDU)",
    cha: "Charisma (CHA)",
    luk: "Luck (LUK)"
  };
  const ATTR_SHORT_LABELS = {
    str: "STR",
    dex: "DEX",
    con: "CON",
    wil: "WIL",
    int: "INT",
    edu: "EDU",
    cha: "CHA",
    luk: "LUK"
  };
  const ATTR_PREVIEW_LABELS = {
    str: "Str",
    dex: "Dex",
    con: "Con",
    wil: "Wil",
    int: "Int",
    edu: "Edu",
    cha: "Cha",
    luk: "Luk"
  };
  const DEF_PREVIEW_LABELS = {
    physical: "Physical",
    willpower: "Willpower",
    constitution: "Constitution",
    armor: "Armor",
    physical_bonus: "Physical Bonus",
    willpower_bonus: "Willpower Bonus",
    constitution_bonus: "Constitution Bonus",
    spiritual: "Spiritual"
  };
  const RES_PREVIEW_LABELS = {
    hp: "Health",
    spirituality: "Spirituality",
    sanity: "Sanity",
    luck: "Luck",
    hp_max: "Max Health",
    spirituality_max: "Max Spirituality",
    sanity_max: "Max Sanity",
    luck_max: "Max Luck",
    digestion_pct: "Digestion"
  };
  const MOD_PREVIEW_LABELS = { bonus: "Bonus" };
  const VITAL_RESOURCE_KEYS = ["spirituality","sanity","luck"];
  const VITAL_RESOURCE_LABELS = {
    spirituality: "Spirituality",
    sanity: "Sanity",
    luck: "Luck"
  };
  const DEFENSE_MANAGER_TARGETS = {
    "def.physical": { field: "physical", short: "PD", label: "Physical Defense" },
    "def.willpower": { field: "willpower", short: "WD", label: "Willpower Defense" },
    "def.constitution": { field: "constitution", short: "CD", label: "Constitution Defense" }
  };

  const PROF_MOD = { untrained:-4, trained:2, proficient:4, advanced:5, expert:6, scholar:7, master:8 };
  const PROF_ORDER = ["untrained","trained","proficient","advanced","expert","scholar","master"];
  const PROF_LABEL = {
    untrained:"Untrained", trained:"Trained", proficient:"Proficient", advanced:"Advanced",
    expert:"Expert", scholar:"Scholar", master:"Master"
  };
  const LEGACY_LANGUAGE_SKILLS = { mysticism_languages:true, common_languages:true };
  const COMMON_LANGUAGE_PRESETS = [
    "Loen",
    "Intis",
    "Feysac",
    "Dutan",
    "Highland",
    "Plateau Language"
  ];
  const MYSTIC_LANGUAGE_PRESETS = [
    "Hermes Language",
    "Ancient Hermes Language",
    "Ancient Feysac",
    "Giant",
    "Dragon Tongue",
    "Elvish",
    "Old One Tongue"
  ];

  const SKILL_GROUPS = [
    { id:"str", title:"Strength (STR) Skills", attr:"str", skills:[
      ["climbing","Climbing"],["throwing","Throwing"],["fighting","Fighting"],["intimidation","Intimidation"],["jumping","Jumping"],["animal_handling","Animal Handling"]
    ]},
    { id:"dex", title:"Agility (DEX) Skills", attr:"dex", skills:[
      ["stealth","Stealth"],["sleight_of_hand","Sleight of Hand"],["swimming","Swimming"],["shooting","Shooting"],["artillery","Artillery"],["lockpicking","Lockpicking"],["dodge","Dodge"],["driving","Driving"],["heavy_machinery","Heavy Machinery"]
    ]},
    { id:"int", title:"Intuition (INT) Skills", attr:"int", skills:[
      ["listen","Listen"],["investigation","Investigation"],["mechanical_repair","Mechanical Repair"],["mysticism","Mysticism"],["psychology","Psychology"],["cooking","Cooking"],["art","Art"],["track","Track"],["lip_reading","Lip Reading"]
    ]},
    { id:"edu", title:"Education (EDU) Skills", attr:"edu", skills:[
      ["navigation","Navigation"],["trade","Trade"],["medicine","Medicine"],["library_use","Library Use"],["writing","Writing"],["demolitions","Demolitions"],["survival","Survival"],["knowledge","Knowledge (Specialty)"],["natural_world","Natural World"]
    ]},
    { id:"cha", title:"Charisma (CHA) Skills", attr:"cha", skills:[
      ["charisma","Charisma"],["deception","Deception"],["fast_talk","Fast Talk"],["persuade","Persuade"],["psychological_guidance","Psychological Guidance"],["performance","Performance"],["disguise","Disguise"],["reputation","Reputation"]
    ]}
  ];

  const BUILTIN_SKILLS = {};
  SKILL_GROUPS.forEach(function(g){
    g.skills.forEach(function(s){ BUILTIN_SKILLS[s[0]] = { label:s[1], attr:g.attr, group:g.title }; });
  });

  const REF_ALIASES = {
    bonus: "mod.bonus",
    "mod.bonus": "mod.bonus",
    "attr.strength":"attr.str", "attr.agility":"attr.dex", "attr.constitution":"attr.con",
    "attr.willpower":"attr.wil", "attr.intuition":"attr.int", "attr.education":"attr.edu",
    "attr.charisma":"attr.cha", "attr.luck":"attr.luk",
    "attr.endurance":"attr.con", "attr.intellect":"attr.int", "attr.perception":"attr.int",
    "def.mental":"def.willpower", "def.corruption":"def.constitution", "def.spiritual":"def.willpower",
    "skill.occultism":"skill.mysticism"
  };

  const DEF_MAP = {
    physical_defense:"@def.physical", willpower_defense:"@def.willpower", constitution_defense:"@def.constitution",
    physical:"@def.physical", willpower:"@def.willpower", constitution:"@def.constitution"
  };
  const ACTION_ORDER = ["attack","cast","swift","free","move","full-round","none"];

  const CONDITION_DEFS = [
    {
      id: "off_balance",
      label: "Off-Balance",
      short: "No Move actions. DEX is halved (rounded up) for movement and Physical Defense.",
      effects: { dexHalf:true, blockMove:true }
    },
    {
      id: "helpless",
      label: "Helpless",
      short: "No actions. Treated as Restrained. Physical Defense loses DEX and Dodge.",
      effects: { blockAllActions:true, suppressPhysicalDexDodge:true, blockMove:true }
    },
    {
      id: "silenced",
      label: "Silenced",
      short: "Speech-related actions/abilities are unavailable.",
      effects: { blockSpeech:true }
    },
    {
      id: "restrained",
      label: "Restrained",
      short: "No Move actions. Physical Defense loses DEX and Dodge.",
      effects: { suppressPhysicalDexDodge:true, blockMove:true }
    },
    {
      id: "caught_off_guard",
      label: "Caught Off Guard",
      short: "Physical Defense loses DEX and Dodge.",
      effects: { suppressPhysicalDexDodge:true }
    },
    {
      id: "dazed",
      label: "Dazed",
      short: "Lose 1 Attack/Casting/Move action or 2 Swift actions (choice each turn).",
      effects: {}
    },
    {
      id: "stunned",
      label: "Stunned",
      short: "No Attack/Casting/Move actions; at most 1 Swift action.",
      effects: { blockAttack:true, blockCast:true, blockMove:true }
    },
    {
      id: "blinded",
      label: "Blinded",
      short: "Targeting is limited; use INT/Listening checks to locate targets.",
      effects: {}
    },
    {
      id: "deafened",
      label: "Deafened",
      short: "Listening checks fail; hearing-based sensing is impaired.",
      effects: {}
    },
    {
      id: "invisible",
      label: "Invisible",
      short: "Enemies need opposed Investigation/Listening/Intuition to locate you.",
      effects: {}
    },
    {
      id: "fear",
      label: "Fear",
      short: "-4 on checks related to the fear source; movement tends away from source.",
      effects: { checkMod:-4 }
    },
    {
      id: "taunted",
      label: "Rage / Taunted",
      short: "-4 on skill/attribute checks until calm is regained.",
      effects: { checkMod:-4 }
    },
    {
      id: "advantage",
      label: "Advantage",
      short: "+2 favorable bonus on checks against enemies.",
      effects: { checkMod:2 }
    },
    {
      id: "disadvantage",
      label: "Disadvantage",
      short: "Physical Defense suffers -2 to DEX/Dodge contribution.",
      effects: { physicalDexDodgePenalty:-2 }
    },
    {
      id: "poisoned",
      label: "Poisoned",
      short: "-2 on skill/attribute checks; takes periodic toxin damage.",
      effects: { checkMod:-2 }
    },
    {
      id: "bloodbath",
      label: "Bloodbath",
      short: "Severe wound state; may cause fainting/bleeding depending on target type.",
      effects: {}
    },
    {
      id: "bleeding",
      label: "Bleeding",
      short: "Loses vitality each round until treatment.",
      effects: {}
    }
  ];

  const SPECIAL_ACTION_DEFS = [
    {
      id:"spiritual_intuition",
      name:"Spiritual Intuition",
      type:"Universal",
      action:"none",
      range:"Self",
      checkExpr:"1d20 + @attr.int + @skill.mysticism",
      effectExpr:"",
      notes:"Difficulty 25 intuition check. Use for danger sense/divination-like guidance.",
      description:"Action: none (passive trigger). Check: Intuition (INT) Difficulty 25. On success, you sense whether an action should or should not be done, or feel vague danger/wrongness. Repeating the same question generally yields the same result until circumstances change."
    },
    {
      id:"grapple",
      name:"Grapple",
      type:"Special",
      action:"attack",
      range:"Melee",
      checkExpr:"1d20 + @attr.str + @skill.fighting",
      effectExpr:function(context){ return strengthDamageExpr(context); },
      notes:"Check contests Physical Defense (ignoring armor). Success applies Restrained.",
      description:"Action: 1 Attack Action. Check: Fighting vs Physical Defense (ignoring armor). Success applies [[Restrained]]. While grappling, both sides are effectively restrained; the grappled side can contest Strength each turn to break free. One-handed grappling is possible but halves the Strength contest."
    },
    {
      id:"double_strike",
      name:"Double Strike",
      type:"Special",
      action:"attack",
      range:"Melee / Thrown Short Weapon",
      checkExpr:"1d20 + @attr.dex + @skill.fighting",
      effectExpr:"",
      checkRollCount:2,
      notes:"Resolve two hit checks within one Attack action.",
      description:"Used with 1 Attack Action while using fists or short-blade style attacks. Make two hit checks using DEX-based fighting. Both attacks happen inside the same Attack Action."
    },
    {
      id:"point_blank_shooting",
      name:"Point-Blank Shooting",
      type:"Special",
      action:"attack",
      range:"Within 1 meter",
      checkExpr:"1d20 + @attr.dex + @skill.shooting + 2",
      effectExpr:"",
      notes:"Point-blank firearm burst. Build-Up Aim benefit is included as +2.",
      description:"Action: 1 Attack Action at very close range. The first shot resolves with reduced defense terms and all three shots gain Build-Up Aim style benefits where applicable. If the target pre-declared and prepared specifically to dodge this point-blank line, the benefit can be negated."
    },
    {
      id:"charge",
      name:"Charge",
      type:"Special",
      action:"attack",
      range:"Melee after movement",
      checkExpr:"1d20 + @attr.str + @skill.fighting",
      effectExpr:"",
      notes:"Contest target STR or DEX. Success applies Off-Balance.",
      description:"Action: 1 Attack Action, often chained with movement. Check: your Strength contests the target's Strength or Agility (DEX). Success causes [[Off-Balance]] (DEX halved, movement impaired until they spend a Move Action to recover)."
    },
    {
      id:"borrow_strength",
      name:"Borrow Strength Against Strength",
      type:"Special",
      action:"attack",
      range:"Melee reaction window",
      checkExpr:"1d20 + @attr.str + @skill.fighting",
      effectExpr:function(context){ return combineExpr("1d3", strengthDamageExpr(context)); },
      notes:"Triggered when enemy melee critically fails. Effect defaults to 1d3 + STR damage die.",
      description:"Trigger: target makes a melee attack against you and critically fails. You exploit momentum to throw or reverse them. Standard effect can deal 1d3 + Strength damage die and may force [[Off-Balance]] / [[Stunned]] follow-up checks depending on circumstances."
    },
    {
      id:"leg_sweep",
      name:"Leg Sweep",
      type:"Special",
      action:"attack",
      range:"Within height/2",
      checkExpr:"1d20 + @attr.dex + @skill.fighting",
      effectExpr:function(context){ return combineExpr("1d3", halfStrengthDamageExpr(context)); },
      requiresDexAtLeast:5,
      notes:"Up to 3 close targets. Damage uses half STR damage die (rounded up).",
      description:"Requirement: higher Agility (DEX) threshold (5+). Action: used with 1 Attack Action, striking with legs instead of hands. You can target up to 3 nearby enemies. Damage is limited to half Strength damage die (rounded up), with special critical-failure consequences."
    },
    {
      id:"intimidate",
      name:"Intimidate",
      type:"Special",
      action:"swift",
      range:"Within 1 meter",
      checkExpr:"1d20 + @attr.cha + @skill.intimidation",
      effectExpr:"",
      notes:"Contest target Willpower check. Success forces immediate movement away.",
      description:"Action: 1 Swift Action (once per round). Target: one creature within 1 meter. Check: Intimidation contested by Willpower (WIL). On success, the target must immediately spend a Move Action to create distance."
    },
    {
      id:"feint",
      name:"Feint",
      type:"Special",
      action:"swift",
      range:"Melee",
      checkExpr:"1d20 + @attr.cha + @skill.deception",
      effectExpr:"",
      notes:"Contest Investigation/Intuition. Success causes Caught Off Guard on next attack.",
      description:"Action: 1 Swift Action. You fake attack or casting posture to deceive. Contest Deception/Performance/Brawling against Investigation or Intuition (INT). Success can put the target into [[Caught Off Guard]] for the following real strike."
    },
    {
      id:"first_aid",
      name:"First Aid",
      type:"Special",
      action:"cast",
      range:"Touch / Adjacent",
      checkExpr:"1d20 + @attr.edu + @skill.medicine",
      effectExpr:"",
      notes:"Ends Bloodbath/Bleeding and external-wound Poisoned. Does not restore vitality.",
      description:"Action: 1 Casting Action (or full-round in severe vitality states). First Aid ends [[Bloodbath]], [[Bleeding]], and external-wound [[Poisoned]] effects. It does not directly restore vitality."
    },
    {
      id:"vital_strike",
      name:"Vital Strike",
      type:"Special",
      action:"attack",
      range:"Weapon range",
      checkExpr:"1d20 + @attr.str + @skill.fighting - 10",
      effectExpr:"2d6",
      notes:"Base vital strike penalty is -10. Use target body-part effects from core rules.",
      description:"Vital Strike is an Attack or Casting action aimed at a body part. The hit check takes -10. On success, body-part effects apply (head/eyes/ears/arms/legs/organs), including extra damage and persistent penalties until treated."
    },
    {
      id:"limb_block",
      name:"Limb Block",
      type:"Special",
      action:"swift",
      range:"Self",
      checkExpr:"1d20 + @attr.dex",
      effectExpr:"",
      notes:"DEX contest to redirect a vital strike onto one chosen limb.",
      description:"Action: 1 Swift Action. Choose one limb to intercept a Vital Strike targeting you. Make a DEX contest; on success the strike is redirected to that limb. Each limb can only be used this way once before reset/recovery."
    },
    {
      id:"burn_luck",
      name:"Burn Luck",
      type:"Special",
      action:"free",
      range:"Self",
      checkExpr:"",
      effectExpr:"",
      notes:"Once per 24h: spend Luck and add the same value to one check (not damage rolls).",
      description:"Action: 1 Free Action. Once per 24 hours, spend current Luck and add the same amount to one eligible check (not damage rolls). Burned Luck recovers over time and cannot reduce Luck below 0."
    },
    {
      id:"reveal_partial_mythos_markings",
      name:"Reveal Partial Mythos Markings",
      type:"Mythos",
      action:"swift",
      range:"Visible targets",
      checkExpr:"",
      effectExpr:"",
      maxSequence:4,
      notes:"Requires Sequence 4 or above (numerically 4 or lower). Exposes rune-based witness effects.",
      description:"Action: 1 Swift Action. Requirement: Sequence 4 or above. Reveal partial Mythos runes on selected body parts without entering full Mythos form. Witnesses may suffer rank-gap mythos witnessing effects unless they avert gaze or pass relevant intuition checks."
    }
  ];

  const STR_BONUS_TABLE = [[0,"-2"],[1,"-1"],[2,"0"],[3,"1"],[4,"1d2"],[5,"1d4"],[6,"1d6"],[7,"1d8"],[8,"1d10"],[9,"1d12"],[10,"2d6"],[11,"2d8"],[12,"2d10"],[13,"2d12"],[14,"3d8"],[15,"3d10"],[20,"3d12"],[25,"4d10"],[30,"4d12"]];

  function attrObj(){ return { str:0,dex:0,con:0,wil:0,int:0,edu:0,cha:0,luk:0 }; }

  function conditionFlagObj(){
    const out = {};
    CONDITION_DEFS.forEach(function(def){ out[def.id] = false; });
    return out;
  }

  const DEFAULT_CHAR = {
    meta: { name:"", player:"", age:"", occupation:"", pathway:"", race:"", gender:"", portrait:"", sequence:"9", level:1 },
    attr: attrObj(),
    attr_base: attrObj(),
    skill: {},
    skill_meta: {},
    def: {
      physical:10,
      physical_temp:0,
      willpower:10,
      willpower_temp:0,
      constitution:10,
      constitution_temp:0,
      armor:0,
      physical_bonus:0,
      willpower_bonus:0,
      constitution_bonus:0,
      spiritual:0
    },
    res: {
      hp:0,
      hp_temp:0,
      hp_max_override:0,
      spirituality:0,
      spirituality_temp:0,
      sanity:0,
      sanity_temp:0,
      luck:0,
      luck_temp:0,
      hp_max:0,
      spirituality_max:0,
      sanity_max:0,
      luck_max:0,
      hp_max_bonus:0,
      spirituality_max_bonus:0,
      sanity_max_bonus:0,
      luck_max_bonus:0,
      digestion_pct:0
    },
    mod: { bonus:0 },
    beyonder: { attr_bonus:attrObj(), digestion_pct:0, npc_companions:"", custom_spells:"", grazed_souls:"", recorded_abilities:"", stolen_abilities:"" },
    abilities: { imported:[], last_import:{ pathway:"", sequence:"" } },
    actions: [],
    adventure_log: [],
    items: [],
    wealth: { total_savings:"", liquid_assets:"", total_assets:"", weekly_pay:"", weekly_rent:"", residence:"", servant:"", lifestyle:"" },
    backstory: "",
    description: { appearance:"", height:"", weight:"", deity_worshipped:"", alignment_faction:"", ideals_beliefs:"", important_person:"", valued_possession:"", meaningful_place:"", wounds_scars:"", likes:"", dislikes:"" },
    conditions: { active:conditionFlagObj(), notes:"" },
    sheet: {
      unspent_intuition_points:0,
      unspent_education_points:0,
      pocket_slots:0,
      carry_slots_override:0,
      hidden_pocket_slots:0,
      carry_slots_used:0,
      custom_skills:[],
      languages:{ mysticism:[], common:[] }
    }
  };

  function cloneDefault(){ return JSON.parse(JSON.stringify(DEFAULT_CHAR)); }
  function safeJsonParse(raw, fallback){ try{ return JSON.parse(raw); }catch(_e){ return fallback; } }
  function isObj(v){ return !!v && typeof v === "object" && !Array.isArray(v); }
  function num(v, fb){ const n = Number(v); return Number.isFinite(n) ? n : fb; }
  function int(v, fb){ const n = Number(v); return Number.isFinite(n) ? Math.trunc(n) : fb; }
  function clamp(v,min,max){ return Math.min(max, Math.max(min, v)); }
  function token(v){ return String(v||"").trim().toLowerCase().replace(/\s+/g,"_").replace(/[^a-z0-9_:-]/g,""); }
  function splitLangText(text){
    return String(text || "")
      .split(/[\n,;]+/)
      .map(function(v){ return String(v || "").trim(); })
      .filter(Boolean);
  }
  function normalizeLanguageEntry(entry){
    if(!isObj(entry)) return null;
    const name = String(entry.name || "").trim();
    const id = String(entry.id || ("lang_" + Math.random().toString(36).slice(2,8)));
    if(!id) return null;
    return {
      id: id,
      name: name,
      level: prof(entry.level || "proficient"),
      preset: !!entry.preset
    };
  }
  function normalizeLanguageList(raw){
    if(Array.isArray(raw)){
      return raw.map(normalizeLanguageEntry).filter(Boolean);
    }
    if(typeof raw === "string"){
      return splitLangText(raw).map(function(name){
        return { id:"lang_" + Math.random().toString(36).slice(2,8), name:name, level:"proficient", preset:false };
      });
    }
    return [];
  }

  function languagePresetList(kind){
    return kind === "mysticism" ? MYSTIC_LANGUAGE_PRESETS : COMMON_LANGUAGE_PRESETS;
  }

  function languageNameKey(name){
    return String(name || "").trim().toLowerCase();
  }

  function ensurePresetLanguages(kind, bucket){
    const list = Array.isArray(bucket) ? bucket : [];
    const seen = new Set(list.map(function(entry){ return languageNameKey(entry && entry.name); }).filter(Boolean));
    languagePresetList(kind).forEach(function(name){
      const key = languageNameKey(name);
      if(!key || seen.has(key)) return;
      list.push({
        id: "lang_" + kind + "_" + token(name),
        name: name,
        level: "proficient",
        preset: true
      });
      seen.add(key);
    });
    return list;
  }

  function normalizeConditionFlags(raw){
    const out = conditionFlagObj();
    if(!isObj(raw)) return out;
    Object.keys(out).forEach(function(id){ out[id] = !!raw[id]; });
    return out;
  }

  function getPath(obj, path){
    const seg = String(path||"").split(".").filter(Boolean);
    let cur = obj, i;
    for(i=0;i<seg.length;i+=1){ if(!isObj(cur) || !Object.prototype.hasOwnProperty.call(cur, seg[i])) return undefined; cur = cur[seg[i]]; }
    return cur;
  }

  function setPath(obj, path, value){
    const seg = String(path||"").split(".").filter(Boolean);
    let cur = obj, i;
    if(!seg.length) return;
    for(i=0;i<seg.length-1;i+=1){ if(!isObj(cur[seg[i]])) cur[seg[i]] = {}; cur = cur[seg[i]]; }
    cur[seg[seg.length-1]] = value;
  }

  function prof(v){ const k = String(v||"").toLowerCase().trim(); return Object.prototype.hasOwnProperty.call(PROF_MOD,k) ? k : "untrained"; }

  function normalizeSkillMeta(raw, fallback){
    const out = {};
    if(isObj(raw)){
      Object.keys(raw).forEach(function(k){
        const id = token(k); if(!id) return;
        if(Object.prototype.hasOwnProperty.call(LEGACY_LANGUAGE_SKILLS, id)) return;
        const e = raw[k];
        if(!isObj(e)){ out[id] = { proficiency:"untrained", intuition:0, education:0, bonus:int(e,0) }; return; }
        out[id] = { proficiency:prof(e.proficiency), intuition:int(e.intuition,0), education:int(e.education,0), bonus:int(e.bonus,0) };
      });
    }
    if(isObj(fallback)){
      Object.keys(fallback).forEach(function(k){
        const id = token(k);
        if(!id || Object.prototype.hasOwnProperty.call(LEGACY_LANGUAGE_SKILLS, id)) return;
        if(!Object.prototype.hasOwnProperty.call(out,id)) out[id] = { proficiency:"untrained", intuition:0, education:0, bonus:int(fallback[k],0) };
      });
    }
    return out;
  }

  function sanitizeActionEntry(raw){
    const a = isObj(raw) ? raw : {};
    const costObj = isObj(a.cost) ? a.cost : {};
    const action = String(a.action || "cast").toLowerCase();
    return {
      id: String(a.id || ("action_" + Math.random().toString(36).slice(2,8))),
      label: String(a.label || a.name || ""),
      type: String(a.type || "active"),
      action: ACTION_ORDER.indexOf(action) >= 0 ? action : "cast",
      expr: String(a.expr || a.roll || ""),
      opposed_by: String(a.opposed_by || a.opposedBy || "none"),
      spirituality_cost: int(a.spirituality_cost ?? costObj.spirituality, 0),
      range: String(a.range || ""),
      target: String(a.target || ""),
      duration: String(a.duration || ""),
      description: String(a.description || a.text || "")
    };
  }

  function itemUsesHiddenPocket(raw){
    const item = isObj(raw) ? raw : {};
    if(typeof item.hidden_pocket === "boolean") return item.hidden_pocket;
    if(typeof item.hiddenPocket === "boolean") return item.hiddenPocket;
    if(typeof item.hidden === "boolean") return item.hidden;
    if(typeof item.is_hidden_pocket === "boolean") return item.is_hidden_pocket;
    const storage = String(item.storage || item.location || "").toLowerCase();
    return storage.indexOf("hidden pocket") >= 0 || storage.indexOf("secret pocket") >= 0;
  }

  function sanitizeItemEntry(raw){
    const item = isObj(raw) ? raw : {};
    return {
      id: String(item.id || ("item_" + Math.random().toString(36).slice(2,8))),
      storage: String(item.storage || item.location || ""),
      name: String(item.name || ""),
      description: String(item.description || ""),
      slots: Math.max(0, int(item.slots, 0)),
      hidden_pocket: itemUsesHiddenPocket(item)
    };
  }

  function normalizeChar(value){
    const c = cloneDefault();
    if(!isObj(value)){ recomputeChar(c); return c; }

    if(isObj(value.meta)) Object.keys(c.meta).forEach(function(k){
      if(Object.prototype.hasOwnProperty.call(value.meta,k)) c.meta[k] = typeof c.meta[k] === "number" ? int(value.meta[k], c.meta[k]) : String(value.meta[k]||"");
    });

    if(isObj(value.attr)) ATTR_KEYS.forEach(function(k){
      c.attr[k] = int(value.attr[k], c.attr[k]);
      if(k === "str") c.attr[k] = int(value.attr[k] ?? value.attr.strength, c.attr[k]);
      if(k === "dex") c.attr[k] = int(value.attr[k] ?? value.attr.agility, c.attr[k]);
      if(k === "con") c.attr[k] = int(value.attr[k] ?? value.attr.constitution ?? value.attr.endurance, c.attr[k]);
      if(k === "wil") c.attr[k] = int(value.attr[k] ?? value.attr.willpower, c.attr[k]);
      if(k === "int") c.attr[k] = int(value.attr[k] ?? value.attr.intuition ?? value.attr.intellect ?? value.attr.perception, c.attr[k]);
      if(k === "edu") c.attr[k] = int(value.attr[k] ?? value.attr.education, c.attr[k]);
      if(k === "cha") c.attr[k] = int(value.attr[k] ?? value.attr.charisma, c.attr[k]);
      if(k === "luk") c.attr[k] = int(value.attr[k] ?? value.attr.luck ?? value.attr.fate, c.attr[k]);
    });

    if(isObj(value.attr_base)) ATTR_KEYS.forEach(function(k){ c.attr_base[k] = int(value.attr_base[k], c.attr_base[k]); });
    else c.attr_base = Object.assign({}, c.attr);

    if(isObj(value.beyonder) && isObj(value.beyonder.attr_bonus)) ATTR_KEYS.forEach(function(k){ c.beyonder.attr_bonus[k] = int(value.beyonder.attr_bonus[k], c.beyonder.attr_bonus[k]); });

    if(isObj(value.skill)) Object.keys(value.skill).forEach(function(k){
      const id = token(k);
      if(id && !Object.prototype.hasOwnProperty.call(LEGACY_LANGUAGE_SKILLS, id)) c.skill[id] = int(value.skill[k],0);
    });
    c.skill_meta = normalizeSkillMeta(value.skill_meta || value.skillMeta, c.skill);

    if(isObj(value.def)){
      c.def.physical = int(value.def.physical, c.def.physical);
      c.def.physical_temp = Math.max(0, int(value.def.physical_temp ?? value.def.temp_physical, c.def.physical_temp));
      c.def.willpower = int(value.def.willpower ?? value.def.mental, c.def.willpower);
      c.def.willpower_temp = Math.max(0, int(value.def.willpower_temp ?? value.def.temp_willpower ?? value.def.temp_mental, c.def.willpower_temp));
      c.def.constitution = int(value.def.constitution ?? value.def.corruption, c.def.constitution);
      c.def.constitution_temp = Math.max(0, int(value.def.constitution_temp ?? value.def.temp_constitution ?? value.def.temp_corruption, c.def.constitution_temp));
      c.def.armor = int(value.def.armor, c.def.armor);
      c.def.physical_bonus = int(value.def.physical_bonus, c.def.physical_bonus);
      c.def.willpower_bonus = int(value.def.willpower_bonus ?? value.def.mental, c.def.willpower_bonus);
      c.def.constitution_bonus = int(value.def.constitution_bonus ?? value.def.corruption, c.def.constitution_bonus);
      c.def.spiritual = int(value.def.spiritual, c.def.spiritual);
    }

    if(isObj(value.res)){
      c.res.hp = int(value.res.hp, c.res.hp);
      c.res.hp_temp = Math.max(0, int(value.res.hp_temp ?? value.res.temp_hp ?? value.res.temporary_hp, c.res.hp_temp));
      c.res.hp_max_override = Math.max(0, int(value.res.hp_max_override ?? value.res.override_hp_max ?? value.res.hp_override, c.res.hp_max_override));
      c.res.spirituality = int(value.res.spirituality, c.res.spirituality);
      c.res.spirituality_temp = Math.max(0, int(value.res.spirituality_temp ?? value.res.temp_spirituality ?? value.res.spirituality_temp_points, c.res.spirituality_temp));
      c.res.sanity = int(value.res.sanity, c.res.sanity);
      c.res.sanity_temp = Math.max(0, int(value.res.sanity_temp ?? value.res.temp_sanity ?? value.res.sanity_temp_points, c.res.sanity_temp));
      c.res.luck = int(value.res.luck ?? value.res.fate ?? value.res.focus, c.res.luck);
      c.res.luck_temp = Math.max(0, int(value.res.luck_temp ?? value.res.temp_luck ?? value.res.luck_temp_points, c.res.luck_temp));
      c.res.hp_max_bonus = int(value.res.hp_max_bonus ?? value.res.hp_ticket ?? value.res.hp_max_ticket, c.res.hp_max_bonus);
      c.res.spirituality_max_bonus = int(value.res.spirituality_max_bonus ?? value.res.spirituality_ticket ?? value.res.spirituality_max_ticket, c.res.spirituality_max_bonus);
      c.res.sanity_max_bonus = int(value.res.sanity_max_bonus ?? value.res.sanity_ticket ?? value.res.sanity_max_ticket, c.res.sanity_max_bonus);
      c.res.luck_max_bonus = int(value.res.luck_max_bonus ?? value.res.luck_ticket ?? value.res.luck_max_ticket, c.res.luck_max_bonus);
      c.res.digestion_pct = int(value.res.digestion_pct, c.res.digestion_pct);
    }

    if(isObj(value.mod)) c.mod.bonus = int(value.mod.bonus, c.mod.bonus);

    if(isObj(value.beyonder)){
      c.beyonder.digestion_pct = int(value.beyonder.digestion_pct, c.beyonder.digestion_pct);
      c.beyonder.npc_companions = String(value.beyonder.npc_companions || "");
      c.beyonder.custom_spells = String(value.beyonder.custom_spells || "");
      c.beyonder.grazed_souls = String(value.beyonder.grazed_souls || "");
      c.beyonder.recorded_abilities = String(value.beyonder.recorded_abilities || "");
      c.beyonder.stolen_abilities = String(value.beyonder.stolen_abilities || "");
    }

    if(isObj(value.abilities)){
      c.abilities.last_import.pathway = String((value.abilities.last_import && value.abilities.last_import.pathway) || "");
      c.abilities.last_import.sequence = String((value.abilities.last_import && value.abilities.last_import.sequence) || "");
      if(Array.isArray(value.abilities.imported)) c.abilities.imported = value.abilities.imported;
    }

    c.actions = Array.isArray(value.actions) ? value.actions.map(sanitizeActionEntry) : [];
    c.adventure_log = Array.isArray(value.adventure_log) ? value.adventure_log : [];
    c.items = Array.isArray(value.items) ? value.items.map(sanitizeItemEntry) : [];

    if(isObj(value.wealth)) Object.keys(c.wealth).forEach(function(k){ c.wealth[k] = String(value.wealth[k] || ""); });
    if(typeof value.backstory === "string") c.backstory = value.backstory;
    if(isObj(value.description)) Object.keys(c.description).forEach(function(k){ c.description[k] = String(value.description[k] || ""); });

    if(isObj(value.conditions)){
      const rawFlags =
        (isObj(value.conditions.active) && value.conditions.active) ||
        (isObj(value.conditions.special) && value.conditions.special) ||
        value.conditions;
      c.conditions.active = normalizeConditionFlags(rawFlags);
      c.conditions.notes = String(value.conditions.notes || value.conditions.note || "");
    }

    if(isObj(value.sheet)){
      c.sheet.unspent_intuition_points = int(value.sheet.unspent_intuition_points, c.sheet.unspent_intuition_points);
      c.sheet.unspent_education_points = int(value.sheet.unspent_education_points, c.sheet.unspent_education_points);
      c.sheet.pocket_slots = int(value.sheet.pocket_slots, c.sheet.pocket_slots);
      c.sheet.carry_slots_override = int(value.sheet.carry_slots_override, c.sheet.carry_slots_override);
      c.sheet.hidden_pocket_slots = int(value.sheet.hidden_pocket_slots, c.sheet.hidden_pocket_slots);
      c.sheet.carry_slots_used = int(value.sheet.carry_slots_used, c.sheet.carry_slots_used);
      c.sheet.custom_skills = Array.isArray(value.sheet.custom_skills) ? value.sheet.custom_skills : [];
      if(isObj(value.sheet.languages)){
        c.sheet.languages = {
          mysticism: normalizeLanguageList(value.sheet.languages.mysticism),
          common: normalizeLanguageList(value.sheet.languages.common)
        };
      }else{
        const maybeMyst = value.sheet.mysticism_languages || value.sheet.mysticismLanguages || "";
        const maybeCommon = value.sheet.common_languages || value.sheet.commonLanguages || "";
        if(maybeMyst || maybeCommon){
          c.sheet.languages = {
            mysticism: normalizeLanguageList(maybeMyst),
            common: normalizeLanguageList(maybeCommon)
          };
        }
      }
    }

    recomputeChar(c);
    return c;
  }

  function hasRequiredSections(v){ return isObj(v) && isObj(v.meta) && isObj(v.attr) && isObj(v.skill) && isObj(v.def) && isObj(v.res) && isObj(v.mod); }

  function loadChar(){
    try{
      const raw = localStorage.getItem(STORAGE_KEY);
      if(!raw) return normalizeChar(cloneDefault());
      const parsed = JSON.parse(raw);
      if(hasRequiredSections(parsed)) return normalizeChar(parsed);
    }catch(e){ console.warn("Failed to load character state:", e); }
    return normalizeChar(cloneDefault());
  }

  function saveChar(state){
    const s = hasRequiredSections(state) ? normalizeChar(state) : normalizeChar(cloneDefault());
    try{ localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); }catch(e){ console.warn("Failed to save character state:", e); }
    return s;
  }

  function resetChar(){ const fresh = normalizeChar(cloneDefault()); try{ localStorage.setItem(STORAGE_KEY, JSON.stringify(fresh)); }catch(e){ console.warn("Failed to reset character state:", e); } return fresh; }

  function scoreToLevel(score){
    const n = int(score,0);
    if(n <= 0) return { key:"untrained", modifier:-4, label:PROF_LABEL.untrained };
    if(n === 1) return { key:"trained", modifier:2, label:PROF_LABEL.trained };
    if(n === 2) return { key:"proficient", modifier:4, label:PROF_LABEL.proficient };
    if(n === 3) return { key:"advanced", modifier:5, label:PROF_LABEL.advanced };
    if(n === 4) return { key:"expert", modifier:6, label:PROF_LABEL.expert };
    if(n === 5) return { key:"scholar", modifier:7, label:PROF_LABEL.scholar };
    if(n === 6) return { key:"master", modifier:8, label:PROF_LABEL.master };
    return {
      key:"master_plus",
      modifier:Math.min(10, 8 + (n - 6)),
      label:"Master +" + String(n - 6)
    };
  }

  function skillMetaScore(meta){
    const intuition = int(meta && meta.intuition,0);
    const education = int(meta && meta.education,0);
    const bonus = int(meta && meta.bonus,0);
    return intuition + (education * 2) + bonus;
  }

  function skillMod(meta){
    return scoreToLevel(skillMetaScore(meta)).modifier;
  }

  function recomputeSkills(state){
    if(!isObj(state.skill_meta)) state.skill_meta = {};
    if(!isObj(state.skill)) state.skill = {};
    Object.keys(state.skill).forEach(function(k){
      const id = token(k);
      if(!id || Object.prototype.hasOwnProperty.call(LEGACY_LANGUAGE_SKILLS, id)) return;
      if(!Object.prototype.hasOwnProperty.call(state.skill_meta,id)) state.skill_meta[id] = { proficiency:"untrained", intuition:0, education:0, bonus:int(state.skill[k],0) };
    });
    state.skill = {};
    Object.keys(state.skill_meta).forEach(function(k){
      const id = token(k); if(!id) return;
      if(Object.prototype.hasOwnProperty.call(LEGACY_LANGUAGE_SKILLS, id)){ if(id !== k) delete state.skill_meta[k]; else delete state.skill_meta[id]; return; }
      const e = state.skill_meta[k];
      state.skill_meta[id] = { proficiency:prof(e.proficiency), intuition:int(e.intuition,0), education:int(e.education,0), bonus:int(e.bonus,0) };
      if(id !== k) delete state.skill_meta[k];
      const lvl = scoreToLevel(skillMetaScore(state.skill_meta[id]));
      state.skill_meta[id].proficiency = Object.prototype.hasOwnProperty.call(PROF_MOD, lvl.key) ? lvl.key : "master";
      state.skill[id] = skillMod(state.skill_meta[id]);
    });
  }

  function signedNumberText(value){
    const n = int(value, 0);
    if(n > 0) return "+" + String(n);
    return String(n);
  }

  function combineExpr(left, right){
    const a = String(left || "").trim();
    const b = String(right || "").trim();
    if(!a && !b) return "";
    if(!a) return b;
    if(!b) return a;
    const n = Number(b);
    if(Number.isFinite(n) && String(Math.trunc(n)) === b){
      if(n < 0) return a + " - " + String(Math.abs(Math.trunc(n)));
      if(n === 0) return a;
      return a + " + " + String(Math.trunc(n));
    }
    if(b.charAt(0) === "-") return a + " - " + b.slice(1);
    return a + " + " + b;
  }

  function strengthDamageExpr(context){
    const score = int(readPathValue(context, "attr.str"), int(readPathValue(context, "attr.strength"), 0));
    return String(strDamageBonus(score));
  }

  function halfStrengthDamageExpr(context){
    const raw = strengthDamageExpr(context);
    const asNum = Number(raw);
    if(Number.isFinite(asNum) && String(Math.trunc(asNum)) === raw){
      return String(Math.ceil(Math.trunc(asNum) / 2));
    }
    const m = raw.match(/^(\d+)d(\d+)$/i);
    if(!m) return raw;
    const count = Math.max(1, int(m[1], 1));
    const sides = Math.max(1, int(m[2], 1));
    const nextSides = Math.max(1, Math.ceil(sides / 2));
    return String(count) + "d" + String(nextSides);
  }

  function activeConditionEffects(context){
    const c = isObj(context) ? context : {};
    const flags = isObj(c.conditions) && isObj(c.conditions.active) ? c.conditions.active : {};
    const activeIds = [];
    const activeLabels = [];
    const notes = [];
    const blocked = { attack:false, cast:false, move:false, swift:false, free:false, speech:false };
    let checkMod = 0;
    let dexHalf = false;
    let suppressPhysicalDexDodge = false;
    let physicalDexDodgePenalty = 0;

    CONDITION_DEFS.forEach(function(def){
      if(!def || !def.id || !flags[def.id]) return;
      activeIds.push(def.id);
      activeLabels.push(def.label);
      if(def.short) notes.push(def.short);
      const e = isObj(def.effects) ? def.effects : {};
      checkMod += int(e.checkMod, 0);
      if(e.dexHalf) dexHalf = true;
      if(e.suppressPhysicalDexDodge) suppressPhysicalDexDodge = true;
      physicalDexDodgePenalty += int(e.physicalDexDodgePenalty, 0);
      if(e.blockAllActions){
        blocked.attack = true;
        blocked.cast = true;
        blocked.move = true;
        blocked.swift = true;
        blocked.free = true;
      }
      if(e.blockAttack) blocked.attack = true;
      if(e.blockCast) blocked.cast = true;
      if(e.blockMove) blocked.move = true;
      if(e.blockSwift) blocked.swift = true;
      if(e.blockFree) blocked.free = true;
      if(e.blockSpeech) blocked.speech = true;
    });

    if(activeIds.indexOf("stunned") >= 0){
      notes.push("Stunned allows at most 1 Swift action each turn.");
    }
    if(activeIds.indexOf("dazed") >= 0){
      notes.push("Dazed removes either one Attack/Casting/Move action or two Swift actions.");
    }
    if(activeIds.indexOf("silenced") >= 0){
      notes.push("Silenced blocks speech-related actions and spoken abilities.");
    }

    const blockedNames = [];
    if(blocked.attack) blockedNames.push("Attack");
    if(blocked.cast) blockedNames.push("Casting");
    if(blocked.move) blockedNames.push("Move");
    if(blocked.swift) blockedNames.push("Swift");
    if(blocked.free) blockedNames.push("Free");

    const uniqNotes = Array.from(new Set(notes.filter(Boolean)));
    return {
      activeIds: activeIds,
      activeLabels: activeLabels,
      checkMod: checkMod,
      dexHalf: dexHalf,
      suppressPhysicalDexDodge: suppressPhysicalDexDodge,
      physicalDexDodgePenalty: physicalDexDodgePenalty,
      blocked: blocked,
      actionSummary: blockedNames.length ? (blockedNames.join(", ") + " actions blocked") : "No hard action locks",
      noteSummary: uniqNotes.join(" ")
    };
  }

  function effectiveAttrValue(attrKey, context){
    const key = String(attrKey || "").toLowerCase();
    const base = int(readPathValue(context, "attr." + key), 0);
    if(key === "dex"){
      const effects = activeConditionEffects(context);
      return effects.dexHalf ? Math.ceil(base / 2) : base;
    }
    return base;
  }

  function blockedActionReason(actionType, context, options){
    const t = String(actionType || "none").toLowerCase();
    const effects = activeConditionEffects(context);
    const blocked = effects.blocked;
    const reasons = [];
    if(blocked.attack && (t === "attack" || t === "full-round")) reasons.push("Attack actions are blocked");
    if(blocked.cast && (t === "cast" || t === "full-round")) reasons.push("Casting actions are blocked");
    if(blocked.move && t === "move") reasons.push("Move actions are blocked");
    if(blocked.swift && t === "swift") reasons.push("Swift actions are blocked");
    if(blocked.free && t === "free") reasons.push("Free actions are blocked");
    if(isObj(options) && options.requiresSpeech && blocked.speech) reasons.push("Speech-based actions are blocked");
    return reasons.join("; ");
  }

  function resolveSpecialActionExpr(entry, kind, context){
    if(!isObj(entry)) return "";
    const val = entry[kind];
    if(typeof val === "function") return String(val(context || charState) || "").trim();
    return String(val || "").trim();
  }

  function resolveSpecialActionRollCount(entry, kind, context){
    if(!isObj(entry)) return 1;
    const key = kind === "effect" ? "effectRollCount" : "checkRollCount";
    const val = entry[key];
    if(typeof val === "function") return Math.max(1, int(val(context || charState), 1));
    return Math.max(1, int(val, 1));
  }

  function specialActionUnavailableReason(entry, context){
    if(!isObj(entry)) return "Invalid action.";
    const seq = sequenceNumber(readPathValue(context, "meta.sequence"));
    if(Number.isFinite(Number(entry.maxSequence)) && seq > int(entry.maxSequence, 9)){
      return "Requires Sequence " + String(int(entry.maxSequence, 9)) + " or lower.";
    }
    if(Number.isFinite(Number(entry.minSequence)) && seq < int(entry.minSequence, 0)){
      return "Requires Sequence " + String(int(entry.minSequence, 0)) + " or higher.";
    }
    if(Number.isFinite(Number(entry.requiresDexAtLeast)) && int(readPathValue(context, "attr.dex"), 0) < int(entry.requiresDexAtLeast, 0)){
      return "Requires DEX " + String(int(entry.requiresDexAtLeast, 0)) + "+.";
    }
    return "";
  }

  function findSpecialActionById(id){
    const sid = String(id || "");
    let i;
    for(i=0;i<SPECIAL_ACTION_DEFS.length;i+=1){
      if(String(SPECIAL_ACTION_DEFS[i].id) === sid) return SPECIAL_ACTION_DEFS[i];
    }
    return null;
  }

  function isCheckLikeLabel(label){
    const t = String(label || "").toLowerCase();
    return t.indexOf("check") >= 0 || t.indexOf("hit") >= 0 || t.indexOf("dc") >= 0 || t.indexOf("contest") >= 0 || t === "roll";
  }

  function strDamageBonus(value){
    const n = clamp(int(value,0),0,30); let out = STR_BONUS_TABLE[0][1], i;
    for(i=0;i<STR_BONUS_TABLE.length;i+=1){ if(n >= STR_BONUS_TABLE[i][0]) out = STR_BONUS_TABLE[i][1]; else break; }
    return out;
  }

  function sequenceNumber(seq){ const n = int(seq, NaN); return Number.isFinite(n) ? clamp(n,0,9) : 9; }

  function recomputeChar(state){
    const s = state || charState;
    ATTR_KEYS.forEach(function(k){ s.attr[k] = int(s.attr_base[k],0) + int(s.beyonder.attr_bonus[k],0); });
    recomputeSkills(s);
    const conditionEffects = activeConditionEffects(s);
    const dexForDefense = conditionEffects.dexHalf ? Math.ceil(int(s.attr.dex,0) / 2) : int(s.attr.dex,0);

    const seq = sequenceNumber(s.meta.sequence);
    const adv = clamp(10 - seq, 0, 10);
    const digest = clamp(int(s.beyonder.digestion_pct || s.res.digestion_pct,0),0,100);
    const digestBonus = Math.floor(digest/5);

    const dodge = conditionEffects.suppressPhysicalDexDodge ? 0 : int(s.skill.dodge,0);
    const dexContribution = conditionEffects.suppressPhysicalDexDodge ? 0 : dexForDefense;
    const dexDodgePenalty = conditionEffects.suppressPhysicalDexDodge ? 0 : int(conditionEffects.physicalDexDodgePenalty,0);
    const physicalMax = Math.max(0, 10 + dexContribution + dodge + dexDodgePenalty + int(s.def.armor,0) + int(s.def.physical_bonus,0));
    const willpowerMax = Math.max(0, 10 + int(s.attr.wil,0) + int(s.def.willpower_bonus,0));
    const constitutionMax = Math.max(0, 10 + int(s.attr.con,0) + int(s.def.constitution_bonus,0));
    s.def.physical_temp = Math.max(0, int(s.def.physical_temp,0));
    s.def.willpower_temp = Math.max(0, int(s.def.willpower_temp,0));
    s.def.constitution_temp = Math.max(0, int(s.def.constitution_temp,0));
    const physicalMaxEffective = physicalMax + s.def.physical_temp;
    const willpowerMaxEffective = willpowerMax + s.def.willpower_temp;
    const constitutionMaxEffective = constitutionMax + s.def.constitution_temp;
    s.def.physical_max = physicalMax;
    s.def.willpower_max = willpowerMax;
    s.def.constitution_max = constitutionMax;
    s.def.physical = clamp(int(s.def.physical, physicalMax), 0, physicalMaxEffective);
    s.def.willpower = clamp(int(s.def.willpower, willpowerMax), 0, willpowerMaxEffective);
    s.def.constitution = clamp(int(s.def.constitution, constitutionMax), 0, constitutionMaxEffective);

    const hpMaxInferred = Math.max(0, 10 + int(s.attr.con,0) + digestBonus + int(s.res.hp_max_bonus,0));
    const hpMaxOverride = Math.max(0, int(s.res.hp_max_override,0));
    const hpMax = hpMaxOverride > 0 ? hpMaxOverride : hpMaxInferred;
    s.res.hp_temp = Math.max(0, int(s.res.hp_temp,0));
    s.res.hp_max_override = hpMaxOverride;
    s.res.hp = clamp(int(s.res.hp,0), 0, hpMax + s.res.hp_temp);
    const sanityMax = Math.max(0, 10 + int(s.attr.wil,0));
    const spiritualityMax = Math.max(0, int(s.attr.wil,0) + int(s.attr.int,0) + adv * int(s.attr.int,0) + digestBonus);
    const luckMax = Math.max(0, int(s.attr.luk,0));
    s.res.spirituality_temp = Math.max(0, int(s.res.spirituality_temp,0));
    s.res.sanity_temp = Math.max(0, int(s.res.sanity_temp,0));
    s.res.luck_temp = Math.max(0, int(s.res.luck_temp,0));
    s.res.spirituality = clamp(int(s.res.spirituality,0), 0, spiritualityMax + s.res.spirituality_temp);
    s.res.sanity = clamp(int(s.res.sanity,0), 0, sanityMax + s.res.sanity_temp);
    s.res.luck = clamp(int(s.res.luck,0), 0, luckMax + s.res.luck_temp);
    s.res.hp_max = hpMax;
    s.res.sanity_max = sanityMax;
    s.res.spirituality_max = spiritualityMax;
    s.res.luck_max = luckMax;
    s.res.digestion_pct = digest;
    s.beyonder.digestion_pct = digest;

    return {
      sequence: seq,
      adv: adv,
      digest: digest,
      digestBonus: digestBonus,
      hpMaxInferred: hpMaxInferred,
      hpMaxOverride: hpMaxOverride,
      defPhysicalMax: physicalMaxEffective,
      defWillpowerMax: willpowerMaxEffective,
      defConstitutionMax: constitutionMaxEffective,
      movement: int(s.attr.str,0) + dexForDefense,
      strDamage: strDamageBonus(s.attr.str),
      conditionEffects: conditionEffects,
      carryTheoretical: Math.max(0, int(s.attr.str,0) * 2),
      carryCapacity: Math.max(0, int(s.sheet.pocket_slots,0)) + Math.max(0, int(s.sheet.carry_slots_override,0)),
      carryUsed: Array.isArray(s.items)
        ? s.items.reduce(function(sum, item){ return sum + Math.max(0, int(item && item.slots,0)); }, 0)
        : 0,
      hiddenUsed: Array.isArray(s.items)
        ? s.items.reduce(function(sum, item){
            if(!itemUsesHiddenPocket(item)) return sum;
            return sum + Math.max(0, int(item && item.slots,0));
          }, 0)
        : 0
    };
  }

  let charState = loadChar();
  let saveTimer = null;
  let compendium = null;
  let compendiumPromise = null;

  let sheetRoot = null;
  let hpManagerEl = null;
  let hpHealInputEl = null;
  let hpDamageInputEl = null;
  let hpQuickValueInputEl = null;
  let valueManagerEl = null;
  let valueManagerTitleEl = null;
  let valueManagerCurrentInputEl = null;
  let valueManagerTempInputEl = null;
  let valueManagerIncInputEl = null;
  let valueManagerDecInputEl = null;
  let valueManagerMaxEl = null;
  let valueManagerProjectedEl = null;
  let valueManagerOpsEl = null;
  let valueManagerResourceKey = "";
  let statusEl = null;
  let validationEl = null;
  let conditionListEl = null;
  let skillBodyEl = null;
  let skillSearchEl = null;
  let skillPoolEl = null;
  let abilityListEl = null;
  let abilitySummaryEl = null;
  let specialActionListEl = null;
  let specialActionSummaryEl = null;
  let abilityDetailEl = null;
  let abilityDetailTitleEl = null;
  let abilityDetailBodyEl = null;
  let actionListEl = null;
  let itemListEl = null;
  let adventureListEl = null;
  let rollListEl = null;
  let mysticismLangListEl = null;
  let commonLangListEl = null;
  let pathwaySelectEl = null;
  let sequenceSelectEl = null;
  let importFileEl = null;
  let portraitFileEl = null;
  let sheetToggleBtn = null;

  let rollLog = [];
  let rollToastEl = null;
  let rollToastTimer = null;
  let initiativeLastResult = "-";

  function scheduleSave(){
    if(saveTimer) clearTimeout(saveTimer);
    saveTimer = window.setTimeout(function(){ charState = saveChar(charState); setStatus("Saved.", false); }, SAVE_DEBOUNCE_MS);
  }

  function setStatus(msg, isError){
    if(!statusEl) return;
    statusEl.textContent = msg || "";
    statusEl.classList.toggle("error", !!isError);
  }

  function pushWarning(warnings, type, message, extra){ warnings.push(Object.assign({ type:type, message:message }, extra||{})); }

  function readPathValue(obj, path){
    const seg = String(path||"").split(".").filter(Boolean);
    let cur = obj, i;
    for(i=0;i<seg.length;i+=1){ if(!isObj(cur) || !Object.prototype.hasOwnProperty.call(cur, seg[i])) return undefined; cur = cur[seg[i]]; }
    return cur;
  }

  function carryPenaltyFromContext(context){
    if(!isObj(context)) return 0;
    const strScore = int(readPathValue(context, "attr.str"), int(readPathValue(context, "attr.strength"), 0));
    const theoretical = Math.max(0, strScore * 2);
    const used = Array.isArray(context.items)
      ? context.items.reduce(function(sum, item){ return sum + Math.max(0, int(item && item.slots, 0)); }, 0)
      : 0;
    const over = Math.max(0, used - theoretical);
    return over > 0 ? -over : 0;
  }

  function resolveRef(rawRef, context, warnings){
    const raw = String(rawRef||"").trim();
    const display = raw.charAt(0) === "@" ? raw : "@" + raw;
    const bare = display.slice(1).toLowerCase();
    if(!bare){ pushWarning(warnings,"unknown_ref",'Unknown ref "@", treated as 0.'); return { ref:display, found:false, value:0, path:"", resolvedPath:null }; }
    const canonical = Object.prototype.hasOwnProperty.call(REF_ALIASES, bare) ? REF_ALIASES[bare] : bare;
    const tries = [canonical];
    if(canonical.indexOf("skill.") === 0) tries.push("skill." + token(canonical.slice(6)));
    let i, val, path = null;
    for(i=0;i<tries.length;i+=1){ val = readPathValue(context, tries[i]); if(val !== undefined){ path = tries[i]; break; } }
    if(val === undefined){ pushWarning(warnings,"unknown_ref",'Unknown ref "'+display+'", treated as 0.',{ ref:display }); return { ref:display, found:false, value:0, path:canonical, resolvedPath:null }; }
    let numericValue = NaN;
    if(Number.isFinite(val)) numericValue = Number(val);
    else if(typeof val === "string" && val.trim() !== "" && Number.isFinite(Number(val))) numericValue = Number(val);
    if(Number.isFinite(numericValue)){
      if(path === "attr.str" || path === "attr.dex"){
        numericValue = effectiveAttrValue(path.slice(5), context) + carryPenaltyFromContext(context);
      }else if(path && path.indexOf("attr.") === 0){
        numericValue = effectiveAttrValue(path.slice(5), context);
      }
      return { ref:display, found:true, value:numericValue, path:canonical, resolvedPath:path };
    }
    pushWarning(warnings,"invalid_ref_value",'Ref "'+display+'" is not numeric, treated as 0.',{ ref:display });
    return { ref:display, found:true, value:0, path:canonical, resolvedPath:path };
  }

  function tokenize(expr){
    const out = []; const t = String(expr||"");
    let i=0, ch, s, c, d, ref;
    while(i<t.length){
      ch = t[i];
      if(/\s/.test(ch)){ i+=1; continue; }
      if(ch === "+" || ch === "-" || ch === "(" || ch === ")"){ out.push({ type:"op", value:ch, raw:ch }); i+=1; continue; }
      if(ch === "@"){
        s = i; i+=1; while(i<t.length && /[A-Za-z0-9_.:-]/.test(t[i])) i+=1;
        ref = t.slice(s,i); if(ref.length <= 1) return { tokens:out, error:'Invalid reference token "@".' };
        out.push({ type:"ref", raw:ref, value:ref.slice(1).toLowerCase() }); continue;
      }
      if(/[0-9]/.test(ch)){
        s = i; while(i<t.length && /[0-9]/.test(t[i])) i+=1;
        if(i<t.length && (t[i] === "d" || t[i] === "D")){
          c = Number(t.slice(s,i)); i+=1; s=i; while(i<t.length && /[0-9]/.test(t[i])) i+=1;
          if(s === i) return { tokens:out, error:'Invalid dice syntax: missing sides after "d".' };
          d = Number(t.slice(s,i)); if(c < 1 || d < 1) return { tokens:out, error:"Dice count and sides must both be >= 1." };
          out.push({ type:"dice", count:c, sides:d, raw:String(c)+"d"+String(d) }); continue;
        }
        out.push({ type:"number", value:Number(t.slice(s,i)), raw:t.slice(s,i) }); continue;
      }
      return { tokens:out, error:'Unexpected token "'+ch+'" at position '+String(i+1)+'.' };
    }
    return { tokens:out, error:null };
  }

  function parseExpr(source){
    const tok = tokenize(source), warnings = []; const tokens = tok.tokens;
    let idx = 0, err = "";
    if(tok.error){ pushWarning(warnings,"parse_error",tok.error,{ expr:source }); return { ok:false, ast:null, warnings:warnings, error:tok.error }; }

    function mark(msg){ if(!err) err = msg; }
    function peek(){ return tokens[idx] || null; }
    function take(){ const t = tokens[idx] || null; idx += 1; return t; }

    function primary(){
      const t = peek();
      if(!t){ mark("Unexpected end of expression."); return { type:"number", value:0, raw:"0" }; }
      if(t.type === "number" || t.type === "dice" || t.type === "ref"){ take(); return t; }
      if(t.type === "op" && t.value === "("){
        take(); const inner = exprNode(); const close = peek();
        if(!close || close.type !== "op" || close.value !== ")") mark('Missing closing ")".'); else take();
        return inner;
      }
      mark('Unexpected token "'+t.raw+'".'); take(); return { type:"number", value:0, raw:"0" };
    }

    function unary(){ const t = peek(); if(t && t.type === "op" && (t.value === "+" || t.value === "-")){ take(); return { type:"unary", op:t.value, node:unary() }; } return primary(); }
    function exprNode(){ let node = unary(), t = peek(); while(t && t.type === "op" && (t.value === "+" || t.value === "-")){ take(); node = { type:"binary", op:t.value, left:node, right:unary() }; t = peek(); } return node; }

    const ast = exprNode();
    if(!err && idx < tokens.length) err = 'Unexpected token "'+tokens[idx].raw+'".';
    if(err){ pushWarning(warnings,"parse_error",err,{ expr:source }); return { ok:false, ast:null, warnings:warnings, error:err }; }
    return { ok:true, ast:ast, warnings:warnings, error:null };
  }

  function diceRoll(count, sides){ const r=[]; let i; for(i=0;i<count;i+=1) r.push(1 + Math.floor(Math.random()*sides)); return r; }

  function evaluate(ast, context, seedWarnings){
    const parts = [], warnings = Array.isArray(seedWarnings) ? seedWarnings.slice() : [];
    function add(node, sign){
      if(!node) return;
      if(node.type === "number"){ parts.push({ type:"number", raw:node.raw, sign:sign, sourceValue:node.value, value:sign*node.value }); return; }
      if(node.type === "dice"){ const rr = diceRoll(node.count,node.sides); const sub = rr.reduce(function(a,b){ return a+b; },0); parts.push({ type:"dice", raw:node.raw, count:node.count, sides:node.sides, results:rr, sign:sign, sourceValue:sub, value:sign*sub }); return; }
      if(node.type === "ref"){ const rs = resolveRef(node.raw, context, warnings); parts.push({ type:"ref", raw:node.raw, ref:rs.ref, path:rs.path, resolvedPath:rs.resolvedPath, found:rs.found, sign:sign, sourceValue:rs.value, value:sign*rs.value }); return; }
      if(node.type === "unary"){ add(node.node, node.op === "-" ? -sign : sign); return; }
      if(node.type === "binary"){ add(node.left, sign); add(node.right, node.op === "-" ? -sign : sign); }
    }
    add(ast,1);
    return { total: parts.reduce(function(a,p){ return a + num(p.value,0); },0), components:parts, warnings:warnings };
  }

  function compText(p, context){
    if(p.type === "dice") return p.raw + "[" + p.results.join(",") + "]=" + String(p.sourceValue);
    if(p.type === "condition_mod") return (p.label || "Condition Mod") + "(" + String(p.sourceValue) + ")";
    if(p.type === "ref"){
      const fallback = String(p.ref || "").replace(/^@/, "");
      const label = previewRefLabel(p.resolvedPath || p.path || fallback, context) || String(p.ref || "@ref");
      return label + "(" + String(p.sourceValue) + ")";
    }
    return String(p.sourceValue);
  }

  function breakdown(parts, total, context){
    const txt = [];
    parts.forEach(function(p){ const t = compText(p, context); if(p.sign < 0) txt.push("- " + t); else if(txt.length > 0) txt.push("+ " + t); else txt.push(t); });
    if(!txt.length) txt.push("0");
    return txt.join(" ") + " => " + String(total);
  }

  function splitVs(raw){
    const t = String(raw||""); let depth=0, i, prev, next, left, right;
    for(i=0;i<t.length-1;i+=1){
      if(t[i] === "("){ depth += 1; continue; }
      if(t[i] === ")"){ depth = Math.max(0, depth-1); continue; }
      if(depth !== 0) continue;
      if(!((t[i] === "v" || t[i] === "V") && (t[i+1] === "s" || t[i+1] === "S"))) continue;
      prev = i===0 ? " " : t[i-1]; next = i+2>=t.length ? " " : t[i+2];
      if(!/\s/.test(prev) || !/\s/.test(next)) continue;
      left = t.slice(0,i).trim(); right = t.slice(i+2).trim(); if(left && right) return { expr:left, defenseRef:right };
    }
    return null;
  }

  function rollBase(expr, context, options){
    const src = String(expr||"").trim();
    if(!src) return { expr:src, total:0, breakdown:"0 => 0", components:[], warnings:[{ type:"parse_error", message:"Expression is empty." }], error:"Expression is empty." };
    const parsed = parseExpr(src);
    if(!parsed.ok || !parsed.ast) return { expr:src, total:0, breakdown:"0 => 0", components:[], warnings:parsed.warnings, error:parsed.error || "Invalid expression." };
    const ev = evaluate(parsed.ast, context, parsed.warnings);
    if(isObj(options) && options.applyConditionCheckMod){
      const conditionMod = int(activeConditionEffects(context).checkMod, 0);
      if(conditionMod !== 0){
        ev.components.push({
          type: "condition_mod",
          label: "Condition Mod",
          sign: conditionMod < 0 ? -1 : 1,
          sourceValue: Math.abs(conditionMod),
          value: conditionMod
        });
        ev.total += conditionMod;
      }
    }
    return { expr:src, total:ev.total, breakdown:breakdown(ev.components, ev.total, context), components:ev.components, warnings:ev.warnings, error:null };
  }

  function resolveDefense(defRef, context, warnings){
    const raw = String(defRef||"").trim();
    if(!raw){ pushWarning(warnings,"unknown_defense","No defense ref supplied for vs clause.",{ ref:raw }); return { ref:"", path:"", resolvedPath:null, found:false, value:0 }; }
    if(raw.charAt(0) === "@") return resolveRef(raw, context, warnings);
    const lit = Number(raw);
    if(Number.isFinite(lit)) return { ref:raw, path:raw, resolvedPath:null, found:true, value:lit };
    pushWarning(warnings,"invalid_defense",'Defense "'+raw+'" is invalid, treated as missing.',{ ref:raw });
    return { ref:raw, path:raw, resolvedPath:null, found:false, value:0 };
  }

  function rollVs(expr, defenseRef, context, options){
    const safe = normalizeChar(isObj(context) ? context : charState);
    const base = rollBase(expr, safe, options), warnings = base.warnings.slice();
    const def = resolveDefense(defenseRef, safe, warnings);
    const defRaw = String(def.ref || "").trim();
    const defIsNumeric = Number.isFinite(Number(defRaw));
    const defLabel = defIsNumeric ? "DV" : (previewRefLabel(def.resolvedPath || def.path || defRaw.replace(/^@/, ""), safe) || defRaw || "(missing)");
    const success = def.found ? base.total >= def.value : null;
    const margin = def.found ? base.total - def.value : null;
    const outcome = def.found ? (success ? "SUCCESS" : "FAIL") : "NO DEFENSE";
    return { expr:base.expr, total:base.total, breakdown:base.breakdown + " vs " + defLabel + "(" + String(def.value) + ") => " + outcome, components:base.components.concat([{ type:"vs", ref:def.ref||"(missing)", path:def.path, resolvedPath:def.resolvedPath, found:def.found, value:def.value, success:success, margin:margin }]), warnings:warnings, vs:{ ref:def.ref||"(missing)", label:defLabel, path:def.path, resolvedPath:def.resolvedPath, found:def.found, value:def.value, success:success, margin:margin }, error:base.error };
  }

  function roll(expr, context, options){
    const src = String(expr||"").trim();
    const safe = normalizeChar(isObj(context) ? context : charState);
    const vs = splitVs(src);
    return vs ? rollVs(vs.expr,vs.defenseRef,safe,options) : rollBase(src,safe,options);
  }

  function rollTimeLabel(dt){ return dt.toLocaleTimeString([], { hour:"2-digit", minute:"2-digit", second:"2-digit" }); }

  function diceResultLines(result){
    if(!isObj(result) || !Array.isArray(result.components)) return [];
    return result.components
      .filter(function(c){ return isObj(c) && c.type === "dice" && Array.isArray(c.results) && c.results.length > 0; })
      .map(function(c){
        const sign = int(c.sign, 1) < 0 ? "- " : "";
        const raw = String(c.raw || "dice");
        const faces = c.results.map(function(v){ return String(int(v,0)); }).join(", ");
        const sum = String(int(c.sourceValue, 0));
        return sign + raw + ": [" + faces + "] = " + sum;
      });
  }

  function logEntry(result, expr, source, meta){
    const now = new Date();
    const displayExpr = (isObj(meta) && typeof meta.expression_display === "string" && meta.expression_display.trim())
      ? meta.expression_display.trim()
      : "";
    return {
      id: String(now.getTime()) + "_" + Math.random().toString(36).slice(2,8),
      timestamp: now.toISOString(),
      timeLabel: rollTimeLabel(now),
      source: (typeof source === "string" && source.trim()) ? source.trim() : "Roll",
      type: (isObj(meta) && typeof meta.type === "string" && meta.type.trim()) ? meta.type.trim() : "",
      expression: String(expr || result.expr || "").trim() || "(empty)",
      expression_display: displayExpr,
      total: int(result.total,0),
      breakdown: String(result.breakdown || ""),
      diceLines: diceResultLines(result),
      vs: result.vs || null,
      warnings: Array.isArray(result.warnings) ? result.warnings.slice() : []
    };
  }

  function renderRollLog(){
    if(!rollListEl) return;
    rollListEl.innerHTML = "";
    if(!rollLog.length){ const e = document.createElement("div"); e.className = "lotm-roll-empty"; e.textContent = "No rolls yet."; rollListEl.appendChild(e); return; }
    rollLog.forEach(function(entry){
      const item = document.createElement("article"); item.className = "lotm-roll-entry";
      const head = document.createElement("div"); head.className = "lotm-roll-head";
      const source = document.createElement("span"); source.className = "lotm-roll-source"; source.textContent = entry.source; head.appendChild(source);
      if(entry.type){ const type = document.createElement("span"); type.className = "lotm-roll-kind"; type.textContent = entry.type; head.appendChild(type); }
      const tm = document.createElement("time"); tm.className = "lotm-roll-time"; tm.dateTime = entry.timestamp; tm.textContent = entry.timeLabel; head.appendChild(tm);
      const expr = document.createElement("div");
      expr.className = "lotm-roll-expr";
      expr.textContent = (typeof entry.expression_display === "string" && entry.expression_display.trim()) ? entry.expression_display : entry.expression;
      if(expr.textContent !== entry.expression) expr.title = entry.expression;
      const total = document.createElement("div"); total.className = "lotm-roll-total"; total.textContent = "Total: " + String(entry.total);
      if(entry.vs){ const tag = document.createElement("span"); const ok = entry.vs.success === true, bad = entry.vs.success === false; tag.className = "lotm-roll-vs " + (ok ? "success" : bad ? "fail" : "neutral"); tag.textContent = ok ? "SUCCESS" : bad ? "FAIL" : "NO DEFENSE"; total.appendChild(tag); }
      let diceEl = null;
      if(Array.isArray(entry.diceLines) && entry.diceLines.length){
        diceEl = document.createElement("div");
        diceEl.className = "lotm-roll-dice";
        diceEl.textContent = "Dice: " + entry.diceLines.join(" | ");
      }
      const details = document.createElement("details"); details.className = "lotm-roll-breakdown";
      const sum = document.createElement("summary"); sum.textContent = "Breakdown"; details.appendChild(sum);
      const pre = document.createElement("pre"); pre.textContent = entry.breakdown || "(none)"; details.appendChild(pre);
      item.appendChild(head); item.appendChild(expr); item.appendChild(total); if(diceEl) item.appendChild(diceEl); item.appendChild(details);
      rollListEl.appendChild(item);
    });
  }

  function appendRollLog(result, expr, source, meta){
    rollLog.unshift(logEntry(result, expr, source, meta));
    if(rollLog.length > ROLL_LOG_MAX) rollLog = rollLog.slice(0, ROLL_LOG_MAX);
    renderRollLog();
  }

  function ensureToast(){
    if(rollToastEl) return rollToastEl;
    if(!document.body) return null;
    rollToastEl = document.createElement("div");
    rollToastEl.className = "lotm-roll-toast";
    rollToastEl.setAttribute("aria-live", "polite");
    document.body.appendChild(rollToastEl);
    return rollToastEl;
  }

  function showToast(result, source, type){
    const toast = ensureToast(), parts = [];
    if(!toast) return;
    if(typeof source === "string" && source.trim()) parts.push(source.trim());
    if(typeof type === "string" && type.trim()) parts.push(type.trim());
    let msg = (parts.length ? parts.join(" - ") : "Roll") + ": " + String(int(result.total,0));
    if(result.vs) msg += " | " + (result.vs.success === true ? "SUCCESS" : result.vs.success === false ? "FAIL" : "NO DEFENSE") + " vs " + String(result.vs.label || result.vs.ref || "(missing)") + "(" + String(result.vs.value) + ")";
    const diceLines = diceResultLines(result);
    if(diceLines.length) msg += " | Dice " + diceLines.join("; ");
    toast.textContent = msg;
    toast.classList.add("show");
    if(rollToastTimer) clearTimeout(rollToastTimer);
    rollToastTimer = window.setTimeout(function(){ toast.classList.remove("show"); }, 1800);
  }

  function logRoll(result, expr, source, type, context){
    const previewExpr = rollPreview(expr, isObj(context) ? context : charState);
    appendRollLog(result, expr, source, { type:type || "", expression_display: previewExpr });
    showToast(result, source, type);
  }

  function debugRoll(expr, sourceLabel, context){
    const safe = normalizeChar(isObj(context) ? context : charState);
    const result = roll(expr, safe);
    logRoll(result, expr, sourceLabel || "Debug", "Roll", safe);
    setStatus("Roll logged.", false);
    return result;
  }

  function spendSpirituality(amount, label){
    const cost = Math.max(0, int(amount,0));
    if(cost <= 0) return 0;
    const before = int(charState.res.spirituality, 0);
    const spent = Math.min(before, cost);
    charState.res.spirituality = Math.max(0, before - cost);
    const shortfall = Math.max(0, cost - before);
    validateAndRender();
    scheduleSave();
    if(shortfall > 0){
      setStatus((label || "Ability") + " spent " + String(spent) + " spirituality (" + String(shortfall) + " short).", true);
    }else{
      setStatus((label || "Ability") + " spent " + String(spent) + " spirituality.", false);
    }
    return spent;
  }

  function vsRef(opposedBy){ const k = String(opposedBy||"").trim().toLowerCase(); return Object.prototype.hasOwnProperty.call(DEF_MAP,k) ? DEF_MAP[k] : ""; }
  function withVs(expr, opposedBy){ const t = String(expr||"").trim(); const ref = vsRef(opposedBy); if(!t) return ""; if(!ref || /\svs\s/i.test(t)) return t; return t + " vs " + ref; }
  function actionLabel(v){
    const t = String(v || "").trim();
    return t ? titleWords(t.replace(/-/g, " ")) : "None";
  }
  function formatCost(cost){
    if(!isObj(cost)) return "None";
    const keys = Object.keys(cost).filter(function(k){ return Number.isFinite(Number(cost[k])) && Number(cost[k]) !== 0; });
    if(!keys.length) return "None";
    return keys.map(function(k){ return titleWords(k) + ": " + String(int(cost[k],0)); }).join(", ");
  }
  function abilitySpiritualityCost(ability){
    if(!isObj(ability) || !isObj(ability.cost)) return 0;
    return Math.max(0, int(ability.cost.spirituality, 0));
  }

  function textSuggestsSpeech(raw){
    const src = String(raw || "").toLowerCase();
    return /speech|speak|spoken|voice|verbal|chant|utter|babbl|command word/.test(src);
  }

  function abilityRequiresSpeech(ability){
    if(!isObj(ability)) return false;
    const bag = [
      ability.name,
      ability.text,
      ability.range,
      ability.target,
      Array.isArray(ability.tags) ? ability.tags.join(" ") : "",
      Array.isArray(ability.conditions) ? ability.conditions.join(" ") : ""
    ].join(" ");
    return textSuggestsSpeech(bag);
  }

  function customActionRequiresSpeech(action){
    if(!isObj(action)) return false;
    const bag = [action.label, action.type, action.description, action.target].join(" ");
    return textSuggestsSpeech(bag);
  }

  function escapeHtml(text){
    return String(text || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function linkWikiText(raw){
    const src = String(raw || "");
    const re = /\[\[([^\]]+)\]\]/g;
    let out = "";
    let last = 0;
    let m;
    while((m = re.exec(src)) !== null){
      const inner = String(m[1] || "").trim();
      const pipe = inner.indexOf("|");
      const target = (pipe >= 0 ? inner.slice(0,pipe) : inner).trim();
      const label = (pipe >= 0 ? inner.slice(pipe+1) : inner).trim();
      out += escapeHtml(src.slice(last, m.index));
      out += "<a class='wikilink' href='/w/" + encodeURIComponent(target) + "'>" + escapeHtml(label || target) + "</a>";
      last = m.index + m[0].length;
    }
    out += escapeHtml(src.slice(last));
    return out;
  }

  function titleWords(raw){
    return String(raw || "")
      .replace(/_/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .replace(/\b([a-z])/g, function(_, ch){ return ch.toUpperCase(); });
  }

  function titleWordsKeepWiki(raw){
    const src = String(raw || "");
    const re = /\[\[[^\]]+\]\]/g;
    let out = "";
    let last = 0;
    let m;
    function titleWordsSegment(seg){
      return String(seg || "")
        .replace(/_/g, " ")
        .replace(/\b([a-z])/g, function(_, ch){ return ch.toUpperCase(); });
    }
    while((m = re.exec(src)) !== null){
      out += titleWordsSegment(src.slice(last, m.index));
      out += m[0];
      last = m.index + m[0].length;
    }
    out += titleWordsSegment(src.slice(last));
    return out;
  }

  function titleLinkedHtml(raw){
    return linkWikiText(titleWordsKeepWiki(raw));
  }

  function richTextHtml(raw){
    const src = String(raw || "").trim();
    if(!src) return "";
    const html = linkWikiText(src).replace(/\r\n/g, "\n");
    const blocks = html.split(/\n{2,}/).map(function(part){ return part.trim(); }).filter(Boolean);
    if(!blocks.length) return "";
    return blocks.map(function(part){
      return "<p>" + part.replace(/\n/g, "<br />") + "</p>";
    }).join("");
  }

  function titleFromToken(raw){
    return String(raw || "")
      .replace(/[_-]+/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .replace(/\b\w/g, function(ch){ return ch.toUpperCase(); });
  }

  function skillPreviewLabel(skillId, context){
    const id = token(skillId);
    if(!id) return "Skill";
    if(Object.prototype.hasOwnProperty.call(BUILTIN_SKILLS, id)) return BUILTIN_SKILLS[id].label;
    if(isObj(context) && isObj(context.sheet) && Array.isArray(context.sheet.custom_skills)){
      const found = context.sheet.custom_skills.find(function(e){ return token(e && e.id) === id; });
      if(found && String(found.label || "").trim()) return String(found.label).trim();
    }
    return titleFromToken(id);
  }

  function previewRefLabel(path, context){
    const raw = String(path || "").trim();
    if(!raw) return "";
    const lower = raw.toLowerCase();
    if(lower === "bonus") return "Bonus";
    if(lower.indexOf("attr.") === 0){
      const attrKey = lower.slice(5);
      if(Object.prototype.hasOwnProperty.call(ATTR_PREVIEW_LABELS, attrKey)) return ATTR_PREVIEW_LABELS[attrKey];
      return titleFromToken(attrKey);
    }
    if(lower.indexOf("skill.") === 0){
      return skillPreviewLabel(lower.slice(6), context);
    }
    if(lower.indexOf("def.") === 0){
      const defKey = lower.slice(4);
      if(Object.prototype.hasOwnProperty.call(DEF_PREVIEW_LABELS, defKey)) return DEF_PREVIEW_LABELS[defKey];
      return titleFromToken(defKey);
    }
    if(lower.indexOf("res.") === 0){
      const resKey = lower.slice(4);
      if(Object.prototype.hasOwnProperty.call(RES_PREVIEW_LABELS, resKey)) return RES_PREVIEW_LABELS[resKey];
      return titleFromToken(resKey);
    }
    if(lower.indexOf("mod.") === 0){
      const modKey = lower.slice(4);
      if(Object.prototype.hasOwnProperty.call(MOD_PREVIEW_LABELS, modKey)) return MOD_PREVIEW_LABELS[modKey];
      return titleFromToken(modKey);
    }
    const lastDot = lower.lastIndexOf(".");
    return titleFromToken(lastDot >= 0 ? lower.slice(lastDot + 1) : lower);
  }

  function rollPreview(expr, context){
    const source = String(expr || "").trim();
    if(!source) return "";
    const vs = splitVs(source);
    if(vs){
      const left = rollPreview(vs.expr, context);
      const def = resolveDefense(vs.defenseRef, context, []);
      const defenseRaw = String(vs.defenseRef || "").trim();
      const rightLabel = Number.isFinite(Number(defenseRaw)) ? "DV" : (previewRefLabel(def.resolvedPath || def.path || defenseRaw, context) || defenseRaw);
      const right = rightLabel + "(" + String(int(def.value,0)) + ")";
      return left + " vs " + right;
    }
    const parsed = tokenize(source);
    const warnings = [];
    if(parsed.error){
      return source;
    }
    return parsed.tokens.map(function(t){
      if(t.type === "ref"){
        const r = resolveRef(t.raw, context, warnings);
        const label = previewRefLabel(r.resolvedPath || r.path || t.value, context) || t.raw;
        return label + "(" + String(int(r.value,0)) + ")";
      }
      return t.raw;
    }).join(" ");
  }

  function rollPreviewWithCondition(expr, context, applyConditionMod){
    const preview = rollPreview(expr, context);
    if(!applyConditionMod) return preview;
    const mod = int(activeConditionEffects(context).checkMod, 0);
    if(mod === 0) return preview;
    return preview + " | Cond " + signedNumberText(mod);
  }

  function setDerived(key, value){ if(!sheetRoot) return; sheetRoot.querySelectorAll('[data-derived="'+key+'"]').forEach(function(el){ el.textContent = String(value); }); }
  function setDerivedTone(key, tone){
    if(!sheetRoot) return;
    sheetRoot.querySelectorAll('[data-derived="'+key+'"]').forEach(function(el){
      el.classList.remove("ok","warn","neutral");
      if(tone) el.classList.add(tone);
    });
  }

  function renderPortraitCard(){
    if(!sheetRoot) return;
    const imgEl = sheetRoot.querySelector(".lotm-portrait-img");
    const emptyEl = sheetRoot.querySelector(".lotm-portrait-empty");
    const clearEl = sheetRoot.querySelector(".lotm-portrait-clear");
    const portrait = String(charState.meta && charState.meta.portrait || "").trim();
    const hasPortrait = !!portrait;
    if(imgEl){
      if(hasPortrait){
        imgEl.src = portrait;
        imgEl.hidden = false;
      }else{
        imgEl.removeAttribute("src");
        imgEl.hidden = true;
      }
    }
    if(emptyEl) emptyEl.hidden = hasPortrait;
    if(clearEl) clearEl.hidden = !hasPortrait;
  }

  function isVitalResourceKey(key){
    return VITAL_RESOURCE_KEYS.indexOf(String(key || "").toLowerCase()) >= 0;
  }

  function vitalResourceLabel(key){
    const id = String(key || "").toLowerCase();
    return Object.prototype.hasOwnProperty.call(VITAL_RESOURCE_LABELS, id)
      ? VITAL_RESOURCE_LABELS[id]
      : titleFromToken(id);
  }

  function vitalResourceTempField(key){
    return String(key || "").toLowerCase() + "_temp";
  }

  function vitalResourceEffectiveMax(key){
    if(!isVitalResourceKey(key)) return 0;
    const id = String(key || "").toLowerCase();
    const base = Math.max(0, int(charState.res[id + "_max"], 0));
    const temp = Math.max(0, int(charState.res[vitalResourceTempField(id)], 0));
    return base + temp;
  }

  function isDefenseManagerTarget(key){
    return Object.prototype.hasOwnProperty.call(DEFENSE_MANAGER_TARGETS, String(key || "").toLowerCase());
  }

  function defenseTempField(field){
    return String(field || "").toLowerCase() + "_temp";
  }

  function defenseEffectiveMax(field){
    const id = String(field || "").toLowerCase();
    const base = Math.max(0, int(charState.def[id + "_max"], 0));
    const temp = Math.max(0, int(charState.def[defenseTempField(id)], 0));
    return base + temp;
  }

  function valueManagerTargetInfo(key){
    const id = String(key || "").toLowerCase();
    if(isVitalResourceKey(id)){
      return {
        id: id,
        kind: "resource",
        label: vitalResourceLabel(id),
        supportsOps: true,
        getCurrent: function(){ return int(charState.res[id], 0); },
        setCurrent: function(v){ charState.res[id] = int(v, 0); },
        getTemp: function(){ return Math.max(0, int(charState.res[vitalResourceTempField(id)], 0)); },
        setTemp: function(v){ charState.res[vitalResourceTempField(id)] = Math.max(0, int(v, 0)); },
        getEffectiveMax: function(){ return vitalResourceEffectiveMax(id); }
      };
    }
    if(isDefenseManagerTarget(id)){
      const meta = DEFENSE_MANAGER_TARGETS[id];
      const field = meta.field;
      return {
        id: id,
        kind: "defense",
        label: meta.label,
        supportsOps: false,
        getCurrent: function(){ return int(charState.def[field], 0); },
        setCurrent: function(v){ charState.def[field] = int(v, 0); },
        getTemp: function(){ return Math.max(0, int(charState.def[defenseTempField(field)], 0)); },
        setTemp: function(v){ charState.def[defenseTempField(field)] = Math.max(0, int(v, 0)); },
        getEffectiveMax: function(){ return defenseEffectiveMax(field); }
      };
    }
    return null;
  }

  function syncManagerBodyLock(){
    const hpOpen = !!(hpManagerEl && hpManagerEl.classList.contains("open"));
    const valueOpen = !!(valueManagerEl && valueManagerEl.classList.contains("open"));
    document.body.classList.toggle("lotm-hp-manager-open", hpOpen || valueOpen);
  }

  function hpProjectedValue(){
    const maxHp = Math.max(0, int(charState.res.hp_max, 0) + Math.max(0, int(charState.res.hp_temp, 0)));
    const currentHp = clamp(int(charState.res.hp, 0), 0, maxHp);
    const heal = Math.max(0, int(hpHealInputEl ? hpHealInputEl.value : 0, 0));
    const damage = Math.max(0, int(hpDamageInputEl ? hpDamageInputEl.value : 0, 0));
    return clamp(currentHp + heal - damage, 0, maxHp);
  }

  function refreshHpProjection(){
    setDerived("hp_projected", hpProjectedValue());
  }

  function valueProjectedValue(){
    const info = valueManagerTargetInfo(valueManagerResourceKey);
    if(!info) return 0;
    const maxValue = Math.max(0, int(info.getEffectiveMax(), 0));
    const currentValue = clamp(int(info.getCurrent(), 0), 0, maxValue);
    if(!info.supportsOps) return currentValue;
    const inc = Math.max(0, int(valueManagerIncInputEl ? valueManagerIncInputEl.value : 0, 0));
    const dec = Math.max(0, int(valueManagerDecInputEl ? valueManagerDecInputEl.value : 0, 0));
    return clamp(currentValue + inc - dec, 0, maxValue);
  }

  function refreshValueProjection(){
    if(!valueManagerEl) return;
    const info = valueManagerTargetInfo(valueManagerResourceKey);
    if(info){
      const maxValue = Math.max(0, int(info.getEffectiveMax(), 0));
      if(valueManagerTitleEl) valueManagerTitleEl.textContent = info.label + " Management";
      if(valueManagerCurrentInputEl) valueManagerCurrentInputEl.value = String(clamp(int(info.getCurrent(), 0), 0, maxValue));
      if(valueManagerTempInputEl) valueManagerTempInputEl.value = String(Math.max(0, int(info.getTemp(), 0)));
      if(valueManagerMaxEl) valueManagerMaxEl.textContent = String(maxValue);
      if(valueManagerOpsEl) valueManagerOpsEl.hidden = !info.supportsOps;
    }else{
      if(valueManagerMaxEl) valueManagerMaxEl.textContent = "0";
      if(valueManagerOpsEl) valueManagerOpsEl.hidden = false;
    }
    if(valueManagerProjectedEl) valueManagerProjectedEl.textContent = String(valueProjectedValue());
  }

  function setHpManagerOpen(open){
    if(!hpManagerEl) return;
    const isOpen = !!open;
    hpManagerEl.classList.toggle("open", isOpen);
    hpManagerEl.setAttribute("aria-hidden", isOpen ? "false" : "true");
    syncManagerBodyLock();
    if(isOpen) refreshHpProjection();
  }

  function setValueManagerOpen(open, key){
    if(!valueManagerEl) return;
    const isOpen = !!open;
    if(isOpen){
      const wanted = String(key || "").toLowerCase();
      if(!valueManagerTargetInfo(wanted)) return;
      valueManagerResourceKey = wanted;
      if(valueManagerIncInputEl) valueManagerIncInputEl.value = "0";
      if(valueManagerDecInputEl) valueManagerDecInputEl.value = "0";
      refreshValueProjection();
    }else{
      valueManagerResourceKey = "";
    }
    valueManagerEl.classList.toggle("open", isOpen);
    valueManagerEl.setAttribute("aria-hidden", isOpen ? "false" : "true");
    syncManagerBodyLock();
  }

  function applyHpHealing(amountOverride){
    const fromOverride = amountOverride !== undefined && amountOverride !== null;
    const amount = Math.max(0, int(fromOverride ? amountOverride : (hpHealInputEl ? hpHealInputEl.value : 0), 0));
    if(amount <= 0){ refreshHpProjection(); return; }
    const maxHp = Math.max(0, int(charState.res.hp_max, 0) + Math.max(0, int(charState.res.hp_temp, 0)));
    const currentHp = Math.max(0, int(charState.res.hp, 0));
    charState.res.hp = clamp(currentHp + amount, 0, maxHp);
    if(!fromOverride && hpHealInputEl) hpHealInputEl.value = "0";
    validateAndRender();
    scheduleSave();
    setStatus("Healing applied: +" + String(amount) + " HP.", false);
  }

  function applyHpDamage(amountOverride){
    const fromOverride = amountOverride !== undefined && amountOverride !== null;
    let amount = Math.max(0, int(fromOverride ? amountOverride : (hpDamageInputEl ? hpDamageInputEl.value : 0), 0));
    if(amount <= 0){ refreshHpProjection(); return; }
    charState.res.hp = Math.max(0, int(charState.res.hp, 0) - amount);
    if(!fromOverride && hpDamageInputEl) hpDamageInputEl.value = "0";
    validateAndRender();
    scheduleSave();
    setStatus("Damage applied: -" + String(amount) + " HP.", false);
  }

  function applyVitalResourceIncrease(key, amountOverride){
    const id = String(key || "").toLowerCase();
    if(!isVitalResourceKey(id)) return;
    const amount = Math.max(0, int(amountOverride, 0));
    if(amount <= 0){ refreshValueProjection(); return; }
    const maxValue = vitalResourceEffectiveMax(id);
    const current = clamp(int(charState.res[id], 0), 0, maxValue);
    charState.res[id] = clamp(current + amount, 0, maxValue);
    validateAndRender();
    scheduleSave();
    setStatus(vitalResourceLabel(id) + " increased by +" + String(amount) + ".", false);
  }

  function applyVitalResourceDecrease(key, amountOverride){
    const id = String(key || "").toLowerCase();
    if(!isVitalResourceKey(id)) return;
    const amount = Math.max(0, int(amountOverride, 0));
    if(amount <= 0){ refreshValueProjection(); return; }
    const current = Math.max(0, int(charState.res[id], 0));
    charState.res[id] = Math.max(0, current - amount);
    validateAndRender();
    scheduleSave();
    setStatus(vitalResourceLabel(id) + " decreased by -" + String(amount) + ".", false);
  }

  function applyValueManagerIncrease(amountOverride){
    const info = valueManagerTargetInfo(valueManagerResourceKey);
    if(!info || !info.supportsOps) return;
    const amount = Math.max(0, int(amountOverride, 0));
    if(amount <= 0){ refreshValueProjection(); return; }
    const maxValue = Math.max(0, int(info.getEffectiveMax(), 0));
    const current = clamp(int(info.getCurrent(), 0), 0, maxValue);
    info.setCurrent(clamp(current + amount, 0, maxValue));
    validateAndRender();
    scheduleSave();
    setStatus(info.label + " increased by +" + String(amount) + ".", false);
  }

  function applyValueManagerDecrease(amountOverride){
    const info = valueManagerTargetInfo(valueManagerResourceKey);
    if(!info || !info.supportsOps) return;
    const amount = Math.max(0, int(amountOverride, 0));
    if(amount <= 0){ refreshValueProjection(); return; }
    const current = Math.max(0, int(info.getCurrent(), 0));
    info.setCurrent(Math.max(0, current - amount));
    validateAndRender();
    scheduleSave();
    setStatus(info.label + " decreased by -" + String(amount) + ".", false);
  }

  function spentPoints(){
    let iPts = 0, ePts = 0;
    if(!isObj(charState.skill_meta)) return { intuition:0, education:0 };
    Object.keys(charState.skill_meta).forEach(function(k){ const e = charState.skill_meta[k]; iPts += Math.max(0,int(e.intuition,0)); ePts += Math.max(0,int(e.education,0)); });
    return { intuition:iPts, education:ePts };
  }

  function validateAndRender(){
    const d = recomputeChar(charState);
    const conditionEffects = isObj(d.conditionEffects) ? d.conditionEffects : activeConditionEffects(charState);
    const carryUsed = Math.max(0, int(d.carryUsed,0));
    const carryCapacity = Math.max(0, int(d.carryCapacity,0));
    const carryStrength = Math.max(0, int(d.carryTheoretical,0));
    const hiddenCapacity = Math.max(0, int(charState.sheet.hidden_pocket_slots,0));
    const hiddenUsed = Math.max(0, int(d.hiddenUsed,0));
    const hiddenOver = Math.max(0, hiddenUsed - hiddenCapacity);
    const hiddenRemaining = Math.max(0, hiddenCapacity - hiddenUsed);
    const carryOver = Math.max(0, d.carryUsed - d.carryTheoretical);
    const carryOverCapacity = Math.max(0, d.carryUsed - d.carryCapacity);
    const carryPenalty = carryOver > 0 ? -carryOver : 0;
    const conditionMod = int(conditionEffects.checkMod,0);
    const iAvail = Math.max(0, int(charState.attr.int,0));
    const eAvail = Math.max(0, int(charState.attr.edu,0));
    const sp = spentPoints();
    const hpMaxEffective = Math.max(0, int(charState.res.hp_max,0) + Math.max(0, int(charState.res.hp_temp,0)));
    const spiritualityMaxEffective = Math.max(0, int(charState.res.spirituality_max,0) + Math.max(0, int(charState.res.spirituality_temp,0)));
    const sanityMaxEffective = Math.max(0, int(charState.res.sanity_max,0) + Math.max(0, int(charState.res.sanity_temp,0)));
    const luckMaxEffective = Math.max(0, int(charState.res.luck_max,0) + Math.max(0, int(charState.res.luck_temp,0)));

    setDerived("hp_max", hpMaxEffective);
    setDerived("hp_current", int(charState.res.hp,0));
    setDerived("hp_temp", Math.max(0, int(charState.res.hp_temp,0)));
    setDerived("spirituality_max", spiritualityMaxEffective);
    setDerived("spirituality_current", int(charState.res.spirituality,0));
    setDerived("spirituality_temp", Math.max(0, int(charState.res.spirituality_temp,0)));
    setDerived("sanity_max", sanityMaxEffective);
    setDerived("sanity_current", int(charState.res.sanity,0));
    setDerived("sanity_temp", Math.max(0, int(charState.res.sanity_temp,0)));
    setDerived("luck_max", luckMaxEffective);
    setDerived("luck_current", int(charState.res.luck,0));
    setDerived("luck_temp", Math.max(0, int(charState.res.luck_temp,0)));
    setDerived("def_physical_max", d.defPhysicalMax);
    setDerived("def_physical_max_base", Math.max(0, int(charState.def.physical_max,0)));
    setDerived("def_physical_temp", Math.max(0, int(charState.def.physical_temp,0)));
    setDerived("def_physical_temp_text", Math.max(0, int(charState.def.physical_temp,0)) > 0 ? ("Temp +" + String(int(charState.def.physical_temp,0))) : "");
    setDerived("def_willpower_max", d.defWillpowerMax);
    setDerived("def_willpower_max_base", Math.max(0, int(charState.def.willpower_max,0)));
    setDerived("def_willpower_temp", Math.max(0, int(charState.def.willpower_temp,0)));
    setDerived("def_willpower_temp_text", Math.max(0, int(charState.def.willpower_temp,0)) > 0 ? ("Temp +" + String(int(charState.def.willpower_temp,0))) : "");
    setDerived("def_constitution_max", d.defConstitutionMax);
    setDerived("def_constitution_max_base", Math.max(0, int(charState.def.constitution_max,0)));
    setDerived("def_constitution_temp", Math.max(0, int(charState.def.constitution_temp,0)));
    setDerived("def_constitution_temp_text", Math.max(0, int(charState.def.constitution_temp,0)) > 0 ? ("Temp +" + String(int(charState.def.constitution_temp,0))) : "");
    setDerived("def_physical", charState.def.physical);
    setDerived("def_willpower", charState.def.willpower);
    setDerived("def_constitution", charState.def.constitution);
    setDerived("sequence_advancements", d.adv);
    setDerived("digestion_bonus", d.digestBonus);
    setDerived("initiative_formula", rollPreview("1d20 + @attr.dex", charState));
    setDerived("initiative_last", initiativeLastResult);
    setDerived("movement", d.movement);
    setDerived("str_damage_bonus", d.strDamage);
    setDerived("carry_theoretical", d.carryTheoretical);
    setDerived("carry_capacity", d.carryCapacity);
    setDerived("carry_overby_used", d.carryUsed);
    setDerived("carry_overby", carryOver);
    setDerived("carry_penalty", carryPenalty);
    setDerived("carry_container_math", String(carryUsed) + " / " + String(carryCapacity));
    setDerived("carry_load_math", String(carryUsed) + " / " + String(carryStrength));
    setDerived("carry_container_state", carryOverCapacity > 0 ? "Over by " + String(carryOverCapacity) : "Within capacity");
    setDerived("carry_load_state", carryOver > 0 ? "Over by " + String(carryOver) : "Within load");
    setDerived("carry_penalty_text", carryPenalty < 0 ? String(carryPenalty) + " to STR/DEX checks" : "No penalty");
    setDerived("hidden_capacity", hiddenCapacity);
    setDerived("hidden_used", hiddenUsed);
    setDerived("hidden_math", String(hiddenUsed) + " / " + String(hiddenCapacity));
    setDerived("hidden_remaining", hiddenRemaining);
    setDerived("hidden_state", hiddenOver > 0 ? "Over by " + String(hiddenOver) : "Within hidden storage");
    setDerived("condition_count", conditionEffects.activeIds.length);
    setDerived("condition_check_mod", signedNumberText(conditionMod));
    setDerived("condition_action_locks", conditionEffects.actionSummary);
    setDerived("condition_notes", conditionEffects.noteSummary || "No extra condition notes.");
    setDerivedTone("carry_container_state", carryOverCapacity > 0 ? "warn" : "ok");
    setDerivedTone("carry_load_state", carryOver > 0 ? "warn" : "ok");
    setDerivedTone("carry_penalty_text", carryPenalty < 0 ? "warn" : "ok");
    setDerivedTone("hidden_state", hiddenOver > 0 ? "warn" : "ok");
    setDerivedTone("hidden_remaining", hiddenOver > 0 ? "warn" : "ok");
    setDerivedTone("condition_check_mod", conditionMod < 0 ? "warn" : (conditionMod > 0 ? "ok" : "neutral"));
    ATTR_KEYS.forEach(function(k){
      setDerived("attr_total_"+k, int(charState.attr[k],0));
      setDerived("attr_bonus_"+k, signedNumberText(int(charState.beyonder.attr_bonus[k],0)));
    });
    renderPortraitCard();
    refreshHpProjection();
    refreshValueProjection();

    const fill = sheetRoot ? sheetRoot.querySelector(".lotm-digestion-fill") : null;
    if(fill) fill.style.width = String(d.digest) + "%";

    if(skillPoolEl){
      skillPoolEl.textContent =
        "Intuition points: "+String(iAvail)+" (spent "+String(sp.intuition)+", remaining "+String(iAvail-sp.intuition)+") | "+
        "Education points: "+String(eAvail)+" (spent "+String(sp.education)+", remaining "+String(eAvail-sp.education)+")";
    }

    if(validationEl){
      const items = [];
      if(!charState.meta.name.trim()) items.push("Character name is empty.");
      if(!charState.meta.pathway.trim()) items.push("Pathway is not selected.");
      if(!Number.isFinite(Number(charState.meta.sequence))) items.push("Sequence should be a number from 0 to 9.");
      if(d.digest < 0 || d.digest > 100) items.push("Digestion should be between 0 and 100.");
      if(carryOverCapacity > 0) items.push("Item slots exceed container slots by " + String(carryOverCapacity) + ".");
      if(carryOver > 0) items.push("Item slots exceed STR load slots by "+String(carryOver)+" (STR/DEX penalty "+String(-carryOver)+").");
      if(hiddenOver > 0) items.push("Items marked as hidden pockets exceed hidden-pocket slots by " + String(hiddenOver) + ".");
      if(conditionEffects.activeIds.length){
        items.push("Active conditions: " + conditionEffects.activeLabels.join(", ") + ".");
      }
      if(conditionEffects.blocked.attack) items.push("Attack actions are currently blocked by active conditions.");
      if(conditionEffects.blocked.cast) items.push("Casting actions are currently blocked by active conditions.");
      if(conditionEffects.blocked.move) items.push("Move actions are currently blocked by active conditions.");
      if(conditionEffects.blocked.swift) items.push("Swift actions are currently blocked by active conditions.");
      if(conditionEffects.blocked.free) items.push("Free actions are currently blocked by active conditions.");
      if(conditionEffects.blocked.speech) items.push("Speech-based actions are blocked while Silenced is active.");
      if(sp.intuition > iAvail) items.push("Spent Intuition points exceed INT-based pool by "+String(sp.intuition - iAvail)+".");
      if(sp.education > eAvail) items.push("Spent Education points exceed EDU-based pool by "+String(sp.education - eAvail)+".");
      if(int(charState.res.hp,0) > hpMaxEffective) items.push("Current Health exceeds computed max.");
      if(int(charState.res.spirituality,0) > spiritualityMaxEffective) items.push("Current Spirituality exceeds computed max.");
      if(int(charState.res.sanity,0) > sanityMaxEffective) items.push("Current Sanity exceeds computed max.");
      if(int(charState.res.luck,0) > luckMaxEffective) items.push("Current Luck exceeds computed max.");
      if(int(charState.def.physical,0) > int(d.defPhysicalMax,0)) items.push("Current Physical Defense exceeds inferred max.");
      if(int(charState.def.willpower,0) > int(d.defWillpowerMax,0)) items.push("Current Willpower Defense exceeds inferred max.");
      if(int(charState.def.constitution,0) > int(d.defConstitutionMax,0)) items.push("Current Constitution Defense exceeds inferred max.");

      validationEl.innerHTML = "";
      if(!items.length){ const li = document.createElement("li"); li.className = "ok"; li.textContent = "No validation warnings."; validationEl.appendChild(li); }
      else items.forEach(function(msg){ const li = document.createElement("li"); li.textContent = msg; validationEl.appendChild(li); });
    }
  }

  function applyBoundInputs(){
    if(!sheetRoot) return;
    sheetRoot.querySelectorAll("[data-bind]").forEach(function(el){
      const path = el.getAttribute("data-bind");
      const value = getPath(charState, path);
      const isNum = el.getAttribute("data-type") === "number" || el.type === "number";
      if(el.tagName === "TEXTAREA") el.value = typeof value === "string" ? value : String(value||"");
      else if(el.tagName === "SELECT") el.value = typeof value === "string" ? value : String(value||"");
      else if(el instanceof HTMLInputElement) el.value = isNum ? String(int(value,0)) : (typeof value === "string" ? value : String(value||""));
    });
  }

  function setTab(tab){
    if(tab !== "abilities") closeAbilityDetail();
    if(tab !== "overview") setHpManagerOpen(false);
    if(tab !== "overview") setValueManagerOpen(false);
    if(!sheetRoot) return;
    sheetRoot.querySelectorAll(".lotm-tab").forEach(function(b){ b.classList.toggle("active", b.getAttribute("data-tab") === tab); });
    sheetRoot.querySelectorAll(".lotm-sheet-panel").forEach(function(p){ p.classList.toggle("active", p.getAttribute("data-panel") === tab); });
    sheetRoot.setAttribute("data-active-tab", tab);
  }

  function setSheetOpen(open){
    if(!open){
      closeAbilityDetail();
      setHpManagerOpen(false);
      setValueManagerOpen(false);
    }
    document.body.classList.toggle("lotm-sheet-open", !!open);
    if(sheetRoot) sheetRoot.setAttribute("aria-hidden", open ? "false" : "true");
    if(sheetToggleBtn){
      sheetToggleBtn.textContent = open ? "Back to Rulebook" : "Character Sheet";
      sheetToggleBtn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    if(open) renderAll();
  }

  function initRulebookSidebar(){
    const body = document.body;
    if(!body) return;
    const sidebar = document.getElementById("sidebar") || document.querySelector(".sidebar");
    const toggles = Array.from(document.querySelectorAll('[data-action="toggle-sidebar"]'));
    const desktopMq = typeof window.matchMedia === "function" ? window.matchMedia("(min-width: 981px)") : null;
    let mobileResizeTick = 0;

    function isDesktop(){
      return desktopMq ? desktopMq.matches : window.innerWidth >= 981;
    }

    function sidebarExpanded(){
      if(isDesktop()) return !body.classList.contains("sidebar-collapsed");
      return body.classList.contains("sidebar-open");
    }

    function syncSidebarButtonA11y(){
      const expanded = sidebarExpanded();
      toggles.forEach(function(btn){
        btn.setAttribute("aria-expanded", expanded ? "true" : "false");
        btn.setAttribute("aria-controls", "sidebar");
      });
    }

    function applyDesktopCollapse(collapsed, persist){
      body.classList.toggle("sidebar-collapsed", !!collapsed);
      body.classList.remove("sidebar-open");
      if(persist){
        if(collapsed) localStorage.setItem(SIDEBAR_COLLAPSE_KEY, "1");
        else localStorage.removeItem(SIDEBAR_COLLAPSE_KEY);
      }
      syncSidebarButtonA11y();
    }

    function syncViewportSidebarState(){
      if(isDesktop()){
        const savedCollapsed = localStorage.getItem(SIDEBAR_COLLAPSE_KEY) === "1";
        applyDesktopCollapse(savedCollapsed, false);
      }else{
        body.classList.remove("sidebar-collapsed");
        syncSidebarButtonA11y();
      }
    }

    syncViewportSidebarState();

    toggles.forEach(function(btn){
      btn.addEventListener("click", function(ev){
        ev.preventDefault();
        if(isDesktop()){
          applyDesktopCollapse(!body.classList.contains("sidebar-collapsed"), true);
          return;
        }
        body.classList.toggle("sidebar-open");
        syncSidebarButtonA11y();
      });
    });

    if(sidebar){
      document.addEventListener("click", function(ev){
        if(isDesktop()) return;
        if(!body.classList.contains("sidebar-open")) return;
        const target = ev.target;
        if(!(target instanceof Element)) return;
        if(sidebar.contains(target)) return;
        if(target.closest('[data-action="toggle-sidebar"]')) return;
        body.classList.remove("sidebar-open");
        syncSidebarButtonA11y();
      });
    }

    if(desktopMq && typeof desktopMq.addEventListener === "function"){
      desktopMq.addEventListener("change", syncViewportSidebarState);
    }else{
      window.addEventListener("resize", function(){
        clearTimeout(mobileResizeTick);
        mobileResizeTick = window.setTimeout(syncViewportSidebarState, 70);
      });
    }

    const nav = document.getElementById("nav") || (sidebar ? sidebar.querySelector("#nav") : null);
    if(!nav) return;

    const dirs = Array.from(nav.querySelectorAll("details.nav-dir[data-path]"));
    if(!dirs.length) return;

    const openSet = new Set(safeJsonParse(localStorage.getItem(NAV_STATE_KEY), []));
    dirs.forEach(function(d){
      const path = String(d.getAttribute("data-path") || "");
      if(path && openSet.has(path)) d.open = true;
      d.addEventListener("toggle", function(){
        if(!path) return;
        if(d.open) openSet.add(path); else openSet.delete(path);
        localStorage.setItem(NAV_STATE_KEY, JSON.stringify(Array.from(openSet)));
      });
    });
  }

  function buildOverviewTopRow(){
    if(!sheetRoot) return;
    const rightCol = sheetRoot.querySelector(".lotm-overview-right");
    const digestion = sheetRoot.querySelector(".lotm-sheet-nav-digestion");
    if(!rightCol || !digestion) return;

    let row = rightCol.querySelector(".lotm-overview-top-row");
    if(!row){
      row = document.createElement("div");
      row.className = "lotm-overview-top-row";
      rightCol.insertBefore(row, rightCol.firstChild || null);
    }

    if(digestion.parentElement !== row){
      row.insertBefore(digestion, row.firstChild || null);
    }

    let initiative = row.querySelector(".lotm-initiative-box");
    if(!initiative){
      initiative = document.createElement("div");
      initiative.className = "lotm-initiative-box";
      initiative.innerHTML =
        "<div class='lotm-initiative-head'>" +
          "<span class='lotm-initiative-label'>Initiative</span>" +
          "<button type='button' class='btn btn-ghost lotm-initiative-btn' data-action='roll-initiative'>Roll</button>" +
        "</div>" +
        "<span class='lotm-initiative-formula' data-derived='initiative_formula'>1d20 + Dex</span>" +
        "<span class='lotm-initiative-last'>Last <strong data-derived='initiative_last'>-</strong></span>";
      row.appendChild(initiative);
    }
  }

  function rebuildVitalResourceCards(){
    if(!sheetRoot) return;
    VITAL_RESOURCE_KEYS.forEach(function(key){
      const oldCurrentInput = sheetRoot.querySelector(".lotm-vital-summary input[data-bind='res." + key + "']");
      const card = oldCurrentInput ? oldCurrentInput.closest(".lotm-vital-summary") : null;
      if(!card) return;
      card.setAttribute("data-resource-card", key);
      card.innerHTML =
        "<div class='lotm-hp-summary-left'>" +
          "<button type='button' class='lotm-hp-summary-chip heal' data-action='resource-inc-quick' data-resource='"+key+"'>Inc</button>" +
          "<input type='number' class='lotm-char-input lotm-hp-quick-input' data-resource-tool='"+key+"-quick' value='0' />" +
          "<button type='button' class='lotm-hp-summary-chip damage' data-action='resource-dec-quick' data-resource='"+key+"'>Dec</button>" +
        "</div>" +
        "<button type='button' class='lotm-hp-summary-main' data-action='open-value-manager' data-resource='"+key+"'>" +
          "<div class='lotm-hp-summary-values'><strong data-derived='"+key+"_current'>0</strong><span>/</span><strong data-derived='"+key+"_max'>0</strong></div>" +
          "<div class='lotm-hp-summary-label'>" + vitalResourceLabel(key) + "</div>" +
          "<div class='lotm-hp-summary-temp'>Temp <strong data-derived='"+key+"_temp'>0</strong></div>" +
        "</button>";
    });
  }

  function rebuildDefenseBoxes(){
    if(!sheetRoot) return;
    if(sheetRoot.querySelector(".lotm-defense-max-row")) return;

    const targets = [
      { target: "def.physical", bind: "def.physical", maxDerived: "def_physical_max_base", tempDerived: "def_physical_temp_text" },
      { target: "def.willpower", bind: "def.willpower", maxDerived: "def_willpower_max_base", tempDerived: "def_willpower_temp_text" },
      { target: "def.constitution", bind: "def.constitution", maxDerived: "def_constitution_max_base", tempDerived: "def_constitution_temp_text" }
    ];

    const cards = targets.map(function(t){
      const oldInput = sheetRoot.querySelector(".lotm-vital-summary input[data-bind='" + t.bind + "']");
      return oldInput ? oldInput.closest(".lotm-vital-summary") : null;
    }).filter(Boolean);
    if(cards.length !== targets.length) return;

    const luckCard = sheetRoot.querySelector(".lotm-vital-summary[data-resource-card='luck']");
    const firstCard = cards[0];
    const parent = firstCard ? firstCard.parentElement : null;
    if(!parent) return;

    const row = document.createElement("section");
    row.className = "lotm-defense-max-row";
    row.innerHTML = targets.map(function(t){
      const meta = DEFENSE_MANAGER_TARGETS[t.target];
      return (
        "<button type='button' class='lotm-defense-max-box' data-action='open-value-manager' data-resource='" + t.target + "'>" +
          "<span class='lotm-defense-max-code'>" + meta.short + "</span>" +
          "<strong class='lotm-defense-max-value' data-derived='" + t.maxDerived + "'>0</strong>" +
          "<span class='lotm-defense-max-temp' data-derived='" + t.tempDerived + "'></span>" +
        "</button>"
      );
    }).join("");

    if(luckCard && luckCard.parentElement === parent){
      if(luckCard.nextSibling) parent.insertBefore(row, luckCard.nextSibling);
      else parent.appendChild(row);
    }else{
      parent.insertBefore(row, firstCard);
    }

    cards.forEach(function(card){ card.remove(); });
  }

  function mountValueManager(){
    if(!sheetRoot || sheetRoot.querySelector(".lotm-value-manager")) return;
    const wrapper = document.createElement("div");
    wrapper.className = "lotm-hp-manager lotm-value-manager";
    wrapper.setAttribute("aria-hidden", "true");
    wrapper.innerHTML =
      "<div class='lotm-hp-manager-backdrop' data-action='close-value-manager'></div>" +
      "<section class='lotm-hp-manager-panel' role='dialog' aria-modal='true' aria-label='Value Management'>" +
        "<header class='lotm-hp-manager-head'><h4 data-value-manager='title'>Value Management</h4><button type='button' class='btn btn-ghost' data-action='close-value-manager'>Close</button></header>" +
        "<div class='lotm-hp-manager-row'>" +
          "<label class='lotm-hp-stat'><span>Current</span><input type='number' class='lotm-char-input' data-value-manager-field='current' /></label>" +
          "<div class='lotm-hp-sep'>/</div>" +
          "<div class='lotm-hp-stat lotm-hp-stat-readonly'><span>Max</span><strong data-value-manager='max'>0</strong></div>" +
          "<label class='lotm-hp-stat'><span>Temp</span><input type='number' class='lotm-char-input' data-value-manager-field='temp' /></label>" +
        "</div>" +
        "<div class='lotm-hp-manager-ops' data-value-manager='ops'>" +
          "<label class='lotm-hp-op-box'><span>Increase</span><input type='number' class='lotm-char-input' data-value-tool='inc-value' value='0' /></label>" +
          "<button type='button' class='btn lotm-hp-op-btn lotm-hp-heal' data-action='resource-inc'>+</button>" +
          "<div class='lotm-hp-new'><span>Projected</span><strong data-value-manager='projected'>0</strong></div>" +
          "<label class='lotm-hp-op-box'><span>Decrease</span><input type='number' class='lotm-char-input' data-value-tool='dec-value' value='0' /></label>" +
          "<button type='button' class='btn lotm-hp-op-btn lotm-hp-damage' data-action='resource-dec'>-</button>" +
        "</div>" +
      "</section>";
    sheetRoot.appendChild(wrapper);
  }

  function mountSheet(){
    const topbar = document.querySelector(".topbar");
    const content = document.querySelector(".content");
    const bodyPanel = document.querySelector(".content-body");
    if(!topbar || !content || !bodyPanel) return;
    if(document.querySelector(".lotm-sheet-toggle") || document.getElementById("lotm-sheet-page")) return;

    sheetToggleBtn = document.createElement("button");
    sheetToggleBtn.type = "button";
    sheetToggleBtn.className = "btn btn-ghost lotm-sheet-toggle";
    sheetToggleBtn.textContent = "Character Sheet";
    sheetToggleBtn.setAttribute("aria-controls","lotm-sheet-page");
    sheetToggleBtn.setAttribute("aria-expanded","false");
    topbar.appendChild(sheetToggleBtn);

    sheetRoot = document.createElement("section");
    sheetRoot.id = "lotm-sheet-page";
    sheetRoot.className = "lotm-sheet-page";
    sheetRoot.setAttribute("aria-hidden","true");
    sheetRoot.setAttribute("data-active-tab", "overview");

    sheetRoot.innerHTML = [
      "<div class='lotm-sheet-shell'>",
      "<header class='lotm-sheet-head'><div><h2>Character Sheet</h2><p>Play-focused page with rolling and tracking.</p></div>",
      "<div class='lotm-sheet-head-actions'><button type='button' class='btn lotm-sheet-export'>Export JSON</button><button type='button' class='btn lotm-sheet-import'>Import JSON</button><button type='button' class='btn btn-ghost lotm-sheet-reset'>Reset</button></div></header>",
      "<nav class='lotm-sheet-tabs' role='tablist'><button type='button' class='lotm-tab active' data-tab='overview'>Overview</button><button type='button' class='lotm-tab' data-tab='skills'>Skills</button><button type='button' class='lotm-tab' data-tab='abilities'>Abilities</button><button type='button' class='lotm-tab' data-tab='inventory'>Inventory</button><button type='button' class='lotm-tab' data-tab='story'>Story</button><button type='button' class='lotm-tab' data-tab='log'>Logs</button></nav>",
      "<div class='lotm-sheet-status' aria-live='polite'></div>",
      "<div class='lotm-sheet-panels'>",

      "<section class='lotm-sheet-panel active' data-panel='overview'><div class='lotm-overview-layout'>",
      "<div class='lotm-overview-left'>",
      "<div class='lotm-attr-grid lotm-sheet-nav-attrs lotm-overview-attrs'></div>",
      "<article class='lotm-sheet-card'><h3>Basic Info</h3><div class='lotm-field-grid'>",
      "<label class='lotm-field'><span>Name</span><input class='lotm-char-input' data-bind='meta.name' /></label>",
      "<label class='lotm-field'><span>Player</span><input class='lotm-char-input' data-bind='meta.player' /></label>",
      "<label class='lotm-field'><span>Pathway</span><select class='lotm-char-input lotm-pathway-select'></select></label>",
      "<label class='lotm-field'><span>Sequence</span><select class='lotm-char-input lotm-sequence-select'><option value='9'>Sequence 9</option><option value='8'>Sequence 8</option><option value='7'>Sequence 7</option><option value='6'>Sequence 6</option><option value='5'>Sequence 5</option><option value='4'>Sequence 4</option><option value='3'>Sequence 3</option><option value='2'>Sequence 2</option><option value='1'>Sequence 1</option><option value='0'>Sequence 0</option></select></label>",
      "</div></article>",
      "<article class='lotm-sheet-card'><details class='lotm-condition-picker'><summary>Special Conditions</summary><div class='lotm-condition-grid'></div></details><div class='lotm-condition-derived'><div class='lotm-condition-pill'><span>Active</span><strong data-derived='condition_count'>0</strong></div><div class='lotm-condition-pill'><span>Check Mod</span><strong data-derived='condition_check_mod'>0</strong></div><div class='lotm-condition-pill lotm-condition-pill-wide'><span>Action Locks</span><strong data-derived='condition_action_locks'>No hard action locks</strong></div></div><div class='lotm-condition-notes' data-derived='condition_notes'>No extra condition notes.</div></article>",
      "<article class='lotm-sheet-card'><h3>Validation</h3><ul class='lotm-validation-list'></ul></article>",
      "</div>",
      "<aside class='lotm-overview-right'><div class='lotm-sheet-nav-digestion'><span class='lotm-sheet-nav-digestion-label'>Digestion %</span><input type='number' min='0' max='100' class='lotm-char-input lotm-sheet-nav-digestion-input' data-bind='beyonder.digestion_pct' data-type='number' /><span class='lotm-sheet-nav-digestion-bonus'>Bonus <strong data-derived='digestion_bonus'>0</strong></span></div><div class='lotm-hp-summary'><div class='lotm-hp-summary-left'><button type='button' class='lotm-hp-summary-chip heal' data-action='hp-heal-quick'>Heal</button><input type='number' class='lotm-char-input lotm-hp-quick-input' data-hp-tool='quick-value' value='0' /><button type='button' class='lotm-hp-summary-chip damage' data-action='hp-damage-quick'>Damage</button></div><button type='button' class='lotm-hp-summary-main' data-action='open-hp-manager'><div class='lotm-hp-summary-values'><strong data-derived='hp_current'>0</strong><span>/</span><strong data-derived='hp_max'>0</strong></div><div class='lotm-hp-summary-label'>Hit Points</div><div class='lotm-hp-summary-temp'>Temp <strong data-derived='hp_temp'>0</strong></div></button></div><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='res.spirituality' data-type='number' /><span>/</span><strong data-derived='spirituality_max'>0</strong></div><div class='lotm-hp-summary-label'>Spirituality</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='res.spirituality_max_bonus' data-type='number' /></label></section><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='res.sanity' data-type='number' /><span>/</span><strong data-derived='sanity_max'>0</strong></div><div class='lotm-hp-summary-label'>Sanity</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='res.sanity_max_bonus' data-type='number' /></label></section><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='res.luck' data-type='number' /><span>/</span><strong data-derived='luck_max'>0</strong></div><div class='lotm-hp-summary-label'>Luck</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='res.luck_max_bonus' data-type='number' /></label></section><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='def.physical' data-type='number' /><span>/</span><strong data-derived='def_physical_max'>0</strong></div><div class='lotm-hp-summary-label'>Physical Defense</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='def.physical_bonus' data-type='number' /></label></section><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='def.willpower' data-type='number' /><span>/</span><strong data-derived='def_willpower_max'>0</strong></div><div class='lotm-hp-summary-label'>Willpower Defense</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='def.willpower_bonus' data-type='number' /></label></section><section class='lotm-vital-summary'><div class='lotm-vital-summary-main'><div class='lotm-hp-summary-values'><input type='number' class='lotm-char-input lotm-vital-current' data-bind='def.constitution' data-type='number' /><span>/</span><strong data-derived='def_constitution_max'>0</strong></div><div class='lotm-hp-summary-label'>Constitution Defense</div></div><label class='lotm-vital-ticket'><span>Max +/-</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='def.constitution_bonus' data-type='number' /></label></section><section class='lotm-vital-summary lotm-vital-summary-meta'><label class='lotm-vital-ticket'><span>Armor Bonus</span><input type='number' class='lotm-char-input lotm-small-number' data-bind='def.armor' data-type='number' /></label><div class='lotm-vital-meta'><span>Movement <strong data-derived='movement'>0</strong></span><span>STR Damage <strong data-derived='str_damage_bonus'>0</strong></span></div></section></aside></div></section>",

      "<section class='lotm-sheet-panel' data-panel='skills'><article class='lotm-sheet-card'><h3>Skill Table</h3><p>Rule formula: 1d20 + related attribute + skill modifier. Intuition and Education pools are derived from your current INT and EDU attributes.</p>",
      "<div class='lotm-skill-controls2'><input type='search' class='lotm-char-input lotm-skill-search2' placeholder='Search skills' /></div>",
      "<div class='lotm-skill-pool-summary'></div>",
      "<div class='lotm-skill-section-title'>Skills</div>",
      "<div class='lotm-skill-body'></div>",
      "<section class='lotm-skill-create-section'><div class='lotm-skill-create-title'>Create Custom Skill</div><div class='lotm-skill-create-controls'><input class='lotm-char-input lotm-custom-token' placeholder='Custom skill token' /><select class='lotm-char-input lotm-custom-attr'>",
      ATTR_KEYS.map(function(k){ return "<option value='"+k+"'>"+ATTR_LABELS[k]+"</option>"; }).join(""),
      "</select><button type='button' class='btn lotm-add-custom-skill'>Add Skill</button></div></section></article></section>",

      "<section class='lotm-sheet-panel' data-panel='abilities'><article class='lotm-sheet-card lotm-collapsible-card'><details class='lotm-card-details lotm-abilities-details' open><summary>Beyonder Abilities</summary><div class='lotm-card-body'><div class='lotm-ability-summary'></div><div class='lotm-ability-list'></div><aside class='lotm-ability-detail' aria-hidden='true'><div class='lotm-ability-detail-head'><h4 class='lotm-ability-detail-title'>Ability Details</h4><button type='button' class='btn btn-ghost lotm-ability-detail-close'>Close</button></div><div class='lotm-ability-detail-body'></div></aside></div></details></article>",
      "<article class='lotm-sheet-card lotm-collapsible-card'><details class='lotm-card-details lotm-special-actions-details' open><summary>Universal Combat Actions</summary><div class='lotm-card-body'><p>Core-rule, non-sequence-specific special actions from the Combat chapter.</p><div class='lotm-special-action-summary'></div><div class='lotm-special-action-list'></div></div></details></article>",
      "<article class='lotm-sheet-card'><h3>Actions</h3><div class='lotm-list-toolbar'><button type='button' class='btn lotm-add-action'>Add Action</button></div><div class='lotm-action-list'></div></article></section>",

      "<section class='lotm-sheet-panel' data-panel='inventory'><article class='lotm-sheet-card'><h3>Carrying Capacity</h3><p class='lotm-carry-help'>Slots used are auto-calculated from your item list. You are checked against both <strong>Container Slots</strong> (Pocket + Extra) and <strong>STR Load Slots</strong> (Strength x 2). Going over STR Load applies a STR/DEX penalty. Mark hidden items in the list below with <strong>Hidden Pocket</strong>.</p><details class='lotm-carry-rule'><summary>Pocket Counts by Clothing (Chapter 3)</summary><p>Formalwear or Performance Tailcoat can choose 2 hidden pockets. Wizard Robe includes 4 hidden pockets. Bags and suitcases may add more hidden pockets based on equipment tier.</p></details><div class='lotm-field-grid'><label class='lotm-field'><span>Pocket Slots</span><input type='number' class='lotm-char-input' data-bind='sheet.pocket_slots' data-type='number' /></label><label class='lotm-field'><span>Container Extra Slots</span><input type='number' class='lotm-char-input' data-bind='sheet.carry_slots_override' data-type='number' /></label><label class='lotm-field'><span>Hidden Pocket Slots</span><input type='number' class='lotm-char-input' data-bind='sheet.hidden_pocket_slots' data-type='number' /></label></div><div class='lotm-carry-summary'><div class='lotm-carry-pill'><span>Slots Used</span><strong data-derived='carry_overby_used'>0</strong></div><div class='lotm-carry-pill'><span>Container Slots</span><strong data-derived='carry_capacity'>0</strong></div><div class='lotm-carry-pill'><span>STR Load Slots</span><strong data-derived='carry_theoretical'>0</strong></div><div class='lotm-carry-pill'><span>Hidden Slots Used</span><strong data-derived='hidden_used'>0</strong></div><div class='lotm-carry-pill'><span>Hidden Slots Allowed</span><strong data-derived='hidden_capacity'>0</strong></div></div><div class='lotm-carry-math'><div class='lotm-carry-line'><span>Container Check: <strong data-derived='carry_container_math'>0 / 0</strong></span><span class='lotm-carry-state' data-derived='carry_container_state'>Within capacity</span></div><div class='lotm-carry-line'><span>Load Check: <strong data-derived='carry_load_math'>0 / 0</strong></span><span class='lotm-carry-state' data-derived='carry_load_state'>Within load</span></div><div class='lotm-carry-line'><span>Hidden Check: <strong data-derived='hidden_math'>0 / 0</strong></span><span class='lotm-carry-state' data-derived='hidden_state'>Within hidden storage</span></div><div class='lotm-carry-line'><span>Hidden Slots Remaining</span><strong class='lotm-carry-penalty' data-derived='hidden_remaining'>0</strong></div><div class='lotm-carry-line'><span>STR/DEX Penalty</span><strong class='lotm-carry-penalty' data-derived='carry_penalty_text'>No penalty</strong></div></div></article><article class='lotm-sheet-card'><h3>Carried Items</h3><p>Each item adds to Slots Used automatically. Use the Hidden Pocket toggle for concealed storage.</p><div class='lotm-list-toolbar'><button type='button' class='btn lotm-add-item'>Add Item</button></div><div class='lotm-item-list'></div></article><article class='lotm-sheet-card lotm-wealth-sidebar'><h3>Personal Wealth / Lifestyle</h3><div class='lotm-field-grid'><label class='lotm-field'><span>Total Savings</span><input class='lotm-char-input' data-bind='wealth.total_savings' /></label><label class='lotm-field'><span>Liquid Assets</span><input class='lotm-char-input' data-bind='wealth.liquid_assets' /></label><label class='lotm-field'><span>Total Assets</span><input class='lotm-char-input' data-bind='wealth.total_assets' /></label><label class='lotm-field'><span>Weekly Pay</span><input class='lotm-char-input' data-bind='wealth.weekly_pay' /></label><label class='lotm-field'><span>Weekly Rent</span><input class='lotm-char-input' data-bind='wealth.weekly_rent' /></label><label class='lotm-field'><span>Residence</span><input class='lotm-char-input' data-bind='wealth.residence' /></label><label class='lotm-field'><span>Servant</span><input class='lotm-char-input' data-bind='wealth.servant' /></label><label class='lotm-field'><span>Lifestyle</span><input class='lotm-char-input' data-bind='wealth.lifestyle' /></label></div></article></section>",

      "<section class='lotm-sheet-panel' data-panel='story'><article class='lotm-sheet-card'><h3>Character Backstory</h3><label class='lotm-field lotm-field-wide'><span>Backstory</span><textarea class='lotm-char-input' data-bind='backstory'></textarea></label></article>",
      "<article class='lotm-sheet-card'><h3>Beyonder Ability Notes</h3><div class='lotm-field-grid'><label class='lotm-field lotm-field-wide'><span>NPC Companions</span><textarea class='lotm-char-input' data-bind='beyonder.npc_companions'></textarea></label><label class='lotm-field lotm-field-wide'><span>Custom Spells</span><textarea class='lotm-char-input' data-bind='beyonder.custom_spells'></textarea></label><label class='lotm-field lotm-field-wide'><span>Grazed Souls</span><textarea class='lotm-char-input' data-bind='beyonder.grazed_souls'></textarea></label><label class='lotm-field lotm-field-wide'><span>Recorded/Stolen Abilities</span><textarea class='lotm-char-input' data-bind='beyonder.recorded_abilities'></textarea></label></div></article>",
      "<article class='lotm-sheet-card'><h3>Character Description</h3><div class='lotm-field-grid'><label class='lotm-field'><span>Age</span><input class='lotm-char-input' data-bind='meta.age' /></label><label class='lotm-field'><span>Occupation</span><input class='lotm-char-input' data-bind='meta.occupation' /></label><label class='lotm-field'><span>Race</span><input class='lotm-char-input' data-bind='meta.race' /></label><label class='lotm-field'><span>Gender</span><input class='lotm-char-input' data-bind='meta.gender' /></label><label class='lotm-field'><span>Appearance</span><input class='lotm-char-input' data-bind='description.appearance' /></label><label class='lotm-field'><span>Height</span><input class='lotm-char-input' data-bind='description.height' /></label><label class='lotm-field'><span>Weight</span><input class='lotm-char-input' data-bind='description.weight' /></label><label class='lotm-field'><span>Deity Worshipped</span><input class='lotm-char-input' data-bind='description.deity_worshipped' /></label><label class='lotm-field'><span>Alignment / Faction</span><input class='lotm-char-input' data-bind='description.alignment_faction' /></label><label class='lotm-field'><span>Ideals & Beliefs</span><input class='lotm-char-input' data-bind='description.ideals_beliefs' /></label><label class='lotm-field'><span>Important Person</span><input class='lotm-char-input' data-bind='description.important_person' /></label><label class='lotm-field'><span>Valued Possession</span><input class='lotm-char-input' data-bind='description.valued_possession' /></label><label class='lotm-field'><span>Meaningful Place</span><input class='lotm-char-input' data-bind='description.meaningful_place' /></label><label class='lotm-field'><span>Wounds & Scars</span><input class='lotm-char-input' data-bind='description.wounds_scars' /></label><label class='lotm-field'><span>Likes</span><input class='lotm-char-input' data-bind='description.likes' /></label><label class='lotm-field'><span>Dislikes</span><input class='lotm-char-input' data-bind='description.dislikes' /></label></div></article></section>",

      "<section class='lotm-sheet-panel' data-panel='log'><article class='lotm-sheet-card'><h3>Roll Log</h3><div class='lotm-list-toolbar'><button type='button' class='btn btn-ghost lotm-roll-clear'>Clear Log</button></div><div class='lotm-roll-list'></div></article><article class='lotm-sheet-card'><h3>Adventure Log</h3><div class='lotm-list-toolbar'><button type='button' class='btn lotm-add-adv'>Add Entry</button></div><div class='lotm-adventure-list'></div></article></section>",

      "</div><div class='lotm-hp-manager' aria-hidden='true'><div class='lotm-hp-manager-backdrop' data-action='close-hp-manager'></div><section class='lotm-hp-manager-panel' role='dialog' aria-modal='true' aria-label='HP Management'><header class='lotm-hp-manager-head'><h4>HP Management</h4><button type='button' class='btn btn-ghost lotm-hp-manager-close' data-action='close-hp-manager'>Close</button></header><div class='lotm-hp-manager-row'><label class='lotm-hp-stat'><span>Current</span><input type='number' class='lotm-char-input' data-bind='res.hp' data-type='number' /></label><div class='lotm-hp-sep'>/</div><div class='lotm-hp-stat lotm-hp-stat-readonly'><span>Max</span><strong data-derived='hp_max'>0</strong></div><label class='lotm-hp-stat'><span>Temp</span><input type='number' class='lotm-char-input' data-bind='res.hp_temp' data-type='number' /></label></div><div class='lotm-hp-manager-ops'><label class='lotm-hp-op-box'><span>Healing</span><input type='number' class='lotm-char-input' data-hp-tool='heal-value' value='0' /></label><button type='button' class='btn lotm-hp-op-btn lotm-hp-heal' data-action='hp-heal'>+</button><div class='lotm-hp-new'><span>New HP</span><strong data-derived='hp_projected'>0</strong></div><label class='lotm-hp-op-box'><span>Damage</span><input type='number' class='lotm-char-input' data-hp-tool='damage-value' value='0' /></label><button type='button' class='btn lotm-hp-op-btn lotm-hp-damage' data-action='hp-damage'>-</button></div><div class='lotm-hp-manager-mods'><label class='lotm-hp-mod'><span>Max HP Modifier</span><input type='number' class='lotm-char-input' data-bind='res.hp_max_bonus' data-type='number' /></label><label class='lotm-hp-mod'><span>Override Max HP</span><input type='number' class='lotm-char-input' data-bind='res.hp_max_override' data-type='number' /></label></div></section></div><input type='file' class='lotm-import-file' accept='application/json,.json' hidden /><input type='file' class='lotm-portrait-file' accept='image/*' hidden /></div>"
    ].join("");

    content.insertBefore(sheetRoot, bodyPanel);
    buildOverviewTopRow();
    rebuildVitalResourceCards();
    rebuildDefenseBoxes();
    mountValueManager();

    statusEl = sheetRoot.querySelector(".lotm-sheet-status");
    validationEl = sheetRoot.querySelector(".lotm-validation-list");
    conditionListEl = sheetRoot.querySelector(".lotm-condition-grid");
    skillBodyEl = sheetRoot.querySelector(".lotm-skill-body");
    skillSearchEl = sheetRoot.querySelector(".lotm-skill-search2");
    skillPoolEl = sheetRoot.querySelector(".lotm-skill-pool-summary");
    abilityListEl = sheetRoot.querySelector(".lotm-ability-list");
    abilitySummaryEl = sheetRoot.querySelector(".lotm-ability-summary");
    specialActionListEl = sheetRoot.querySelector(".lotm-special-action-list");
    specialActionSummaryEl = sheetRoot.querySelector(".lotm-special-action-summary");
    abilityDetailEl = sheetRoot.querySelector(".lotm-ability-detail");
    abilityDetailTitleEl = sheetRoot.querySelector(".lotm-ability-detail-title");
    abilityDetailBodyEl = sheetRoot.querySelector(".lotm-ability-detail-body");
    actionListEl = sheetRoot.querySelector(".lotm-action-list");
    itemListEl = sheetRoot.querySelector(".lotm-item-list");
    adventureListEl = sheetRoot.querySelector(".lotm-adventure-list");
    rollListEl = sheetRoot.querySelector(".lotm-roll-list");
    mysticismLangListEl = sheetRoot.querySelector("[data-language-list='mysticism']");
    commonLangListEl = sheetRoot.querySelector("[data-language-list='common']");
    pathwaySelectEl = sheetRoot.querySelector(".lotm-pathway-select");
    sequenceSelectEl = sheetRoot.querySelector(".lotm-sequence-select");
    importFileEl = sheetRoot.querySelector(".lotm-import-file");
    portraitFileEl = sheetRoot.querySelector(".lotm-portrait-file");
    hpManagerEl = sheetRoot.querySelector(".lotm-hp-manager:not(.lotm-value-manager)");
    hpHealInputEl = sheetRoot.querySelector('[data-hp-tool="heal-value"]');
    hpDamageInputEl = sheetRoot.querySelector('[data-hp-tool="damage-value"]');
    hpQuickValueInputEl = sheetRoot.querySelector('[data-hp-tool="quick-value"]');
    valueManagerEl = sheetRoot.querySelector(".lotm-value-manager");
    valueManagerTitleEl = sheetRoot.querySelector('[data-value-manager="title"]');
    valueManagerCurrentInputEl = sheetRoot.querySelector('[data-value-manager-field="current"]');
    valueManagerTempInputEl = sheetRoot.querySelector('[data-value-manager-field="temp"]');
    valueManagerIncInputEl = sheetRoot.querySelector('[data-value-tool="inc-value"]');
    valueManagerDecInputEl = sheetRoot.querySelector('[data-value-tool="dec-value"]');
    valueManagerMaxEl = sheetRoot.querySelector('[data-value-manager="max"]');
    valueManagerProjectedEl = sheetRoot.querySelector('[data-value-manager="projected"]');
    valueManagerOpsEl = sheetRoot.querySelector('[data-value-manager="ops"]');

    const attrGrid = sheetRoot.querySelector(".lotm-overview-attrs");
    if(attrGrid){
      attrGrid.innerHTML = "";
      const portraitCard = document.createElement("section");
      portraitCard.className = "lotm-attr-card lotm-portrait-card";
      portraitCard.innerHTML =
        "<button type='button' class='lotm-portrait-trigger' data-action='pick-portrait' title='Insert portrait image'>" +
          "<span class='lotm-portrait-empty'>Portrait</span>" +
          "<img class='lotm-portrait-img' alt='Character portrait' hidden />" +
        "</button>" +
        "<button type='button' class='lotm-portrait-clear' data-action='clear-portrait' hidden aria-label='Clear portrait'>x</button>";
      attrGrid.appendChild(portraitCard);
      ATTR_KEYS.forEach(function(k){
        const card = document.createElement("section");
        card.className = "lotm-attr-card";
        card.setAttribute("title", ATTR_LABELS[k]);
        card.innerHTML =
          "<div class='lotm-attr-ticket lotm-attr-ticket-top'>" +
            "<strong class='lotm-attr-bonus' data-derived='attr_bonus_"+k+"'>+0</strong>" +
          "</div>" +
          "<div class='lotm-attr-main'>" +
            "<span class='lotm-attr-short'>" + ATTR_SHORT_LABELS[k] + "</span>" +
            "<strong class='lotm-attr-total' data-derived='attr_total_"+k+"'>0</strong>" +
          "</div>" +
          "<div class='lotm-attr-ticket lotm-attr-ticket-bottom lotm-attr-base-wrap'>" +
            "<input type='number' class='lotm-char-input lotm-attr-ticket-input lotm-attr-base-input' data-bind='attr_base."+k+"' data-type='number' />" +
          "</div>";
        attrGrid.appendChild(card);
      });
    }
  }

  function ensureSkillMeta(id){
    const k = token(id); if(!k) return null;
    if(!isObj(charState.skill_meta)) charState.skill_meta = {};
    if(!Object.prototype.hasOwnProperty.call(charState.skill_meta,k)){
      charState.skill_meta[k] = { proficiency:"untrained", intuition:(k === "dodge" ? 1 : 0), education:0, bonus:0 };
    }
    return charState.skill_meta[k];
  }

  function customSkillMap(){
    const out = {};
    const list = Array.isArray(charState.sheet.custom_skills) ? charState.sheet.custom_skills : [];
    list.forEach(function(e){
      if(!isObj(e)) return;
      const id = token(e.id || e.label || ""); if(!id) return;
      out[id] = { id:id, label:String(e.label || id), attr: ATTR_KEYS.indexOf(String(e.attr||"").toLowerCase()) >= 0 ? String(e.attr||"").toLowerCase() : "int" };
    });
    return out;
  }

  function ensureLanguageBucket(kind){
    const k = kind === "mysticism" ? "mysticism" : "common";
    if(!isObj(charState.sheet.languages)) charState.sheet.languages = { mysticism:[], common:[] };
    if(!Array.isArray(charState.sheet.languages[k])) charState.sheet.languages[k] = [];
    charState.sheet.languages[k] = charState.sheet.languages[k].map(normalizeLanguageEntry).filter(Boolean);
    charState.sheet.languages[k] = ensurePresetLanguages(k, charState.sheet.languages[k]);
    return charState.sheet.languages[k];
  }

  function renderLanguageList(kind, mount){
    if(!mount) return;
    const bucket = ensureLanguageBucket(kind);
    mount.innerHTML = "";
    if(!bucket.length){
      const empty = document.createElement("div");
      empty.className = "lotm-roll-empty";
      empty.textContent = kind === "mysticism" ? "No mysticism languages listed." : "No common languages listed.";
      mount.appendChild(empty);
      return;
    }
    bucket.forEach(function(entry){
      const row = document.createElement("div");
      row.className = "lotm-list-row lotm-language-row";
      row.setAttribute("data-language-kind", kind);
      row.setAttribute("data-language-id", entry.id);
      if(entry.preset){
        row.innerHTML =
          "<div class='lotm-language-name'>"+escapeHtml(entry.name)+"</div>" +
          "<select class='lotm-char-input' data-language-field='level'>" +
            PROF_ORDER.map(function(p){ return "<option value='"+p+"'"+(entry.level===p?" selected":"")+">"+PROF_LABEL[p]+"</option>"; }).join("") +
          "</select>" +
          "<span class='lotm-language-fixed'>Preset</span>";
      }else{
        row.innerHTML =
          "<input class='lotm-char-input' data-language-field='name' value='"+escapeHtml(entry.name)+"' placeholder='Language name' />" +
          "<select class='lotm-char-input' data-language-field='level'>" +
            PROF_ORDER.map(function(p){ return "<option value='"+p+"'"+(entry.level===p?" selected":"")+">"+PROF_LABEL[p]+"</option>"; }).join("") +
          "</select>" +
          "<button type='button' class='btn btn-ghost lotm-remove-language'>Remove</button>";
      }
      mount.appendChild(row);
    });
  }

  function renderLanguages(){
    renderLanguageList("mysticism", mysticismLangListEl);
    renderLanguageList("common", commonLangListEl);
  }

  function ensureConditionState(){
    if(!isObj(charState.conditions)) charState.conditions = { active:conditionFlagObj(), notes:"" };
    if(!isObj(charState.conditions.active)) charState.conditions.active = conditionFlagObj();
    charState.conditions.active = normalizeConditionFlags(charState.conditions.active);
    if(typeof charState.conditions.notes !== "string") charState.conditions.notes = String(charState.conditions.notes || "");
  }

  function renderConditions(){
    if(!conditionListEl) return;
    ensureConditionState();
    conditionListEl.innerHTML = "";
    CONDITION_DEFS.forEach(function(def){
      const checked = !!charState.conditions.active[def.id];
      const row = document.createElement("label");
      row.className = "lotm-condition-item" + (checked ? " active" : "");
      row.innerHTML =
        "<input type='checkbox' data-condition-id='" + escapeHtml(def.id) + "'" + (checked ? " checked" : "") + " />" +
        "<span class='lotm-condition-name'>" + escapeHtml(def.label) + "</span>" +
        "<small>" + escapeHtml(def.short || "") + "</small>";
      conditionListEl.appendChild(row);
    });
  }

  function specialRollChipHtml(entry, label, expr, kind){
    const classes = ["lotm-roll-chip", "lotm-roll-special"];
    if(kind === "check") classes.push("is-hit");
    if(kind === "effect") classes.push("is-effect");
    return "<button type='button' class='" + classes.join(" ") + "' data-special-id='" + escapeHtml(entry.id) + "' data-roll-kind='" + escapeHtml(kind) + "' data-roll-label='" + escapeHtml(label) + "' data-roll-expr='" + escapeHtml(expr) + "' title='" + escapeHtml(label + ": " + expr) + "'>" + escapeHtml(rollPreviewWithCondition(expr, charState, kind === "check")) + "</button>";
  }

  function renderSpecialActions(){
    if(!specialActionListEl) return;
    const groupOpen = {};
    specialActionListEl.querySelectorAll(".lotm-special-group[data-group-id]").forEach(function(node){
      const gid = node.getAttribute("data-group-id");
      if(gid) groupOpen[gid] = !!node.open;
    });
    specialActionListEl.innerHTML = "";
    const groups = { attack:[], cast:[], swift:[], free:[], move:[], "full-round":[], none:[] };
    const availableEntries = SPECIAL_ACTION_DEFS.filter(function(entry){
      return !specialActionUnavailableReason(entry, charState);
    });
    availableEntries.forEach(function(entry){
      const k = String(entry.action || "none").toLowerCase();
      if(!Object.prototype.hasOwnProperty.call(groups, k)) groups.none.push(entry);
      else groups[k].push(entry);
    });

    Object.keys(groups).forEach(function(groupId){
      const list = groups[groupId];
      if(!list.length) return;
      const sec = document.createElement("details");
      sec.className = "lotm-special-group";
      sec.setAttribute("data-group-id", groupId);
      sec.open = Object.prototype.hasOwnProperty.call(groupOpen, groupId) ? !!groupOpen[groupId] : true;
      sec.innerHTML = "<summary>" + (groupId === "none" ? "No Action" : actionLabel(groupId) + " Action") + "</summary><div class='lotm-special-table-wrap'><table class='lotm-special-table'><thead><tr><th>Name</th><th>Type</th><th>Range</th><th>Check Roll</th><th>Effect Roll</th><th>Notes</th></tr></thead><tbody></tbody></table></div>";
      const body = sec.querySelector("tbody");
      list.forEach(function(entry){
        const checkExpr = resolveSpecialActionExpr(entry, "checkExpr", charState);
        const effectExpr = resolveSpecialActionExpr(entry, "effectExpr", charState);
        const checkHtml = isUsableExpr(checkExpr) ? specialRollChipHtml(entry, "Check", checkExpr, "check") : noneHtml();
        const effectHtml = isUsableExpr(effectExpr) ? specialRollChipHtml(entry, "Effect", effectExpr, "effect") : noneHtml();
        const tr = document.createElement("tr");
        tr.className = "lotm-special-row";
        tr.setAttribute("data-special-id", String(entry.id || ""));
        tr.innerHTML =
          "<td class='lotm-special-name-cell'><button type='button' class='lotm-ability-open lotm-special-open' data-special-id='" + escapeHtml(entry.id) + "'>" + escapeHtml(entry.name) + "</button><div class='lotm-sheet-ability-meta'>Core Combat Action</div></td>" +
          "<td><span class='lotm-sheet-ability-tag'>" + escapeHtml(titleWords(entry.type || "Special")) + "</span></td>" +
          "<td class='lotm-ability-range-cell'>" + titleLinkedHtml(entry.range || "-") + "</td>" +
          "<td>" + checkHtml + "</td>" +
          "<td>" + effectHtml + "</td>" +
          "<td><div class='lotm-special-notes'>" + linkWikiText(entry.notes || "") + "</div></td>";
        body.appendChild(tr);
      });
      specialActionListEl.appendChild(sec);
    });

    if(specialActionSummaryEl){
      const seq = sequenceNumber(charState.meta.sequence);
      const active = activeConditionEffects(charState).activeLabels;
      specialActionSummaryEl.textContent = "Universal actions shown: " + String(availableEntries.length) + " | Sequence: " + String(seq) + (active.length ? " | Active conditions: " + active.join(", ") : "");
    }
    if(abilityDetailEl && abilityDetailEl.classList.contains("open")){
      const kind = String(abilityDetailEl.getAttribute("data-detail-kind") || "");
      if(kind === "special"){
        const detailId = abilityDetailEl.getAttribute("data-detail-id") || abilityDetailEl.getAttribute("data-special-id") || "";
        const current = findSpecialActionById(detailId);
        if(current && !specialActionUnavailableReason(current, charState)) openSpecialActionDetail(current);
        else closeAbilityDetail();
      }
    }
  }

  function renderSkills(){
    if(!skillBodyEl) return;
    const filter = token(skillSearchEl ? skillSearchEl.value : "");
    const custom = customSkillMap();
    const openState = {};
    skillBodyEl.querySelectorAll(".lotm-skill-group[data-skill-group]").forEach(function(node){
      const gid = node.getAttribute("data-skill-group");
      if(gid) openState[gid] = node.open;
    });
    skillBodyEl.innerHTML = "";

    function section(title, rows, groupId, allowEmpty, countOverride){
      if(!rows.length && !allowEmpty) return null;
      const sec = document.createElement("details");
      sec.className = "lotm-skill-group";
      sec.setAttribute("data-skill-group", groupId || token(title));
      sec.open = Object.prototype.hasOwnProperty.call(openState, groupId || token(title)) ? !!openState[groupId || token(title)] : true;
      sec.innerHTML = "<summary>"+title+" ("+String(Number.isFinite(Number(countOverride)) ? int(countOverride, rows.length) : rows.length)+")</summary><table class='lotm-skill-table'><thead><tr><th>Skill</th><th>Related Attr</th><th>Total Level</th><th>INT Slots</th><th>EDU Slots</th><th>Bonus</th><th>Total Mod</th><th>Roll</th></tr></thead><tbody></tbody></table>";
      const body = sec.querySelector("tbody");
      rows.forEach(function(r){ body.appendChild(r); });
      skillBodyEl.appendChild(sec);
      return sec;
    }

    function buildStandardSkillRow(id, label, attrId, extraClass){
      const m = ensureSkillMeta(id);
      const total = skillMod(m);
      const lvl = scoreToLevel(skillMetaScore(m));
      const ex = skillExpr(attrId, total);
      const prev = rollPreviewWithCondition(ex, charState, true);
      const tr = document.createElement("tr");
      tr.setAttribute("data-skill-id", id);
      tr.setAttribute("data-attr-id", attrId);
      if(extraClass) tr.className = extraClass;
      tr.innerHTML = "<td class='lotm-skill-name'>"+escapeHtml(label)+"</td><td>"+ATTR_LABELS[attrId]+" ("+String(int(charState.attr[attrId],0))+")</td><td><span class='lotm-skill-level'>"+escapeHtml(lvl.label)+"</span></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='intuition' value='"+String(int(m.intuition,0))+"' /></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='education' value='"+String(int(m.education,0))+"' /></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='bonus' value='"+String(int(m.bonus,0))+"' /></td>"+
        "<td class='lotm-skill-total'>"+String(total)+"</td><td><button type='button' class='btn btn-ghost lotm-roll-skill' data-roll-expr='"+escapeHtml(ex)+"'>Roll</button><div class='lotm-roll-preview'>"+escapeHtml(prev)+"</div></td>";
      return tr;
    }

    function buildLanguageSkillRow(skillId, label){
      const m = ensureSkillMeta(skillId);
      const total = skillMod(m);
      const lvl = scoreToLevel(skillMetaScore(m));
      const ex = skillExpr("edu", total);
      const prev = rollPreviewWithCondition(ex, charState, true);
      const tr = document.createElement("tr");
      tr.setAttribute("data-skill-id", skillId);
      tr.setAttribute("data-attr-id", "edu");
      tr.className = "lotm-language-skill-row";
      tr.innerHTML =
        "<td class='lotm-language-skill-cell'>" +
          "<div class='lotm-language-skill-head'><span class='lotm-skill-name'>"+escapeHtml(label)+"</span><span class='lotm-skill-level'>"+escapeHtml(lvl.label)+"</span></div>" +
          "<div class='lotm-language-skill-meta'>Related Attr: "+ATTR_LABELS.edu+" ("+String(int(charState.attr.edu,0))+") | Total Mod: "+String(total)+"</div>" +
          "<div class='lotm-language-skill-controls'>" +
            "<label>INT <input type='number' class='lotm-char-input lotm-small-number' data-skill-field='intuition' value='"+String(int(m.intuition,0))+"' /></label>" +
            "<label>EDU <input type='number' class='lotm-char-input lotm-small-number' data-skill-field='education' value='"+String(int(m.education,0))+"' /></label>" +
            "<label>Bonus <input type='number' class='lotm-char-input lotm-small-number' data-skill-field='bonus' value='"+String(int(m.bonus,0))+"' /></label>" +
            "<button type='button' class='btn btn-ghost lotm-roll-skill' data-roll-expr='"+escapeHtml(ex)+"'>Roll</button>" +
          "</div>" +
          "<div class='lotm-roll-preview'>"+escapeHtml(prev)+"</div>" +
        "</td>";
      return tr;
    }

    function buildLanguageRows(kind){
      const rows = [];
      ensureLanguageBucket(kind).forEach(function(entry){
        const name = String(entry && entry.name || "").trim();
        if(!name) return;
        if(filter && token(name + " " + kind + " language").indexOf(filter) < 0) return;
        const skillId = token("language_" + kind + "_" + String(entry.id || name));
        rows.push(buildLanguageSkillRow(skillId, name));
      });
      return rows;
    }

    function appendEducationLanguages(sec, commonRows, mysticismRows){
      if(!sec || (!commonRows.length && !mysticismRows.length)) return;
      const wrap = document.createElement("div");
      wrap.className = "lotm-edu-language-grid";

      function addColumn(title, rows){
        if(!rows.length) return;
        const col = document.createElement("section");
        col.className = "lotm-edu-language-col";
        col.innerHTML = "<h5>"+escapeHtml(title)+"</h5><div class='lotm-edu-language-table-wrap'><table class='lotm-skill-table'><thead><tr><th>Language Skills</th></tr></thead><tbody></tbody></table></div>";
        const body = col.querySelector("tbody");
        rows.forEach(function(r){ body.appendChild(r); });
        wrap.appendChild(col);
      }

      addColumn("Common Languages", commonRows);
      addColumn("Mysticism Languages", mysticismRows);
      sec.appendChild(wrap);
    }

    SKILL_GROUPS.forEach(function(g){
      const rows = [];
      g.skills.forEach(function(s){
        const id = s[0], label = s[1];
        if(filter && token(id+" "+label).indexOf(filter) < 0) return;
        rows.push(buildStandardSkillRow(id, label, g.attr));
      });
      if(g.id === "edu"){
        const commonRows = buildLanguageRows("common");
        const mysticismRows = buildLanguageRows("mysticism");
        const sec = section(g.title, rows, g.id, commonRows.length > 0 || mysticismRows.length > 0, rows.length + commonRows.length + mysticismRows.length);
        appendEducationLanguages(sec, commonRows, mysticismRows);
        return;
      }
      section(g.title, rows, g.id, false);
    });

    const customRows = [];
    Object.keys(custom).sort().forEach(function(id){
      const c = custom[id];
      if(filter && token(c.id+" "+c.label).indexOf(filter) < 0) return;
      const m = ensureSkillMeta(c.id);
      const total = skillMod(m);
      const lvl = scoreToLevel(skillMetaScore(m));
      const ex = skillExpr(c.attr, total);
      const prev = rollPreviewWithCondition(ex, charState, true);
      const tr = document.createElement("tr");
      tr.setAttribute("data-skill-id", c.id); tr.setAttribute("data-attr-id", c.attr); tr.setAttribute("data-custom-skill", "1");
      tr.innerHTML = "<td class='lotm-skill-name'>"+escapeHtml(c.label)+"</td><td><select class='lotm-char-input' data-skill-field='attr'>"+
        ATTR_KEYS.map(function(a){ return "<option value='"+a+"'"+(c.attr===a?" selected":"")+">"+ATTR_LABELS[a]+"</option>"; }).join("")+"</select></td>"+
        "<td><span class='lotm-skill-level'>"+escapeHtml(lvl.label)+"</span></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='intuition' value='"+String(int(m.intuition,0))+"' /></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='education' value='"+String(int(m.education,0))+"' /></td>"+
        "<td><input type='number' class='lotm-char-input' data-skill-field='bonus' value='"+String(int(m.bonus,0))+"' /></td>"+
        "<td class='lotm-skill-total'>"+String(total)+"</td><td><button type='button' class='btn btn-ghost lotm-roll-skill' data-roll-expr='"+escapeHtml(ex)+"'>Roll</button><button type='button' class='btn btn-ghost lotm-remove-skill'>Remove</button><div class='lotm-roll-preview'>"+escapeHtml(prev)+"</div></td>";
      customRows.push(tr);
    });
    section("Custom Skills", customRows, "custom");

    if(!skillBodyEl.children.length){ const e=document.createElement("div"); e.className="lotm-skill-empty"; e.textContent = "No matching skills."; skillBodyEl.appendChild(e); }
  }

  function renderActions(){
    if(!actionListEl) return;
    actionListEl.innerHTML = "";
    if(!Array.isArray(charState.actions) || !charState.actions.length){ const e=document.createElement("div"); e.className="lotm-roll-empty"; e.textContent="No custom actions yet."; actionListEl.appendChild(e); return; }
    charState.actions.forEach(function(a){
      const entry = sanitizeActionEntry(a);
      const ex = withVs(entry.expr, entry.opposed_by);
      const prev = ex ? rollPreview(ex, charState) : "No roll expression.";
      const row = document.createElement("div");
      row.className = "lotm-list-row lotm-action-row";
      row.setAttribute("data-action-id", entry.id || "");
      row.innerHTML =
        "<div class='lotm-action-grid'>" +
          "<input class='lotm-char-input' data-action-field='label' value='"+escapeHtml(entry.label)+"' placeholder='Action / ability name' />" +
          "<input class='lotm-char-input' data-action-field='type' value='"+escapeHtml(entry.type)+"' placeholder='Type (active/passive/toggle)' />" +
          "<select class='lotm-char-input' data-action-field='action'>" +
            ACTION_ORDER.map(function(v){ return "<option value='"+v+"'"+(entry.action===v?" selected":"")+">"+actionLabel(v)+"</option>"; }).join("") +
          "</select>" +
          "<input class='lotm-char-input lotm-action-expr' data-action-field='expr' value='"+escapeHtml(entry.expr)+"' placeholder='Roll expression' />" +
          "<input class='lotm-char-input' data-action-field='opposed_by' value='"+escapeHtml(entry.opposed_by)+"' placeholder='Opposed by (e.g. willpower_defense)' />" +
          "<input type='number' class='lotm-char-input lotm-small-number' data-action-field='spirituality_cost' value='"+String(int(entry.spirituality_cost,0))+"' placeholder='Spirituality cost' />" +
          "<input class='lotm-char-input' data-action-field='range' value='"+escapeHtml(entry.range)+"' placeholder='Range' />" +
          "<input class='lotm-char-input' data-action-field='target' value='"+escapeHtml(entry.target)+"' placeholder='Target' />" +
          "<input class='lotm-char-input' data-action-field='duration' value='"+escapeHtml(entry.duration)+"' placeholder='Duration' />" +
          "<textarea class='lotm-char-input' data-action-field='description' placeholder='Full description'>"+escapeHtml(entry.description)+"</textarea>" +
        "</div>" +
        "<div class='lotm-action-controls'>" +
          "<button type='button' class='btn btn-ghost lotm-roll-action' data-roll-expr='"+escapeHtml(ex)+"'>Roll "+escapeHtml(actionLabel(entry.action))+"</button>" +
          "<button type='button' class='btn btn-ghost lotm-remove-action'>Remove</button>" +
          "<div class='lotm-roll-preview'>"+escapeHtml(prev)+"</div>" +
        "</div>" +
        (entry.description ? "<details class='lotm-sheet-ability-text'><summary>Description</summary><p>"+linkWikiText(entry.description)+"</p></details>" : "");
      actionListEl.appendChild(row);
    });
  }

  function renderItems(){
    if(!itemListEl) return;
    itemListEl.innerHTML = "";
    if(!Array.isArray(charState.items) || !charState.items.length){ const e=document.createElement("div"); e.className="lotm-roll-empty"; e.textContent="No carried items listed."; itemListEl.appendChild(e); return; }
    charState.items.forEach(function(it){
      const row=document.createElement("div"); row.className="lotm-list-row lotm-item-row"; row.setAttribute("data-item-id", it.id || "");
      const hidden = itemUsesHiddenPocket(it);
      row.innerHTML = "<input class='lotm-char-input' data-item-field='storage' value='"+String(it.storage||"").replace(/'/g,"&#39;")+"' placeholder='Stored in' />"+
        "<input class='lotm-char-input' data-item-field='name' value='"+String(it.name||"").replace(/'/g,"&#39;")+"' placeholder='Item name' />"+
        "<input class='lotm-char-input' data-item-field='description' value='"+String(it.description||"").replace(/'/g,"&#39;")+"' placeholder='Description' />"+
        "<input type='number' class='lotm-char-input lotm-small-number' data-item-field='slots' value='"+String(int(it.slots,0))+"' placeholder='Slots' />"+
        "<label class='lotm-item-hidden'><input type='checkbox' data-item-field='hidden_pocket'"+(hidden ? " checked" : "")+" />Hidden Pocket</label>"+
        "<button type='button' class='btn btn-ghost lotm-remove-item'>Remove</button>";
      itemListEl.appendChild(row);
    });
  }

  function renderAdventure(){
    if(!adventureListEl) return;
    adventureListEl.innerHTML = "";
    if(!Array.isArray(charState.adventure_log) || !charState.adventure_log.length){ const e=document.createElement("div"); e.className="lotm-roll-empty"; e.textContent="No adventure log entries yet."; adventureListEl.appendChild(e); return; }
    charState.adventure_log.forEach(function(a){
      const row = document.createElement("div"); row.className = "lotm-list-row lotm-log-row"; row.setAttribute("data-adv-id", a.id || "");
      row.innerHTML = "<input class='lotm-char-input' data-adv-field='type' value='"+String(a.type||"").replace(/'/g,"&#39;")+"' placeholder='Type' />"+
        "<input class='lotm-char-input' data-adv-field='title' value='"+String(a.title||"").replace(/'/g,"&#39;")+"' placeholder='Title' />"+
        "<textarea class='lotm-char-input' data-adv-field='notes' placeholder='Notes'>"+String(a.notes||"").replace(/</g,"&lt;").replace(/>/g,"&gt;")+"</textarea>"+
        "<button type='button' class='btn btn-ghost lotm-remove-adv'>Remove</button>";
      adventureListEl.appendChild(row);
    });
  }

  function sanitizeAbility(a){
    const d = isObj(a && a.dice) ? a.dice : {};
    const c = isObj(a && a.cost) ? a.cost : {};
    const safeCost = {};
    Object.keys(c).forEach(function(k){ if(Number.isFinite(Number(c[k]))) safeCost[k] = int(c[k],0); });
    return {
      id: String((a && a.id) || ("ability_"+Math.random().toString(36).slice(2,8))),
      name: String((a && a.name) || "Ability"),
      action: String((a && a.action) || "none"),
      type: String((a && a.type) || "active"),
      opposed_by: String((a && a.opposed_by) || ""),
      roll: String((a && a.roll) || ""),
      sequence: int(a && a.sequence, 9),
      pathway: String((a && a.pathway) || ""),
      status: String((a && a.status) || ""),
      cost: safeCost,
      range: String((a && a.range) || ""),
      target: String((a && a.target) || ""),
      duration: String((a && a.duration) || ""),
      text: String((a && a.text) || ""),
      conditions: Array.isArray(a && a.conditions) ? a.conditions.map(function(v){ return String(v || ""); }) : [],
      tags: Array.isArray(a && a.tags) ? a.tags.map(function(v){ return String(v || ""); }) : [],
      damage_types: Array.isArray(a && a.damage_types) ? a.damage_types.map(function(v){ return String(v || ""); }) : [],
      scaling: Array.isArray(a && a.scaling) ? a.scaling : [],
      dice: { check_roll:String(d.check_roll||""), damage_roll:String(d.damage_roll||""), heal_roll:String(d.heal_roll||""), effect_roll:String(d.effect_roll||""), notes:String(d.notes||"") }
    };
  }

  function abilityRollEntries(a){
    const out = [];
    [["Check",a.dice.check_roll],["Damage",a.dice.damage_roll],["Heal",a.dice.heal_roll],["Effect",a.dice.effect_roll]].forEach(function(p){
      const e = withVs(p[1], a.opposed_by);
      if(!e || String(e).trim().toLowerCase() === "none") return;
      out.push({ label:p[0], expr:e });
    });
    if(String(a.roll||"").trim()){
      const ex = withVs(a.roll, a.opposed_by);
      if(ex && String(ex).trim().toLowerCase() !== "none") out.push({ label:"Roll", expr:ex });
    }
    return out;
  }

  function isUsableExpr(expr){
    const t = String(expr || "").trim().toLowerCase();
    return !!t && t !== "none";
  }

  function hitExprNoVs(expr){
    const t = String(expr || "").trim();
    if(!isUsableExpr(t)) return "";
    const vs = splitVs(t);
    return vs ? String(vs.expr || "").trim() : t;
  }

  function abilityHitExpr(a){
    const checkExpr = hitExprNoVs(a && a.dice ? a.dice.check_roll : "");
    if(isUsableExpr(checkExpr)) return checkExpr;
    const rollExpr = hitExprNoVs(a ? a.roll : "");
    return isUsableExpr(rollExpr) ? rollExpr : "";
  }

  function abilityEffectEntries(a){
    const out = [];
    [["Damage",a && a.dice ? a.dice.damage_roll : ""],["Heal",a && a.dice ? a.dice.heal_roll : ""],["Effect",a && a.dice ? a.dice.effect_roll : ""]].forEach(function(p){
      if(isUsableExpr(p[1])) out.push({ label:p[0], expr:String(p[1]).trim() });
    });
    return out;
  }

  function abilityRollChipHtml(ability, label, expr, extraClass){
    const classes = ["lotm-roll-chip", "lotm-roll-ability"];
    if(extraClass) classes.push(extraClass);
    return "<button type='button' class='"+classes.join(" ")+"' data-ability-id='"+escapeHtml(ability.id)+"' data-roll-label='"+escapeHtml(label)+"' data-roll-expr='"+escapeHtml(expr)+"' title='"+escapeHtml(label)+": "+escapeHtml(expr)+"'>"+escapeHtml(rollPreviewWithCondition(expr, charState, isCheckLikeLabel(label)))+"</button>";
  }

  function abilityEffectCellHtml(a){
    const entries = abilityEffectEntries(a);
    if(!entries.length) return "<span class='lotm-ability-none'>None</span>";
    return "<div class='lotm-roll-chip-list'>" + entries.map(function(entry){
      return abilityRollChipHtml(a, entry.label, entry.expr, "is-effect");
    }).join("") + "</div>";
  }

  function noneHtml(){ return "<span class='lotm-ability-none'>None</span>"; }
  function scalarLinkedHtml(value, makeTitle){
    const text = String(value || "").trim();
    if(!text || text.toLowerCase() === "none") return noneHtml();
    return makeTitle ? titleLinkedHtml(text) : linkWikiText(text);
  }

  function rollExprReadableHtml(expr){
    const t = String(expr || "").trim();
    if(!isUsableExpr(t)) return noneHtml();
    return "<div class='lotm-inline-roll-expr'><code>"+escapeHtml(t)+"</code><div class='lotm-roll-preview'>"+escapeHtml(rollPreview(t, charState))+"</div></div>";
  }

  function arrayLinkedHtml(values){
    if(!Array.isArray(values) || !values.length) return noneHtml();
    return titleLinkedHtml(values.join(", "));
  }

  function scalingReadableHtml(scaling){
    if(!Array.isArray(scaling) || !scaling.length) return noneHtml();
    return "<ul class='lotm-yaml-scaling'>" + scaling.map(function(item){
      const when = scalarLinkedHtml(item && item.when ? item.when : "Condition", true);
      const changesObj = isObj(item && item.changes) ? item.changes : {};
      const changeKeys = Object.keys(changesObj);
      const changes = changeKeys.length
        ? changeKeys.map(function(k){
            const value = changesObj[k];
            if(value === null || value === undefined) return escapeHtml(titleWords(k)) + ": None";
            if(typeof value === "number" || typeof value === "boolean") return escapeHtml(titleWords(k)) + ": " + escapeHtml(String(value));
            return escapeHtml(titleWords(k)) + ": " + linkWikiText(String(value));
          }).join("; ")
        : "No explicit change fields.";
      return "<li><strong>When:</strong> " + when + "<br /><strong>Changes:</strong> " + changes + "</li>";
    }).join("") + "</ul>";
  }

  function interpretedRow(label, html){
    return "<div class='lotm-yaml-row'><dt>" + escapeHtml(label) + "</dt><dd>" + html + "</dd></div>";
  }

  function abilityInterpretedHtml(a){
    const rows = [];
    rows.push(interpretedRow("ID", escapeHtml(String(a.id || "-"))));
    rows.push(interpretedRow("Name", escapeHtml(String(a.name || "-"))));
    rows.push(interpretedRow("Pathway", titleLinkedHtml(String(a.pathway || "-"))));
    rows.push(interpretedRow("Sequence", escapeHtml(String(int(a.sequence, 0)))));
    rows.push(interpretedRow("Status", scalarLinkedHtml(a.status, true)));
    rows.push(interpretedRow("Type", scalarLinkedHtml(a.type, true)));
    rows.push(interpretedRow("Action", scalarLinkedHtml(actionLabel(a.action), true)));
    rows.push(interpretedRow("Cost", escapeHtml(formatCost(a.cost))));
    rows.push(interpretedRow("Opposed By", scalarLinkedHtml(String(a.opposed_by || "none").replace(/-/g, " "), true)));
    rows.push(interpretedRow("Range", scalarLinkedHtml(a.range, true)));
    rows.push(interpretedRow("Target", scalarLinkedHtml(a.target, true)));
    rows.push(interpretedRow("Duration", scalarLinkedHtml(a.duration, true)));
    rows.push(interpretedRow("Roll", rollExprReadableHtml(a.roll)));
    rows.push(interpretedRow("Check Roll", rollExprReadableHtml(a.dice && a.dice.check_roll)));
    rows.push(interpretedRow("Damage Roll", rollExprReadableHtml(a.dice && a.dice.damage_roll)));
    rows.push(interpretedRow("Heal Roll", rollExprReadableHtml(a.dice && a.dice.heal_roll)));
    rows.push(interpretedRow("Effect Roll", rollExprReadableHtml(a.dice && a.dice.effect_roll)));
    rows.push(interpretedRow("Dice Notes", scalarLinkedHtml(a.dice && a.dice.notes, false)));
    rows.push(interpretedRow("Conditions", arrayLinkedHtml(a.conditions)));
    rows.push(interpretedRow("Damage Types", arrayLinkedHtml(a.damage_types)));
    rows.push(interpretedRow("Tags", arrayLinkedHtml(a.tags)));
    rows.push(interpretedRow("Scaling", scalingReadableHtml(a.scaling)));
    rows.push(interpretedRow("Source Text", scalarLinkedHtml(a.text, false)));
    return "<dl class='lotm-yaml-readable'>" + rows.join("") + "</dl>";
  }

  function closeAbilityDetail(){
    if(!abilityDetailEl) return false;
    const wasOpen = abilityDetailEl.classList.contains("open") || document.body.classList.contains("lotm-ability-detail-open");
    abilityDetailEl.classList.remove("open");
    abilityDetailEl.setAttribute("aria-hidden", "true");
    abilityDetailEl.removeAttribute("data-detail-kind");
    abilityDetailEl.removeAttribute("data-detail-id");
    abilityDetailEl.removeAttribute("data-ability-id");
    abilityDetailEl.removeAttribute("data-special-id");
    document.body.classList.remove("lotm-ability-detail-open");
    return wasOpen;
  }

  function openAbilityDetail(a){
    if(!abilityDetailEl || !abilityDetailBodyEl || !isObj(a)) return;
    const hitExpr = abilityHitExpr(a);
    const effectEntries = abilityEffectEntries(a);
    const effectHtml = effectEntries.length
      ? "<div class='lotm-roll-chip-list'>" + effectEntries.map(function(entry){ return abilityRollChipHtml(a, entry.label, entry.expr, "is-effect"); }).join("") + "</div>"
      : "<span class='lotm-ability-none'>None</span>";

    if(abilityDetailTitleEl) abilityDetailTitleEl.textContent = String(a.name || "Ability Details");
    abilityDetailBodyEl.innerHTML =
      "<div class='lotm-sheet-ability-meta'>Seq " + String(a.sequence) + " | " + escapeHtml(String(a.pathway || "-")) + "</div>" +
      abilityMetaHtml(a) +
      "<div class='lotm-ability-detail-roll-grid'>" +
        "<div><h5>Hit / DC</h5>" + (hitExpr ? abilityRollChipHtml(a, "Hit/DC", hitExpr, "is-hit") : "<span class='lotm-ability-none'>None</span>") + "</div>" +
        "<div><h5>Effect Roll</h5>" + effectHtml + "</div>" +
      "</div>" +
      (a.text ? "<section class='lotm-ability-detail-section'><h5>Description</h5><div class='lotm-ability-detail-description'>" + linkWikiText(a.text) + "</div></section>" : "");

    abilityDetailEl.classList.add("open");
    abilityDetailEl.setAttribute("aria-hidden", "false");
    abilityDetailEl.setAttribute("data-detail-kind", "ability");
    abilityDetailEl.setAttribute("data-detail-id", String(a.id || ""));
    abilityDetailEl.setAttribute("data-ability-id", String(a.id || ""));
    abilityDetailEl.removeAttribute("data-special-id");
    document.body.classList.add("lotm-ability-detail-open");
  }

  function abilityMetaHtml(a){
    const chunks = [];
    chunks.push("<span><strong>Type:</strong> "+escapeHtml(titleWords(a.type || "-"))+"</span>");
    chunks.push("<span><strong>Action:</strong> "+escapeHtml(actionLabel(a.action || "none"))+"</span>");
    chunks.push("<span><strong>Cost:</strong> "+escapeHtml(formatCost(a.cost))+"</span>");
    chunks.push("<span><strong>Opposed by:</strong> "+titleLinkedHtml(String(a.opposed_by || "none").replace(/-/g, " "))+"</span>");
    chunks.push("<span><strong>Range:</strong> "+titleLinkedHtml(a.range || "-")+"</span>");
    chunks.push("<span><strong>Target:</strong> "+titleLinkedHtml(a.target || "-")+"</span>");
    chunks.push("<span><strong>Duration:</strong> "+titleLinkedHtml(a.duration || "-")+"</span>");
    if(a.status) chunks.push("<span><strong>Status:</strong> "+titleLinkedHtml(a.status)+"</span>");
    if(Array.isArray(a.tags) && a.tags.length) chunks.push("<span><strong>Tags:</strong> "+titleLinkedHtml(a.tags.join(", "))+"</span>");
    if(Array.isArray(a.conditions) && a.conditions.length) chunks.push("<span><strong>Conditions:</strong> "+titleLinkedHtml(a.conditions.join(", "))+"</span>");
    if(Array.isArray(a.damage_types) && a.damage_types.length) chunks.push("<span><strong>Damage Types:</strong> "+titleLinkedHtml(a.damage_types.join(", "))+"</span>");
    if(a.dice && a.dice.notes) chunks.push("<span class='wide'><strong>Dice Notes:</strong> "+linkWikiText(a.dice.notes)+"</span>");
    return "<div class='lotm-ability-meta-grid'>" + chunks.join("") + "</div>";
  }

  function specialActionMetaHtml(a){
    const chunks = [];
    chunks.push("<span><strong>Type:</strong> " + escapeHtml(titleWords(a.type || "Special")) + "</span>");
    chunks.push("<span><strong>Action:</strong> " + escapeHtml(actionLabel(a.action || "none")) + "</span>");
    chunks.push("<span><strong>Range:</strong> " + titleLinkedHtml(a.range || "-") + "</span>");
    if(Number.isFinite(Number(a.requiresDexAtLeast))) chunks.push("<span><strong>Requirement:</strong> DEX " + escapeHtml(String(int(a.requiresDexAtLeast, 0))) + "+</span>");
    if(Number.isFinite(Number(a.maxSequence))) chunks.push("<span><strong>Requirement:</strong> Sequence " + escapeHtml(String(int(a.maxSequence, 9))) + " or lower</span>");
    if(Number.isFinite(Number(a.minSequence))) chunks.push("<span><strong>Requirement:</strong> Sequence " + escapeHtml(String(int(a.minSequence, 0))) + " or higher</span>");
    if(a.notes) chunks.push("<span class='wide'><strong>Rules Notes:</strong> " + linkWikiText(a.notes) + "</span>");
    return "<div class='lotm-ability-meta-grid'>" + chunks.join("") + "</div>";
  }

  function openSpecialActionDetail(a){
    if(!abilityDetailEl || !abilityDetailBodyEl || !isObj(a)) return;
    const checkExpr = resolveSpecialActionExpr(a, "checkExpr", charState);
    const effectExpr = resolveSpecialActionExpr(a, "effectExpr", charState);
    const checkCount = resolveSpecialActionRollCount(a, "check", charState);
    const effectCount = resolveSpecialActionRollCount(a, "effect", charState);
    const checkHtml = isUsableExpr(checkExpr)
      ? specialRollChipHtml(a, "Check", checkExpr, "check") + (checkCount > 1 ? "<div class='lotm-roll-preview'>Rolls: " + String(checkCount) + "x</div>" : "")
      : "<span class='lotm-ability-none'>None</span>";
    const effectHtml = isUsableExpr(effectExpr)
      ? specialRollChipHtml(a, "Effect", effectExpr, "effect") + (effectCount > 1 ? "<div class='lotm-roll-preview'>Rolls: " + String(effectCount) + "x</div>" : "")
      : "<span class='lotm-ability-none'>None</span>";

    if(abilityDetailTitleEl) abilityDetailTitleEl.textContent = String(a.name || "Special Action");
    abilityDetailBodyEl.innerHTML =
      "<div class='lotm-sheet-ability-meta'>Core Rule | Universal Combat Action</div>" +
      specialActionMetaHtml(a) +
      "<div class='lotm-ability-detail-roll-grid'>" +
        "<div><h5>Check Roll</h5>" + checkHtml + "</div>" +
        "<div><h5>Effect Roll</h5>" + effectHtml + "</div>" +
      "</div>" +
      (a.description ? "<section class='lotm-ability-detail-section'><h5>Rulebook Description</h5><div class='lotm-ability-detail-description'>" + richTextHtml(a.description) + "</div></section>" : "");

    abilityDetailEl.classList.add("open");
    abilityDetailEl.setAttribute("aria-hidden", "false");
    abilityDetailEl.setAttribute("data-detail-kind", "special");
    abilityDetailEl.setAttribute("data-detail-id", String(a.id || ""));
    abilityDetailEl.setAttribute("data-special-id", String(a.id || ""));
    abilityDetailEl.removeAttribute("data-ability-id");
    document.body.classList.add("lotm-ability-detail-open");
  }

  function renderAbilities(){
    if(!abilityListEl) return;
    const list = Array.isArray(charState.abilities.imported) ? charState.abilities.imported : [];
    const groupOpen = {};
    abilityListEl.querySelectorAll(".lotm-ability-group[data-group-id]").forEach(function(node){
      const gid = node.getAttribute("data-group-id");
      if(gid) groupOpen[gid] = !!node.open;
    });
    abilityListEl.innerHTML = "";
    if(!list.length){
      const e = document.createElement("div");
      e.className = "lotm-roll-empty";
      e.textContent = "No Beyonder abilities loaded. Set Pathway and Sequence in Basic Info.";
      abilityListEl.appendChild(e);
      if(abilitySummaryEl) abilitySummaryEl.textContent = "Imported abilities: 0";
      if(abilityDetailEl && String(abilityDetailEl.getAttribute("data-detail-kind") || "") === "ability") closeAbilityDetail();
      return;
    }

    const groups = { attack:[], cast:[], swift:[], free:[], move:[], "full-round":[], none:[] };
    list.forEach(function(a){ const k = String(a.action||"none").toLowerCase(); if(!Object.prototype.hasOwnProperty.call(groups,k)) groups.none.push(a); else groups[k].push(a); });

    Object.keys(groups).forEach(function(k){
      if(!groups[k].length) return;
      const sec = document.createElement("details");
      sec.className = "lotm-ability-group";
      sec.setAttribute("data-group-id", k);
      sec.open = Object.prototype.hasOwnProperty.call(groupOpen, k) ? !!groupOpen[k] : true;
      sec.innerHTML = "<summary>"+(k==="none"?"No Action":actionLabel(k)+" Action")+"</summary><div class='lotm-ability-table-wrap'><table class='lotm-ability-table'><colgroup><col class='lotm-col-name' /><col class='lotm-col-type' /><col class='lotm-col-range' /><col class='lotm-col-hit' /><col class='lotm-col-effect' /><col class='lotm-col-sc' /></colgroup><thead><tr><th>Name</th><th>Type</th><th>Range</th><th>Hit / DC</th><th>Effect Roll</th><th>SC</th></tr></thead><tbody></tbody></table></div>";
      const tbody = sec.querySelector("tbody");
      groups[k].slice().sort(function(a,b){ return int(b.sequence,0)-int(a.sequence,0); }).forEach(function(a){
        const hitExpr = abilityHitExpr(a);
        const tr = document.createElement("tr");
        tr.className = "lotm-ability-row";
        tr.setAttribute("data-ability-id", String(a.id || ""));
        tr.innerHTML =
          "<td class='lotm-ability-name-cell'><button type='button' class='lotm-ability-open' data-ability-id='"+escapeHtml(a.id)+"'>"+escapeHtml(a.name)+"</button><div class='lotm-sheet-ability-meta'>Seq "+String(a.sequence)+" | "+escapeHtml(String(a.pathway || "-"))+"</div></td>" +
          "<td><span class='lotm-sheet-ability-tag'>"+escapeHtml(titleWords(a.type || "-"))+"</span></td>" +
          "<td class='lotm-ability-range-cell'>"+titleLinkedHtml(a.range || "-")+"</td>" +
          "<td>" + (hitExpr ? abilityRollChipHtml(a, "Hit/DC", hitExpr, "is-hit") : "<span class='lotm-ability-none'>None</span>") + "</td>" +
          "<td>" + abilityEffectCellHtml(a) + "</td>" +
          "<td class='lotm-ability-sc'>" + (abilitySpiritualityCost(a) > 0 ? String(abilitySpiritualityCost(a)) : "-") + "</td>";
        tbody.appendChild(tr);
      });
      abilityListEl.appendChild(sec);
    });

    if(abilitySummaryEl) abilitySummaryEl.textContent = "Imported abilities: "+String(list.length)+" | Pathway: "+String(charState.meta.pathway||"-")+" | Sequence: "+String(charState.meta.sequence||"-");
    if(abilityDetailEl && abilityDetailEl.classList.contains("open")){
      const kind = String(abilityDetailEl.getAttribute("data-detail-kind") || "");
      if(kind === "ability"){
        const detailId = abilityDetailEl.getAttribute("data-detail-id") || abilityDetailEl.getAttribute("data-ability-id") || "";
        const current = findAbilityById(detailId);
        if(current) openAbilityDetail(current);
        else closeAbilityDetail();
      }
    }
  }

  function renderAll(){
    applyBoundInputs();
    syncMetaSelectors();
    renderConditions();
    renderLanguages();
    renderSkills();
    renderAbilities();
    renderSpecialActions();
    renderActions();
    renderItems();
    renderAdventure();
    validateAndRender();
    renderRollLog();
  }

  function parseAttrName(raw){
    const t = String(raw||"").toLowerCase();
    if(t.indexOf("strength")>=0 || t.indexOf("str")>=0) return "str";
    if(t.indexOf("agility")>=0 || t.indexOf("dex")>=0) return "dex";
    if(t.indexOf("constitution")>=0 || t.indexOf("con")>=0) return "con";
    if(t.indexOf("willpower")>=0 || t.indexOf("wil")>=0) return "wil";
    if(t.indexOf("intuition")>=0 || t.indexOf("int")>=0 || t.indexOf("inspiration")>=0) return "int";
    if(t.indexOf("education")>=0 || t.indexOf("edu")>=0) return "edu";
    if(t.indexOf("charisma")>=0 || t.indexOf("cha")>=0) return "cha";
    if(t.indexOf("luck")>=0 || t.indexOf("luk")>=0) return "luk";
    return "";
  }

  function pathwaySlug(v){ return String(v||"").trim().toLowerCase().replace(/\s+/g,"-"); }

  function loadCompendium(){
    if(compendium) return Promise.resolve(compendium);
    if(compendiumPromise) return compendiumPromise;
    compendiumPromise = fetch(COMPENDIUM_URL, { cache:"no-store" }).then(function(r){ if(!r.ok) throw new Error("Compendium request failed: "+String(r.status)); return r.json(); }).then(function(data){ if(!isObj(data) || !Array.isArray(data.sequences)) throw new Error("Invalid compendium format."); compendium = data; return data; }).finally(function(){ compendiumPromise = null; });
    return compendiumPromise;
  }

  function fillPathwayOptions(data){
    if(!pathwaySelectEl) return;
    pathwaySelectEl.innerHTML = "<option value=''>Select pathway</option>";
    const list = Array.isArray(data.pathways) ? data.pathways.slice().sort(function(a,b){ return String(a.canonical_pathway||a.slug||"").localeCompare(String(b.canonical_pathway||b.slug||"")); }) : [];
    list.forEach(function(p){ const o=document.createElement("option"); o.value = pathwaySlug(p.slug||""); o.textContent = String(p.canonical_pathway || p.slug || ""); pathwaySelectEl.appendChild(o); });
    syncMetaSelectors();
  }

  function syncMetaSelectors(){
    if(sequenceSelectEl) sequenceSelectEl.value = String(sequenceNumber(charState.meta.sequence));
    if(pathwaySelectEl){
      const wanted = pathwaySlug(charState.meta.pathway || "");
      const hasWanted = Array.from(pathwaySelectEl.options).some(function(opt){ return String(opt.value || "") === wanted; });
      pathwaySelectEl.value = hasWanted ? wanted : "";
    }
  }

  function importAbilities(data, pathway, seq, opts){
    const options = isObj(opts) ? opts : {};
    const records = data.sequences.filter(function(s){ return pathwaySlug(s.pathway) === pathwaySlug(pathway) && Number.isFinite(Number(s.sequence)) && int(s.sequence,99) >= seq; }).sort(function(a,b){ return int(b.sequence,0)-int(a.sequence,0); });
    const imported = [];
    const bonus = attrObj();
    records.forEach(function(r){
      if(isObj(r.attribute_gain) && Array.isArray(r.attribute_gain.attributes)) r.attribute_gain.attributes.forEach(function(g){ const id = parseAttrName(g.name); if(id) bonus[id] += int(g.delta,0); });
      if(Array.isArray(r.abilities)) r.abilities.forEach(function(a){ imported.push(sanitizeAbility(Object.assign({}, a, { sequence:r.sequence, pathway:r.pathway, status:a.status || r.status || "" }))); });
    });
    charState.meta.pathway = pathwaySlug(pathway);
    charState.meta.sequence = String(seq);
    charState.abilities.imported = imported;
    charState.abilities.last_import = { pathway:charState.meta.pathway, sequence:charState.meta.sequence };
    charState.beyonder.attr_bonus = bonus;
    renderAll();
    scheduleSave();
    if(!options.silent) setStatus("Imported "+String(imported.length)+" abilities from pathway "+charState.meta.pathway+" (sequence "+charState.meta.sequence+" and above).", false);
  }

  function autoRefreshImportedAbilities(opts){
    const options = isObj(opts) ? opts : {};
    const seq = sequenceNumber(sequenceSelectEl ? sequenceSelectEl.value : charState.meta.sequence);
    const pathway = pathwaySlug(pathwaySelectEl ? pathwaySelectEl.value : charState.meta.pathway);
    charState.meta.sequence = String(seq);
    charState.meta.pathway = pathway;
    syncMetaSelectors();
    if(!pathway){
      charState.abilities.imported = [];
      charState.abilities.last_import = { pathway:"", sequence:String(seq) };
      charState.beyonder.attr_bonus = attrObj();
      renderAll();
      scheduleSave();
      if(!options.silent) setStatus("Select a pathway in Basic Info to load Beyonder abilities.", true);
      return Promise.resolve();
    }
    return loadCompendium()
      .then(function(data){ importAbilities(data, pathway, seq, { silent:!!options.silent }); })
      .catch(function(err){
        if(!options.silent) setStatus("Ability auto-update failed: " + String(err.message || err), true);
      });
  }

  function exportJson(){
    recomputeChar(charState);
    charState = saveChar(charState);
    const payload = JSON.stringify(charState, null, 2);
    const blob = new Blob([payload], { type:"application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url; a.download = "lotm-character.json";
    document.body.appendChild(a); a.click(); a.remove();
    window.setTimeout(function(){ URL.revokeObjectURL(url); }, 1500);
    setStatus("Exported lotm-character.json", false);
  }

  function importFromText(text){
    let parsed;
    try{ parsed = JSON.parse(text); }catch(e){ setStatus("Import failed: invalid JSON.", true); return; }
    if(!hasRequiredSections(parsed)){ setStatus("Import failed: missing required sections.", true); return; }
    charState = saveChar(parsed);
    initiativeLastResult = "-";
    renderAll();
    autoRefreshImportedAbilities({ silent:true });
    setStatus("Import complete.", false);
  }

  function importFromFile(file){
    if(!file) return;
    if(typeof file.text === "function"){
      file.text().then(importFromText).catch(function(){ setStatus("Import failed: could not read file.", true); });
      return;
    }
    const r = new FileReader();
    r.onload = function(){ importFromText(String(r.result || "")); };
    r.onerror = function(){ setStatus("Import failed: could not read file.", true); };
    r.readAsText(file);
  }

  function parseBindInput(target){
    const isNum = target.getAttribute("data-type") === "number" || target.type === "number";
    return isNum ? int(target.value,0) : target.value;
  }

  function findAbilityById(id){
    const list = Array.isArray(charState.abilities.imported) ? charState.abilities.imported : [];
    let i; for(i=0;i<list.length;i+=1) if(String(list[i].id) === String(id)) return list[i];
    return null;
  }

  function skillExpr(attrId, m){
    const a = "@attr."+String(attrId||"int"), mod = int(m,0);
    if(mod > 0) return "1d20 + " + a + " + " + String(mod);
    if(mod < 0) return "1d20 + " + a + " - " + String(Math.abs(mod));
    return "1d20 + " + a;
  }

  function addCustomSkill(tk, attr){
    const id = token(tk);
    if(!id){ setStatus("Enter a valid skill token.", true); return; }
    if(Object.prototype.hasOwnProperty.call(BUILTIN_SKILLS,id)){ setStatus("That is already a built-in skill.", true); return; }
    if(!Array.isArray(charState.sheet.custom_skills)) charState.sheet.custom_skills = [];
    if(charState.sheet.custom_skills.some(function(e){ return token(e.id) === id; })){ setStatus("Custom skill already exists.", true); return; }
    charState.sheet.custom_skills.push({ id:id, label:id, attr: ATTR_KEYS.indexOf(String(attr||"").toLowerCase()) >= 0 ? String(attr||"").toLowerCase() : "int" });
    ensureSkillMeta(id);
    renderSkills();
    renderAbilities();
    renderSpecialActions();
    renderActions();
    attachDocAbilityButtons(document);
    validateAndRender();
    scheduleSave();
    setStatus("Custom skill added.", false);
  }

  function initInteractions(){
    if(!sheetRoot) return;

    sheetToggleBtn.addEventListener("click", function(){ setSheetOpen(!document.body.classList.contains("lotm-sheet-open")); });

    sheetRoot.addEventListener("input", function(ev){
      const t = ev.target;
      if(!(t instanceof HTMLElement)) return;
      if(t.hasAttribute("data-hp-tool")){
        refreshHpProjection();
        return;
      }
      if(t.hasAttribute("data-value-tool")){
        refreshValueProjection();
        return;
      }
      if(t.hasAttribute("data-value-manager-field")){
        const info = valueManagerTargetInfo(valueManagerResourceKey);
        if(!info) return;
        const field = String(t.getAttribute("data-value-manager-field") || "");
        if(field === "current"){
          info.setCurrent(int(t.value, 0));
        }else if(field === "temp"){
          info.setTemp(Math.max(0, int(t.value, 0)));
        }else{
          return;
        }
        validateAndRender();
        scheduleSave();
        return;
      }
      const bind = t.getAttribute("data-bind");
      if(bind){
        setPath(charState, bind, parseBindInput(t));
        if(bind === "meta.sequence"){
          const s = sequenceNumber(charState.meta.sequence);
          charState.meta.sequence = String(s);
          if(sequenceSelectEl) sequenceSelectEl.value = String(s);
          renderSpecialActions();
        }
        if(bind === "meta.pathway" && pathwaySelectEl) pathwaySelectEl.value = pathwaySlug(charState.meta.pathway || "");
        if(bind.indexOf("attr_base.") === 0 || bind === "mod.bonus"){
          renderSkills();
          renderAbilities();
          renderSpecialActions();
          renderActions();
          attachDocAbilityButtons(document);
        }
        validateAndRender();
        scheduleSave();
      }
    });

    sheetRoot.addEventListener("click", function(ev){
      const t = ev.target;
      if(!(t instanceof HTMLElement)) return;

      const actionBtn = t.closest("[data-action]");
      if(actionBtn){
        const action = String(actionBtn.getAttribute("data-action") || "");
        if(action === "pick-portrait"){
          if(portraitFileEl){
            portraitFileEl.value = "";
            portraitFileEl.click();
          }
          return;
        }
        if(action === "clear-portrait"){
          charState.meta.portrait = "";
          renderPortraitCard();
          scheduleSave();
          setStatus("Portrait cleared.", false);
          return;
        }
        if(action === "roll-initiative"){
          const expr = "1d20 + @attr.dex";
          const rs = roll(expr, charState);
          initiativeLastResult = String(int(rs.total, 0));
          logRoll(rs, expr, "Initiative", "Initiative");
          setStatus("Initiative rolled: " + initiativeLastResult + ".", false);
          validateAndRender();
          return;
        }
        if(action === "open-hp-manager"){ setValueManagerOpen(false); setHpManagerOpen(true); return; }
        if(action === "close-hp-manager"){ setHpManagerOpen(false); return; }
        if(action === "open-value-manager"){
          setHpManagerOpen(false);
          setValueManagerOpen(true, actionBtn.getAttribute("data-resource") || "");
          return;
        }
        if(action === "close-value-manager"){ setValueManagerOpen(false); return; }
        if(action === "hp-heal"){ applyHpHealing(); return; }
        if(action === "hp-damage"){ applyHpDamage(); return; }
        if(action === "hp-heal-quick"){
          applyHpHealing(Math.max(0, int(hpQuickValueInputEl ? hpQuickValueInputEl.value : 0, 0)));
          return;
        }
        if(action === "hp-damage-quick"){
          applyHpDamage(Math.max(0, int(hpQuickValueInputEl ? hpQuickValueInputEl.value : 0, 0)));
          return;
        }
        if(action === "resource-inc-quick"){
          const key = String(actionBtn.getAttribute("data-resource") || "").toLowerCase();
          const quickInput = sheetRoot.querySelector('[data-resource-tool="' + key + '-quick"]');
          applyVitalResourceIncrease(key, Math.max(0, int(quickInput ? quickInput.value : 0, 0)));
          return;
        }
        if(action === "resource-dec-quick"){
          const key = String(actionBtn.getAttribute("data-resource") || "").toLowerCase();
          const quickInput = sheetRoot.querySelector('[data-resource-tool="' + key + '-quick"]');
          applyVitalResourceDecrease(key, Math.max(0, int(quickInput ? quickInput.value : 0, 0)));
          return;
        }
        if(action === "resource-inc"){
          applyValueManagerIncrease(Math.max(0, int(valueManagerIncInputEl ? valueManagerIncInputEl.value : 0, 0)));
          if(valueManagerIncInputEl) valueManagerIncInputEl.value = "0";
          refreshValueProjection();
          return;
        }
        if(action === "resource-dec"){
          applyValueManagerDecrease(Math.max(0, int(valueManagerDecInputEl ? valueManagerDecInputEl.value : 0, 0)));
          if(valueManagerDecInputEl) valueManagerDecInputEl.value = "0";
          refreshValueProjection();
          return;
        }
      }

      if(t.classList.contains("lotm-tab")){ setTab(t.getAttribute("data-tab") || "overview"); return; }
      if(t.classList.contains("lotm-sheet-export")){ exportJson(); return; }
      if(t.classList.contains("lotm-sheet-import")){ if(importFileEl){ importFileEl.value = ""; importFileEl.click(); } return; }
      if(t.classList.contains("lotm-sheet-reset")){ if(!window.confirm("Reset character data to defaults?")) return; charState = resetChar(); initiativeLastResult = "-"; renderAll(); setStatus("Character reset.", false); return; }
      const detailOpenBtn = t.closest(".lotm-ability-open");
      if(detailOpenBtn){
        if(detailOpenBtn.classList.contains("lotm-special-open")){
          const sp = findSpecialActionById(detailOpenBtn.getAttribute("data-special-id") || "");
          if(sp) openSpecialActionDetail(sp);
        }else{
          const ab = findAbilityById(detailOpenBtn.getAttribute("data-ability-id") || "");
          if(ab) openAbilityDetail(ab);
        }
        return;
      }
      if(t.closest(".lotm-ability-detail-close")){
        closeAbilityDetail();
        return;
      }

      if(t.classList.contains("lotm-roll-clear")){ rollLog = []; renderRollLog(); setStatus("Roll log cleared.", false); return; }

      if(t.classList.contains("lotm-add-custom-skill")){
        const tokenInput = sheetRoot.querySelector(".lotm-custom-token");
        const attrInput = sheetRoot.querySelector(".lotm-custom-attr");
        addCustomSkill(tokenInput ? tokenInput.value : "", attrInput ? attrInput.value : "int");
        if(tokenInput) tokenInput.value = "";
        return;
      }

      if(t.classList.contains("lotm-add-language")){
        const kind = t.getAttribute("data-language-kind") === "mysticism" ? "mysticism" : "common";
        const bucket = ensureLanguageBucket(kind);
        bucket.push({ id:"lang_" + Math.random().toString(36).slice(2,8), name:"", level:"proficient" });
        renderLanguages();
        scheduleSave();
        return;
      }

      if(t.classList.contains("lotm-add-action")){
        if(!Array.isArray(charState.actions)) charState.actions = [];
        charState.actions.push(sanitizeActionEntry({}));
        renderActions();
        scheduleSave();
        return;
      }
      if(t.classList.contains("lotm-add-item")){
        if(!Array.isArray(charState.items)) charState.items=[];
        charState.items.push({ id:"item_"+Math.random().toString(36).slice(2,8), storage:"", name:"", description:"", slots:1, hidden_pocket:false });
        renderItems();
        renderSkills();
        renderAbilities();
        renderSpecialActions();
        renderActions();
        attachDocAbilityButtons(document);
        validateAndRender();
        scheduleSave();
        return;
      }
      if(t.classList.contains("lotm-add-adv")){ if(!Array.isArray(charState.adventure_log)) charState.adventure_log=[]; charState.adventure_log.unshift({ id:"adv_"+Math.random().toString(36).slice(2,8), type:"Encounter", title:"", notes:"" }); renderAdventure(); scheduleSave(); return; }

      const skillRow = t.closest("[data-skill-id]");
      if(skillRow){
        const sid = token(skillRow.getAttribute("data-skill-id"));
        const meta = ensureSkillMeta(sid);
        if(t.classList.contains("lotm-roll-skill")){
          const attr = skillRow.getAttribute("data-attr-id") || (BUILTIN_SKILLS[sid] ? BUILTIN_SKILLS[sid].attr : "int");
          const ex = skillExpr(attr, skillMod(meta));
          const rs = roll(ex, charState, { applyConditionCheckMod:true });
          logRoll(rs, ex, "Skill: "+(BUILTIN_SKILLS[sid] ? BUILTIN_SKILLS[sid].label : sid), "Skill Check");
          setStatus("Skill roll logged.", false);
          return;
        }
        if(t.classList.contains("lotm-remove-skill")){
          charState.sheet.custom_skills = (Array.isArray(charState.sheet.custom_skills) ? charState.sheet.custom_skills : []).filter(function(e){ return token(e.id) !== sid; });
          if(isObj(charState.skill_meta)) delete charState.skill_meta[sid];
          if(isObj(charState.skill)) delete charState.skill[sid];
          renderSkills();
          renderAbilities();
          renderSpecialActions();
          renderActions();
          attachDocAbilityButtons(document);
          validateAndRender();
          scheduleSave();
          setStatus("Custom skill removed.", false);
          return;
        }
      }

      if(t.classList.contains("lotm-roll-ability")){
        const aid = t.getAttribute("data-ability-id") || "";
        const ex = t.getAttribute("data-roll-expr") || "";
        const label = t.getAttribute("data-roll-label") || "Roll";
        const ab = findAbilityById(aid);
        const actionLock = blockedActionReason(ab ? ab.action : "none", charState, { requiresSpeech:ab ? abilityRequiresSpeech(ab) : false });
        if(actionLock){
          setStatus((ab ? ab.name : "Ability") + " blocked by conditions: " + actionLock + ".", true);
          return;
        }
        const spent = spendSpirituality(ab ? abilitySpiritualityCost(ab) : 0, ab ? ab.name : "Ability");
        const rs = roll(ex, charState, { applyConditionCheckMod:isCheckLikeLabel(label) });
        const typeLabel = spent > 0 ? (label + " | -" + String(spent) + " SP") : label;
        logRoll(rs, ex, ab ? ab.name : "Ability", typeLabel);
        if(spent <= 0) setStatus("Ability roll logged.", false);
        return;
      }

      if(t.classList.contains("lotm-roll-special")){
        const sid = t.getAttribute("data-special-id") || "";
        const rollKind = String(t.getAttribute("data-roll-kind") || "check").toLowerCase();
        const label = t.getAttribute("data-roll-label") || titleWords(rollKind || "roll");
        const ex = t.getAttribute("data-roll-expr") || "";
        const special = findSpecialActionById(sid);
        if(!special){ setStatus("Special action not found.", true); return; }
        const unavailable = specialActionUnavailableReason(special, charState);
        if(unavailable){ setStatus(special.name + " unavailable: " + unavailable, true); return; }
        const actionLock = blockedActionReason(special.action, charState, { requiresSpeech: !!special.requiresSpeech });
        if(actionLock){ setStatus(special.name + " blocked by conditions: " + actionLock + ".", true); return; }
        if(!String(ex || "").trim()){ setStatus(special.name + " has no roll expression.", true); return; }
        const repeats = resolveSpecialActionRollCount(special, rollKind === "effect" ? "effect" : "check", charState);
        const applyCondition = rollKind !== "effect";
        let i;
        for(i=0;i<repeats;i+=1){
          const rs = roll(ex, charState, { applyConditionCheckMod:applyCondition });
          const suffix = repeats > 1 ? " (" + String(i + 1) + "/" + String(repeats) + ")" : "";
          logRoll(rs, ex, "Special Action: " + special.name, label + suffix);
        }
        setStatus(special.name + " roll logged.", false);
        return;
      }

      const actionRow = t.closest("[data-action-id]");
      if(actionRow){
        const id = actionRow.getAttribute("data-action-id");
        const entry = Array.isArray(charState.actions) ? charState.actions.find(function(a){ return String(a.id)===String(id); }) : null;
        if(entry){
          if(t.classList.contains("lotm-remove-action")){
            charState.actions = charState.actions.filter(function(a){ return String(a.id)!==String(id); });
            renderActions();
            scheduleSave();
            return;
          }
          if(t.classList.contains("lotm-roll-action")){
            const action = sanitizeActionEntry(entry);
            const ex = withVs(action.expr, action.opposed_by);
            if(!String(ex||"").trim()){ setStatus("Action expression is empty.", true); return; }
            const actionLock = blockedActionReason(action.action, charState, { requiresSpeech:customActionRequiresSpeech(action) });
            if(actionLock){ setStatus((action.label || "Custom Action") + " blocked by conditions: " + actionLock + ".", true); return; }
            const spent = spendSpirituality(action.spirituality_cost, action.label || "Custom Action");
            const rs = roll(ex, charState, { applyConditionCheckMod:true });
            const rollType = (action.type || "Action") + (spent > 0 ? " | -" + String(spent) + " SP" : "");
            logRoll(rs, ex, action.label || "Custom Action", rollType);
            if(spent <= 0) setStatus("Custom action roll logged.", false);
            return;
          }
        }
      }

      const langRow = t.closest("[data-language-id]");
      if(langRow && t.classList.contains("lotm-remove-language")){
        const kind = langRow.getAttribute("data-language-kind") === "mysticism" ? "mysticism" : "common";
        const id = String(langRow.getAttribute("data-language-id") || "");
        charState.sheet.languages[kind] = ensureLanguageBucket(kind).filter(function(l){ return String(l.id) !== id; });
        renderLanguages();
        scheduleSave();
        return;
      }

      const itemRow = t.closest("[data-item-id]");
      if(itemRow && t.classList.contains("lotm-remove-item")){
        const id = itemRow.getAttribute("data-item-id");
        charState.items = (Array.isArray(charState.items)?charState.items:[]).filter(function(a){ return String(a.id)!==String(id); });
        renderItems();
        renderSkills();
        renderAbilities();
        renderSpecialActions();
        renderActions();
        attachDocAbilityButtons(document);
        validateAndRender();
        scheduleSave();
        return;
      }
      const advRow = t.closest("[data-adv-id]");
      if(advRow && t.classList.contains("lotm-remove-adv")){ const id = advRow.getAttribute("data-adv-id"); charState.adventure_log = (Array.isArray(charState.adventure_log)?charState.adventure_log:[]).filter(function(a){ return String(a.id)!==String(id); }); renderAdventure(); scheduleSave(); return; }
    });

    sheetRoot.addEventListener("change", function(ev){
      const t = ev.target;
      if(!(t instanceof HTMLElement)) return;
      if(t instanceof HTMLInputElement && t.hasAttribute("data-condition-id")){
        ensureConditionState();
        const id = String(t.getAttribute("data-condition-id") || "");
        if(Object.prototype.hasOwnProperty.call(charState.conditions.active, id)){
          charState.conditions.active[id] = !!t.checked;
          renderAll();
          attachDocAbilityButtons(document);
          scheduleSave();
        }
        return;
      }
      const skillRow = t.closest("[data-skill-id]");
      if(skillRow){
        const sid = token(skillRow.getAttribute("data-skill-id"));
        const meta = ensureSkillMeta(sid);
        const field = t.getAttribute("data-skill-field");
        if(field === "intuition" || field === "education" || field === "bonus") meta[field] = int(t.value,0);
        else if(field === "attr") charState.sheet.custom_skills = (Array.isArray(charState.sheet.custom_skills)?charState.sheet.custom_skills:[]).map(function(e){ if(token(e.id)!==sid) return e; return { id:e.id, label:e.label, attr:ATTR_KEYS.indexOf(String(t.value||"").toLowerCase())>=0 ? String(t.value||"").toLowerCase() : "int" }; });
        renderSkills();
        renderAbilities();
        renderSpecialActions();
        renderActions();
        attachDocAbilityButtons(document);
        validateAndRender();
        scheduleSave();
        return;
      }

      const actionRow = t.closest("[data-action-id]");
      if(actionRow){
        const id = actionRow.getAttribute("data-action-id");
        const e = Array.isArray(charState.actions) ? charState.actions.find(function(a){ return String(a.id)===String(id); }) : null;
        if(e){
          const f = t.getAttribute("data-action-field");
          if(f){
            if(f === "spirituality_cost") e[f] = int(t.value,0);
            else e[f] = t.value;
            renderActions();
            scheduleSave();
          }
        }
        return;
      }
      const itemRow = t.closest("[data-item-id]");
      if(itemRow){
        const id=itemRow.getAttribute("data-item-id");
        const e=Array.isArray(charState.items)?charState.items.find(function(a){ return String(a.id)===String(id); }):null;
        if(e){
          const f=t.getAttribute("data-item-field");
          if(f){
            if(f==="slots") e[f]=int(t.value,0);
            else if(f==="hidden_pocket" && t instanceof HTMLInputElement) e[f]=!!t.checked;
            else e[f]=t.value;
            renderSkills();
            renderAbilities();
            renderSpecialActions();
            renderActions();
            attachDocAbilityButtons(document);
            validateAndRender();
            scheduleSave();
          }
        }
        return;
      }
      const advRow = t.closest("[data-adv-id]");
      if(advRow){ const id=advRow.getAttribute("data-adv-id"); const e=Array.isArray(charState.adventure_log)?charState.adventure_log.find(function(a){ return String(a.id)===String(id); }):null; if(e){ const f=t.getAttribute("data-adv-field"); if(f){ e[f]=t.value; scheduleSave(); } } return; }

      const langRow = t.closest("[data-language-id]");
      if(langRow){
        const kind = langRow.getAttribute("data-language-kind") === "mysticism" ? "mysticism" : "common";
        const id = String(langRow.getAttribute("data-language-id") || "");
        const field = t.getAttribute("data-language-field");
        const list = ensureLanguageBucket(kind);
        const entry = list.find(function(l){ return String(l.id) === id; });
        if(entry && field){
          if(field === "level") entry[field] = prof(t.value);
          else entry[field] = String(t.value || "");
          renderLanguages();
          scheduleSave();
        }
        return;
      }

      if(t.classList.contains("lotm-pathway-select")){
        autoRefreshImportedAbilities({ silent:false });
        return;
      }
      if(t.classList.contains("lotm-sequence-select")){
        autoRefreshImportedAbilities({ silent:false });
        return;
      }
    });

    if(skillSearchEl) skillSearchEl.addEventListener("input", function(){ renderSkills(); });
    if(importFileEl) importFileEl.addEventListener("change", function(){ const f = importFileEl.files && importFileEl.files[0]; importFromFile(f || null); });
    if(portraitFileEl) portraitFileEl.addEventListener("change", function(){
      const file = portraitFileEl.files && portraitFileEl.files[0];
      if(!file) return;
      if(file.size > 1500 * 1024){
        setStatus("Portrait image is too large. Use a file under 1.5MB.", true);
        return;
      }
      if(file.type && file.type.indexOf("image/") !== 0){
        setStatus("Select an image file for portrait.", true);
        return;
      }
      const reader = new FileReader();
      reader.onload = function(){
        charState.meta.portrait = String(reader.result || "");
        renderPortraitCard();
        scheduleSave();
        setStatus("Portrait updated.", false);
      };
      reader.onerror = function(){ setStatus("Could not read portrait image.", true); };
      reader.readAsDataURL(file);
    });

    loadCompendium()
      .then(function(data){
        fillPathwayOptions(data);
        return autoRefreshImportedAbilities({ silent:true });
      })
      .catch(function(err){ setStatus("Compendium load failed: "+String(err.message || err), true); });
  }

  function attachDocAbilityButtons(root){
    const scope = root && typeof root.querySelectorAll === "function" ? root : document;
    const cards = scope.querySelectorAll(".ability-card");
    cards.forEach(function(card){
      const nm = card.querySelector(".ability-name");
      const abilityName = nm ? String(nm.textContent||"").trim() : "Ability";
      card.querySelectorAll(".ability-dice tr").forEach(function(row){
        const th = row.querySelector("th"), td = row.querySelector("td");
        if(!th || !td) return;
        const key = String(th.textContent||"").trim().replace(/:$/,"").toLowerCase();
        if(["check","damage","heal","effect"].indexOf(key) < 0) return;
        const clone = td.cloneNode(true); clone.querySelectorAll(".lotm-ability-roll-wrap").forEach(function(el){ el.remove(); });
        const expr = String(clone.textContent||"").replace(/\s+/g," ").trim();
        if(!expr || expr.toLowerCase() === "none") return;
        const existingBtn = td.querySelector(".lotm-ability-roll");
        const applyCondition = key === "check";
        if(existingBtn){
          existingBtn.setAttribute("data-roll-expr", expr);
          const existingPreview = td.querySelector(".lotm-ability-roll-wrap .lotm-roll-preview");
          if(existingPreview) existingPreview.textContent = rollPreviewWithCondition(expr, charState, applyCondition);
          return;
        }
        const wrap = document.createElement("div"); wrap.className = "lotm-ability-roll-wrap";
        const b = document.createElement("button"); b.type = "button"; b.className = "btn btn-ghost lotm-ability-roll"; b.textContent = "Roll " + key.charAt(0).toUpperCase()+key.slice(1);
        b.setAttribute("data-roll-expr", expr);
        const prev = document.createElement("div"); prev.className = "lotm-roll-preview"; prev.textContent = rollPreviewWithCondition(expr, charState, applyCondition);
        b.addEventListener("click", function(){
          const sourceExpr = b.getAttribute("data-roll-expr") || expr;
          const rs = roll(sourceExpr, charState, { applyConditionCheckMod:key === "check" });
          logRoll(rs, sourceExpr, abilityName, key.charAt(0).toUpperCase()+key.slice(1));
          setStatus(abilityName+" - "+key+" rolled.", false);
        });
        wrap.appendChild(b);
        wrap.appendChild(prev);
        td.appendChild(wrap);
      });
    });
  }

  function init(){
    initRulebookSidebar();
    mountSheet();
    initInteractions();
    renderAll();
    attachDocAbilityButtons(document);

    const main = document.getElementById("main");
    if(main && typeof MutationObserver !== "undefined"){
      const observer = new MutationObserver(function(){ window.setTimeout(function(){ attachDocAbilityButtons(document); }, 60); });
      observer.observe(main, { childList:true, subtree:true });
    }

    window.addEventListener("pageshow", function(){ attachDocAbilityButtons(document); });
    document.addEventListener("keydown", function(e){
      if(e.key !== "Escape") return;
      if(hpManagerEl && hpManagerEl.classList.contains("open")){
        setHpManagerOpen(false);
        e.preventDefault();
        return;
      }
      if(valueManagerEl && valueManagerEl.classList.contains("open")){
        setValueManagerOpen(false);
        e.preventDefault();
        return;
      }
      if(closeAbilityDetail()){
        e.preventDefault();
        return;
      }
      if(document.body.classList.contains("lotm-sheet-open")){
        setSheetOpen(false);
        return;
      }
      if(document.body.classList.contains("sidebar-open")) document.body.classList.remove("sidebar-open");
    });
  }

  window.LOTM = {
    loadChar: loadChar,
    saveChar: saveChar,
    resetChar: resetChar,
    roll: roll,
    rollVs: rollVs,
    debugRoll: debugRoll,
    openSheet: function(){ setSheetOpen(true); },
    closeSheet: function(){ setSheetOpen(false); },
    getState: function(){ return normalizeChar(charState); },
    getConditionEffects: function(){ return activeConditionEffects(normalizeChar(charState)); },
    specialActions: SPECIAL_ACTION_DEFS.slice()
  };

  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();

  console.log("viewer_theme.js loaded");
})();
