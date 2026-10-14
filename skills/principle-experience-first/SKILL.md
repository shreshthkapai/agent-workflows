---
name: principle-experience-first
description: "Shape product or API decisions around the experience of its consumers and maintainers."
---

# Experience First

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Judge product and implementation choices by how they affect the people who use and maintain the result. For an interface, consider the requested flow, feedback, error states, and responsiveness. For a library or internal API, consider the caller’s effort and the next maintainer’s ability to understand it. Respect the user’s requested scope and preserve required capabilities; do not remove features or narrow behavior merely to make implementation easier. A sketch or prototype can clarify an uncertain interaction when it is proportionate, but is not a required step for routine work. Explain meaningful tradeoffs from the consumer’s point of view.
