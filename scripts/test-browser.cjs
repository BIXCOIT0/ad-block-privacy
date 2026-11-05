'use strict';
const {chromium}=require('playwright'),assert=require('node:assert/strict'),fs=require('node:fs/promises'),path=require('node:path');
const root=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage();
  await page.route('**/*',async route=>{
   const u=new URL(route.request().url());assert.equal(u.origin,'https://privacy.test');
   const name=u.pathname==='/'?'index.html':u.pathname.slice(1);
   if(!['index.html','PRIVACY.md','PRIVACY.en.md'].includes(name))return route.fulfill({status:404,body:''});
   await route.fulfill({status:200,contentType:name.endsWith('.html')?'text/html':'text/plain',body:await fs.readFile(path.join(root,name))});
  });
  await page.goto('https://privacy.test/');await page.keyboard.press('Tab');assert.equal(await page.locator('.skip').evaluate(e=>e===document.activeElement),true);
  await page.keyboard.press('Enter');assert.equal(await page.locator('#content').evaluate(e=>e===document.activeElement),true);
  await page.locator('.languages a[lang="en"]').click();assert.ok(page.url().endsWith('#en'));
  await page.locator('.languages a[lang="pt-BR"]').click();assert.ok(page.url().endsWith('#pt'));
  await fs.mkdir(path.join(root,'test-results'),{recursive:true});
  for(const width of [320,375,768,1440])for(const zoom of [1,2]){
   await page.setViewportSize({width,height:900});await page.evaluate(z=>{document.documentElement.style.zoom=String(z);window.scrollTo(0,0);},zoom);
   const fit=await page.evaluate(()=>document.documentElement.scrollWidth<=document.documentElement.clientWidth+1);assert.ok(fit,`overflow ${width}/${zoom}`);
   await page.screenshot({path:path.join(root,`test-results/privacy-${width}-${zoom}.png`)});
  }
  await page.emulateMedia({forcedColors:'active'});await page.screenshot({path:path.join(root,'test-results/privacy-high-contrast.png')});
  console.log('PASS semantic page: skip link, PT/EN navigation, four widths x CSS zoom 1/2, forced-colors capture. Local fixtures only.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
