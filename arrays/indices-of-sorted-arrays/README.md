<div style='padding:16px'>This problem was recently asked by AirBNB:<BR><BR>
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.<BR><BR>Example:<pre style="font-size:12px;font-family:courier;background-color:#f0f0f0;padding:4px;">Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9<BR>Output: [6,8]<BR><BR>Input: A = [100, 150, 150, 153], target = 150<BR>Output: [1,2]<BR><BR>Input: A = [1,2,3,4,5,6,10], target = 9<BR>Output: [-1, -1]<BR></pre>Here is a function signature example:<BR><BR><div style="background: #f8f8f8; overflow:auto;width:auto;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; font-family:courier;font-size:12px; line-height: 100%"><span style="color: #204a87; font-weight: bold">class</span> <span style="color: #000000">Solution</span><span style="color: #000000; font-weight: bold">:</span> <BR>  <span style="color: #204a87; font-weight: bold">def</span> <span style="color: #000000">getRange</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">arr</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">target</span><span style="color: #000000; font-weight: bold">):</span><BR>    <span style="color: #8f5902; font-style: italic"># Fill this in.</span><BR>  <BR><span style="color: #8f5902; font-style: italic"># Test program </span><BR><span style="color: #000000">arr</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000; font-weight: bold">[</span><span style="color: #0000cf; font-weight: bold">1</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">2</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">2</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">2</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">2</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">3</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">4</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">7</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">8</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #0000cf; font-weight: bold">8</span><span style="color: #000000; font-weight: bold">]</span> <BR><span style="color: #000000">x</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #0000cf; font-weight: bold">2</span><BR><span style="color: #204a87; font-weight: bold">print</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #000000">Solution</span><span style="color: #000000; font-weight: bold">()</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">getRange</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #000000">arr</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">x</span><span style="color: #000000; font-weight: bold">))</span><BR><span style="color: #8f5902; font-style: italic"># [1, 4]</span><BR></pre>