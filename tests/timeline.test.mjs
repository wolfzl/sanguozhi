import test from "node:test";
import assert from "node:assert/strict";
const api = await import("../src/lib/timeline.mjs").catch(() => ({}));
const event = { title:"吴蜀恢复联盟", aliases:["孫劉復盟"], importance:"standard", lanes:["shu","wu"], categories:["diplomacy"] };
test("restores a shareable compound timeline state and ignores invalid filter values",()=>{
  assert.equal(typeof api.parseTimelineState,"function");
  const state=api.parseTimelineState("?importance=all&lane=shu&category=diplomacy&q=孫劉&view=list");
  assert.deepEqual(state,{importance:"all",lane:"shu",category:"diplomacy",q:"孫劉",view:"list"});
  assert.deepEqual(api.parseTimelineState("?importance=bad&lane=bad&view=bad"),{importance:"key",lane:"all",category:"all",q:"",view:"parallel"});
  assert.deepEqual(api.parseTimelineState(api.encodeTimelineState(state)),state);
});
test("combines importance, lane, category and simplified/traditional aliases",()=>{
  assert.equal(typeof api.matchesEvent,"function");
  assert.equal(api.matchesEvent(event,{importance:"all",lane:"shu",category:"diplomacy",q:"孙刘"}),true);
  assert.equal(api.matchesEvent(event,{importance:"key",lane:"shu",category:"diplomacy",q:""}),false);
  assert.equal(api.matchesEvent(event,{importance:"all",lane:"wei",category:"diplomacy",q:""}),false);
  assert.equal(api.matchesEvent(event,{importance:"all",lane:"shu",category:"war",q:""}),false);
});
test("uses historically appropriate track labels and closes Shu after 263",()=>{
  assert.equal(typeof api.laneLabel,"function");
  assert.equal(api.laneLabel("wei",219),"曹氏势力");
  assert.equal(api.laneLabel("wei",220),"曹魏");
  assert.equal(api.laneLabel("wei",265),"西晋");
  assert.equal(api.laneLabel("shu",220),"刘备势力");
  assert.equal(api.laneLabel("wu",228),"孙氏势力");
  assert.equal(api.laneLabel("wu",229),"孙吴");
  assert.equal(api.laneStatus("shu",263),"ending");
  assert.equal(api.laneStatus("shu",264),"ended");
  assert.equal(api.laneStatus("wu",280),"ending");
});
test("cross-party event spans its participating tracks without changing canonical ID",()=>{
  assert.equal(typeof api.lanePlacement,"function");
  assert.deepEqual(api.lanePlacement(["shu","wu"]),{start:2,span:2});
  assert.deepEqual(api.lanePlacement(["wei","wu"]),{start:1,span:3});
  assert.deepEqual(api.lanePlacement(["common"]),{start:1,span:3});
});
test("aligns independent same-year events even when the right-hand track comes first",()=>{
  assert.equal(typeof api.layoutYearEvents,"function");
  assert.deepEqual(api.layoutYearEvents([{lanes:['wu']},{lanes:['wei']},{lanes:['shu']},{lanes:['wei','shu']}]),[{start:3,span:1,row:1},{start:1,span:1,row:1},{start:2,span:1,row:1},{start:1,span:2,row:2}]);
});
