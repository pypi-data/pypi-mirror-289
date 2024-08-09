var c=`<div class="pglite-app-container">

    <h1><tt>pglite</tt></h1>

    <div>Executed commands:</div>
    <div class="code-editor" title="code-editor"></div>
    <div id="timestamp"></div>
    <hr>
    <div>Result:</div>
    <div title="results"></div>
    <div>Raw Output:</div>
    <div title="output"></div>
</div>`;function l(){return"xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,function(t){let e=Math.random()*16|0;return(t==="x"?e:e&3|8).toString(16)})}import{PGlite as u}from"https://cdn.jsdelivr.net/npm/@electric-sql/pglite/dist/index.js";var R=`
-- Optionally select statements to execute.

CREATE TABLE IF NOT EXISTS test  (
        id serial primary key,
        title varchar not null
      );

INSERT INTO test (title) values ('dummy');

`.trim();function g(t){let e=document.createElement("table"),i=e.insertRow();return t.fields.forEach(n=>{let r=document.createElement("th");r.textContent=n.name,i.appendChild(r)}),e}function f(t,e){t.rows.forEach(i=>{let n=e.insertRow();t.fields.forEach(r=>{let o=n.insertCell();o.textContent=String(i[r.name])})})}function v({model:t,el:e}){let i=new u,n=document.createElement("div");n.innerHTML=c;let r=l();n.id=r,e.appendChild(n),t.on("change:code_content",async()=>{let o=e.querySelector('div[title="code-editor"]'),m=e.querySelector('div[title="output"]'),d=e.querySelector('div[title="results"]');if(o){let p=t.get("code_content"),a=await i.query(p);t.set("response",a),o.innerHTML=o.innerHTML+"<br>"+t.get("code_content"),m.innerHTML=JSON.stringify(a);let s=g(a);f(a,s),d.innerHTML="",d.append(s)}t.save_changes()})}var S={render:v};export{S as default};
