const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let list;for(let i=0;i<30;i++){try{list=await (await fetch('http://127.0.0.1:9333/json')).json();if(list.find(t=>t.type==='page'))break}catch(e){}await sleep(300)}
const ws=new WebSocket(list.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend=new Map(),errs=[];
ws.onmessage=m=>{const d=JSON.parse(m.data);if(d.id&&pend.has(d.id)){pend.get(d.id)(d);pend.delete(d.id)}
 if(d.method==='Runtime.exceptionThrown')errs.push(d.params.exceptionDetails.exception?.description||d.params.exceptionDetails.text);
 if(d.method==='Runtime.consoleAPICalled'&&d.params.type==='error')errs.push('console: '+d.params.args.map(a=>a.value).join(' '))};
const send=(method,params={})=>new Promise(r=>{pend.set(++id,r);ws.send(JSON.stringify({id,method,params}))});
const ev=async e=>{const r=await send('Runtime.evaluate',{expression:e,awaitPromise:true,returnByValue:true});if(r.result.exceptionDetails)throw new Error(e+' → '+JSON.stringify(r.result.exceptionDetails.exception?.description));return r.result.result.value};
await send('Runtime.enable');await send('Page.enable');
const URL='http://127.0.0.1:8742/index.html';
await send('Page.navigate',{url:URL});await sleep(1500);
await ev(`localStorage.clear()`);await send('Page.navigate',{url:URL});await sleep(1500);
let fails=0;const ok=(n,c,x)=>{console.log((c?'PASS':'FAIL')+' '+n+(x!==undefined?'  ['+x+']':''));if(!c)fails++};
const N=e=>ev(e);
ok('carrega com 6 players, cap.1 selecionado',await N(`EPS.length>=6&&cur===0`));
await N(`toggle(0)`);await sleep(2000);
ok('play toca',await N(`!engine.paused&&engine.currentTime>0.5`),await N(`engine.currentTime`));
ok('metadata cap.1',(await N(`navigator.mediaSession.metadata.title`)).startsWith('Ep. 1'));
await N(`seekTo(100)`);await sleep(1000);
let t0=await N(`engine.currentTime`);await N(`ACTIONS.nexttrack()`);await sleep(700);
ok('carro ⏭ avança ~10 s no mesmo capítulo',await N(`cur===0&&Math.abs(engine.currentTime-${t0}-10.7)<1.5`),await N(`engine.currentTime`));
t0=await N(`engine.currentTime`);await N(`ACTIONS.previoustrack()`);await sleep(700);
ok('carro ⏮ volta ~10 s no mesmo capítulo',await N(`cur===0&&Math.abs(engine.currentTime-${t0}+9.3)<1.5`),await N(`engine.currentTime`));
// ── travessia para FRENTE: fim do cap.1 → começo do cap.2
await N(`seekTo(engine.duration-4)`);await sleep(800);await N(`ACTIONS.nexttrack()`);await sleep(2000);
ok('⏭ a 4 s do fim do cap.1 → cap.2 em ~6 s, tocando',await N(`cur===1&&!engine.paused&&engine.currentTime>5&&engine.currentTime<10`),await N(`cur+' @ '+engine.currentTime`));
ok('metadata acompanha (cap.2)',(await N(`navigator.mediaSession.metadata.title`)).startsWith('Ep. 2'));
// ── travessia para TRÁS: começo do cap.2 → fim do cap.1
await N(`seekTo(3)`);await sleep(800);await N(`ACTIONS.previoustrack()`);await sleep(2000);
ok('⏮ a 3 s do início do cap.2 → cap.1 a ~7 s do fim, tocando',await N(`cur===0&&!engine.paused&&(engine.duration-engine.currentTime)<8&&(engine.duration-engine.currentTime)>3`),await N(`'faltam '+(engine.duration-engine.currentTime)`));
// ── rajada: 3 toques seguidos para trás cruzando a fronteira, pausado
await N(`load(2,false,4)`);await sleep(1500);await N(`engine.pause()`);
await N(`ACTIONS.previoustrack();ACTIONS.previoustrack();ACTIONS.previoustrack()`);await sleep(2000);
ok('3 toques ⏮ a 4 s do início do cap.3 → cap.2 a ~26 s do fim, continua pausado',await N(`cur===1&&engine.paused&&Math.abs((engine.duration-engine.currentTime)-26)<1.5`),await N(`'faltam '+(engine.duration-engine.currentTime)`));
// ── limites da faixa
await N(`load(0,false,3)`);await sleep(1200);await N(`ACTIONS.previoustrack()`);await sleep(500);
ok('⏮ no início do cap.1 para em 0:00',await N(`cur===0&&engine.currentTime<0.5`),await N(`engine.currentTime`));
await N(`load(EPS.length-1,false,0)`);await sleep(1200);await N(`seekTo(engine.duration-4)`);await sleep(600);await N(`ACTIONS.nexttrack()`);await sleep(600);
ok('⏭ no fim do último capítulo não sai dele',await N(`cur===EPS.length-1`),await N(`engine.currentTime`));
// ── demais comportamentos
await N(`load(0,true,0)`);await sleep(1000);
await N(`ACTIONS.pause()`);await sleep(300);ok('pause pelo carro',await N(`engine.paused&&navigator.mediaSession.playbackState==='paused'`));
await N(`ACTIONS.play()`);await sleep(600);ok('play pelo carro',await N(`!engine.paused`));
await N(`nextEpisode()`);await sleep(1500);ok('⏭ da TELA troca de capítulo',await N(`cur===1&&!engine.paused`));
await N(`load(0,true,0)`);await sleep(1200);await N(`seekTo(engine.duration-2)`);await sleep(4500);
ok('fim do cap.1 emenda no cap.2 e zera a posição do cap.1',await N(`cur===1&&!engine.paused&&localStorage.getItem('iso27001_audio-1')==='0'`),await N(`localStorage.getItem('iso27001_audio-1')`));
await N(`skip('audio-4',30)`);await sleep(1500);
ok('botão +30 de outro card carrega o cap.4 em 30 s',await N(`cur===3&&Math.abs(engine.currentTime-30)<2`),await N(`engine.currentTime`));
await N(`engine.pause();localStorage.setItem('iso27001_audio-3','123.4');localStorage.setItem('iso27001_last','3')`);
await send('Page.navigate',{url:URL});await sleep(2500);
ok('reabrir a página retoma cap.3 em 123 s',await N(`cur===2&&Math.abs(engine.currentTime-123.4)<2`),await N(`engine.currentTime`));
ok('UI do card mostra a posição',(await N(`EPS[2].time.textContent`)).startsWith('2:03'),await N(`EPS[2].time.textContent`));
await N(`togglePanel('quiz-1',document.querySelector('#card-1 .btn-toggle:nth-child(2)'))`);await sleep(300);
ok('quiz antigo continua abrindo',await N(`document.querySelector('#quiz-1-body').children.length>0`));
ok('sem erros de JavaScript',errs.length===0,errs.join(' | '));
console.log(fails?`\n${fails} FALHA(S)`:'\nTUDO OK');ws.close();process.exit(fails?1:0);
