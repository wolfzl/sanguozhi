export function validateReferences(book, refs) {
  const errors = [];
  for (const ref of refs) {
    const volume = book.volumes.find((v) => v.id === ref.volume);
    const block = volume?.blocks.find((b) => b.id === ref.blockId);
    const note = volume?.blocks
      .flatMap((b) => b.notes)
      .find((n) => n.id === ref.blockId);
    const text = ref.kind === "peizhu" ? note?.text : block?.mainText;
    if (!text || !ref.quote || !text.includes(ref.quote))
      errors.push(`Invalid ${ref.kind} quote at ${ref.volume}/${ref.blockId}`);
    else if (ref.kind === "peizhu" && !ref.sourceBook)
      errors.push(`Missing cited work at ${ref.blockId}`);
  }
  return errors;
}
export function collectReferences(value) {
  if (!value || typeof value !== "object") return [];
  if (Array.isArray(value)) return value.flatMap(collectReferences);
  if ("blockId" in value && "quote" in value) return [value];
  return Object.values(value).flatMap(collectReferences);
}
