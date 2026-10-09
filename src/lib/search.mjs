import { Converter } from "opencc-js/t2cn";
const simplify = Converter({ from: "tw", to: "cn" });
export function normalizeSearch(value) {
  return simplify(String(value ?? ""))
    .normalize("NFKC")
    .toLowerCase()
    .replace(/\s+/g, "");
}
export function searchText(card) {
  return normalizeSearch(
    [
      card.name,
      card.title,
      card.courtesy,
      ...(card.aliases ?? []),
      ...(card.tags ?? []),
    ]
      .filter(Boolean)
      .join(" "),
  );
}
export function matchesCard(card, query, faction = "all") {
  return (
    (faction === "all" || card.faction === faction) &&
    searchText(card).includes(normalizeSearch(query))
  );
}
