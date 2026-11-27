# Thesis Writing Guidelines

## Sentences
- Write concise sentences. One idea per sentence.
- Every sentence either explains the previous statement or is the statement that the next sentence illustrates (claim, then evidence or example).
- Prefer active voice and concrete verbs. Cut filler such as "it is worth noting that" or "in order to".
- Use one term per concept and keep it throughout. Define every acronym once, then reuse it.

## Paragraphs and sections
- One paragraph, one point. Open with the point, then support it.
- Each paragraph and section leads into the next. End with a link forward, or open by referencing what was just established.
- Each chapter opens with what it covers and why, and closes with what it hands over to the next chapter.

## Scope
- This is a thesis on <topic in one sentence>. Include only what serves that question.
- No irrelevant side facts, no unpublished work, no speculation about features that were not built.
- Introduce background only if the reader needs it to follow the method or results.
- The methodology describes what the method does and why. Keep engineering implementation details out of the prose: hyperparameters, network widths, simulator settings, timings, thresholds, library and API names, and the history of earlier implementations. Put the facts needed for reproduction in appendix tables and reference them from the text.
- In the theoretical background, state what a method does, why it is used, and what it is generally used for. Leave specific experimental results of other works to the related work and results chapters.

## Facts and claims
- Use facts. Every claim is backed by a citation, a number, a figure, or a result from this work.
- Report numbers with units, sample sizes, and variance where available.
- Describe the method exactly as implemented. Never invent hyperparameters, results, or architecture details.
- When citing an example the reader may not know (e.g. a benchmark task from another paper), first describe its setup: task, robot, what is varied and what is measured. Then state the result.
- Separate observation (what the data shows) from interpretation (why it might be so). Hedge only where the evidence is genuinely uncertain.
- State limitations plainly, in the discussion, without apology.

## Figures, tables, equations
- Introduce every figure and table in the text before it appears, and say what the reader should take from it.
- Captions are self-contained: what is shown, under which setup.
- Introduce every symbol at first use and keep notation consistent with the notation list.

## Style
- Formal but plain. No marketing language ("novel", "significant", "state-of-the-art") unless backed by a comparison.
- Never write "need not". Write "do not need to" or rephrase.
- No dashes as sentence punctuation. Use a comma or split the sentence.
- No semicolons. Never join two clauses with ";". Write two sentences. Do not use semicolons to separate list items either. Rewrite the list as sentences or an itemized list.
- Keep tense consistent: past for what was done, present for what the thesis shows or states.

## Abstract
The abstract follows four moves in this order: identify the problem, explain our work, emphasize our results, and close with one sentence that states the novelty.

- **Problem.** Open by placing the task in its research field. Then state each challenge in its own sentence, together with its consequence for learning (e.g. "..., which limits ..."). Name only the challenges that the method answers.
- **Our work.** Introduce the method with its name and type before any detail: "We therefore propose <name>, a framework that combines <A> and <B> to <goal>." Then give one sentence per component, with parallel openings that name it ("In the teacher training phase, ...", "In the student training phase, ...").
- **Results.** Report the headline numbers with units, first in simulation, then on the physical system. Include the strongest comparison. Summarize generalization in one sentence instead of listing every condition.
- **Novelty.** End with a single claim of what is new, hedged as "To the best of our knowledge, ...". The claim must be backed by the related work chapter.
- Write the abstract in the first person plural ("we propose", "we train"). The chapters use "this thesis" instead.
- Use the field's vocabulary instead of everyday words (see Soft rules below).
- Make the logic explicit with connectives ("Therefore", "Additionally"). Complete paired connectives: "On the one hand" needs "On the other hand".
- Use no vague qualifiers such as "a certain degree of precision". State the number instead.
- Define every acronym at first use. Name an established component (e.g. the DP3 visual encoder) only together with what it does.

## Soft rules
These rules are defaults, not requirements. Apply them where they make the text clearer, and break them where they do not.

### Section and subsection structure
- Build every section and subsection like the abstract. Open with the problem it handles and why it matters. Then say what this thesis does about it, give the evidence or justification, and close with the consequence and a link to what follows.
- Raise only problems that the thesis answers, and link each one to the component that answers it.

### Sentence level
- State a problem together with its consequence for the method, e.g. "..., limiting parallelization when RL algorithms are involved" or "..., which ...".
- Prefer field vocabulary to everyday words: "must" or "requires" instead of "has to", "challenging" or "difficult" instead of "hard", "locate" instead of "find".
- Make the logical relation explicit with "therefore", "because", "in contrast", or "as a consequence" instead of ", so".
- Describe a system in the order in which data flows through it, one stage per clause.
- Name a component once and reuse exactly that name in headings, text, tables, and captions.
- Match the detail to the level of the text. Overviews (chapter openings, summaries, introduction, conclusion) carry only the headline numbers.
- Report measured outcomes with the plain verb ("completes"). Reserve "is able to" for contrasting a capability with methods that lack it.
- Use "this thesis" in the chapters and "we" only in the abstract. Make the method, the policy, or the experiment the subject where possible ("the teacher learns", not "this thesis learns").
