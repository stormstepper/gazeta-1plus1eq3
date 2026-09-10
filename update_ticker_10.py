import re

old_ticker_inner = '<div class="ticker__inner"><span><b>BREAKING:</b> Ministri dënohet 1 vit me kusht — gazi lotsjellës merr pension të hershëm</span><span><b>LIVE:</b> 29% e shportës shqiptare shkon në bukë — pjesa tjetër shkon në pritje</span><span><b>BREAKING:</b> 57% e familjeve kosovare s\'kanë para për pushime — plazhi zhvendoset në ballkon</span><span><b>BREAKING:</b> Kosova drejt 4 tetorit pa president — ora kushtetuese tik-tak</span><span><b>LIVE:</b> Donjeta Sadiku merr arin, kundërshtarja nuk vjen ta marrë argjendin</span><span><b>BREAKING:</b> Qumështarët presin autorizimin e AUV-së — deri të premten, ose sërish jo</span><span><b>BREAKING:</b> Ministri dënohet 1 vit me kusht — gazi lotsjellës merr pension të hershëm</span><span><b>LIVE:</b> 29% e shportës shqiptare shkon në bukë — pjesa tjetër shkon në pritje</span><span><b>BREAKING:</b> 57% e familjeve kosovare s\'kanë para për pushime — plazhi zhvendoset në ballkon</span><span><b>BREAKING:</b> Kosova drejt 4 tetorit pa president — ora kushtetuese tik-tak</span><span><b>LIVE:</b> Donjeta Sadiku merr arin, kundërshtarja nuk vjen ta marrë argjendin</span><span><b>BREAKING:</b> Qumështarët presin autorizimin e AUV-së — deri të premten, ose sërish jo</span></div>'

new_span_block = '<span><b>BREAKING:</b> KEK shet 3 milionë ton qymyr jashtë — rryma vazhdon të vijë nga jashtë, në drejtim të kundërt</span><span><b>LIVE:</b> Malisheva lider në Superligë, Uka: "pse jo edhe kampion", redaksia jonë shton "pse jo edhe 1+1=5"</span><span><b>BREAKING:</b> Divjaka në ditën e 41-të të protestës — kalendari lokal ka tashmë muajin e vet</span><span><b>LIVE:</b> Showbiz rajonal: një shpullë, dy ndjesë, tri deklarata për shtyp</span><span><b>BREAKING:</b> Kosova drejt 4 tetorit pa president — ora kushtetuese tik-tak</span><span><b>LIVE:</b> Donjeta Sadiku merr arin, kundërshtarja nuk vjen ta marrë argjendin</span>'

new_ticker_inner = '<div class="ticker__inner">' + new_span_block + new_span_block + '</div>'

files = ['index.html', 'politike.html', 'ekonomia.html', 'edukimi.html', 'turizmi.html', 'showbiz.html', 'sporti.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_ticker_inner in content:
        content = content.replace(old_ticker_inner, new_ticker_inner)
        print(f"{fn}: ticker updated")
    else:
        print(f"{fn}: OLD TICKER NOT FOUND (check manually)")
    # Update masthead date
    content = content.replace('Edicioni i mërkurë, 9 shtator 2026', 'Edicioni i enjte, 10 shtator 2026')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done.")
