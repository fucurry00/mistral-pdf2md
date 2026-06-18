## User

抽象的な構造を策定したいので、すでに実装された具象的なディレクトリ構造を見ずに判断してください。
次の文章はこのプロジェクトをなぜ始めたのか、どのような実装を行いたいのかについて私なりに考えたものです。
次のような視点から批判的に考察しこのアイディアをより洗練されたものにできるように手伝ってください。
1. 発想自体に不備はないか
2. 各仕様について妥当性があるか
3. 全体的な構想と個別の実装アイディアとの乖離がないか

## 背景
pdfやword、html、google docsといった文書は人が読みやすいような形になっている。
これはAIには読みづらい。 
事前知識として、これらが上記文書にまとまっている場合には、AIエージェントにも読ませたいですが、この処理が問題になります。 特にPDFは画像などで取り込む方法と、文書化、文字化してテキストにして取り込む方法2つがあり、これらを同時に行うのでコンテキストを大幅に食います。 では、AIとユーザーが共通の知識を共有するために、どのようにすればよりトークン効率のいいものができるかという部分が今回の背景です。 

## ocrを利用してmdへ
PDFや写真はOCRを利用して文字情報を抽出することができます。 特にこれらで構造化されたマークダウンを出力することによって、ある文章をそのままマークダウンという軽量なものに変換することができます。 
利点
- ファイルが軽量
- 入力トークンの削減
- grepを利用した特定文言が存在する部分の探索が容易

## ocrだけで十分なのか？
ocrだけでは文字化けや変換ミスなどがどうしても発生してしまう。
- mがrnに誤変換
- 講義資料には繰り返し「講義名」「教授名」「セクション名」などのノイズが混入する
これらをどのように排除すべきだろうか。

## LLMを校正エージェントとして使う
LLMは文脈を読み、このノイズが多い文書の内容を損なわず返還させることができる。つまりocrで高精度に変換された文書をよりキレイに再構築することができるのである。

## 動的編集と静的編集
LLMにだけ丸投げするのはトークン効率的にも出力精度的にも良くないと予想される。LLMに作業をさせるのなら、減らせるノイズは事前に潰し、より人が見ながら気づくような固有の判断をLLMに任せて編集するのがエージェント的な編集・ハーネスとして理にかなっていると言える。

## LLMにはどのような判断をさせるべきなのだろうか
LLMには編集する箇所を見つけ、編集するという行為が必要である。

## Assistant

抽象設計の批判として扱い、既存の実装ディレクトリやファイル構成は見ません。計画系の観点だけ使って、前提・仕様・全体構想との整合性を点検します。

**Tool Call: Read SKILL.md**
Status: Completed

