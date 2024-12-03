<h1 class="title">A. Плот</h1><table><tbody><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></tbody></table></div><h2></h2><div class="legend"><p>Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (<span class="math inline"><span class="katex"><span class="katex-mathml">
    Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (
x
1
​
 , 
y
1
​
 ), северо-восточный угол – координаты (
x
2
​
 , 
y
2
​
 ).

Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.
<p><img src="https://contest-problem-files.s3-private.mds.yandex.net/problems/10000167-13ba-548b-2661-af44a319ec69/files/a1791b28-e3ff-4aeb-9eed-ae1ba9c58c2b?response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241203T145514Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=V0T1EzqIkxfG5tKj9dfL%2F20241203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bdb81b8ba1cb2f62e24a51c6a5b01ae32a09d5745e6a769916ca2ab9d3132ee6" alt="image"></p>

<h2>Формат ввода</h2>
<div>Программа получает на вход шесть чисел в следующем порядке: 
x
1
​
 , 
y
1

​
  (координаты юго-западного угла плота), 
x
2
​
 , 
y
2
​
  (координаты северо-восточного угла плота), 
x, 
y (координаты пловца). Все числа целые и по модулю не превосходят 100. Гарантируется, что 
x
1
<
x
2
, 
y
1
<
y
2
, 
x
≠
x
1
, 
x
≠
x
2
, 
y
≠
y
1
, 
y
≠
y
2
, координаты пловца находятся вне плота.
</div>

<h2>Формат вывода</h2><div class="output-specification"><p>Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”, к южной&nbsp;— символ ”S”, к западной&nbsp;— символ ”W”, к восточной&nbsp;— символ ”E”. Если пловцу следует плыть к углу плота, нужно вывести одну из следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th><th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th></tr></thead><tbody><tr><td><pre>-1
-2
5
3
-4
6
</pre></td><td><pre>NW
</pre></td></tr></tbody></table></div></div>
