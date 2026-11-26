'use strict';
const el = id => document.getElementById(id);
const balloon = '../decor-balloon-hd.webp';
const tabs = [...document.querySelectorAll('[role=tab]')];
function selectTab(key, updateAddress) {
  const current = tabs.find(t => t.id === 't-'+key) || tabs[0];
  for (const tab of tabs) {
    const active = tab === current;
    tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1;
    el(tab.getAttribute('aria-controls')).hidden = !active;
  }
  if (updateAddress) history.replaceState(null,'','#'+current.id.slice(2));
}
tabs.forEach((tab,i)=>{
  tab.onclick = () => selectTab(tab.id.slice(2),true);
  tab.onkeydown = e => {
    const pos={ArrowRight:(i+1)%4,ArrowLeft:(i+3)%4,Home:0,End:3}[e.key];
    if(pos===undefined)return;
    e.preventDefault();tabs[pos].focus();tabs[pos].click();
  };
});
addEventListener('hashchange',()=>selectTab(location.hash.slice(1),false));
const colors=[
  ['Сирень','#ad84cf','hue-rotate(290deg) saturate(1.25)','сиреневый'],
  ['Жемчуг','#f0e9dd','saturate(.13) brightness(1.35)','жемчужный'],
  ['Роза','#de9ab8','saturate(1.1)','розовый'],
  ['Золото','#d9ac69','sepia(.82) saturate(1.35) brightness(1.03)','золотой'],
  ['Мята','#99c7bf','hue-rotate(150deg) saturate(.75) brightness(1.07)','мятный'],
  ['Слива','#80518c','hue-rotate(293deg) saturate(1.65) brightness(.70)','сливовый']
];
const palette=[0,1];
const positions=[
  [5,79,11,-36],[10,72,13,14],[5,62,15,-27],[13,59,11,48],[7,50,13,-47],[11,40,16,-42],[18,43,12,7],[14,30,16,-28],[20,24,17,-23],[24,31,11,32],[29,19,17,-3],[36,24,13,55],[40,15,17,5],[49,15,13,16],[53,20,10,22],[59,13,14,21],[66,16,12,44],[72,15,9,54],
  [11,68,8,-5],[9,54,8,-39],[17,35,7,5],[25,24,8,-2],[36,17,9,12],[47,20,7,-7],[62,17,6,40]
];
function wb(query){return 'https://www.wildberries.ru/catalog/0/search.aspx?search='+encodeURIComponent('Мишины шарики '+query);}
function renderGarland(animate){
  el('arch').replaceChildren();
  positions.forEach(([x,y,w,deg],i)=>{
    const im=new Image();im.src=balloon;im.alt='';im.className='ball';
    im.style.left=x+'%';im.style.top=y+'%';im.style.width=w+'%';
    im.style.setProperty('--rot',deg+'deg'); im.style.setProperty('--delay',(i%12)*20+'ms');
    im.style.filter=colors[palette[[0,1,0,0,1][i%5]]][2];
    if(!animate)im.style.animation='none';
    el('arch').append(im);
  });
  const a=colors[palette[0]],b=colors[palette[1]];
  el('palette-label').textContent=a[0]+' × '+b[0];el('palette-link').href=wb('набор гирлянда '+a[3]+' '+b[3]);
  ['color-a','color-b'].forEach((id,group)=>[...el(id).children].forEach((button,i)=>button.setAttribute('aria-pressed',String(i===palette[group]))));
}
['color-a','color-b'].forEach((id,group)=>colors.forEach(([title,hex],index)=>{
  const button=document.createElement('button');button.type='button';button.className='swatch';button.title=title;
  button.setAttribute('aria-label',title);button.style.setProperty('--color',hex);if(index===5)button.style.setProperty('--tick','#fff');
  button.onclick=()=>{if(palette[1-group]===index)palette[1-group]=palette[group];palette[group]=index;renderGarland(true)};
  el(id).append(button);
}));
const steps=[
  ['Подготовьте шары и ленту','Для демонстрационного набора понадобятся надутые шары двух размеров с завязанными хвостиками и монтажная лента с отверстиями.'],
  ['Закрепите первый шар','Проденьте завязанный хвостик в большое отверстие монтажной ленты и сдвиньте его в узкую часть. Слегка потяните шар, чтобы проверить крепление.'],
  ['Заполните просветы','Чередуйте цвета. Маленькие шары добавляйте туда, где между крупными остались просветы. Посмотрите на гирлянду с небольшого расстояния.']
];
let step=0;
function showStep(n){step=Math.max(0,Math.min(n,2));el('step-count').textContent='Шаг '+(step+1)+' из 3';el('step-art').dataset.step=String(step);el('step-title').textContent=steps[step][0];el('step-copy').textContent=steps[step][1];el('prev').disabled=step===0;el('next').disabled=step===2;}
el('prev').onclick=()=>showStep(step-1);el('next').onclick=()=>showStep(step+1);
function checkSku(){
  const value=el('sku').value.trim().toUpperCase().replace(/[\s-]/g,'');
  const ok=['ДЕМО01','DEMO01'].includes(value);
  el('questions').hidden=!ok;
  el('helper-status').textContent=ok?'Открыта инструкция к набору «Гирлянда».':'Этот артикул пока не подключён. Для примера введите ДЕМО-01.';
  return ok;
}
el('kit-form').onsubmit=e=>{e.preventDefault();if(checkSku())showStep(0)};
document.querySelectorAll('[data-q]').forEach(b=>b.onclick=()=>{if(checkSku()){showStep(+b.dataset.q);el('helper-status').textContent='Открыт шаг «'+steps[step][0]+'».'}});
el('ask').onsubmit=e=>{
  e.preventDefault();if(!checkSku())return;const q=el('question').value.trim().toLowerCase();
  let target;
  if(/просвет|пробел|пустот|маленьк|зазор/.test(q))target=2;
  else if(/креп|первый|встав|отверст|хвост|лент/.test(q))target=1;
  else if(/нача|подготов|нужн|понадоб|размер/.test(q))target=0;
  if(target===undefined){el('helper-status').textContent='В демо есть ответы о подготовке, креплении и просветах. Выберите один из вопросов выше.';return;}
  showStep(target);el('helper-status').textContent='Открыт шаг «'+steps[target][0]+'».';
};
let currentAge=5;
function numberWord(n){return n%10===1&&n%100!==11?'год':n%10>=2&&n%10<=4&&(n%100<12||n%100>14)?'года':'лет';}
function setAge(value){
  const n=Number(value),valid=value!==''&&Number.isInteger(n)&&n>=1&&n<=99;
  el('age-note').textContent=valid?'':'Введите целое число от 1 до 99.';el('age').setAttribute('aria-invalid',String(!valid));
  el('age-link').hidden=!valid;
  if(!valid){el('number-art').replaceChildren();el('age-caption').textContent='Выберите возраст';el('minus').disabled=el('plus').disabled=false;return;}
  currentAge=n;el('age').value=n;el('minus').disabled=n===1;el('plus').disabled=n===99;
  const art=n===5?new Image():document.createElement('span');
  if(n===5){art.src='../decor-five-hd.webp';art.alt='';art.className='number-five inflate'}else{art.textContent=String(n);art.className='foil inflate'}
  el('number-art').replaceChildren(art);el('age-caption').textContent=n+' '+numberWord(n);el('age-link').href=wb('фольгированные шары цифра '+n);
}
el('age').oninput=e=>setAge(e.target.value);
el('minus').onclick=()=>setAge(Math.max(1,currentAge-1));el('plus').onclick=()=>setAge(Math.min(99,currentAge+1));
const chapters=[
  ['2021','Первые наборы','Начали с наборов воздушных шаров. Идея была простой: чтобы гирлянду или фотозону можно было собрать дома своими руками.'],
  ['2023','Больше деталей для праздника','К шарам добавились растяжки, свечи, праздничная посуда и декор. Теперь украшения можно было подбирать вместе.'],
  ['Сегодня','Праздник в одном стиле','Готовые наборы, декор и сервировка помогают оформить и домашний день рождения, и большое торжество.']
];
let chapter=0;
function story(n){
  chapter=n;const [year,title,copy]=chapters[n];el('story-year').textContent=year;el('story-title').textContent=title;el('story-copy').textContent=copy;el('story-next').textContent=n===2?'Посмотреть с начала':'Следующая глава';
  const stage=el('story-bear');stage.replaceChildren();
  const all=[[-20,2],[8,0],[35,1]];const used=n===0?[all[0]]:n===1?all.slice(0,2):all;
  used.forEach(([angle,shade],i)=>{const wrap=document.createElement('span');wrap.className='held';wrap.style.setProperty('--angle',angle+'deg');wrap.style.setProperty('--lag',i*85+'ms');const im=new Image();im.src=balloon;im.alt='';im.style.filter=colors[shade][2];wrap.append(im);stage.append(wrap)});
  const bear=document.createElement('span');bear.className='mascot';stage.append(bear);
  document.querySelectorAll('[data-year]').forEach((b,i)=>b.setAttribute('aria-pressed',String(n===i)));
}
document.querySelectorAll('[data-year]').forEach(b=>b.onclick=()=>story(+b.dataset.year));el('story-next').onclick=()=>story((chapter+1)%3);
renderGarland(true);showStep(0);setAge(5);story(0);selectTab(location.hash.slice(1),false);