```json
{
  "call_id": "call_5tKfezXfdiEpt4vQz0FSJ09P",
  "process_id": "80142",
  "turn_id": "019ed4c3-7b7b-7711-bdf6-381d72858e04",
  "completed_at_ms": 1781686064651,
  "command": [
    "/bin/zsh",
    "-lc",
    "sed -n '1,220p' /Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/plan/SKILL.md"
  ],
  "cwd": "/Users/kentaro/area_of_responsibility/extend_claude/yt-transcript",
  "parsed_cmd": [
    {
      "type": "read",
      "cmd": "sed -n '1,220p' /Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/plan/SKILL.md",
      "name": "SKILL.md",
      "path": "/Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/plan/SKILL.md"
    }
  ],
  "source": "unified_exec_startup",
  "stdout": "---\nname: plan\ndescription: \"[OMX] Strategic planning with optional interview workflow\"\n---\n\n<Purpose>\nPlan creates comprehensive, actionable work plans through intelligent interaction. It auto-detects whether to interview the user (broad requests) or plan directly (detailed requests), and supports consensus mode (iterative Planner/Architect/Critic loop with RALPLAN-DR structured deliberation) and review mode (Critic evaluation of existing plans).\n</Purpose>\n\n<Use_When>\n- User wants to plan before implementing -- \"plan this\", \"plan the\", \"let's plan\"\n- User wants structured requirements gathering for a vague idea\n- User wants an existing plan reviewed -- \"review this plan\", `--review`\n- User wants multi-perspective consensus on a plan -- `--consensus`, \"ralplan\"\n- Task is broad or vague and needs scoping before any code is written\n</Use_When>\n\n<Do_Not_Use_When>\n- User wants autonomous end-to-end execution -- use `autopilot` instead\n- User wants to start coding immediately with a clear task -- use `ralph` or delegate to executor\n- User asks a simple question that can be answered directly -- just answer it\n- Task is a single focused fix with obvious scope -- skip planning, just do it\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nJumping into code without understanding requirements leads to rework, scope creep, and missed edge cases. Plan provides structured requirements gathering, expert analysis, and quality-gated plans so that execution starts from a solid foundation. The consensus mode adds multi-perspective validation for high-stakes projects.\n</Why_This_Exists>\n\n<Execution_Policy>\n- Auto-detect interview vs direct mode based on request specificity\n- Ask one question at a time during interviews -- never batch multiple interview rounds into one question form\n- Gather codebase facts via `explore` agent before asking the user about them\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only repository lookups during planning; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep prompt-heavy or ambiguous planning work on the richer normal path.\n- Plans must meet quality standards: 80%+ claims cite file/line, 90%+ criteria are testable\n- Implementation step count must be right-sized to task scope; avoid defaulting to exactly five steps when the work is clearly smaller or larger\n- Consensus mode outputs the final plan by default; add `--interactive` to enable execution handoff\n- Consensus mode uses RALPLAN-DR short mode by default; switch to deliberate mode with `--deliberate` or when the request explicitly signals high risk (auth/security, data migration, destructive/irreversible changes, production incident, compliance/PII, public API breakage)\n- Apply the shared workflow guidance pattern: outcome-first framing, concise visible updates for multi-step planning, local overrides for the active workflow branch, evidence-backed planning and validation expectations, explicit stop rules, and automatic continuation for safe reversible steps. Ask only for material, destructive, credentialed, external-production, or preference-dependent branches.\n</Execution_Policy>\n\n<Steps>\n\n### Mode Selection\n\n| Mode | Trigger | Behavior |\n|------|---------|----------|\n| Interview | Default for broad requests | Interactive requirements gathering |\n| Direct | `--direct`, or detailed request | Skip interview, generate plan directly |\n| Consensus | `--consensus`, \"ralplan\" | Planner -> Architect -> Critic loop until agreement with RALPLAN-DR structured deliberation (short by default, `--deliberate` for high-risk); outputs plan by default |\n| Consensus Interactive | `--consensus --interactive` | Same as Consensus but pauses for user feedback at draft and approval steps, then hands off to execution |\n| Review | `--review`, \"review this plan\" | Critic evaluation of existing plan |\n\n### Interview Mode (broad/vague requests)\n\n1. **Classify the request**: Broad (vague verbs, no specific files, touches 3+ areas) triggers interview mode\n2. **Ask one focused question** using the surface-appropriate structured question path for preferences, scope, and constraints: in attached-tmux OMX runtime use `omx question`; outside tmux use native structured input when available; use plain text only as a last fallback\n3. **Gather codebase facts first**: Before asking \"what patterns does your code use?\", spawn an `explore` agent to find out, then ask informed follow-up questions\n4. **Build on answers**: Each question builds on the previous answer\n5. **Consult Analyst** (THOROUGH tier) for hidden requirements, edge cases, and risks\n6. **Create plan** when the user signals readiness: \"create the plan\", \"I'm ready\", \"make it a work plan\"\n\n### Direct Mode (detailed requests)\n\n1. **Quick Analysis**: Optional brief Analyst consultation\n2. **Create plan**: Generate comprehensive work plan immediately\n3. **Review** (optional): Critic review if requested\n\n### Consensus Mode (`--consensus` / \"ralplan\")\n\n**RALPLAN-DR modes**: **Short** (default, bounded structure) and **Deliberate** (for `--deliberate` or explicit high-risk requests). Both modes keep the same Planner -> Architect -> Critic sequence. The workflow auto-proceeds through planning steps (Planner/Architect/Critic) but outputs the final plan without executing.\n\n1. **Planner** creates initial plan and a compact **RALPLAN-DR summary** before any Architect review. The summary **MUST** include:\n   - **Principles** (3-5)\n   - **Decision Drivers** (top 3)\n   - **Viable Options** (>=2) with bounded pros/cons for each option\n   - If only one viable option remains, an explicit **invalidation rationale** for the alternatives that were rejected\n   - In **deliberate mode**: a **pre-mortem** (3 failure scenarios) and an **expanded test plan** covering **unit / integration / e2e / observability**\n2. **User feedback** *(--interactive only)*: If running with `--interactive`, **MUST** use `AskUserQuestion` / the structured question UI (`omx question` in attached tmux; native structured input outside tmux when available) to present the draft plan **plus the RALPLAN-DR Principles / Decision Drivers / Options summary for early direction alignment** with these options:\n   - **Proceed to review** — send to Architect and Critic for evaluation\n   - **Request changes** — return to step 1 with user feedback incorporated\n   - **Skip review** — go directly to final approval (step 7)\n   If NOT running with `--interactive`, automatically proceed to review (step 3).\n3. **Architect** reviews for architectural soundness as a dedicated subsequent `Architect` subagent with the full task, current plan text/path, RALPLAN-DR summary, and relevant artifact context. Architect review **MUST** include: strongest steelman counterargument (antithesis) against the favored option, at least one meaningful tradeoff tension, and (when possible) a synthesis path. In deliberate mode, Architect should explicitly flag principle violations. **Wait for this step to complete before proceeding to step 4.** Do NOT run steps 3 and 4 in parallel. Do NOT substitute a default/improvised subagent prompt for the role-specific `Architect` prompt.\n4. **Critic** evaluates against quality criteria as a dedicated subsequent `Critic` subagent with the full task, current plan text/path, RALPLAN-DR summary, artifact context, and the completed `Architect` result. Critic **MUST** verify principle-option consistency, fair alternative exploration, risk mitigation clarity, testable acceptance criteria, and concrete verification steps. Critic **MUST** explicitly reject shallow alternatives, driver contradictions, vague risks, or weak verification. In deliberate mode, Critic **MUST** reject missing/weak pre-mortem or missing/weak expanded test plan. Run only after step 3 is complete. Do NOT let the `Architect` response self-approve the Critic gate.\n5. **Re-review loop** (max 5 iterations): If Critic rejects or iterates, execute this closed loop:\n   a. Collect all feedback from Architect + Critic\n   b. Pass feedback to Planner to produce a revised plan\n   c. **Return to Step 3** — Architect reviews the revised plan\n   d. **Return to Step 4** — Critic evaluates the revised plan\n   e. Repeat until Critic approves OR max 5 iterations reached\n   f. If max iterations reached without approval, present the best version to user via the structured question UI with note that expert consensus was not reached\n6. **Apply improvements**: When reviewers approve with improvement suggestions, merge all accepted improvements into the plan file before proceeding. Final consensus output **MUST** include an **ADR** section with: **Decision**, **Drivers**, **Alternatives considered**, **Why chosen**, **Consequences**, **Follow-ups**. Specifically:\n   a. Collect all improvement suggestions from Architect and Critic responses\n   b. Deduplicate and categorize the suggestions\n   c. Update the plan file in `.omx/plans/` with the accepted improvements (add missing details, refine steps, strengthen acceptance criteria, ADR updates, etc.)\n   d. Note which improvements were applied in a brief changelog section at the end of the plan\n   e. Before any execution handoff, derive an explicit **available-agent-types roster** from the known prompt catalog and add concrete **follow-up staffing guidance** for `$ultragoal` and `$team` (recommended roles, counts, suggested reasoning levels by lane, and why each lane exists), plus an explicit `$ralph` fallback note only when persistent single-owner verification is intentionally selected\n   f. Add a product-facing **Goal-Mode Follow-up Suggestions** section: recommend `$ultragoal` by default for general goal-oriented follow-up, `$autoresearch-goal` only when the context is a research project with a research deliverable/evaluator, and `$performance-goal` when the context is an optimization or performance project. Keep these suggestions alongside the Team path and any explicit Ralph fallback rather than replacing implementation-delivery guidance. For ordinary pre-planning external docs or best-practice lookup, cite `$best-practice-research` evidence and synthesize it into the plan instead of recommending Autoresearch as a final architecture component. For durable-goal work that is also parallelizable, explicitly recommend **Team + Ultragoal**: Ultragoal remains leader-owned goal/ledger state and Team returns checkpoint-ready execution evidence.\n   g. For the `$team` path, add an explicit launch-hint block with concrete `omx team` / `$team` commands and a **team verification path** (what Team proves before shutdown and what Ultragoal checkpoints as durable completion evidence). Distinguish Team + Ultragoal from any explicit Ralph fallback: Team handles coordinated parallel lanes; Ultragoal is the default durable follow-up/ledger owner, and Ralph is only an explicitly requested legacy-style persistent sequential verification/fix lane when needed.\n7. On Critic approval (with improvements applied): *(--interactive only)* If running with `--interactive`, use `AskUserQuestion` / the structured question UI to present the plan with these options:\n   - **Approve durable goal execution** — proceed via `$ultragoal` by default (optionally with `$team` for parallel lanes)\n   - **Approve and implement via team** — proceed to implementation via coordinated parallel team agents\n   - **Start goal-mode follow-up** — proceed via `$ultragoal` by default, or `$autoresearch-goal` / `$performance-goal` when the approved plan specifically fits research validation or measurable optimization\n   - **Request changes** — return to step 1 with user feedback\n   - **Reject** — discard the plan entirely\n   If NOT running with `--interactive`, output the final approved plan and stop. Do NOT auto-execute.\n8. *(--interactive only)* User chooses via the structured question UI (never ask for approval in plain text when a structured surface is available)\n9. On user approval (--interactive only):\n   - **Approve durable goal execution**: **MUST** invoke `$ultragoal` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete role allocation guidance, and direct launch hints for Ultragoal follow-up work**. Use `$team` alongside Ultragoal when parallel lanes are warranted. Do NOT implement directly. Do NOT edit source code files in the planning agent. Ralph is not the default follow-up; only invoke `$ralph` when the user explicitly selects a legacy/persistent single-owner execution lane.\n   - **Approve and implement via team**: **MUST** invoke `$team` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete staffing / worker-role allocation guidance, explicit `omx team` / `$team` launch hints, and the team verification path**. Do NOT implement directly. The team skill coordinates parallel agents across the staged pipeline for faster execution on large tasks.\n   - **Start goal-mode follow-up**: **MUST** invoke the selected goal workflow with the approved plan path and appropriate success context: `$ultragoal` as the default goal-mode path, `$autoresearch-goal` for research projects, or `$performance-goal` for optimization/performance projects with measurable evaluator criteria. Do NOT implement directly in the planning agent.\n\n### Review Mode (`--review`)\n\n0. Treat review as a reviewer-only pass. The context that wrote the plan, cleanup proposal, or diff MUST NOT be the context that approves it.\n1. Read plan file from `.omx/plans/`\n2. Evaluate via Critic using `ask_codex` with `agent_role: \"critic\"`\n3. For cleanup/refactor/anti-slop work, verify that the artifact includes a cleanup plan, regression tests or an explicit test gap, smell-by-smell passes, and quality gates.\n4. Return verdict: APPROVED, REVISE (with specific feedback), or REJECT (replanning required)\n5. If the current context authored the artifact, hand the review to `$code-review`, `critic`, `quality-reviewer`, or `verifier` as appropriate.\n\n### Plan Output Format\n\nEvery plan includes:\n- Requirements Summary\n- Acceptance Criteria (testable)\n- Implementation Steps (with file references)\n- Adaptive step count sized to the actual scope (not a fixed five-step template)\n- Risks and Mitigations\n- Verification Steps\n- For consensus/ralplan: **RALPLAN-DR summary** (Principles, Decision Drivers, Options)\n- For consensus/ralplan final output: **ADR** (Decision, Drivers, Alternatives considered, Why chosen, Consequences, Follow-ups)\n- For consensus/ralplan execution handoff: **Available-Agent-Types Roster**, **Follow-up Staffing Guidance** (including suggested reasoning levels by lane), product-facing **Goal-Mode Follow-up Suggestions** (`$ultragoal`, `$autoresearch-goal`, `$performance-goal` when contextually appropriate), explicit `omx team` / `$team` **Launch Hints**, and **Team Verification Path**\n- For deliberate consensus mode: **Pre-mortem (3 scenarios)** and **Expanded Test Plan** (unit/integration/e2e/observability)\n\nPlans are saved to `.omx/plans/`. Drafts go to `.omx/drafts/`.\n</Steps>\n\n<Tool_Usage>\n- Use `AskUserQuestion` for preference questions (scope, priority, timeline, risk tolerance) -- provides clickable UI\n- Use plain text for questions needing specific values (port numbers, names, follow-up clarifications)\n- Use the `explore` agent (LOW tier, bounded quick pass) to gather codebase facts before asking the user\n- Use `ask_codex` with `agent_role: \"planner\"` for planning validation on large-scope plans\n- Use `ask_codex` with `agent_role: \"analyst\"` for requirements analysis\n- Use `ask_codex` with `agent_role: \"critic\"` for standalone review mode. In consensus mode, use the dedicated sequential role-specific `Architect` and `Critic` subagents described in steps 3-4 instead of a single critic-only review call.\n- If optional MCP compatibility tools or Codex consultation are unavailable, fall back to equivalent OMX prompt/native agents -- never block on external tools\n- **CRITICAL — Consensus mode agent calls MUST be sequential, never parallel.** Always await the subsequent role-specific `Architect` result before issuing the subsequent role-specific `Critic` call.\n- In consensus mode, default to RALPLAN-DR short mode; enable deliberate mode on `--deliberate` or explicit high-risk signals (auth/security, migrations, destructive changes, production incidents, compliance/PII, public API breakage)\n- In consensus mode with `--interactive`: use `AskUserQuestion` / the structured question UI for the user feedback step (step 2) and the final approval step (step 7) -- never ask for approval in plain text when a structured surface is available. Without `--interactive`, auto-proceed through planning steps without pausing. Output the final plan without execution.\n- In consensus mode with `--interactive`, on user approval **MUST** invoke the selected follow-up lane from step 9 (`$ultragoal`, `$team`, `$autoresearch-goal`, `$performance-goal`, or explicit `$ralph` fallback) -- never implement directly in the planning agent\n- In consensus mode, execution follow-up handoff **MUST** include an explicit available-agent-types roster plus concrete staffing / role-allocation guidance grounded in that roster, suggested reasoning levels by lane, product-facing goal-mode follow-up suggestions (`$ultragoal` by default, `$autoresearch-goal` for research projects, `$performance-goal` for optimization/performance projects), explicit `omx team` / `$team` launch hints, and a team verification path. For parallelizable durable-goal plans, recommend Team + Ultragoal with leader-owned checkpointing from Team evidence; reserve Ralph for persistent sequential single-owner verification/fix follow-up.\n</Tool_Usage>\n\n## Scenario Examples\n\n**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.\n\n**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.\n\n**Bad:** The user says `continue`, and the workflow restarts discovery or stops before the missing verification/evidence is gathered.\n\n<Examples>\n<Good>\nAdaptive interview (gathering facts before asking):\n```\nPlanner: [spawns explore agent: \"find authentication implementation\"]\nPlanner: [receives: \"Auth is in src/auth/ using JWT with passport.js\"]\nPlanner: \"I see you're using JWT authentication with passport.js in src/auth/.\n         For this new feature, should we extend the existing auth or add a separate auth flow?\"\n```\nWhy good: Answers its own codebase question first, then asks an informed preference question.\n</Good>\n\n<Good>\nSingle question at a time:\n```\nQ1: \"What's the main goal?\"\nA1: \"Improve performance\"\nQ2: \"For performance, what matters more -- latency or throughput?\"\nA2: \"Latency\"\nQ3: \"For latency, are we optimizing for p50 or p99?\"\n```\nWhy good: Each question builds on the previous answer. Focused and progressive.\n</Good>\n\n<Bad>\nAsking about things you could look up:\n```\nPlanner: \"Where is authentication implemented in your codebase?\"\nUser: \"Uh, somewhere in src/auth I think?\"\n```\nWhy bad: The planner should spawn an explore agent to find this, not ask the user.\n</Bad>\n\n<Bad>\nBatching multiple questions:\n```\n\"What's the scope? And the timeline? And who's the audience?\"\n```\nWhy bad: Three questions at once causes shallow answers. Ask one at a time.\n</Bad>\n\n<Bad>\nPresenting all design options at once:\n```\n\"Here are 4 approaches: Option A... Option B... Option C... Option D... Which do you prefer?\"\n```\nWhy bad: Decision fatigue. Present one option with trade-offs, get reaction, then present the next.\n</Bad>\n</Examples>\n\n<Escalation_And_Stop_Conditions>\n- Stop interviewing when requirements are clear enough to plan -- do not over-interview\n- In consensus mode, stop after 5 Planner/Architect/Critic iterations and present the best version\n- Consensus mode outputs the plan by default; with `--interactive`, user can approve and hand off to ultragoal/team, with Ralph only as an explicit legacy/persistent single-owner lane\n- If the user says \"just do it\" or \"skip planning\", **MUST** invoke `$ultragoal` to transition to durable goal execution mode by default; use `$ralph` only when the user explicitly asks for that fallback. Do NOT implement directly in the planning agent.\n- Escalate to the user when there are irreconcilable trade-offs that require a business decision\n</Escalation_And_Stop_Conditions>\n\n<Final_Checklist>\n",
  "stderr": "",
  "aggregated_output": "---\nname: plan\ndescription: \"[OMX] Strategic planning with optional interview workflow\"\n---\n\n<Purpose>\nPlan creates comprehensive, actionable work plans through intelligent interaction. It auto-detects whether to interview the user (broad requests) or plan directly (detailed requests), and supports consensus mode (iterative Planner/Architect/Critic loop with RALPLAN-DR structured deliberation) and review mode (Critic evaluation of existing plans).\n</Purpose>\n\n<Use_When>\n- User wants to plan before implementing -- \"plan this\", \"plan the\", \"let's plan\"\n- User wants structured requirements gathering for a vague idea\n- User wants an existing plan reviewed -- \"review this plan\", `--review`\n- User wants multi-perspective consensus on a plan -- `--consensus`, \"ralplan\"\n- Task is broad or vague and needs scoping before any code is written\n</Use_When>\n\n<Do_Not_Use_When>\n- User wants autonomous end-to-end execution -- use `autopilot` instead\n- User wants to start coding immediately with a clear task -- use `ralph` or delegate to executor\n- User asks a simple question that can be answered directly -- just answer it\n- Task is a single focused fix with obvious scope -- skip planning, just do it\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nJumping into code without understanding requirements leads to rework, scope creep, and missed edge cases. Plan provides structured requirements gathering, expert analysis, and quality-gated plans so that execution starts from a solid foundation. The consensus mode adds multi-perspective validation for high-stakes projects.\n</Why_This_Exists>\n\n<Execution_Policy>\n- Auto-detect interview vs direct mode based on request specificity\n- Ask one question at a time during interviews -- never batch multiple interview rounds into one question form\n- Gather codebase facts via `explore` agent before asking the user about them\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only repository lookups during planning; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep prompt-heavy or ambiguous planning work on the richer normal path.\n- Plans must meet quality standards: 80%+ claims cite file/line, 90%+ criteria are testable\n- Implementation step count must be right-sized to task scope; avoid defaulting to exactly five steps when the work is clearly smaller or larger\n- Consensus mode outputs the final plan by default; add `--interactive` to enable execution handoff\n- Consensus mode uses RALPLAN-DR short mode by default; switch to deliberate mode with `--deliberate` or when the request explicitly signals high risk (auth/security, data migration, destructive/irreversible changes, production incident, compliance/PII, public API breakage)\n- Apply the shared workflow guidance pattern: outcome-first framing, concise visible updates for multi-step planning, local overrides for the active workflow branch, evidence-backed planning and validation expectations, explicit stop rules, and automatic continuation for safe reversible steps. Ask only for material, destructive, credentialed, external-production, or preference-dependent branches.\n</Execution_Policy>\n\n<Steps>\n\n### Mode Selection\n\n| Mode | Trigger | Behavior |\n|------|---------|----------|\n| Interview | Default for broad requests | Interactive requirements gathering |\n| Direct | `--direct`, or detailed request | Skip interview, generate plan directly |\n| Consensus | `--consensus`, \"ralplan\" | Planner -> Architect -> Critic loop until agreement with RALPLAN-DR structured deliberation (short by default, `--deliberate` for high-risk); outputs plan by default |\n| Consensus Interactive | `--consensus --interactive` | Same as Consensus but pauses for user feedback at draft and approval steps, then hands off to execution |\n| Review | `--review`, \"review this plan\" | Critic evaluation of existing plan |\n\n### Interview Mode (broad/vague requests)\n\n1. **Classify the request**: Broad (vague verbs, no specific files, touches 3+ areas) triggers interview mode\n2. **Ask one focused question** using the surface-appropriate structured question path for preferences, scope, and constraints: in attached-tmux OMX runtime use `omx question`; outside tmux use native structured input when available; use plain text only as a last fallback\n3. **Gather codebase facts first**: Before asking \"what patterns does your code use?\", spawn an `explore` agent to find out, then ask informed follow-up questions\n4. **Build on answers**: Each question builds on the previous answer\n5. **Consult Analyst** (THOROUGH tier) for hidden requirements, edge cases, and risks\n6. **Create plan** when the user signals readiness: \"create the plan\", \"I'm ready\", \"make it a work plan\"\n\n### Direct Mode (detailed requests)\n\n1. **Quick Analysis**: Optional brief Analyst consultation\n2. **Create plan**: Generate comprehensive work plan immediately\n3. **Review** (optional): Critic review if requested\n\n### Consensus Mode (`--consensus` / \"ralplan\")\n\n**RALPLAN-DR modes**: **Short** (default, bounded structure) and **Deliberate** (for `--deliberate` or explicit high-risk requests). Both modes keep the same Planner -> Architect -> Critic sequence. The workflow auto-proceeds through planning steps (Planner/Architect/Critic) but outputs the final plan without executing.\n\n1. **Planner** creates initial plan and a compact **RALPLAN-DR summary** before any Architect review. The summary **MUST** include:\n   - **Principles** (3-5)\n   - **Decision Drivers** (top 3)\n   - **Viable Options** (>=2) with bounded pros/cons for each option\n   - If only one viable option remains, an explicit **invalidation rationale** for the alternatives that were rejected\n   - In **deliberate mode**: a **pre-mortem** (3 failure scenarios) and an **expanded test plan** covering **unit / integration / e2e / observability**\n2. **User feedback** *(--interactive only)*: If running with `--interactive`, **MUST** use `AskUserQuestion` / the structured question UI (`omx question` in attached tmux; native structured input outside tmux when available) to present the draft plan **plus the RALPLAN-DR Principles / Decision Drivers / Options summary for early direction alignment** with these options:\n   - **Proceed to review** — send to Architect and Critic for evaluation\n   - **Request changes** — return to step 1 with user feedback incorporated\n   - **Skip review** — go directly to final approval (step 7)\n   If NOT running with `--interactive`, automatically proceed to review (step 3).\n3. **Architect** reviews for architectural soundness as a dedicated subsequent `Architect` subagent with the full task, current plan text/path, RALPLAN-DR summary, and relevant artifact context. Architect review **MUST** include: strongest steelman counterargument (antithesis) against the favored option, at least one meaningful tradeoff tension, and (when possible) a synthesis path. In deliberate mode, Architect should explicitly flag principle violations. **Wait for this step to complete before proceeding to step 4.** Do NOT run steps 3 and 4 in parallel. Do NOT substitute a default/improvised subagent prompt for the role-specific `Architect` prompt.\n4. **Critic** evaluates against quality criteria as a dedicated subsequent `Critic` subagent with the full task, current plan text/path, RALPLAN-DR summary, artifact context, and the completed `Architect` result. Critic **MUST** verify principle-option consistency, fair alternative exploration, risk mitigation clarity, testable acceptance criteria, and concrete verification steps. Critic **MUST** explicitly reject shallow alternatives, driver contradictions, vague risks, or weak verification. In deliberate mode, Critic **MUST** reject missing/weak pre-mortem or missing/weak expanded test plan. Run only after step 3 is complete. Do NOT let the `Architect` response self-approve the Critic gate.\n5. **Re-review loop** (max 5 iterations): If Critic rejects or iterates, execute this closed loop:\n   a. Collect all feedback from Architect + Critic\n   b. Pass feedback to Planner to produce a revised plan\n   c. **Return to Step 3** — Architect reviews the revised plan\n   d. **Return to Step 4** — Critic evaluates the revised plan\n   e. Repeat until Critic approves OR max 5 iterations reached\n   f. If max iterations reached without approval, present the best version to user via the structured question UI with note that expert consensus was not reached\n6. **Apply improvements**: When reviewers approve with improvement suggestions, merge all accepted improvements into the plan file before proceeding. Final consensus output **MUST** include an **ADR** section with: **Decision**, **Drivers**, **Alternatives considered**, **Why chosen**, **Consequences**, **Follow-ups**. Specifically:\n   a. Collect all improvement suggestions from Architect and Critic responses\n   b. Deduplicate and categorize the suggestions\n   c. Update the plan file in `.omx/plans/` with the accepted improvements (add missing details, refine steps, strengthen acceptance criteria, ADR updates, etc.)\n   d. Note which improvements were applied in a brief changelog section at the end of the plan\n   e. Before any execution handoff, derive an explicit **available-agent-types roster** from the known prompt catalog and add concrete **follow-up staffing guidance** for `$ultragoal` and `$team` (recommended roles, counts, suggested reasoning levels by lane, and why each lane exists), plus an explicit `$ralph` fallback note only when persistent single-owner verification is intentionally selected\n   f. Add a product-facing **Goal-Mode Follow-up Suggestions** section: recommend `$ultragoal` by default for general goal-oriented follow-up, `$autoresearch-goal` only when the context is a research project with a research deliverable/evaluator, and `$performance-goal` when the context is an optimization or performance project. Keep these suggestions alongside the Team path and any explicit Ralph fallback rather than replacing implementation-delivery guidance. For ordinary pre-planning external docs or best-practice lookup, cite `$best-practice-research` evidence and synthesize it into the plan instead of recommending Autoresearch as a final architecture component. For durable-goal work that is also parallelizable, explicitly recommend **Team + Ultragoal**: Ultragoal remains leader-owned goal/ledger state and Team returns checkpoint-ready execution evidence.\n   g. For the `$team` path, add an explicit launch-hint block with concrete `omx team` / `$team` commands and a **team verification path** (what Team proves before shutdown and what Ultragoal checkpoints as durable completion evidence). Distinguish Team + Ultragoal from any explicit Ralph fallback: Team handles coordinated parallel lanes; Ultragoal is the default durable follow-up/ledger owner, and Ralph is only an explicitly requested legacy-style persistent sequential verification/fix lane when needed.\n7. On Critic approval (with improvements applied): *(--interactive only)* If running with `--interactive`, use `AskUserQuestion` / the structured question UI to present the plan with these options:\n   - **Approve durable goal execution** — proceed via `$ultragoal` by default (optionally with `$team` for parallel lanes)\n   - **Approve and implement via team** — proceed to implementation via coordinated parallel team agents\n   - **Start goal-mode follow-up** — proceed via `$ultragoal` by default, or `$autoresearch-goal` / `$performance-goal` when the approved plan specifically fits research validation or measurable optimization\n   - **Request changes** — return to step 1 with user feedback\n   - **Reject** — discard the plan entirely\n   If NOT running with `--interactive`, output the final approved plan and stop. Do NOT auto-execute.\n8. *(--interactive only)* User chooses via the structured question UI (never ask for approval in plain text when a structured surface is available)\n9. On user approval (--interactive only):\n   - **Approve durable goal execution**: **MUST** invoke `$ultragoal` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete role allocation guidance, and direct launch hints for Ultragoal follow-up work**. Use `$team` alongside Ultragoal when parallel lanes are warranted. Do NOT implement directly. Do NOT edit source code files in the planning agent. Ralph is not the default follow-up; only invoke `$ralph` when the user explicitly selects a legacy/persistent single-owner execution lane.\n   - **Approve and implement via team**: **MUST** invoke `$team` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete staffing / worker-role allocation guidance, explicit `omx team` / `$team` launch hints, and the team verification path**. Do NOT implement directly. The team skill coordinates parallel agents across the staged pipeline for faster execution on large tasks.\n   - **Start goal-mode follow-up**: **MUST** invoke the selected goal workflow with the approved plan path and appropriate success context: `$ultragoal` as the default goal-mode path, `$autoresearch-goal` for research projects, or `$performance-goal` for optimization/performance projects with measurable evaluator criteria. Do NOT implement directly in the planning agent.\n\n### Review Mode (`--review`)\n\n0. Treat review as a reviewer-only pass. The context that wrote the plan, cleanup proposal, or diff MUST NOT be the context that approves it.\n1. Read plan file from `.omx/plans/`\n2. Evaluate via Critic using `ask_codex` with `agent_role: \"critic\"`\n3. For cleanup/refactor/anti-slop work, verify that the artifact includes a cleanup plan, regression tests or an explicit test gap, smell-by-smell passes, and quality gates.\n4. Return verdict: APPROVED, REVISE (with specific feedback), or REJECT (replanning required)\n5. If the current context authored the artifact, hand the review to `$code-review`, `critic`, `quality-reviewer`, or `verifier` as appropriate.\n\n### Plan Output Format\n\nEvery plan includes:\n- Requirements Summary\n- Acceptance Criteria (testable)\n- Implementation Steps (with file references)\n- Adaptive step count sized to the actual scope (not a fixed five-step template)\n- Risks and Mitigations\n- Verification Steps\n- For consensus/ralplan: **RALPLAN-DR summary** (Principles, Decision Drivers, Options)\n- For consensus/ralplan final output: **ADR** (Decision, Drivers, Alternatives considered, Why chosen, Consequences, Follow-ups)\n- For consensus/ralplan execution handoff: **Available-Agent-Types Roster**, **Follow-up Staffing Guidance** (including suggested reasoning levels by lane), product-facing **Goal-Mode Follow-up Suggestions** (`$ultragoal`, `$autoresearch-goal`, `$performance-goal` when contextually appropriate), explicit `omx team` / `$team` **Launch Hints**, and **Team Verification Path**\n- For deliberate consensus mode: **Pre-mortem (3 scenarios)** and **Expanded Test Plan** (unit/integration/e2e/observability)\n\nPlans are saved to `.omx/plans/`. Drafts go to `.omx/drafts/`.\n</Steps>\n\n<Tool_Usage>\n- Use `AskUserQuestion` for preference questions (scope, priority, timeline, risk tolerance) -- provides clickable UI\n- Use plain text for questions needing specific values (port numbers, names, follow-up clarifications)\n- Use the `explore` agent (LOW tier, bounded quick pass) to gather codebase facts before asking the user\n- Use `ask_codex` with `agent_role: \"planner\"` for planning validation on large-scope plans\n- Use `ask_codex` with `agent_role: \"analyst\"` for requirements analysis\n- Use `ask_codex` with `agent_role: \"critic\"` for standalone review mode. In consensus mode, use the dedicated sequential role-specific `Architect` and `Critic` subagents described in steps 3-4 instead of a single critic-only review call.\n- If optional MCP compatibility tools or Codex consultation are unavailable, fall back to equivalent OMX prompt/native agents -- never block on external tools\n- **CRITICAL — Consensus mode agent calls MUST be sequential, never parallel.** Always await the subsequent role-specific `Architect` result before issuing the subsequent role-specific `Critic` call.\n- In consensus mode, default to RALPLAN-DR short mode; enable deliberate mode on `--deliberate` or explicit high-risk signals (auth/security, migrations, destructive changes, production incidents, compliance/PII, public API breakage)\n- In consensus mode with `--interactive`: use `AskUserQuestion` / the structured question UI for the user feedback step (step 2) and the final approval step (step 7) -- never ask for approval in plain text when a structured surface is available. Without `--interactive`, auto-proceed through planning steps without pausing. Output the final plan without execution.\n- In consensus mode with `--interactive`, on user approval **MUST** invoke the selected follow-up lane from step 9 (`$ultragoal`, `$team`, `$autoresearch-goal`, `$performance-goal`, or explicit `$ralph` fallback) -- never implement directly in the planning agent\n- In consensus mode, execution follow-up handoff **MUST** include an explicit available-agent-types roster plus concrete staffing / role-allocation guidance grounded in that roster, suggested reasoning levels by lane, product-facing goal-mode follow-up suggestions (`$ultragoal` by default, `$autoresearch-goal` for research projects, `$performance-goal` for optimization/performance projects), explicit `omx team` / `$team` launch hints, and a team verification path. For parallelizable durable-goal plans, recommend Team + Ultragoal with leader-owned checkpointing from Team evidence; reserve Ralph for persistent sequential single-owner verification/fix follow-up.\n</Tool_Usage>\n\n## Scenario Examples\n\n**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.\n\n**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.\n\n**Bad:** The user says `continue`, and the workflow restarts discovery or stops before the missing verification/evidence is gathered.\n\n<Examples>\n<Good>\nAdaptive interview (gathering facts before asking):\n```\nPlanner: [spawns explore agent: \"find authentication implementation\"]\nPlanner: [receives: \"Auth is in src/auth/ using JWT with passport.js\"]\nPlanner: \"I see you're using JWT authentication with passport.js in src/auth/.\n         For this new feature, should we extend the existing auth or add a separate auth flow?\"\n```\nWhy good: Answers its own codebase question first, then asks an informed preference question.\n</Good>\n\n<Good>\nSingle question at a time:\n```\nQ1: \"What's the main goal?\"\nA1: \"Improve performance\"\nQ2: \"For performance, what matters more -- latency or throughput?\"\nA2: \"Latency\"\nQ3: \"For latency, are we optimizing for p50 or p99?\"\n```\nWhy good: Each question builds on the previous answer. Focused and progressive.\n</Good>\n\n<Bad>\nAsking about things you could look up:\n```\nPlanner: \"Where is authentication implemented in your codebase?\"\nUser: \"Uh, somewhere in src/auth I think?\"\n```\nWhy bad: The planner should spawn an explore agent to find this, not ask the user.\n</Bad>\n\n<Bad>\nBatching multiple questions:\n```\n\"What's the scope? And the timeline? And who's the audience?\"\n```\nWhy bad: Three questions at once causes shallow answers. Ask one at a time.\n</Bad>\n\n<Bad>\nPresenting all design options at once:\n```\n\"Here are 4 approaches: Option A... Option B... Option C... Option D... Which do you prefer?\"\n```\nWhy bad: Decision fatigue. Present one option with trade-offs, get reaction, then present the next.\n</Bad>\n</Examples>\n\n<Escalation_And_Stop_Conditions>\n- Stop interviewing when requirements are clear enough to plan -- do not over-interview\n- In consensus mode, stop after 5 Planner/Architect/Critic iterations and present the best version\n- Consensus mode outputs the plan by default; with `--interactive`, user can approve and hand off to ultragoal/team, with Ralph only as an explicit legacy/persistent single-owner lane\n- If the user says \"just do it\" or \"skip planning\", **MUST** invoke `$ultragoal` to transition to durable goal execution mode by default; use `$ralph` only when the user explicitly asks for that fallback. Do NOT implement directly in the planning agent.\n- Escalate to the user when there are irreconcilable trade-offs that require a business decision\n</Escalation_And_Stop_Conditions>\n\n<Final_Checklist>\n",
  "exit_code": 0,
  "duration": {
    "secs": 0,
    "nanos": 253167
  },
  "formatted_output": "---\nname: plan\ndescription: \"[OMX] Strategic planning with optional interview workflow\"\n---\n\n<Purpose>\nPlan creates comprehensive, actionable work plans through intelligent interaction. It auto-detects whether to interview the user (broad requests) or plan directly (detailed requests), and supports consensus mode (iterative Planner/Architect/Critic loop with RALPLAN-DR structured deliberation) and review mode (Critic evaluation of existing plans).\n</Purpose>\n\n<Use_When>\n- User wants to plan before implementing -- \"plan this\", \"plan the\", \"let's plan\"\n- User wants structured requirements gathering for a vague idea\n- User wants an existing plan reviewed -- \"review this plan\", `--review`\n- User wants multi-perspective consensus on a plan -- `--consensus`, \"ralplan\"\n- Task is broad or vague and needs scoping before any code is written\n</Use_When>\n\n<Do_Not_Use_When>\n- User wants autonomous end-to-end execution -- use `autopilot` instead\n- User wants to start coding immediately with a clear task -- use `ralph` or delegate to executor\n- User asks a simple question that can be answered directly -- just answer it\n- Task is a single focused fix with obvious scope -- skip planning, just do it\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nJumping into code without understanding requirements leads to rework, scope creep, and missed edge cases. Plan provides structured requirements gathering, expert analysis, and quality-gated plans so that execution starts from a solid foundation. The consensus mode adds multi-perspective validation for high-stakes projects.\n</Why_This_Exists>\n\n<Execution_Policy>\n- Auto-detect interview vs direct mode based on request specificity\n- Ask one question at a time during interviews -- never batch multiple interview rounds into one question form\n- Gather codebase facts via `explore` agent before asking the user about them\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only repository lookups during planning; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep prompt-heavy or ambiguous planning work on the richer normal path.\n- Plans must meet quality standards: 80%+ claims cite file/line, 90%+ criteria are testable\n- Implementation step count must be right-sized to task scope; avoid defaulting to exactly five steps when the work is clearly smaller or larger\n- Consensus mode outputs the final plan by default; add `--interactive` to enable execution handoff\n- Consensus mode uses RALPLAN-DR short mode by default; switch to deliberate mode with `--deliberate` or when the request explicitly signals high risk (auth/security, data migration, destructive/irreversible changes, production incident, compliance/PII, public API breakage)\n- Apply the shared workflow guidance pattern: outcome-first framing, concise visible updates for multi-step planning, local overrides for the active workflow branch, evidence-backed planning and validation expectations, explicit stop rules, and automatic continuation for safe reversible steps. Ask only for material, destructive, credentialed, external-production, or preference-dependent branches.\n</Execution_Policy>\n\n<Steps>\n\n### Mode Selection\n\n| Mode | Trigger | Behavior |\n|------|---------|----------|\n| Interview | Default for broad requests | Interactive requirements gathering |\n| Direct | `--direct`, or detailed request | Skip interview, generate plan directly |\n| Consensus | `--consensus`, \"ralplan\" | Planner -> Architect -> Critic loop until agreement with RALPLAN-DR structured deliberation (short by default, `--deliberate` for high-risk); outputs plan by default |\n| Consensus Interactive | `--consensus --interactive` | Same as Consensus but pauses for user feedback at draft and approval steps, then hands off to execution |\n| Review | `--review`, \"review this plan\" | Critic evaluation of existing plan |\n\n### Interview Mode (broad/vague requests)\n\n1. **Classify the request**: Broad (vague verbs, no specific files, touches 3+ areas) triggers interview mode\n2. **Ask one focused question** using the surface-appropriate structured question path for preferences, scope, and constraints: in attached-tmux OMX runtime use `omx question`; outside tmux use native structured input when available; use plain text only as a last fallback\n3. **Gather codebase facts first**: Before asking \"what patterns does your code use?\", spawn an `explore` agent to find out, then ask informed follow-up questions\n4. **Build on answers**: Each question builds on the previous answer\n5. **Consult Analyst** (THOROUGH tier) for hidden requirements, edge cases, and risks\n6. **Create plan** when the user signals readiness: \"create the plan\", \"I'm ready\", \"make it a work plan\"\n\n### Direct Mode (detailed requests)\n\n1. **Quick Analysis**: Optional brief Analyst consultation\n2. **Create plan**: Generate comprehensive work plan immediately\n3. **Review** (optional): Critic review if requested\n\n### Consensus Mode (`--consensus` / \"ralplan\")\n\n**RALPLAN-DR modes**: **Short** (default, bounded structure) and **Deliberate** (for `--deliberate` or explicit high-risk requests). Both modes keep the same Planner -> Architect -> Critic sequence. The workflow auto-proceeds through planning steps (Planner/Architect/Critic) but outputs the final plan without executing.\n\n1. **Planner** creates initial plan and a compact **RALPLAN-DR summary** before any Architect review. The summary **MUST** include:\n   - **Principles** (3-5)\n   - **Decision Drivers** (top 3)\n   - **Viable Options** (>=2) with bounded pros/cons for each option\n   - If only one viable option remains, an explicit **invalidation rationale** for the alternatives that were rejected\n   - In **deliberate mode**: a **pre-mortem** (3 failure scenarios) and an **expanded test plan** covering **unit / integration / e2e / observability**\n2. **User feedback** *(--interactive only)*: If running with `--interactive`, **MUST** use `AskUserQuestion` / the structured question UI (`omx question` in attached tmux; native structured input outside tmux when available) to present the draft plan **plus the RALPLAN-DR Principles / Decision Drivers / Options summary for early direction alignment** with these options:\n   - **Proceed to review** — send to Architect and Critic for evaluation\n   - **Request changes** — return to step 1 with user feedback incorporated\n   - **Skip review** — go directly to final approval (step 7)\n   If NOT running with `--interactive`, automatically proceed to review (step 3).\n3. **Architect** reviews for architectural soundness as a dedicated subsequent `Architect` subagent with the full task, current plan text/path, RALPLAN-DR summary, and relevant artifact context. Architect review **MUST** include: strongest steelman counterargument (antithesis) against the favored option, at least one meaningful tradeoff tension, and (when possible) a synthesis path. In deliberate mode, Architect should explicitly flag principle violations. **Wait for this step to complete before proceeding to step 4.** Do NOT run steps 3 and 4 in parallel. Do NOT substitute a default/improvised subagent prompt for the role-specific `Architect` prompt.\n4. **Critic** evaluates against quality criteria as a dedicated subsequent `Critic` subagent with the full task, current plan text/path, RALPLAN-DR summary, artifact context, and the completed `Architect` result. Critic **MUST** verify principle-option consistency, fair alternative exploration, risk mitigation clarity, testable acceptance criteria, and concrete verification steps. Critic **MUST** explicitly reject shallow alternatives, driver contradictions, vague risks, or weak verification. In deliberate mode, Critic **MUST** reject missing/weak pre-mortem or missing/weak expanded test plan. Run only after step 3 is complete. Do NOT let the `Architect` response self-approve the Critic gate.\n5. **Re-review loop** (max 5 iterations): If Critic rejects or iterates, execute this closed loop:\n   a. Collect all feedback from Architect + Critic\n   b. Pass feedback to Planner to produce a revised plan\n   c. **Return to Step 3** — Architect reviews the revised plan\n   d. **Return to Step 4** — Critic evaluates the revised plan\n   e. Repeat until Critic approves OR max 5 iterations reached\n   f. If max iterations reached without approval, present the best version to user via the structured question UI with note that expert consensus was not reached\n6. **Apply improvements**: When reviewers approve with improvement suggestions, merge all accepted improvements into the plan file before proceeding. Final consensus output **MUST** include an **ADR** section with: **Decision**, **Drivers**, **Alternatives considered**, **Why chosen**, **Consequences**, **Follow-ups**. Specifically:\n   a. Collect all improvement suggestions from Architect and Critic responses\n   b. Deduplicate and categorize the suggestions\n   c. Update the plan file in `.omx/plans/` with the accepted improvements (add missing details, refine steps, strengthen acceptance criteria, ADR updates, etc.)\n   d. Note which improvements were applied in a brief changelog section at the end of the plan\n   e. Before any execution handoff, derive an explicit **available-agent-types roster** from the known prompt catalog and add concrete **follow-up staffing guidance** for `$ultragoal` and `$team` (recommended roles, counts, suggested reasoning levels by lane, and why each lane exists), plus an explicit `$ralph` fallback note only when persistent single-owner verification is intentionally selected\n   f. Add a product-facing **Goal-Mode Follow-up Suggestions** section: recommend `$ultragoal` by default for general goal-oriented follow-up, `$autoresearch-goal` only when the context is a research project with a research deliverable/evaluator, and `$performance-goal` when the context is an optimization or performance project. Keep these suggestions alongside the Team path and any explicit Ralph fallback rather than replacing implementation-delivery guidance. For ordinary pre-planning external docs or best-practice lookup, cite `$best-practice-research` evidence and synthesize it into the plan instead of recommending Autoresearch as a final architecture component. For durable-goal work that is also parallelizable, explicitly recommend **Team + Ultragoal**: Ultragoal remains leader-owned goal/ledger state and Team returns checkpoint-ready execution evidence.\n   g. For the `$team` path, add an explicit launch-hint block with concrete `omx team` / `$team` commands and a **team verification path** (what Team proves before shutdown and what Ultragoal checkpoints as durable completion evidence). Distinguish Team + Ultragoal from any explicit Ralph fallback: Team handles coordinated parallel lanes; Ultragoal is the default durable follow-up/ledger owner, and Ralph is only an explicitly requested legacy-style persistent sequential verification/fix lane when needed.\n7. On Critic approval (with improvements applied): *(--interactive only)* If running with `--interactive`, use `AskUserQuestion` / the structured question UI to present the plan with these options:\n   - **Approve durable goal execution** — proceed via `$ultragoal` by default (optionally with `$team` for parallel lanes)\n   - **Approve and implement via team** — proceed to implementation via coordinated parallel team agents\n   - **Start goal-mode follow-up** — proceed via `$ultragoal` by default, or `$autoresearch-goal` / `$performance-goal` when the approved plan specifically fits research validation or measurable optimization\n   - **Request changes** — return to step 1 with user feedback\n   - **Reject** — discard the plan entirely\n   If NOT running with `--interactive`, output the final approved plan and stop. Do NOT auto-execute.\n8. *(--interactive only)* User chooses via the structured question UI (never ask for approval in plain text when a structured surface is available)\n9. On user approval (--interactive only):\n   - **Approve durable goal execution**: **MUST** invoke `$ultragoal` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete role allocation guidance, and direct launch hints for Ultragoal follow-up work**. Use `$team` alongside Ultragoal when parallel lanes are warranted. Do NOT implement directly. Do NOT edit source code files in the planning agent. Ralph is not the default follow-up; only invoke `$ralph` when the user explicitly selects a legacy/persistent single-owner execution lane.\n   - **Approve and implement via team**: **MUST** invoke `$team` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete staffing / worker-role allocation guidance, explicit `omx team` / `$team` launch hints, and the team verification path**. Do NOT implement directly. The team skill coordinates parallel agents across the staged pipeline for faster execution on large tasks.\n   - **Start goal-mode follow-up**: **MUST** invoke the selected goal workflow with the approved plan path and appropriate success context: `$ultragoal` as the default goal-mode path, `$autoresearch-goal` for research projects, or `$performance-goal` for optimization/performance projects with measurable evaluator criteria. Do NOT implement directly in the planning agent.\n\n### Review Mode (`--review`)\n\n0. Treat review as a reviewer-only pass. The context that wrote the plan, cleanup proposal, or diff MUST NOT be the context that approves it.\n1. Read plan file from `.omx/plans/`\n2. Evaluate via Critic using `ask_codex` with `agent_role: \"critic\"`\n3. For cleanup/refactor/anti-slop work, verify that the artifact includes a cleanup plan, regression tests or an explicit test gap, smell-by-smell passes, and quality gates.\n4. Return verdict: APPROVED, REVISE (with specific feedback), or REJECT (replanning required)\n5. If the current context authored the artifact, hand the review to `$code-review`, `critic`, `quality-reviewer`, or `verifier` as appropriate.\n\n### Plan Output Format\n\nEvery plan includes:\n- Requirements Summary\n- Acceptance Criteria (testable)\n- Implementation Steps (with file references)\n- Adaptive step count sized to the actual scope (not a fixed five-step template)\n- Risks and Mitigations\n- Verification Steps\n- For consensus/ralplan: **RALPLAN-DR summary** (Principles, Decision Drivers, Options)\n- For consensus/ralplan final output: **ADR** (Decision, Drivers, Alternatives considered, Why chosen, Consequences, Follow-ups)\n- For consensus/ralplan execution handoff: **Available-Agent-Types Roster**, **Follow-up Staffing Guidance** (including suggested reasoning levels by lane), product-facing **Goal-Mode Follow-up Suggestions** (`$ultragoal`, `$autoresearch-goal`, `$performance-goal` when contextually appropriate), explicit `omx team` / `$team` **Launch Hints**, and **Team Verification Path**\n- For deliberate consensus mode: **Pre-mortem (3 scenarios)** and **Expanded Test Plan** (unit/integration/e2e/observability)\n\nPlans are saved to `.omx/plans/`. Drafts go to `.omx/drafts/`.\n</Steps>\n\n<Tool_Usage>\n- Use `AskUserQuestion` for preference questions (scope, priority, timeline, risk tolerance) -- provides clickable UI\n- Use plain text for questions needing specific values (port numbers, names, follow-up clarifications)\n- Use the `explore` agent (LOW tier, bounded quick pass) to gather codebase facts before asking the user\n- Use `ask_codex` with `agent_role: \"planner\"` for planning validation on large-scope plans\n- Use `ask_codex` with `agent_role: \"analyst\"` for requirements analysis\n- Use `ask_codex` with `agent_role: \"critic\"` for standalone review mode. In consensus mode, use the dedicated sequential role-specific `Architect` and `Critic` subagents described in steps 3-4 instead of a single critic-only review call.\n- If optional MCP compatibility tools or Codex consultation are unavailable, fall back to equivalent OMX prompt/native agents -- never block on external tools\n- **CRITICAL — Consensus mode agent calls MUST be sequential, never parallel.** Always await the subsequent role-specific `Architect` result before issuing the subsequent role-specific `Critic` call.\n- In consensus mode, default to RALPLAN-DR short mode; enable deliberate mode on `--deliberate` or explicit high-risk signals (auth/security, migrations, destructive changes, production incidents, compliance/PII, public API breakage)\n- In consensus mode with `--interactive`: use `AskUserQuestion` / the structured question UI for the user feedback step (step 2) and the final approval step (step 7) -- never ask for approval in plain text when a structured surface is available. Without `--interactive`, auto-proceed through planning steps without pausing. Output the final plan without execution.\n- In consensus mode with `--interactive`, on user approval **MUST** invoke the selected follow-up lane from step 9 (`$ultragoal`, `$team`, `$autoresearch-goal`, `$performance-goal`, or explicit `$ralph` fallback) -- never implement directly in the planning agent\n- In consensus mode, execution follow-up handoff **MUST** include an explicit available-agent-types roster plus concrete staffing / role-allocation guidance grounded in that roster, suggested reasoning levels by lane, product-facing goal-mode follow-up suggestions (`$ultragoal` by default, `$autoresearch-goal` for research projects, `$performance-goal` for optimization/performance projects), explicit `omx team` / `$team` launch hints, and a team verification path. For parallelizable durable-goal plans, recommend Team + Ultragoal with leader-owned checkpointing from Team evidence; reserve Ralph for persistent sequential single-owner verification/fix follow-up.\n</Tool_Usage>\n\n## Scenario Examples\n\n**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.\n\n**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.\n\n**Bad:** The user says `continue`, and the workflow restarts discovery or stops before the missing verification/evidence is gathered.\n\n<Examples>\n<Good>\nAdaptive interview (gathering facts before asking):\n```\nPlanner: [spawns explore agent: \"find authentication implementation\"]\nPlanner: [receives: \"Auth is in src/auth/ using JWT with passport.js\"]\nPlanner: \"I see you're using JWT authentication with passport.js in src/auth/.\n         For this new feature, should we extend the existing auth or add a separate auth flow?\"\n```\nWhy good: Answers its own codebase question first, then asks an informed preference question.\n</Good>\n\n<Good>\nSingle question at a time:\n```\nQ1: \"What's the main goal?\"\nA1: \"Improve performance\"\nQ2: \"For performance, what matters more -- latency or throughput?\"\nA2: \"Latency\"\nQ3: \"For latency, are we optimizing for p50 or p99?\"\n```\nWhy good: Each question builds on the previous answer. Focused and progressive.\n</Good>\n\n<Bad>\nAsking about things you could look up:\n```\nPlanner: \"Where is authentication implemented in your codebase?\"\nUser: \"Uh, somewhere in src/auth I think?\"\n```\nWhy bad: The planner should spawn an explore agent to find this, not ask the user.\n</Bad>\n\n<Bad>\nBatching multiple questions:\n```\n\"What's the scope? And the timeline? And who's the audience?\"\n```\nWhy bad: Three questions at once causes shallow answers. Ask one at a time.\n</Bad>\n\n<Bad>\nPresenting all design options at once:\n```\n\"Here are 4 approaches: Option A... Option B... Option C... Option D... Which do you prefer?\"\n```\nWhy bad: Decision fatigue. Present one option with trade-offs, get reaction, then present the next.\n</Bad>\n</Examples>\n\n<Escalation_And_Stop_Conditions>\n- Stop interviewing when requirements are clear enough to plan -- do not over-interview\n- In consensus mode, stop after 5 Planner/Architect/Critic iterations and present the best version\n- Consensus mode outputs the plan by default; with `--interactive`, user can approve and hand off to ultragoal/team, with Ralph only as an explicit legacy/persistent single-owner lane\n- If the user says \"just do it\" or \"skip planning\", **MUST** invoke `$ultragoal` to transition to durable goal execution mode by default; use `$ralph` only when the user explicitly asks for that fallback. Do NOT implement directly in the planning agent.\n- Escalate to the user when there are irreconcilable trade-offs that require a business decision\n</Escalation_And_Stop_Conditions>\n\n<Final_Checklist>\n",
  "status": "completed"
}
```

## Assistant

既存ディレクトリは見ていません。抽象設計として見ると、発想はかなり妥当ですが、中心命題は少し修正した方がよいです。

**結論**
「文書をMarkdown化する」ことが目的ではなく、目的は **原文への追跡可能性を保ったまま、AIに必要な範囲だけを低トークンで渡せる知識表現を作ること** です。Markdownは有力な出力形式ですが、内部の正本にするには弱いです。座標、ページ、OCR信頼度、画像領域、表、見出し構造などを失いやすいためです。

**批判点**
1. PDF/Word/HTML/Google Docsを同列に扱うのは粗いです。HTMLやGoogle Docsはすでに構造化されています。OCRは主にスキャンPDFや写真向けで、born-digital PDFならまずテキスト層・レイアウト抽出を使うべきです。

2. OCR後Markdown化だけでは、トークン効率の問題は解決しません。巨大なMarkdownも巨大な入力です。必要なのは全文変換より、検索・要約・引用・部分展開を支える中間表現です。

3. 「ノイズ除去」は危険です。講義名や教授名は本文ではノイズでも、メタデータや出典アンカーとしては価値があります。削除ではなく、本文から分離して metadata に移す、という発想がよいです。

4. LLM校正は有効ですが、直接本文を書き換えさせると危険です。LLMは「編集候補を検出し、根拠つきパッチを提案する」役に限定し、適用前後を検証できる形にするべきです。

**仕様の整理案**
抽象構造はこう分けるとよいです。

1. **Raw Evidence Layer**  
   元PDF、ページ画像、既存テキスト層、OCR生出力を保存する。絶対に破壊しない。

2. **Extraction Layer**  
   テキストブロック、ページ番号、座標、OCR信頼度、ブロック種別、表・画像・脚注などを抽出する。ここではまだMarkdownにしない。

3. **Deterministic Cleanup Layer**  
   Unicode正規化、改行結合、ページ番号、反復ヘッダー/フッター、空白、明確なOCR崩れなどをルールで処理する。

4. **LLM Patch Layer**  
   LLMは曖昧な箇所だけを見る。役割は「検出」「理由」「修正案」「信頼度」「元位置」の出力。全文丸投げは避ける。

5. **Verification Layer**  
   原文との対応、削除された情報、低信頼箇所、LLM変更差分を監査する。ここがないと“きれいだが間違った文書”が生まれます。

6. **Context Packaging Layer**  
   AIに渡すための最小単位を作る。全文Markdown、概要、章ごとの要約、検索インデックス、引用つきチャンク、用語集を用途別に生成する。

**LLMに任せるべき判断**
LLMに任せるのは「意味的に判断が必要な編集」です。

- 反復する講義名が本文かヘッダーか判断する
- m/rn のようなOCR誤りを文脈から推定する
- 見出し・箇条書き・段落境界を復元する
- 図表の説明文を生成する
- ノイズ候補に削除/metadata化/保持の分類をつける

一方で、空白正規化、単純なヘッダー除去、ページ番号除去、重複行検出などはルール処理で十分です。

**洗練後の中心コンセプト**
「OCRでMarkdownを作るツール」ではなく、  
**文書を、証拠つき・検索可能・段階的に展開可能なAI用知識パッケージへ変換するハーネス**  
として設計すると、全体構想と実装アイディアの乖離が小さくなります。

最初に仕様化すべき軸は、`Markdown生成`ではなく、`原文保持`、`構造抽出`、`ノイズ分類`、`LLMパッチ`、`検証`、`コンテキスト組み立て` の6つです。

## User

この計画のあらゆる側面について、私たちが共通理解に達するまで徹底的に質問してください。設計ツリーの各枝をたどり、決定事項間の依存関係を一つずつ解決していきましょう。それぞれの質問に対して、あなたの推奨する回答を提示してください。

質問は一つずつしてください。

## Assistant

`deep-interview` を使います。目的は実装に入らず、設計上の分岐と依存関係を一問ずつ固定していくことです。

**Tool Call: Read SKILL.md**
Status: Completed

```json
{
  "call_id": "call_8wIalY0GFkbRHbFHqGz43XWq",
  "process_id": "34659",
  "turn_id": "019ed4c6-ca9b-7301-a157-123e1f45c928",
  "completed_at_ms": 1781686278641,
  "command": [
    "/bin/zsh",
    "-lc",
    "sed -n '1,240p' /Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/deep-interview/SKILL.md"
  ],
  "cwd": "/Users/kentaro/area_of_responsibility/extend_claude/yt-transcript",
  "parsed_cmd": [
    {
      "type": "read",
      "cmd": "sed -n '1,240p' /Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/deep-interview/SKILL.md",
      "name": "SKILL.md",
      "path": "/Users/kentaro/area_of_responsibility/extend_claude/yt-transcript/.codex/skills/deep-interview/SKILL.md"
    }
  ],
  "source": "unified_exec_startup",
  "stdout": "---\nname: deep-interview\ndescription: \"[OMX] Socratic deep interview with mathematical ambiguity gating before execution\"\nargument-hint: \"[--quick|--standard|--deep] [--autoresearch] <idea or vague description>\"\n---\n\n<Purpose>\nDeep Interview is an intent-first Socratic clarification loop before planning or implementation. It turns vague ideas into execution-ready specifications by asking targeted questions about why the user wants a change, how far it should go, what should stay out of scope, and what OMX may decide without confirmation.\n</Purpose>\n\n<Use_When>\n- The request is broad, ambiguous, or missing concrete acceptance criteria\n- The user says \"deep interview\", \"interview me\", \"ask me everything\", \"don't assume\", or \"ouroboros\"\n- The user wants to avoid misaligned implementation from underspecified requirements\n- You need a requirements artifact before handing off to `ralplan`, `autopilot`, `ralph`, or `team`\n</Use_When>\n\n<Do_Not_Use_When>\n- The request already has concrete file/symbol targets and clear acceptance criteria\n- The user explicitly asks to skip planning/interview and execute immediately\n- The user asks for lightweight brainstorming only (use `plan` instead)\n- A complete PRD/plan already exists and execution should start\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nExecution quality is usually bottlenecked by intent clarity, not just missing implementation detail. A single expansion pass often misses why the user wants a change, where the scope should stop, which tradeoffs are unacceptable, and which decisions still require user approval. This workflow applies Socratic pressure + quantitative ambiguity scoring so orchestration modes begin with an explicit, testable, intent-aligned spec.\n</Why_This_Exists>\n\n<Depth_Profiles>\n- **Quick (`--quick`)**: fast pre-PRD pass; target threshold `<= 0.30`; max rounds 5\n- **Standard (`--standard`, default)**: full requirement interview; target threshold `<= 0.20`; max rounds 12\n- **Deep (`--deep`)**: high-rigor exploration; target threshold `<= 0.15`; max rounds 20\n- **Autoresearch (`--autoresearch`)**: same interview rigor as Standard, but specialized for `$autoresearch` mission readiness and `.omx/specs/` artifact handoff\n\nProfile `max rounds` is a hard cap, not a target. Do not continue only to reach a numbered round count. Extra Socratic rigor does not override the active threshold unless the profile/config changes.\n\nIf no flag is provided, use **Standard**.\n\n<Mode_Flags>\n- **`--autoresearch`**: switch the interview into autoresearch-intake mode for `$autoresearch` handoff. In this mode, the interview should converge on a validator-ready research mission, write canonical artifacts under `.omx/specs/`, and preserve the explicit `refine further` vs `launch` boundary for downstream skill intake.\n</Mode_Flags>\n</Depth_Profiles>\n\n<Execution_Policy>\n- Ask ONE question per round (never batch multiple interview rounds into one `questions[]` form)\n- Ask about intent and boundaries before implementation detail\n- Target the weakest clarity dimension each round after applying the stage-priority rules below\n- Treat every answer as a claim to pressure-test before moving on: the next question should usually demand evidence or examples, expose a hidden assumption, force a tradeoff or boundary, or reframe root cause vs symptom\n- Do not rotate to a new clarity dimension just for coverage when the current answer is still vague; stay on the same thread until one layer deeper, one assumption clearer, or one boundary tighter\n- Before crystallizing, complete at least one explicit pressure pass that revisits an earlier answer with a deeper, assumption-focused, or tradeoff-focused follow-up\n- Gather codebase facts via `explore` before asking user about internals\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only brownfield fact gathering; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep ambiguous or non-shell-only investigation on the richer normal path.\n- Always run a preflight context intake before the first interview question\n- If initial context is oversized or would exceed the prompt budget, do not paste or forward the raw payload into interview prompts; request and record a prompt-safe initial-context summary first\n- The oversized initial-context summary gate is blocking: wait for the concise summary before ambiguity scoring, crystallizing artifacts, or any downstream execution handoff\n- The summary must preserve goals, constraints, success criteria, non-goals, decision boundaries, and references to any full source documents so downstream consumers receive a prompt-safe but faithful context\n- Keep total prompt payloads within a safe budget by summarizing or trimming retained history; preserve newest/highest-signal answers and never let raw oversized context crowd out the current question\n- Reduce user effort: ask only the highest-leverage unresolved question, and never ask the user for codebase facts that can be discovered directly\n- For brownfield work, prefer evidence-backed confirmation questions such as \"I found X in Y. Should this change follow that pattern?\"\n- Route facts before judgment in the Ouroboros style: before presenting a user-facing interview round, classify whether the needed information is a discoverable fact, a fact needing confirmation, or a human decision. The interview is with the human for judgment, not for facts the agent can inspect.\n- When unresolved ambiguity depends on current external best practices, official/upstream guidance, standards, or version-aware behavior, use `$best-practice-research` as the bounded evidence wrapper before crystallizing requirements or handing off to planning/execution.\n- Use these transcript/spec labels only; never use them as `omx question` `source` values, and never replace the runtime `source: \"deep-interview\"` contract for user-facing deep-interview questions:\n  - `[from-code][auto-confirmed]` — exact, high-confidence codebase facts from manifests/configs or direct source evidence, with no prescription attached.\n  - `[from-code]` — codebase findings that are useful but inferred, pattern-based, or low/medium confidence and therefore need a confirmation-style user-facing round before being treated as settled.\n  - `[from-research]` — externally sourced facts such as API limits, compatibility, or public documentation; facts only, not decisions.\n  - `[from-user]` — goals, preferences, business logic, scope, non-goals, acceptance criteria, tradeoffs, and any decision-bearing interpretation.\n- Treat `[from-code][auto-confirmed]` and other non-user fact discoveries as context/transcript updates, not interview rounds: do not call `omx question`, do not create a pending deep-interview question obligation, and do not increment the user-facing round number for facts the agent can safely establish.\n- Auto-confirm only descriptive facts. If a finding implies what the new feature should do, which pattern it should follow, which tradeoff to accept, or what should stay in/out of scope, route the entire decision-bearing question to the user as `[from-user]` even when code or research facts are available.\n- In attached-tmux Codex CLI, deep-interview uses `omx question` as the required OMX-owned structured questioning path for every interview round\n- When invoking `omx question` through attached-tmux Bash/tool paths, preserve the leader-pane return target by prefixing the command with `OMX_QUESTION_RETURN_PANE=$TMUX_PANE` (or a concrete `%pane` value)\n- If you launch `omx question` in a background terminal, immediately wait for that background terminal to finish and read its JSON answer before scoring ambiguity, asking another round, or handing off\n- Treat `answers[]` as the primary `omx question` success contract. For a single interview round, read `answers[0].answer`; use legacy top-level `answer` only as a compatibility fallback when needed.\n- If the current runtime is outside tmux and cannot render `omx question`, use the native structured question tool when available; otherwise ask exactly one concise plain-text question and wait for the answer\n- Re-score ambiguity after each answer and show progress transparently\n- Once ambiguity is at or below the active profile threshold, stop ordinary questioning. Run the practical closure audit: crystallize/handoff when readiness gates pass; otherwise ask only the final closure question needed to satisfy a named gate.\n- Treat `max_rounds` as a stop cap, not evidence that more rounds are needed.\n- Do not hand off to execution while ambiguity remains above threshold unless user explicitly opts to proceed with warning\n- Do not crystallize or hand off while `Non-goals` or `Decision Boundaries` remain unresolved, even if the weighted ambiguity threshold is met\n- Treat early exit as a safety valve, not the default success path\n- Persist mode state for resume safety with CLI-first state commands (`omx state write/read --input '<json>' --json`); use `state_write` / `state_read` only when explicit MCP compatibility is enabled\n</Execution_Policy>\n\n<Steps>\n\n## Phase 0: Preflight Context Intake\n\n1. Parse `{{ARGUMENTS}}` and derive a short task slug.\n2. Attempt to load the latest relevant context snapshot from `.omx/context/{slug}-*.md`.\n3. Check whether the provided initial context or loaded snapshot is too large for safe prompt use. If it is oversized, the first interview round must ask for a concise prompt-safe summary instead of scoring ambiguity or continuing to downstream handoff.\n4. If no snapshot exists, create a minimum context snapshot with:\n   - Task statement\n   - Desired outcome\n   - Stated solution (what the user asked for)\n   - Probable intent hypothesis (why they likely want it)\n   - Known facts/evidence\n   - Constraints\n   - Unknowns/open questions\n   - Decision-boundary unknowns\n   - Likely codebase touchpoints\n   - Prompt-safe initial-context summary status (`not_needed`, `needed`, or `recorded`)\n5. Save snapshot to `.omx/context/{slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) and reference it in mode state.\n\n## Phase 1: Initialize\n\n1. Parse `{{ARGUMENTS}}` and depth profile (`--quick|--standard|--deep`).\n2. Detect project context:\n   - Run `explore` to classify **brownfield** (existing codebase target) vs **greenfield**.\n   - For brownfield, collect relevant codebase context before questioning.\n3. Initialize state via `omx state write --input '{\"mode\":\"deep-interview\",\"active\":true}' --json`:\n\n```json\n{\n  \"active\": true,\n  \"current_phase\": \"deep-interview\",\n  \"state\": {\n    \"interview_id\": \"<uuid>\",\n    \"profile\": \"quick|standard|deep\",\n    \"type\": \"greenfield|brownfield\",\n    \"initial_idea\": \"<user input>\",\n    \"rounds\": [],\n    \"current_ambiguity\": 1.0,\n    \"threshold\": 0.3,\n    \"max_rounds\": 5,\n    \"challenge_modes_used\": [],\n    \"codebase_context\": null,\n    \"current_stage\": \"intent-first\",\n    \"current_focus\": \"intent\",\n    \"context_snapshot_path\": \".omx/context/<slug>-<timestamp>.md\"\n  }\n}\n```\n\n4. Announce kickoff with profile, threshold, and current ambiguity.\n\n## Phase 2: Socratic Interview Loop\n\nRepeat until ambiguity `<= threshold`, the pressure pass is complete, the readiness gates are explicit, the user exits with warning, or max rounds are reached. This is a stop condition: below threshold, do not open a new ordinary interview branch.\n\n### 2a) Generate next question\nIf the initial context is oversized and no prompt-safe summary has been recorded yet, the next question must be only a summary request. Do not score ambiguity, do not run readiness gates, and do not hand off to `$ralplan`, `$autopilot`, `$ralph`, or `$team` until that summary answer is captured.\n\nUse:\n- Original idea\n- Prior Q&A rounds\n- Current dimension scores\n- Brownfield context (if any)\n- Activated challenge mode injection (Phase 3)\n\nTarget the lowest-scoring dimension, but respect stage priority:\n- **Stage 1 — Intent-first:** Intent, Outcome, Scope, Non-goals, Decision Boundaries\n- **Stage 2 — Feasibility:** Constraints, Success Criteria\n- **Stage 3 — Brownfield grounding:** Context Clarity (brownfield only)\n\nFollow-up pressure ladder after each answer:\n1. Ask for a concrete example, counterexample, or evidence signal behind the latest claim\n2. Probe the hidden assumption, dependency, or belief that makes the claim true\n3. Force a boundary or tradeoff: what would you explicitly not do, defer, or reject?\n4. If the answer still describes symptoms, reframe toward essence / root cause before moving on\n\nPrefer staying on the same thread for multiple rounds when it has the highest leverage. Breadth without pressure is not progress.\n\nMaintain a **Breadth Ledger** across independent ambiguity tracks: scope, constraints, outputs, verification, brownfield integration, and any user-mentioned deliverable tracks. The ledger is a guard, not a mandatory rotation rule: stay deep on the current thread until it has been pressure-tested, then zoom out only when another material track remains unresolved and would change execution.\n\nDetailed dimensions:\n- Intent Clarity — why the user wants this\n- Outcome Clarity — what end state they want\n- Scope Clarity — how far the change should go\n- Constraint Clarity — technical or business limits that must hold\n- Success Criteria Clarity — how completion will be judged\n- Context Clarity — existing codebase understanding (brownfield only)\n\n`Non-goals` and `Decision Boundaries` are mandatory readiness gates. Ask about them early and keep revisiting them until they are explicit.\n\n### 2b) Ask the question\nUse the surface-appropriate structured questioning path for every interview round. In attached-tmux sessions, use OMX-owned structured questioning via `omx question` (this is the required structured-question equivalent and required `AskUserQuestion` equivalent for deep-interview). Outside tmux, use native structured input when available; otherwise ask exactly one concise plain-text question and wait for the answer. Present:\n\n```\nRound {n} | Target: {weakest_dimension} | Ambiguity: {score}%\n\n{question}\n```\n\n`omx question` payload guidance for interview rounds:\n- Deep-interview is Socratic: ask one focused round at a time. Do not use batch `questions[]` to combine multiple interview rounds, even though `omx question` supports batch forms for other workflows.\n- Use canonical `type` values instead of authoring raw `multi_select` flags by hand. `type: \"single-answerable\"` is the default for one-path decisions; `type: \"multi-answerable\"` is the canonical shape for bounded multi-select rounds. The runtime will keep `multi_select` aligned with `type`.\n- Use `single-answerable` when exactly one answer should drive the next branch, the options are mutually exclusive, or selecting more than one answer would blur the decision boundary. Typical cases: handoff lane selection, choosing the primary failure mode, or confirming which of several competing interpretations is correct.\n- Use `multi-answerable` when multiple options may all be true at once and you need to capture a bounded set of coexisting constraints, non-goals, risks, or acceptance checks in one round. Typical cases: selecting all out-of-scope items, all success metrics that must hold, or all deployment constraints that apply together.\n- If one selected option would immediately require a follow-up question to disambiguate the others, prefer a `single-answerable` round now and ask the follow-up next. Do not hide a branching interview tree inside one overloaded multi-select prompt.\n- Keep interview options bounded and concrete. If the valid answers are already known, set `allow_other: false`; only leave `allow_other: true` when the interview genuinely needs one user-supplied option that cannot be enumerated in advance.\n- Read answers structurally from the primary `answers[]` array. For a normal single-round interview response, use `answers[0].answer` as the source of truth; the top-level `answer` field is a legacy single-question projection/fallback only.\n- For `single-answerable`, expect one decisive selection in the `value` field of `answers[0].answer` plus its selected-values metadata. For `multi-answerable`, treat the selected-values field inside `answers[0].answer` as the source of truth for all chosen constraints/non-goals and preserve the full set in the transcript/spec. In legacy single-question projections, this is equivalent to: For `multi-answerable`, treat `answer.selected_values` as the source of truth.\n\nCanonical bounded single-choice payload:\n\n```json\n{\n  \"question\": \"Which execution lane should own this once the interview is complete?\",\n  \"type\": \"single-answerable\",\n  \"options\": [\n    {\n      \"label\": \"Plan first\",\n      \"value\": \"ralplan\",\n      \"description\": \"Need architecture and test-shape review before execution\"\n    },\n    {\n      \"label\": \"Execute directly\",\n      \"value\": \"autopilot\",\n      \"description\": \"Requirements are already explicit enough for planning plus execution\"\n    },\n    {\n      \"label\": \"Refine further\",\n      \"value\": \"refine\",\n      \"description\": \"Clarification is still needed before any handoff\"\n    }\n  ],\n  \"allow_other\": false,\n  \"other_label\": \"Other\",\n  \"source\": \"deep-interview\"\n}\n```\n\nCanonical bounded multi-select payload:\n\n```json\n{\n  \"question\": \"Which non-goals must stay out of scope for the first pass?\",\n  \"type\": \"multi-answerable\",\n  \"options\": [\n    {\n      \"label\": \"No UI redesign\",\n      \"value\": \"no-ui-redesign\",\n      \"description\": \"Keep layout and styling unchanged\"\n    },\n    {\n      \"label\": \"No new dependencies\",\n      \"value\": \"no-new-dependencies\",\n      \"description\": \"Work within the existing toolchain\"\n    },\n    {\n      \"label\": \"No API contract changes\",\n",
  "stderr": "",
  "aggregated_output": "---\nname: deep-interview\ndescription: \"[OMX] Socratic deep interview with mathematical ambiguity gating before execution\"\nargument-hint: \"[--quick|--standard|--deep] [--autoresearch] <idea or vague description>\"\n---\n\n<Purpose>\nDeep Interview is an intent-first Socratic clarification loop before planning or implementation. It turns vague ideas into execution-ready specifications by asking targeted questions about why the user wants a change, how far it should go, what should stay out of scope, and what OMX may decide without confirmation.\n</Purpose>\n\n<Use_When>\n- The request is broad, ambiguous, or missing concrete acceptance criteria\n- The user says \"deep interview\", \"interview me\", \"ask me everything\", \"don't assume\", or \"ouroboros\"\n- The user wants to avoid misaligned implementation from underspecified requirements\n- You need a requirements artifact before handing off to `ralplan`, `autopilot`, `ralph`, or `team`\n</Use_When>\n\n<Do_Not_Use_When>\n- The request already has concrete file/symbol targets and clear acceptance criteria\n- The user explicitly asks to skip planning/interview and execute immediately\n- The user asks for lightweight brainstorming only (use `plan` instead)\n- A complete PRD/plan already exists and execution should start\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nExecution quality is usually bottlenecked by intent clarity, not just missing implementation detail. A single expansion pass often misses why the user wants a change, where the scope should stop, which tradeoffs are unacceptable, and which decisions still require user approval. This workflow applies Socratic pressure + quantitative ambiguity scoring so orchestration modes begin with an explicit, testable, intent-aligned spec.\n</Why_This_Exists>\n\n<Depth_Profiles>\n- **Quick (`--quick`)**: fast pre-PRD pass; target threshold `<= 0.30`; max rounds 5\n- **Standard (`--standard`, default)**: full requirement interview; target threshold `<= 0.20`; max rounds 12\n- **Deep (`--deep`)**: high-rigor exploration; target threshold `<= 0.15`; max rounds 20\n- **Autoresearch (`--autoresearch`)**: same interview rigor as Standard, but specialized for `$autoresearch` mission readiness and `.omx/specs/` artifact handoff\n\nProfile `max rounds` is a hard cap, not a target. Do not continue only to reach a numbered round count. Extra Socratic rigor does not override the active threshold unless the profile/config changes.\n\nIf no flag is provided, use **Standard**.\n\n<Mode_Flags>\n- **`--autoresearch`**: switch the interview into autoresearch-intake mode for `$autoresearch` handoff. In this mode, the interview should converge on a validator-ready research mission, write canonical artifacts under `.omx/specs/`, and preserve the explicit `refine further` vs `launch` boundary for downstream skill intake.\n</Mode_Flags>\n</Depth_Profiles>\n\n<Execution_Policy>\n- Ask ONE question per round (never batch multiple interview rounds into one `questions[]` form)\n- Ask about intent and boundaries before implementation detail\n- Target the weakest clarity dimension each round after applying the stage-priority rules below\n- Treat every answer as a claim to pressure-test before moving on: the next question should usually demand evidence or examples, expose a hidden assumption, force a tradeoff or boundary, or reframe root cause vs symptom\n- Do not rotate to a new clarity dimension just for coverage when the current answer is still vague; stay on the same thread until one layer deeper, one assumption clearer, or one boundary tighter\n- Before crystallizing, complete at least one explicit pressure pass that revisits an earlier answer with a deeper, assumption-focused, or tradeoff-focused follow-up\n- Gather codebase facts via `explore` before asking user about internals\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only brownfield fact gathering; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep ambiguous or non-shell-only investigation on the richer normal path.\n- Always run a preflight context intake before the first interview question\n- If initial context is oversized or would exceed the prompt budget, do not paste or forward the raw payload into interview prompts; request and record a prompt-safe initial-context summary first\n- The oversized initial-context summary gate is blocking: wait for the concise summary before ambiguity scoring, crystallizing artifacts, or any downstream execution handoff\n- The summary must preserve goals, constraints, success criteria, non-goals, decision boundaries, and references to any full source documents so downstream consumers receive a prompt-safe but faithful context\n- Keep total prompt payloads within a safe budget by summarizing or trimming retained history; preserve newest/highest-signal answers and never let raw oversized context crowd out the current question\n- Reduce user effort: ask only the highest-leverage unresolved question, and never ask the user for codebase facts that can be discovered directly\n- For brownfield work, prefer evidence-backed confirmation questions such as \"I found X in Y. Should this change follow that pattern?\"\n- Route facts before judgment in the Ouroboros style: before presenting a user-facing interview round, classify whether the needed information is a discoverable fact, a fact needing confirmation, or a human decision. The interview is with the human for judgment, not for facts the agent can inspect.\n- When unresolved ambiguity depends on current external best practices, official/upstream guidance, standards, or version-aware behavior, use `$best-practice-research` as the bounded evidence wrapper before crystallizing requirements or handing off to planning/execution.\n- Use these transcript/spec labels only; never use them as `omx question` `source` values, and never replace the runtime `source: \"deep-interview\"` contract for user-facing deep-interview questions:\n  - `[from-code][auto-confirmed]` — exact, high-confidence codebase facts from manifests/configs or direct source evidence, with no prescription attached.\n  - `[from-code]` — codebase findings that are useful but inferred, pattern-based, or low/medium confidence and therefore need a confirmation-style user-facing round before being treated as settled.\n  - `[from-research]` — externally sourced facts such as API limits, compatibility, or public documentation; facts only, not decisions.\n  - `[from-user]` — goals, preferences, business logic, scope, non-goals, acceptance criteria, tradeoffs, and any decision-bearing interpretation.\n- Treat `[from-code][auto-confirmed]` and other non-user fact discoveries as context/transcript updates, not interview rounds: do not call `omx question`, do not create a pending deep-interview question obligation, and do not increment the user-facing round number for facts the agent can safely establish.\n- Auto-confirm only descriptive facts. If a finding implies what the new feature should do, which pattern it should follow, which tradeoff to accept, or what should stay in/out of scope, route the entire decision-bearing question to the user as `[from-user]` even when code or research facts are available.\n- In attached-tmux Codex CLI, deep-interview uses `omx question` as the required OMX-owned structured questioning path for every interview round\n- When invoking `omx question` through attached-tmux Bash/tool paths, preserve the leader-pane return target by prefixing the command with `OMX_QUESTION_RETURN_PANE=$TMUX_PANE` (or a concrete `%pane` value)\n- If you launch `omx question` in a background terminal, immediately wait for that background terminal to finish and read its JSON answer before scoring ambiguity, asking another round, or handing off\n- Treat `answers[]` as the primary `omx question` success contract. For a single interview round, read `answers[0].answer`; use legacy top-level `answer` only as a compatibility fallback when needed.\n- If the current runtime is outside tmux and cannot render `omx question`, use the native structured question tool when available; otherwise ask exactly one concise plain-text question and wait for the answer\n- Re-score ambiguity after each answer and show progress transparently\n- Once ambiguity is at or below the active profile threshold, stop ordinary questioning. Run the practical closure audit: crystallize/handoff when readiness gates pass; otherwise ask only the final closure question needed to satisfy a named gate.\n- Treat `max_rounds` as a stop cap, not evidence that more rounds are needed.\n- Do not hand off to execution while ambiguity remains above threshold unless user explicitly opts to proceed with warning\n- Do not crystallize or hand off while `Non-goals` or `Decision Boundaries` remain unresolved, even if the weighted ambiguity threshold is met\n- Treat early exit as a safety valve, not the default success path\n- Persist mode state for resume safety with CLI-first state commands (`omx state write/read --input '<json>' --json`); use `state_write` / `state_read` only when explicit MCP compatibility is enabled\n</Execution_Policy>\n\n<Steps>\n\n## Phase 0: Preflight Context Intake\n\n1. Parse `{{ARGUMENTS}}` and derive a short task slug.\n2. Attempt to load the latest relevant context snapshot from `.omx/context/{slug}-*.md`.\n3. Check whether the provided initial context or loaded snapshot is too large for safe prompt use. If it is oversized, the first interview round must ask for a concise prompt-safe summary instead of scoring ambiguity or continuing to downstream handoff.\n4. If no snapshot exists, create a minimum context snapshot with:\n   - Task statement\n   - Desired outcome\n   - Stated solution (what the user asked for)\n   - Probable intent hypothesis (why they likely want it)\n   - Known facts/evidence\n   - Constraints\n   - Unknowns/open questions\n   - Decision-boundary unknowns\n   - Likely codebase touchpoints\n   - Prompt-safe initial-context summary status (`not_needed`, `needed`, or `recorded`)\n5. Save snapshot to `.omx/context/{slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) and reference it in mode state.\n\n## Phase 1: Initialize\n\n1. Parse `{{ARGUMENTS}}` and depth profile (`--quick|--standard|--deep`).\n2. Detect project context:\n   - Run `explore` to classify **brownfield** (existing codebase target) vs **greenfield**.\n   - For brownfield, collect relevant codebase context before questioning.\n3. Initialize state via `omx state write --input '{\"mode\":\"deep-interview\",\"active\":true}' --json`:\n\n```json\n{\n  \"active\": true,\n  \"current_phase\": \"deep-interview\",\n  \"state\": {\n    \"interview_id\": \"<uuid>\",\n    \"profile\": \"quick|standard|deep\",\n    \"type\": \"greenfield|brownfield\",\n    \"initial_idea\": \"<user input>\",\n    \"rounds\": [],\n    \"current_ambiguity\": 1.0,\n    \"threshold\": 0.3,\n    \"max_rounds\": 5,\n    \"challenge_modes_used\": [],\n    \"codebase_context\": null,\n    \"current_stage\": \"intent-first\",\n    \"current_focus\": \"intent\",\n    \"context_snapshot_path\": \".omx/context/<slug>-<timestamp>.md\"\n  }\n}\n```\n\n4. Announce kickoff with profile, threshold, and current ambiguity.\n\n## Phase 2: Socratic Interview Loop\n\nRepeat until ambiguity `<= threshold`, the pressure pass is complete, the readiness gates are explicit, the user exits with warning, or max rounds are reached. This is a stop condition: below threshold, do not open a new ordinary interview branch.\n\n### 2a) Generate next question\nIf the initial context is oversized and no prompt-safe summary has been recorded yet, the next question must be only a summary request. Do not score ambiguity, do not run readiness gates, and do not hand off to `$ralplan`, `$autopilot`, `$ralph`, or `$team` until that summary answer is captured.\n\nUse:\n- Original idea\n- Prior Q&A rounds\n- Current dimension scores\n- Brownfield context (if any)\n- Activated challenge mode injection (Phase 3)\n\nTarget the lowest-scoring dimension, but respect stage priority:\n- **Stage 1 — Intent-first:** Intent, Outcome, Scope, Non-goals, Decision Boundaries\n- **Stage 2 — Feasibility:** Constraints, Success Criteria\n- **Stage 3 — Brownfield grounding:** Context Clarity (brownfield only)\n\nFollow-up pressure ladder after each answer:\n1. Ask for a concrete example, counterexample, or evidence signal behind the latest claim\n2. Probe the hidden assumption, dependency, or belief that makes the claim true\n3. Force a boundary or tradeoff: what would you explicitly not do, defer, or reject?\n4. If the answer still describes symptoms, reframe toward essence / root cause before moving on\n\nPrefer staying on the same thread for multiple rounds when it has the highest leverage. Breadth without pressure is not progress.\n\nMaintain a **Breadth Ledger** across independent ambiguity tracks: scope, constraints, outputs, verification, brownfield integration, and any user-mentioned deliverable tracks. The ledger is a guard, not a mandatory rotation rule: stay deep on the current thread until it has been pressure-tested, then zoom out only when another material track remains unresolved and would change execution.\n\nDetailed dimensions:\n- Intent Clarity — why the user wants this\n- Outcome Clarity — what end state they want\n- Scope Clarity — how far the change should go\n- Constraint Clarity — technical or business limits that must hold\n- Success Criteria Clarity — how completion will be judged\n- Context Clarity — existing codebase understanding (brownfield only)\n\n`Non-goals` and `Decision Boundaries` are mandatory readiness gates. Ask about them early and keep revisiting them until they are explicit.\n\n### 2b) Ask the question\nUse the surface-appropriate structured questioning path for every interview round. In attached-tmux sessions, use OMX-owned structured questioning via `omx question` (this is the required structured-question equivalent and required `AskUserQuestion` equivalent for deep-interview). Outside tmux, use native structured input when available; otherwise ask exactly one concise plain-text question and wait for the answer. Present:\n\n```\nRound {n} | Target: {weakest_dimension} | Ambiguity: {score}%\n\n{question}\n```\n\n`omx question` payload guidance for interview rounds:\n- Deep-interview is Socratic: ask one focused round at a time. Do not use batch `questions[]` to combine multiple interview rounds, even though `omx question` supports batch forms for other workflows.\n- Use canonical `type` values instead of authoring raw `multi_select` flags by hand. `type: \"single-answerable\"` is the default for one-path decisions; `type: \"multi-answerable\"` is the canonical shape for bounded multi-select rounds. The runtime will keep `multi_select` aligned with `type`.\n- Use `single-answerable` when exactly one answer should drive the next branch, the options are mutually exclusive, or selecting more than one answer would blur the decision boundary. Typical cases: handoff lane selection, choosing the primary failure mode, or confirming which of several competing interpretations is correct.\n- Use `multi-answerable` when multiple options may all be true at once and you need to capture a bounded set of coexisting constraints, non-goals, risks, or acceptance checks in one round. Typical cases: selecting all out-of-scope items, all success metrics that must hold, or all deployment constraints that apply together.\n- If one selected option would immediately require a follow-up question to disambiguate the others, prefer a `single-answerable` round now and ask the follow-up next. Do not hide a branching interview tree inside one overloaded multi-select prompt.\n- Keep interview options bounded and concrete. If the valid answers are already known, set `allow_other: false`; only leave `allow_other: true` when the interview genuinely needs one user-supplied option that cannot be enumerated in advance.\n- Read answers structurally from the primary `answers[]` array. For a normal single-round interview response, use `answers[0].answer` as the source of truth; the top-level `answer` field is a legacy single-question projection/fallback only.\n- For `single-answerable`, expect one decisive selection in the `value` field of `answers[0].answer` plus its selected-values metadata. For `multi-answerable`, treat the selected-values field inside `answers[0].answer` as the source of truth for all chosen constraints/non-goals and preserve the full set in the transcript/spec. In legacy single-question projections, this is equivalent to: For `multi-answerable`, treat `answer.selected_values` as the source of truth.\n\nCanonical bounded single-choice payload:\n\n```json\n{\n  \"question\": \"Which execution lane should own this once the interview is complete?\",\n  \"type\": \"single-answerable\",\n  \"options\": [\n    {\n      \"label\": \"Plan first\",\n      \"value\": \"ralplan\",\n      \"description\": \"Need architecture and test-shape review before execution\"\n    },\n    {\n      \"label\": \"Execute directly\",\n      \"value\": \"autopilot\",\n      \"description\": \"Requirements are already explicit enough for planning plus execution\"\n    },\n    {\n      \"label\": \"Refine further\",\n      \"value\": \"refine\",\n      \"description\": \"Clarification is still needed before any handoff\"\n    }\n  ],\n  \"allow_other\": false,\n  \"other_label\": \"Other\",\n  \"source\": \"deep-interview\"\n}\n```\n\nCanonical bounded multi-select payload:\n\n```json\n{\n  \"question\": \"Which non-goals must stay out of scope for the first pass?\",\n  \"type\": \"multi-answerable\",\n  \"options\": [\n    {\n      \"label\": \"No UI redesign\",\n      \"value\": \"no-ui-redesign\",\n      \"description\": \"Keep layout and styling unchanged\"\n    },\n    {\n      \"label\": \"No new dependencies\",\n      \"value\": \"no-new-dependencies\",\n      \"description\": \"Work within the existing toolchain\"\n    },\n    {\n      \"label\": \"No API contract changes\",\n",
  "exit_code": 0,
  "duration": {
    "secs": 0,
    "nanos": 530375
  },
  "formatted_output": "---\nname: deep-interview\ndescription: \"[OMX] Socratic deep interview with mathematical ambiguity gating before execution\"\nargument-hint: \"[--quick|--standard|--deep] [--autoresearch] <idea or vague description>\"\n---\n\n<Purpose>\nDeep Interview is an intent-first Socratic clarification loop before planning or implementation. It turns vague ideas into execution-ready specifications by asking targeted questions about why the user wants a change, how far it should go, what should stay out of scope, and what OMX may decide without confirmation.\n</Purpose>\n\n<Use_When>\n- The request is broad, ambiguous, or missing concrete acceptance criteria\n- The user says \"deep interview\", \"interview me\", \"ask me everything\", \"don't assume\", or \"ouroboros\"\n- The user wants to avoid misaligned implementation from underspecified requirements\n- You need a requirements artifact before handing off to `ralplan`, `autopilot`, `ralph`, or `team`\n</Use_When>\n\n<Do_Not_Use_When>\n- The request already has concrete file/symbol targets and clear acceptance criteria\n- The user explicitly asks to skip planning/interview and execute immediately\n- The user asks for lightweight brainstorming only (use `plan` instead)\n- A complete PRD/plan already exists and execution should start\n</Do_Not_Use_When>\n\n<Why_This_Exists>\nExecution quality is usually bottlenecked by intent clarity, not just missing implementation detail. A single expansion pass often misses why the user wants a change, where the scope should stop, which tradeoffs are unacceptable, and which decisions still require user approval. This workflow applies Socratic pressure + quantitative ambiguity scoring so orchestration modes begin with an explicit, testable, intent-aligned spec.\n</Why_This_Exists>\n\n<Depth_Profiles>\n- **Quick (`--quick`)**: fast pre-PRD pass; target threshold `<= 0.30`; max rounds 5\n- **Standard (`--standard`, default)**: full requirement interview; target threshold `<= 0.20`; max rounds 12\n- **Deep (`--deep`)**: high-rigor exploration; target threshold `<= 0.15`; max rounds 20\n- **Autoresearch (`--autoresearch`)**: same interview rigor as Standard, but specialized for `$autoresearch` mission readiness and `.omx/specs/` artifact handoff\n\nProfile `max rounds` is a hard cap, not a target. Do not continue only to reach a numbered round count. Extra Socratic rigor does not override the active threshold unless the profile/config changes.\n\nIf no flag is provided, use **Standard**.\n\n<Mode_Flags>\n- **`--autoresearch`**: switch the interview into autoresearch-intake mode for `$autoresearch` handoff. In this mode, the interview should converge on a validator-ready research mission, write canonical artifacts under `.omx/specs/`, and preserve the explicit `refine further` vs `launch` boundary for downstream skill intake.\n</Mode_Flags>\n</Depth_Profiles>\n\n<Execution_Policy>\n- Ask ONE question per round (never batch multiple interview rounds into one `questions[]` form)\n- Ask about intent and boundaries before implementation detail\n- Target the weakest clarity dimension each round after applying the stage-priority rules below\n- Treat every answer as a claim to pressure-test before moving on: the next question should usually demand evidence or examples, expose a hidden assumption, force a tradeoff or boundary, or reframe root cause vs symptom\n- Do not rotate to a new clarity dimension just for coverage when the current answer is still vague; stay on the same thread until one layer deeper, one assumption clearer, or one boundary tighter\n- Before crystallizing, complete at least one explicit pressure pass that revisits an earlier answer with a deeper, assumption-focused, or tradeoff-focused follow-up\n- Gather codebase facts via `explore` before asking user about internals\n- `omx explore` is deprecated. Use normal repository inspection tools/subagents for simple read-only brownfield fact gathering; use `omx sparkshell` only for explicit shell-native read-only evidence, and keep ambiguous or non-shell-only investigation on the richer normal path.\n- Always run a preflight context intake before the first interview question\n- If initial context is oversized or would exceed the prompt budget, do not paste or forward the raw payload into interview prompts; request and record a prompt-safe initial-context summary first\n- The oversized initial-context summary gate is blocking: wait for the concise summary before ambiguity scoring, crystallizing artifacts, or any downstream execution handoff\n- The summary must preserve goals, constraints, success criteria, non-goals, decision boundaries, and references to any full source documents so downstream consumers receive a prompt-safe but faithful context\n- Keep total prompt payloads within a safe budget by summarizing or trimming retained history; preserve newest/highest-signal answers and never let raw oversized context crowd out the current question\n- Reduce user effort: ask only the highest-leverage unresolved question, and never ask the user for codebase facts that can be discovered directly\n- For brownfield work, prefer evidence-backed confirmation questions such as \"I found X in Y. Should this change follow that pattern?\"\n- Route facts before judgment in the Ouroboros style: before presenting a user-facing interview round, classify whether the needed information is a discoverable fact, a fact needing confirmation, or a human decision. The interview is with the human for judgment, not for facts the agent can inspect.\n- When unresolved ambiguity depends on current external best practices, official/upstream guidance, standards, or version-aware behavior, use `$best-practice-research` as the bounded evidence wrapper before crystallizing requirements or handing off to planning/execution.\n- Use these transcript/spec labels only; never use them as `omx question` `source` values, and never replace the runtime `source: \"deep-interview\"` contract for user-facing deep-interview questions:\n  - `[from-code][auto-confirmed]` — exact, high-confidence codebase facts from manifests/configs or direct source evidence, with no prescription attached.\n  - `[from-code]` — codebase findings that are useful but inferred, pattern-based, or low/medium confidence and therefore need a confirmation-style user-facing round before being treated as settled.\n  - `[from-research]` — externally sourced facts such as API limits, compatibility, or public documentation; facts only, not decisions.\n  - `[from-user]` — goals, preferences, business logic, scope, non-goals, acceptance criteria, tradeoffs, and any decision-bearing interpretation.\n- Treat `[from-code][auto-confirmed]` and other non-user fact discoveries as context/transcript updates, not interview rounds: do not call `omx question`, do not create a pending deep-interview question obligation, and do not increment the user-facing round number for facts the agent can safely establish.\n- Auto-confirm only descriptive facts. If a finding implies what the new feature should do, which pattern it should follow, which tradeoff to accept, or what should stay in/out of scope, route the entire decision-bearing question to the user as `[from-user]` even when code or research facts are available.\n- In attached-tmux Codex CLI, deep-interview uses `omx question` as the required OMX-owned structured questioning path for every interview round\n- When invoking `omx question` through attached-tmux Bash/tool paths, preserve the leader-pane return target by prefixing the command with `OMX_QUESTION_RETURN_PANE=$TMUX_PANE` (or a concrete `%pane` value)\n- If you launch `omx question` in a background terminal, immediately wait for that background terminal to finish and read its JSON answer before scoring ambiguity, asking another round, or handing off\n- Treat `answers[]` as the primary `omx question` success contract. For a single interview round, read `answers[0].answer`; use legacy top-level `answer` only as a compatibility fallback when needed.\n- If the current runtime is outside tmux and cannot render `omx question`, use the native structured question tool when available; otherwise ask exactly one concise plain-text question and wait for the answer\n- Re-score ambiguity after each answer and show progress transparently\n- Once ambiguity is at or below the active profile threshold, stop ordinary questioning. Run the practical closure audit: crystallize/handoff when readiness gates pass; otherwise ask only the final closure question needed to satisfy a named gate.\n- Treat `max_rounds` as a stop cap, not evidence that more rounds are needed.\n- Do not hand off to execution while ambiguity remains above threshold unless user explicitly opts to proceed with warning\n- Do not crystallize or hand off while `Non-goals` or `Decision Boundaries` remain unresolved, even if the weighted ambiguity threshold is met\n- Treat early exit as a safety valve, not the default success path\n- Persist mode state for resume safety with CLI-first state commands (`omx state write/read --input '<json>' --json`); use `state_write` / `state_read` only when explicit MCP compatibility is enabled\n</Execution_Policy>\n\n<Steps>\n\n## Phase 0: Preflight Context Intake\n\n1. Parse `{{ARGUMENTS}}` and derive a short task slug.\n2. Attempt to load the latest relevant context snapshot from `.omx/context/{slug}-*.md`.\n3. Check whether the provided initial context or loaded snapshot is too large for safe prompt use. If it is oversized, the first interview round must ask for a concise prompt-safe summary instead of scoring ambiguity or continuing to downstream handoff.\n4. If no snapshot exists, create a minimum context snapshot with:\n   - Task statement\n   - Desired outcome\n   - Stated solution (what the user asked for)\n   - Probable intent hypothesis (why they likely want it)\n   - Known facts/evidence\n   - Constraints\n   - Unknowns/open questions\n   - Decision-boundary unknowns\n   - Likely codebase touchpoints\n   - Prompt-safe initial-context summary status (`not_needed`, `needed`, or `recorded`)\n5. Save snapshot to `.omx/context/{slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) and reference it in mode state.\n\n## Phase 1: Initialize\n\n1. Parse `{{ARGUMENTS}}` and depth profile (`--quick|--standard|--deep`).\n2. Detect project context:\n   - Run `explore` to classify **brownfield** (existing codebase target) vs **greenfield**.\n   - For brownfield, collect relevant codebase context before questioning.\n3. Initialize state via `omx state write --input '{\"mode\":\"deep-interview\",\"active\":true}' --json`:\n\n```json\n{\n  \"active\": true,\n  \"current_phase\": \"deep-interview\",\n  \"state\": {\n    \"interview_id\": \"<uuid>\",\n    \"profile\": \"quick|standard|deep\",\n    \"type\": \"greenfield|brownfield\",\n    \"initial_idea\": \"<user input>\",\n    \"rounds\": [],\n    \"current_ambiguity\": 1.0,\n    \"threshold\": 0.3,\n    \"max_rounds\": 5,\n    \"challenge_modes_used\": [],\n    \"codebase_context\": null,\n    \"current_stage\": \"intent-first\",\n    \"current_focus\": \"intent\",\n    \"context_snapshot_path\": \".omx/context/<slug>-<timestamp>.md\"\n  }\n}\n```\n\n4. Announce kickoff with profile, threshold, and current ambiguity.\n\n## Phase 2: Socratic Interview Loop\n\nRepeat until ambiguity `<= threshold`, the pressure pass is complete, the readiness gates are explicit, the user exits with warning, or max rounds are reached. This is a stop condition: below threshold, do not open a new ordinary interview branch.\n\n### 2a) Generate next question\nIf the initial context is oversized and no prompt-safe summary has been recorded yet, the next question must be only a summary request. Do not score ambiguity, do not run readiness gates, and do not hand off to `$ralplan`, `$autopilot`, `$ralph`, or `$team` until that summary answer is captured.\n\nUse:\n- Original idea\n- Prior Q&A rounds\n- Current dimension scores\n- Brownfield context (if any)\n- Activated challenge mode injection (Phase 3)\n\nTarget the lowest-scoring dimension, but respect stage priority:\n- **Stage 1 — Intent-first:** Intent, Outcome, Scope, Non-goals, Decision Boundaries\n- **Stage 2 — Feasibility:** Constraints, Success Criteria\n- **Stage 3 — Brownfield grounding:** Context Clarity (brownfield only)\n\nFollow-up pressure ladder after each answer:\n1. Ask for a concrete example, counterexample, or evidence signal behind the latest claim\n2. Probe the hidden assumption, dependency, or belief that makes the claim true\n3. Force a boundary or tradeoff: what would you explicitly not do, defer, or reject?\n4. If the answer still describes symptoms, reframe toward essence / root cause before moving on\n\nPrefer staying on the same thread for multiple rounds when it has the highest leverage. Breadth without pressure is not progress.\n\nMaintain a **Breadth Ledger** across independent ambiguity tracks: scope, constraints, outputs, verification, brownfield integration, and any user-mentioned deliverable tracks. The ledger is a guard, not a mandatory rotation rule: stay deep on the current thread until it has been pressure-tested, then zoom out only when another material track remains unresolved and would change execution.\n\nDetailed dimensions:\n- Intent Clarity — why the user wants this\n- Outcome Clarity — what end state they want\n- Scope Clarity — how far the change should go\n- Constraint Clarity — technical or business limits that must hold\n- Success Criteria Clarity — how completion will be judged\n- Context Clarity — existing codebase understanding (brownfield only)\n\n`Non-goals` and `Decision Boundaries` are mandatory readiness gates. Ask about them early and keep revisiting them until they are explicit.\n\n### 2b) Ask the question\nUse the surface-appropriate structured questioning path for every interview round. In attached-tmux sessions, use OMX-owned structured questioning via `omx question` (this is the required structured-question equivalent and required `AskUserQuestion` equivalent for deep-interview). Outside tmux, use native structured input when available; otherwise ask exactly one concise plain-text question and wait for the answer. Present:\n\n```\nRound {n} | Target: {weakest_dimension} | Ambiguity: {score}%\n\n{question}\n```\n\n`omx question` payload guidance for interview rounds:\n- Deep-interview is Socratic: ask one focused round at a time. Do not use batch `questions[]` to combine multiple interview rounds, even though `omx question` supports batch forms for other workflows.\n- Use canonical `type` values instead of authoring raw `multi_select` flags by hand. `type: \"single-answerable\"` is the default for one-path decisions; `type: \"multi-answerable\"` is the canonical shape for bounded multi-select rounds. The runtime will keep `multi_select` aligned with `type`.\n- Use `single-answerable` when exactly one answer should drive the next branch, the options are mutually exclusive, or selecting more than one answer would blur the decision boundary. Typical cases: handoff lane selection, choosing the primary failure mode, or confirming which of several competing interpretations is correct.\n- Use `multi-answerable` when multiple options may all be true at once and you need to capture a bounded set of coexisting constraints, non-goals, risks, or acceptance checks in one round. Typical cases: selecting all out-of-scope items, all success metrics that must hold, or all deployment constraints that apply together.\n- If one selected option would immediately require a follow-up question to disambiguate the others, prefer a `single-answerable` round now and ask the follow-up next. Do not hide a branching interview tree inside one overloaded multi-select prompt.\n- Keep interview options bounded and concrete. If the valid answers are already known, set `allow_other: false`; only leave `allow_other: true` when the interview genuinely needs one user-supplied option that cannot be enumerated in advance.\n- Read answers structurally from the primary `answers[]` array. For a normal single-round interview response, use `answers[0].answer` as the source of truth; the top-level `answer` field is a legacy single-question projection/fallback only.\n- For `single-answerable`, expect one decisive selection in the `value` field of `answers[0].answer` plus its selected-values metadata. For `multi-answerable`, treat the selected-values field inside `answers[0].answer` as the source of truth for all chosen constraints/non-goals and preserve the full set in the transcript/spec. In legacy single-question projections, this is equivalent to: For `multi-answerable`, treat `answer.selected_values` as the source of truth.\n\nCanonical bounded single-choice payload:\n\n```json\n{\n  \"question\": \"Which execution lane should own this once the interview is complete?\",\n  \"type\": \"single-answerable\",\n  \"options\": [\n    {\n      \"label\": \"Plan first\",\n      \"value\": \"ralplan\",\n      \"description\": \"Need architecture and test-shape review before execution\"\n    },\n    {\n      \"label\": \"Execute directly\",\n      \"value\": \"autopilot\",\n      \"description\": \"Requirements are already explicit enough for planning plus execution\"\n    },\n    {\n      \"label\": \"Refine further\",\n      \"value\": \"refine\",\n      \"description\": \"Clarification is still needed before any handoff\"\n    }\n  ],\n  \"allow_other\": false,\n  \"other_label\": \"Other\",\n  \"source\": \"deep-interview\"\n}\n```\n\nCanonical bounded multi-select payload:\n\n```json\n{\n  \"question\": \"Which non-goals must stay out of scope for the first pass?\",\n  \"type\": \"multi-answerable\",\n  \"options\": [\n    {\n      \"label\": \"No UI redesign\",\n      \"value\": \"no-ui-redesign\",\n      \"description\": \"Keep layout and styling unchanged\"\n    },\n    {\n      \"label\": \"No new dependencies\",\n      \"value\": \"no-new-dependencies\",\n      \"description\": \"Work within the existing toolchain\"\n    },\n    {\n      \"label\": \"No API contract changes\",\n",
  "status": "completed"
}
```

## Assistant

読み取りました。このセッションは tmux 外なので、構造化 `omx question` は使わず、ここでは一問ずつ本文で進めます。まず最上位の目的を固定します。Round 1 | Target: 目的境界 | Ambiguity: 90%

このプロジェクトの第一目的はどれですか？

**推奨回答:**  
「OCR/Markdown変換ツール」ではなく、**原文に追跡可能なAI用知識パッケージを作ること**を第一目的にする。Markdownは最終出力の一つに留め、内部の正本はページ・座標・抽出信頼度・原文参照を持つ構造化データにする。

この推奨でよいですか？それとも第一目的を別のものに置きますか？

## User

おそらく、はい。基本的にweb上の`claude.ai`と`chatgpt.com`のプロジェクトの情報ソース、或いはローカルにてclaude codeやcowork、codexに処理させるために使っていました。既存は講義資料をmd化して突っ込むだけでした

## Assistant

Round 2 | Target: 利用先の優先順位 | Ambiguity: 78%

今の回答から、目的は「AIに読ませるための知識ソース化」だと理解しました。次に決めるべき依存関係は、**最初に最適化する利用先**です。ここで出力形式・チャンク粒度・メタデータ量・検索設計が変わります。

第一版では、どれを主対象にしますか？

**推奨回答:**  
**ローカルエージェント向けを正本にし、claude.ai / chatgpt.com のプロジェクト知識向けには軽量エクスポートを生成する。**  
理由は、ローカルではファイル分割・grep・インデックス・原文参照・検証ログを保持でき、Webプロジェクト知識は容量や検索挙動の制約が強いため、正本にするには不安定だからです。

この優先順位でよいですか？それとも、Web上のプロジェクト知識投入を第一ターゲットにしますか？

## User

推奨の方で。軽量エクスポートの作成も次回の視野に入れ、web上での動作条件を調査した後に決定しよう
追記：ただ、mdは人も意外と読みやすいという点はあるが... あまり重要ではなさそうだ

## Assistant

Round 3 | Target: 入力スコープ | Ambiguity: 68%

次に固定すべき依存関係は、**初版でどの文書形式を主対象にするか**です。ここで抽出方式、OCRの扱い、検証方法、データモデルが変わります。

**推奨回答:**  
初版は **講義資料PDFを主対象** にする。さらに優先順位は、  
**born-digital PDF、つまり文字レイヤーを持つPDFを第一対象**、スキャンPDF・写真OCRは第二対象にする。Word / HTML / Google Docs は将来の入力アダプタとして設計上は見越すが、初版の成功条件には入れない。

理由は、最初から全形式を等価に扱うと「文書変換基盤」になりすぎて、知識パッケージ化という目的がぼやけるからです。

この入力スコープでよいですか？

## User

はい

## Assistant

Round 4 | Target: 正本と派生物の境界 | Ambiguity: 58%

初版の内部正本を何にしますか？  
ここが決まると、Markdown、検索、LLM校正、原文参照、軽量エクスポートの位置づけが決まります。

**推奨回答:**  
**Markdownは正本にしない。**  
正本は、PDF原本 + 抽出済み構造データにする。たとえば、ページ番号、ブロックID、座標、抽出テキスト、信頼度、ブロック種別、原文参照を持つ構造化データを持ち、Markdownはそこから生成される派生物にする。

理由は、Markdownだけを正本にすると「どのページのどの位置から来た情報か」「OCRやLLMがどこを変更したか」「後から再抽出できるか」が弱くなるためです。

この方針でよいですか？

## User

うーん、一旦それで大丈夫そうかなあ

## Assistant

Round 5 | Target: 変換の許容範囲 | Ambiguity: 49%

次に決めるべきなのは、**本文をどこまで“きれいにしてよい”か**です。ここを曖昧にすると、LLM校正が「読みやすいが原文と違う」ものを作る危険があります。

**推奨回答:**  
本文は3層に分ける。

1. **raw**: PDFから抽出した生テキスト。絶対に変更しない。  
2. **normalized**: 改行、空白、Unicode、明確なヘッダー/フッターなどを機械的に整えたもの。  
3. **curated**: LLMや人間の判断で読みやすく再構成したもの。ただし全変更は raw / normalized への参照と差分理由を持つ。

つまり、AIに普段渡すのは curated でよいが、正しさ検証は raw / normalized に戻れるようにする。

この3層方針でよいですか？

## User

階層構造には賛成ではあるが複雑すぎるのではないだろうか？
1. pdf元本
2. curated
の2つにすることによって正しさはpdfに直接アクセスして該当ページを確認するのがよさそうだ。
元のrawとnormalizedは資料を読み込むllmではなくこの作業を実行するllmとスクリプトにこそ必要なのではないだろうか？

## Assistant

Round 6 | Target: 中間生成物の扱い | Ambiguity: 43%

その反論は妥当です。ここで分けるべきなのは、**ユーザー/読ませるAIに見せる成果物**と、**変換パイプラインが使う作業用証跡**です。

**推奨回答:**  
第一版の成果物モデルは **PDF元本 + curated** の2つにする。  
ただし、raw / normalized / OCR結果 / LLMパッチ案は「正本」ではなく、変換・検証用の一時またはキャッシュ証跡として扱う。常に人間や読ませるLLMへ渡す対象にはしない。

つまり設計上はこうです。

- 永続的な知識ソース: `PDF元本`, `curated`
- 内部処理用: `raw`, `normalized`, `extraction trace`, `LLM patch log`
- 検証時: curated の各セクションから PDF ページへ戻れる参照だけは残す

質問です。  
**raw / normalized などの内部処理用データは、デバッグと再現性のために保存しますか？ それとも第一版では原則破棄し、必要時だけ再生成する方針にしますか？**

私の推奨は、**通常は保存せず、`--debug` や検証失敗時だけ保存する**です。

## User

失敗した時にだけ確認すれば良いということですね？また実装の検証時にはデバッグフラグをしようすれば良い、と？

## Assistant

はい、その理解です。

通常運用では **PDF元本 + curated** だけを成果物として残す。  
raw / normalized / OCR中間結果 / LLMパッチ案 / 差分ログは、毎回ユーザーや下流LLMに見せる正本ではなく、**失敗調査・品質検証・実装テスト用の診断情報**として扱うのがよいです。

Round 7 | Target: 診断情報の保存ポリシー | Ambiguity: 38%

では、診断情報の保存ポリシーをどこまで強くしますか？

**推奨回答:**  
初版では次の方針にする。

- 通常実行: PDF元本 + curated + 最小限のページ参照だけ保存
- `--debug`: raw / normalized / 抽出ブロック / LLM編集候補 / 適用差分を保存
- 検証失敗時: 自動的に debug bundle を保存
- テスト実行時: 常に debug bundle を保存して回帰確認に使う

これなら通常成果物は単純に保ちつつ、問題が起きたときだけ原因追跡できます。

この保存ポリシーでよいですか？

## User

はい

## Assistant

Round 8 | Target: curated の粒度 | Ambiguity: 32%

次は **curated をどの単位で持つか** です。ここで検索性、人間の読みやすさ、Web向け軽量エクスポート、PDF参照の方法が決まります。

**推奨回答:**  
第一版では、**PDF 1本につき curated Markdown 1本** を基本にする。  
ただし内部構造として、見出し・章・ページ範囲・安定したセクションIDを持たせる。細かいチャンクファイルは正本にせず、必要になったら curated から派生生成する。

理由は、最初からチャンク単位を正本にすると運用が複雑になる一方、1本のMarkdownなら人間も読みやすく、grepもしやすいからです。ページ参照とセクションIDだけあれば、あとから軽量エクスポートにも展開できます。

この粒度でよいですか？

## User

これはどの程度の大きさのpdfファイルを想定しているのか？

## Assistant

想定は **講義資料1本あたり 10〜80ページ程度**、テキスト量で **数千〜数万トークン程度** です。スライドPDFなら100ページ前後でも、1ページあたりの文字量が少なければ `curated.md` 1本で扱えます。

ただし、以下を超えるなら1本Markdown正本は厳しくなります。

- 100〜150ページ超
- 教科書・論文集のように1ページの文字密度が高い
- curated が 5〜10万トークン級になる
- Webプロジェクト知識へそのまま投入したい
- 章単位で頻繁に差し替えたい

Round 9 | Target: 大型PDFへの分割方針 | Ambiguity: 30%

大型PDFはどう扱うべきでしょうか？

**推奨回答:**  
第一版は次のルールにする。

- 通常PDF: `curated.md` 1本
- 大型PDF: `curated.md` は目次・概要・章リンクだけにし、本文は章単位ファイルへ分割
- 分割判断はページ数だけでなく、抽出後の文字量・見出し構造・章境界で決める
- どちらの場合も、各セクションに PDF ページ範囲を残す

これなら小さな講義資料は単純に扱え、大きな資料だけ複雑化できます。

この分割方針でよいですか？

## User

はい

## Assistant

Round 10 | Target: 原文参照の粒度 | Ambiguity: 26%

次に決めるべき依存関係は、**curated から PDF 元本へどの粒度で戻れるようにするか**です。ここで成果物の読みやすさと検証可能性のバランスが決まります。

**推奨回答:**  
通常の `curated.md` には **セクション単位のページ範囲参照** を持たせる。

例:

```md
## 第3章 注意機構
Source: PDF p.12-18
```

本文中のすべての文に細かい座標やブロックIDは付けない。  
ただし、`--debug` 時だけページ内座標・抽出ブロックID・OCR信頼度などを保存する。

理由は、通常成果物を人間にもAIにも読みやすく保ちつつ、必要なときはPDFページへ戻って検証できるからです。

この参照粒度でよいですか？

## User

他の粒度にはどのようなものがあるでしょうか？

## Assistant

主な選択肢は5段階あります。

1. **文書単位**
   `Source: lecture01.pdf` だけ。最も軽いが、検証時に該当箇所を探しにくい。

2. **ページ範囲単位**
   `Source: p.12-18`。読みやすさと検証性のバランスがよい。講義資料向き。

3. **セクション + ページ範囲単位**
   `section_id: attention_intro`, `Source: p.12-18`。あとで検索・分割・Web向けエクスポートに強い。私の推奨。

4. **段落/箇条書き単位**
   各段落に `p.13` や `block_id` を付ける。検証性は高いがMarkdownが読みにくくなる。

5. **ブロック座標単位**
   `page=13, bbox=(x,y,w,h)` まで持つ。監査・OCR検証には強いが、通常の知識ソースとしては重い。`--debug` 向け。

Round 10 | Target: 原文参照の粒度 | Ambiguity: 26%

**推奨回答:**  
通常成果物は **セクションID + ページ範囲** にする。  
章・節・スライドまとまりごとに参照を置き、段落単位・座標単位は通常Markdownには入れず、debug bundle に回す。

この粒度でよいですか？

## User

はい

## Assistant

Round 11 | Target: curated の忠実度 | Ambiguity: 23%

次に決めるべきなのは、`curated` が **忠実な再構成文書** なのか、**要約・圧縮された知識ノート** なのかです。ここでLLMの編集許容範囲が大きく変わります。

**推奨回答:**  
`curated` は **要約ではなく、原文に忠実な再構成文書** にする。  
つまり、講義資料に含まれる主張・定義・例・手順・注意点は落とさず、削るのは反復ヘッダー、ページ番号、装飾、明らかな重複などに限定する。

要約やWeb投入用の軽量版は、`curated` から派生生成する別成果物にする。  
LLMが補足説明を加える場合は、本文に混ぜず `AI Note:` のように明確に分離する。

この方針でよいですか？

## User

はい

## Assistant

Round 12 | Target: LLM編集権限 | Ambiguity: 20%

次に固定すべきなのは、LLMに **curated 本文を直接生成させるか**、それとも **編集候補を出させて適用するか** です。

**推奨回答:**  
LLMには原則として **直接全文を書き換えさせない**。  
役割は次に限定する。

- ノイズ候補の分類: ヘッダー、フッター、ページ番号、重複、本文
- OCR/抽出ミス候補の検出
- 見出し・箇条書き・段落構造の復元候補
- `before -> after` 形式の編集パッチ提案
- 各提案の理由と信頼度の出力

実際の適用はスクリプト側が行う。  
ただし、初版では実装簡略化のため、**小さなセクション単位に限ってLLMに curated セクションを生成させる**ことは許可する。その場合も、セクションの PDF ページ範囲と debug bundle で検証できるようにする。

この「LLMは直接全文生成ではなく、セクション単位の限定生成またはパッチ提案に留める」方針でよいですか？

## User

作業方針は2つ。この方法論か、あるいはより良い代替案・折衷案か？
1. 全体を作業させる
2. 細かなチャンクに分けて作業する
1はocrによって生成されたファイルをそのまま作業することになる。これはエージェントが全体を把握しつつ作業でき、1体のエージェントが責任を持って実行する形である。
2は生成されたファイルをチャンクに分け同時に複数のワーカーを起動し並列で作業を進める。全体像を共有できるようにプロンプトを初期に注入しそれぞれの領域において集中して作業する形である。

## Assistant

これは二択ではなく、**折衷案のハイブリッド**がよいです。

**推奨方針:**  
1体のエージェントが全体責任を持つ。ただし、実作業はチャンク単位に分ける。

構造はこうです。

1. **Global Planning Pass**  
   全体を読んで、章構造、用語、反復ノイズ、講義資料の癖、編集ルールを決める。

2. **Chunk Editing Pass**  
   章・節・ページ範囲ごとに小さく処理する。各チャンクには全体方針、用語表、前後の短い文脈を渡す。

3. **Global Reconciliation Pass**  
   最後に1体の責任エージェントが、見出し整合性、用語統一、重複、チャンク境界の欠落、ページ参照、全体の読み流れを検証する。

理由は、全体一括処理は一貫性が出る一方で、長文では見落とし・トークン過多・修正不能な大崩れが起きやすいからです。逆に完全並列チャンク処理は速いですが、用語・文体・見出し粒度・重複除去の判断がばらつきます。

Round 13 | Target: 編集オーケストレーション | Ambiguity: 17%

第一版では、次の方針でよいですか？

**推奨回答:**  
**単独責任者 + チャンク作業 + 全体再統合** を採用する。  
複数ワーカー並列は将来拡張として見越すが、初版ではまず逐次チャンク処理でもよい。重要なのは、チャンクごとの局所編集ではなく、最初と最後に必ず全体パスを置くこと。

この方針でよいですか？

## User

はい。
Round 12に対する回答：編集候補を出させて適用する
理由：入れ替えを生成するより適用する方が最近のモデルにとって理に適っているはずである。

## Assistant

了解です。Round 12 は次で固定します。

**決定:** LLMは `curated` を直接全文生成しない。LLMは構造化された編集候補、つまりパッチを出し、スクリプト側が適用する。  
理由は、生成よりも「該当箇所を特定して、限定的な差分を提案する」方が制御・検証・再現性に優れるため。

Round 14 | Target: パッチの自動適用基準 | Ambiguity: 15%

LLMが出した編集パッチは、どこまで自動適用してよいですか？

**推奨回答:**  
第一版では次の基準にする。

- 自動適用してよい: 反復ヘッダー/フッター除去、ページ番号除去、明確な改行修復、箇条書き復元、局所的なOCR誤り修正
- 自動適用しない: 意味の追加、要約、言い換え、大きな段落再構成、図表の解釈、本文かノイズか曖昧な削除
- LLMパッチには必ず `対象範囲`, `before`, `after`, `理由`, `信頼度`, `変更種別`, `PDFページ範囲` を持たせる
- 低信頼・高影響のパッチは適用せず、debug bundle に隔離する
- 適用済みパッチは通常成果物には出さず、debug 時だけ確認できるようにする

この自動適用基準でよいですか？

## User

はい

## Assistant

Round 15 | Target: PDF抽出方式 | Ambiguity: 13%

次に決めるべき依存関係は、PDFから最初にどうテキストを取り出すかです。ここを誤ると、OCR前提で不要に精度・コスト・トークンを失います。

**推奨回答:**  
第一版では **PDFのテキストレイヤー抽出を最優先** にする。OCRは常用ではなく、次の場合だけ使う。

- PDFにテキストレイヤーがない
- 抽出テキストが明らかに壊れている
- 図表・スクリーンショット内の文字を拾う必要がある
- ページ単位で抽出品質が低いと判定された

つまり、基本順序は  
**PDF text extraction → layout-aware cleanup → 必要ページだけOCR → LLMパッチ提案**  
にする。

この抽出方針でよいですか？

## User

ocrから入る方がよさそうだ。質のいいpdfの存在を前提にするべきではない。ocrを回すよりも元のpdfのテキストレイヤーがいいとするならば、それはどういった理由からだろうか？

## Assistant

その指摘は正しいです。「質のいいPDFを前提にする」は危険です。前回の推奨は少し born-digital PDF に寄りすぎていました。

PDFテキストレイヤーがOCRより有利な理由は主にこれです。

- **文字が正確なことが多い**: OCRは `rn/m`、濁点、数式、英数字、専門用語で誤認識しやすい。
- **高速で安い**: OCRはページ画像化と認識が必要で、処理時間・コストが増える。
- **再現性が高い**: OCRはモデルや設定で結果が揺れやすいが、テキスト抽出は比較的決定的。
- **本文検索に強い**: テキストレイヤーが正常なら、文字列検索・差分・引用に向く。
- **不要な視覚ノイズを拾いにくい**: OCRはヘッダー、フッター、透かし、スライド番号、ロゴ内文字まで拾いやすい。

ただし逆に、PDFテキストレイヤーには大きな欠点があります。

- 読み順が壊れる
- 段組みやスライド配置に弱い
- 文字が分断される
- フォント埋め込みやエンコードで文字化けする
- 画像化された文字は当然拾えない

なので、より良い方針は **OCR-first** でも **text-layer-first** でもなく、**page-level dual extraction** だと思います。

Round 15 revised | Target: PDF抽出方式 | Ambiguity: 13%

**推奨回答:**  
第一版では、ページごとに **テキストレイヤー抽出とOCRの両方を候補** として扱う。  
ただし常に両方を最終採用するのではなく、品質判定でページごとに採用元を決める。

- テキストレイヤーが正常: text layer を優先
- テキストレイヤーが空、文字化け、順序崩壊: OCRを優先
- OCRとtext layerが大きく食い違う: debug対象
- 図表やスクリーンショット内文字: OCRを補助的に使う
- curatedには採用元を細かく出さず、必要なら debug bundle に残す

つまり「質のいいPDFを前提にしない」が、「使えるテキストレイヤーも捨てない」という方針です。

この **ページ単位の二系統抽出 + 品質判定** を採用しますか？

## User

品質判定ではなく、統合方式は可能だろうか？使える部品を組み合わせる感じd3

## Assistant

可能です。むしろ設計としては **二者択一の品質判定** より、**複数抽出結果の統合** の方が筋がよいです。

ただし「品質判定を完全になくす」のではなく、品質判定は **採用元を1つ選ぶため** ではなく、**統合時の重み付け・衝突検出・要確認箇所の検出** に使うのがよいです。

イメージはこうです。

- PDF text layer: 正確な文字列候補
- OCR: 視覚上の読み順・画像内文字・欠落補完
- layout解析: ブロック、見出し、表、ページ上の位置
- LLM patch: 衝突や不自然な箇所の修正候補

これらをページ全体で勝者決定するのではなく、**ブロック単位で evidence を集めて統合**します。

Round 16 | Target: 抽出結果の統合粒度 | Ambiguity: 12%

統合はどの粒度で行うべきでしょうか？

**推奨回答:**  
第一版では **ブロック単位の統合** を採用する。  
ページ全体で text layer / OCR のどちらかを選ぶのではなく、見出し・本文段落・箇条書き・表・図注のようなブロックごとに候補を並べ、使える部品を組み合わせる。

ただし、語単位・文字単位の細かすぎる統合は初版では避ける。複雑になりすぎるためです。  
衝突がある場合は、LLMに「どちらが自然か」を判断させるのではなく、まず debug 対象として残し、明確な場合だけパッチ化する。

この **ブロック単位の抽出統合** 方針でよいですか？

## User

はい

## Assistant

決定: 抽出は **ブロック単位で text layer / OCR / layout / LLM patch を統合**する。ページ単位で勝者を選ばない。

Round 17 | Target: ブロック分類

次は、統合対象となる「ブロック」をどの種類に分けるかです。ここが決まると、ノイズ除去・Markdown生成・LLMパッチの対象範囲が決まります。

**推奨回答:**  
第一版のブロック種別は最小限にする。

- `title`
- `heading`
- `paragraph`
- `list_item`
- `table`
- `figure_caption`
- `header_footer`
- `page_number`
- `unknown`

通常の `curated` に出すのは `title / heading / paragraph / list_item / table / figure_caption` だけ。  
`header_footer / page_number / unknown` は削除候補または debug 対象にする。

この最小ブロック分類でよいですか？

## User

おそらく？一旦これで

## Assistant

Round 18 | Target: 表・図の扱い | Ambiguity: 10%

次に決めるべきなのは、講義資料で重要になりやすい **表・図・グラフ・数式** を `curated` にどう入れるかです。ここはトークン効率と情報損失の衝突点です。

**推奨回答:**  
第一版では次の扱いにする。

- **表**: 可能ならMarkdown tableへ変換する。崩れる場合は、無理に整形せず箇条書き化する。
- **図・グラフ**: 画像そのものは `curated` に埋め込まない。代わりに、キャプション・周辺本文・OCR文字を元に「図の要点」を短く入れる。ただし `AI Note:` として本文と分離する。
- **数式**: OCRで壊れやすいので、確信が低い場合は無理に復元せず `[Formula on PDF p.X]` のように原文参照を残す。
- **重要図**: 必要なら将来、画像切り出しとリンクを追加するが、初版の必須要件にはしない。

この方針でよいですか？

## User

はい

## Assistant

Round 19 | Target: ノイズ除去の方針 | Ambiguity: 9%

次は、講義資料で頻出する「講義名・教授名・セクション名・ページ番号・大学名・日付」などをどう扱うかです。ここは削除しすぎると文脈を失い、残しすぎるとトークン効率が落ちます。

**推奨回答:**  
ノイズは **削除** ではなく、まず **分類** する。

- 文書全体の識別に必要: metadata へ移す
- 章やセクション境界として有用: heading として保持
- 各ページに繰り返されるだけ: header_footer として除外
- 内容理解に必要か曖昧: unknown として debug 対象
- 本文の意味を担う: paragraph / heading として保持

つまり、講義名や教授名は毎ページには残さないが、文書冒頭 metadata には残す。セクション名は反復ノイズではなく構造情報として使う。

このノイズ分類方針でよいですか？

## User

はい

## Assistant

Round 20 | Target: metadata の範囲 | Ambiguity: 8%

次は、ノイズから分離した情報を **metadata としてどこまで残すか** です。ここを決めると、講義名・教授名・日付・ページ範囲などの扱いが固定できます。

**推奨回答:**  
第一版の metadata は最小限にする。

- `title`
- `source_pdf`
- `page_count`
- `course_name` / `lecture_name`
- `instructor`
- `date` または `term`
- `section_index`: セクションID、見出し、PDFページ範囲
- `processing_summary`: text layer / OCR / LLM patch を使った概要
- `warnings`: 低信頼箇所、未解決の表・図・数式

講義名や教授名は本文中に毎回残さず、metadata に一度だけ置く。確信が低い項目は空欄にせず `uncertain` として扱う。

この metadata 方針でよいですか？

## User

はい

## Assistant

Round 21 | Target: 成功判定 | Ambiguity: 7%

ここまでで構造はかなり固まりました。次は、第一版が「成功した」と言える基準です。ここを曖昧にすると、実装後に品質判断ができません。

**推奨回答:**  
第一版の成功基準は次にする。

- 講義資料PDFから `curated.md` を生成できる
- `curated.md` は人間が通読できる
- 各セクションに PDF ページ範囲がある
- 反復ヘッダー/フッター/ページ番号が本文から概ね除外される
- 主要な見出し・箇条書き・段落が保たれる
- 低信頼箇所は `warnings` に出る
- `--debug` で抽出候補・LLMパッチ・適用差分を確認できる
- 少なくとも3種類の講義PDFで破綻しない

「情報を一切落とさない」や「完全なOCR精度」は第一版の成功基準にしない。

この成功基準でよいですか？

## User

次は必要なさそうだ。原本pdfを読めば事足りるからである。（よりリッチな見た目が必要なら `curated.md` の内容からhtmlでも作らせれば良いからである。）
- `curated.md` は人間が通読できる

## Assistant

了解です。成功基準から **「人間が通読できる」** は外すのが自然です。  
このプロジェクトの `curated.md` は人間向け清書ではなく、**AIが参照しやすい構造化テキスト** です。人間が確認する正本はPDF、見た目が必要ならHTML等を派生生成する、という位置づけにします。

Round 22 | Target: curated の読者モデル | Ambiguity: 6%

では `curated.md` の読者モデルを明確に固定します。

**推奨回答:**  
`curated.md` は **人間が快適に通読する文書ではなく、AIエージェントが検索・引用・部分読解しやすい中間成果物** にする。  
ただし、人間がデバッグ時に読める程度の最低限の可読性は保つ。

この読者モデルでよいですか？

## User

はい

## Assistant

Round 23 | Target: 第一版の非目標 | Ambiguity: 5%

ここで非目標を明文化します。非目標がないと、実装時に「ついでにHTML」「ついでにWebプロジェクト最適化」「ついでに完全OCR」へ膨らみます。

**推奨回答:**  
第一版では次を明確に非目標にする。

- Web上の claude.ai / chatgpt.com プロジェクト知識への最適化
- HTMLやリッチビューの生成
- 人間向けの美しいMarkdown清書
- PDF内容の要約
- 完全なOCR精度保証
- 図表・数式の完全復元
- Word / HTML / Google Docs 入力対応
- 複数ワーカーによる本格並列編集
- 人手レビューUI
- 情報の追加説明や教材化

必要なのは、講義PDFから **原文参照つきAI用 curated Markdown** を作れることです。

この非目標リストでよいですか？

## User

はい

## Assistant

Round 24 | Target: 決定境界 | Ambiguity: 4%

最後に、実装時にエージェントやスクリプトが自動で決めてよいことと、人間に確認すべきことを分けます。

**推奨回答:**  
自動で決めてよい:

- ヘッダー/フッター/ページ番号の除外
- 明確なOCR誤りの修正
- 見出し・段落・箇条書きの構造復元
- PDFページ範囲の付与
- 大型PDFの章単位分割
- debug bundle の保存有無
- warnings への低信頼箇所記録

人間確認が必要:

- 本文の意味を変える削除
- 要約や圧縮
- 図表・数式の解釈
- 曖昧なノイズ除去
- PDF元本にない補足説明の追加
- Web向け軽量エクスポート仕様
- 新しい入力形式の追加

この決定境界でよいですか？

## User

はい

## Assistant

Round 25 | Target: 共通理解の確定 | Ambiguity: 3%

ここまでの合意を、第一版の設計原則として固定してよいですか？

**推奨される確定版:**  
このプロジェクトは、講義PDFを **AIエージェント向けの原文参照つき curated Markdown** に変換する。  
正本は **PDF元本 + curated**。raw / normalized / OCR候補 / LLMパッチログは通常成果物ではなく、`--debug` や検証失敗時の診断情報として扱う。

抽出は、PDFテキストレイヤーとOCRをページ単位で勝者選択するのではなく、**ブロック単位で統合**する。ブロック種別は最小限にし、反復ノイズは削除ではなく metadata / header_footer / unknown / 本文へ分類する。

LLMは全文清書を担当しない。LLMは編集候補パッチを出し、スクリプトが適用する。自動適用は低リスクな修正に限定し、意味変更・要約・図表解釈・曖昧な削除は確認または warnings/debug に回す。

`curated.md` は人間が快適に通読する文書ではなく、AIが検索・引用・部分読解しやすい中間成果物とする。Webプロジェクト知識向け軽量エクスポート、HTML生成、Word/Google Docs対応、本格並列編集、人手レビューUIは第一版の非目標とする。

この内容で共通理解として確定してよいですか？

## User

はい

## Assistant

確定しました。共通理解は次の通りです。

このプロジェクトの第一版は、講義PDFを **AIエージェント向けの原文参照つき `curated.md`** に変換するものです。人間向けの美しいMarkdown清書やHTML生成ではなく、AIが検索・引用・部分読解しやすい知識ソース化が目的です。

正本は **PDF元本 + curated**。`raw`、`normalized`、OCR候補、LLMパッチログ、差分などは通常成果物ではなく、`--debug`、検証失敗時、テスト時の診断情報として扱います。

抽出は **PDFテキストレイヤー vs OCR の勝者選択** ではなく、text layer / OCR / layout 情報を **ブロック単位で統合**します。ブロック分類は最小限にし、反復ノイズは削除前提ではなく metadata / header_footer / unknown / 本文へ分類します。

LLMは全文清書しません。LLMは **編集候補パッチ** を出し、スクリプト側が適用します。自動適用はヘッダー除去、ページ番号除去、明確な改行修復、局所的OCR誤りなど低リスクなものに限定します。意味変更、要約、図表解釈、曖昧な削除は warnings/debug 側に回します。

第一版の非目標は、Webプロジェクト知識最適化、HTML生成、人間向け清書、要約、完全OCR、図表・数式の完全復元、Word/HTML/Google Docs対応、本格並列編集、人手レビューUIです。

次に進むなら、この合意をそのまま **設計仕様/PRD** に落とし、処理パイプライン・データモデル・CLI仕様・検証基準へ分解する段階です。

## User

まずこの合意の内容をまとめて出力してください、引き継ぎします。（作業するディレクトリを間違えてしまいした...泣）

## Assistant

以下、引き継ぎ用の合意まとめです。

**プロジェクト目的**

講義PDFを、AIエージェントが検索・引用・部分読解しやすい **原文参照つき `curated.md`** に変換する。

目的は人間向けの美しいMarkdown清書ではなく、`claude code`、`codex`、`cowork` などローカルAIエージェントが扱いやすい知識ソース化。  
`claude.ai` / `chatgpt.com` のプロジェクト知識向け軽量エクスポートは将来検討とし、第一版の主対象にはしない。

**正本と成果物**

第一版の正本は次の2つ。

- PDF元本
- `curated.md`

`raw`、`normalized`、OCR候補、LLMパッチログ、適用差分などは通常成果物ではなく、変換・検証・デバッグ用の内部証跡として扱う。

保存方針:

- 通常実行: PDF元本 + `curated.md` + 最小限のページ参照
- `--debug`: raw / normalized / 抽出ブロック / LLM編集候補 / 適用差分を保存
- 検証失敗時: debug bundle を自動保存
- テスト実行時: debug bundle を保存して回帰確認に使う

**入力スコープ**

第一版は講義資料PDFを対象にする。  
Word / HTML / Google Docs / 写真入力は将来の入力アダプタとして見越すが、第一版の成功条件には含めない。

PDFは高品質なテキストレイヤーを持つとは限らないため、text layer 前提にはしない。

**抽出方針**

PDFテキストレイヤーとOCRのどちらかをページ単位で勝者選択するのではなく、**ブロック単位で統合**する。

利用する候補:

- PDF text layer: 正確な文字列候補
- OCR: 視覚上の読み順、画像内文字、欠落補完
- layout解析: ブロック、見出し、表、位置
- LLM patch: 衝突や不自然な箇所の修正候補

品質判定は「どちらを採用するか」ではなく、統合時の重み付け、衝突検出、warnings/debug 対象の判定に使う。

**ブロック分類**

第一版のブロック種別は最小限にする。

- `title`
- `heading`
- `paragraph`
- `list_item`
- `table`
- `figure_caption`
- `header_footer`
- `page_number`
- `unknown`

通常の `curated.md` に出すのは以下。

- `title`
- `heading`
- `paragraph`
- `list_item`
- `table`
- `figure_caption`

`header_footer`、`page_number`、`unknown` は除外候補または debug/warnings 対象。

**curated.md の性質**

`curated.md` は要約ではなく、原文に忠実な再構成文書にする。  
講義資料に含まれる主張、定義、例、手順、注意点は落とさない。削るのは反復ヘッダー、ページ番号、装飾、明らかな重複などに限定する。

ただし `curated.md` は人間が快適に通読するための文書ではない。  
AIが検索・引用・部分読解しやすい中間成果物であり、人間が確認する正本はPDF元本。見た目が必要なら、将来 `curated.md` からHTMLなどを派生生成する。

**粒度と分割**

通常PDFは、PDF 1本につき `curated.md` 1本を基本にする。

大型PDFの場合:

- `curated.md` は目次・概要・章リンク中心
- 本文は章単位ファイルへ分割
- 分割判断はページ数だけでなく、抽出後の文字量・見出し構造・章境界で決める

想定サイズ:

- 通常: 講義資料 10〜80ページ程度
- スライドPDFなら100ページ前後でも文字量が少なければ1本で可
- 100〜150ページ超、文字密度が高い、5〜10万トークン級なら分割対象

**原文参照**

通常成果物では **セクションID + PDFページ範囲** を持たせる。

例:

```md
## 第3章 注意機構
Source: PDF p.12-18
```

段落単位・座標単位の参照は通常Markdownには入れない。  
ページ内座標、抽出ブロックID、OCR信頼度などは `--debug` 時の debug bundle に保存する。

**metadata**

第一版の metadata は最小限にする。

- `title`
- `source_pdf`
- `page_count`
- `course_name` / `lecture_name`
- `instructor`
- `date` または `term`
- `section_index`: セクションID、見出し、PDFページ範囲
- `processing_summary`: text layer / OCR / LLM patch を使った概要
- `warnings`: 低信頼箇所、未解決の表・図・数式

講義名や教授名は本文中に毎回残さず、metadata に一度だけ置く。  
確信が低い項目は空欄ではなく `uncertain` として扱う。

**ノイズ処理**

ノイズは削除前提ではなく、まず分類する。

- 文書全体の識別に必要: metadata へ移す
- 章やセクション境界として有用: heading として保持
- 各ページに繰り返されるだけ: header_footer として除外
- 内容理解に必要か曖昧: unknown として debug/warnings 対象
- 本文の意味を担う: paragraph / heading として保持

講義名や教授名は毎ページには残さないが、metadata には残す。  
セクション名は反復ノイズではなく構造情報として使う。

**LLMの役割**

LLMは `curated.md` を全文清書しない。  
LLMの役割は、**編集候補パッチを出すこと**。

LLMが行うこと:

- ノイズ候補の分類
- OCR/抽出ミス候補の検出
- 見出し・箇条書き・段落構造の復元候補
- `before -> after` 形式の編集パッチ提案
- 各提案の理由と信頼度の出力

パッチには以下を持たせる。

- 対象範囲
- `before`
- `after`
- 理由
- 信頼度
- 変更種別
- PDFページ範囲

実際の適用はスクリプト側が行う。

**パッチ自動適用基準**

自動適用してよいもの:

- 反復ヘッダー/フッター除去
- ページ番号除去
- 明確な改行修復
- 箇条書き復元
- 局所的なOCR誤り修正

自動適用しないもの:

- 意味の追加
- 要約
- 言い換え
- 大きな段落再構成
- 図表の解釈
- 本文かノイズか曖昧な削除

低信頼・高影響のパッチは適用せず、debug bundle / warnings に隔離する。

**表・図・数式**

第一版の扱い:

- 表: 可能ならMarkdown tableへ変換。崩れる場合は箇条書き化。
- 図・グラフ: 画像そのものは `curated.md` に埋め込まない。キャプション・周辺本文・OCR文字から短い要点を入れる場合は `AI Note:` として本文から分離。
- 数式: 確信が低い場合は無理に復元せず `[Formula on PDF p.X]` のように原文参照を残す。
- 重要図の画像切り出しやリンクは将来拡張で、第一版の必須要件ではない。

**編集オーケストレーション**

作業方式は **単独責任者 + チャンク作業 + 全体再統合**。

流れ:

1. Global Planning Pass  
   全体を見て、章構造、用語、反復ノイズ、編集ルールを決める。

2. Chunk Editing Pass  
   章・節・ページ範囲ごとに小さく処理する。各チャンクには全体方針、用語表、前後の短い文脈を渡す。

3. Global Reconciliation Pass  
   最後に1体の責任エージェントが、見出し整合性、用語統一、重複、チャンク境界の欠落、ページ参照、全体の読み流れを検証する。

複数ワーカー並列は将来拡張。第一版では逐次チャンク処理でもよい。

**成功基準**

第一版の成功基準:

- 講義資料PDFから `curated.md` を生成できる
- 各セクションにPDFページ範囲がある
- 反復ヘッダー/フッター/ページ番号が本文から概ね除外される
- 主要な見出し・箇条書き・段落が保たれる
- 低信頼箇所は `warnings` に出る
- `--debug` で抽出候補・LLMパッチ・適用差分を確認できる
- 少なくとも3種類の講義PDFで破綻しない

成功基準に含めないもの:

- 人間が快適に通読できる
- 情報を一切落とさない
- 完全なOCR精度
- 図表・数式の完全復元

**第一版の非目標**

第一版では以下をやらない。

- Web上の claude.ai / chatgpt.com プロジェクト知識への最適化
- HTMLやリッチビューの生成
- 人間向けの美しいMarkdown清書
- PDF内容の要約
- 完全なOCR精度保証
- 図表・数式の完全復元
- Word / HTML / Google Docs 入力対応
- 複数ワーカーによる本格並列編集
- 人手レビューUI
- 情報の追加説明や教材化

**決定境界**

自動で決めてよいこと:

- ヘッダー/フッター/ページ番号の除外
- 明確なOCR誤りの修正
- 見出し・段落・箇条書きの構造復元
- PDFページ範囲の付与
- 大型PDFの章単位分割
- debug bundle の保存有無
- warnings への低信頼箇所記録

人間確認が必要なこと:

- 本文の意味を変える削除
- 要約や圧縮
- 図表・数式の解釈
- 曖昧なノイズ除去
- PDF元本にない補足説明の追加
- Web向け軽量エクスポート仕様
- 新しい入力形式の追加
