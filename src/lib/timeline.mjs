import { normalizeSearch, searchText } from "./search.mjs";
export const categories = {war:"战争",state:"建国与政权更替",succession:"继承与权力变化",diplomacy:"联盟外交",governance:"治理"};
export const phases = {formation:{title:"汉末动荡与势力形成",period:"184—209",lead:"从汉廷失序到诸侯竞逐，看各方如何形成势力。"},states:{title:"三国建立与竞争",period:"211—238",lead:"建国、战争与外交，让三条线不断交汇。"},unification:{title:"政权变化与归于统一",period:"239—280",lead:"继承与权力转移，最终汇入新的时代。"}};
export const laneIds = ["wei","shu","wu","lords"];
export const relationTypes = {context:"背景与后果",process:"同一历史进程",parallel:"并行对照",succession:"政权承继"};
export function parseTimelineState(search = "") {
  const params = new URLSearchParams(search);
  const allowed = (name, values, fallback) => values.includes(params.get(name)) ? params.get(name) : fallback;
  return {importance:allowed("importance",["key","all"],"all"),lane:allowed("lane",["all",...laneIds],"all"),category:allowed("category",["all",...Object.keys(categories)],"all"),q:params.get("q") ?? "",view:allowed("view",["parallel","list"],"parallel")};
}
export function encodeTimelineState(state) {
  const defaults = parseTimelineState();
  const params = new URLSearchParams();
  for (const key of Object.keys(defaults)) if(state[key] !== defaults[key]) params.set(key,state[key]);
  return params.size ? "?" + params.toString() : "";
}
export function matchesEvent(event,state) {
  return (state.importance === "all" || event.importance === "key") && (state.lane === "all" || (event.lanes.includes(state.lane) || (state.lane === "lords" && event.lanes.includes("common")))) && (state.category === "all" || event.categories.includes(state.category)) && searchText(event).includes(normalizeSearch(state.q));
}
export function laneLabel(lane,year) {
  if (lane === "lords") return "汉末诸侯";
  if (lane === "wei") return year < 220 ? "曹氏势力" : year < 265 ? "曹魏" : "西晋";
  if (lane === "shu") return year < 221 ? "刘备势力" : "蜀汉";
  if (lane === "wu") return year < 229 ? "孙氏势力" : "孙吴";
  return "汉末共同背景";
}
export function laneStatus(lane,year) {
  const end = lane === "shu" ? 263 : lane === "wu" ? 280 : Infinity;
  return year > end ? "ended" : year === end ? "ending" : "active";
}
export function lanePlacement(lanes) {
  if (lanes.includes("common")) return {start:1,span:laneIds.length};
  const positions = lanes.map(lane => laneIds.indexOf(lane)+1);
  const start = Math.min(...positions);
  return {start,span:Math.max(...positions)-start+1};
}
// Share a row when same-year events occupy independent tracks. DOM order stays chronological.
export function layoutYearEvents(events) {
  const occupied = [];
  return events.map(event => {
    const position = lanePlacement(event.lanes);
    const columns = Array.from({length:position.span},(_,i)=>position.start+i);
    let row = occupied.findIndex(used => columns.every(column => !used.has(column)));
    if (row === -1) { row = occupied.length; occupied.push(new Set()); }
    for (const column of columns) occupied[row].add(column);
    return {...position,row:row+1};
  });
}
