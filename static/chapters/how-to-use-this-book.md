# How to use this book

CSS is not a list of isolated declarations. A property only makes sense in a formatting context, with a value grammar, inside the cascade, and under a browser-support policy. Read the concept chapters first, then use the property catalog as a working reference.

The browser-support language in this manuscript is deliberately conservative. “Baseline” means that a fallback is still required for some targets. “Stable” means that the feature is ready for a modern evergreen primary path, provided your actual analytics agree. “Experimental” means that the feature may be incomplete, changing, or unevenly implemented. Compatibility is a release-time check, not a permanent fact.

### How this book presents information

The examples below are a visual legend for the rest of the book. Each treatment has a job: prose explains the mental model, quotes preserve a principle, code demonstrates a working pattern, and tables make comparisons scannable.

> Good CSS is not the CSS with the most rules. It is the CSS whose rules make the intended behavior obvious.

**Example code block.** Code is shown in a dark, syntax-highlighted panel with line numbers. Copy the smallest useful example, then adapt the selector and values to the component you own.

```css
.card {
  display: grid;
  gap: 1rem;
  padding: 1.25rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
}
```

**Inline code.** Names such as `box-sizing`, values such as `border-box`, and functions such as `clamp()` appear inline when the surrounding sentence is the important part.

**Compatibility note.** A compatibility note tells you when to check browser data, provide a fallback, or gate an enhancement with `@supports`. It is a release decision, not a permanent promise.

**Accessibility note.** Accessibility guidance calls out focus, contrast, motion, semantics, zoom, writing modes, and assistive technology. Treat it as part of the feature design rather than a final polish step.

**Reference table.** Tables summarize values, browser behavior, or property families. Read across a row for one feature; read down a column to compare related choices.

| Pattern | What it helps you decide |
|---|---|
| Concept | Why the feature exists and when to reach for it |
| Example | A concrete starting point you can adapt |
| Compatibility | Whether the feature needs a fallback or test |
| Accessibility | What must remain usable for every reader |
| Related concepts | Which properties, APIs, or chapters deepen the idea |

**Practical checklist.** Before shipping an example, ask:

- Does the baseline remain useful when the enhancement is unavailable?
- Can the component be read and operated with keyboard, zoom, and assistive technology?
- Is the value grammar valid, and can the cascade explain the computed result?
- Have the relevant browser or email-client support tables been checked?
