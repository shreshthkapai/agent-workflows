---
name: visual-parity
description: Match a provided visual reference or preserve appearance during a component or framework migration.
---

# Visual Parity

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user asks to match a visual reference or preserve appearance through a component or framework migration. It is available automatically for visual-parity work and through {{INVOKE}}visual-parity. Establish the reference and target state, viewport, theme, fonts, assets, and rendering conditions. Capture the reference and target under the same conditions with available browser or screenshot tools; do not replace the baseline or alter the checker to hide a mismatch.

Use installed Impeccable guidance for relevant interface decisions. Compare images with available image-comparison tools, or label a manual visual comparison as manual. Match layout, spacing, typography, color, states, and interactions within the requested scope; avoid inventing a redesign. Honor an agreed tolerance. Do not claim pixel-perfect output without objective comparison evidence, and account for antialiasing and font-rendering variation.

Make focused component or shared-style changes. For substantial, understood, bounded implementation, use one native worker. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check; inspect the actual diff. Verify the target again after each meaningful unit. Follow {{GLOBAL_INSTRUCTIONS}} and keep one primary workflow with only relevant supporting steps. If the baseline or comparison capability is missing, state that verification is inconclusive. Do not add a visual test harness automatically.
