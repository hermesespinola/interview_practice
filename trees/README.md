# Tree Serialization

You are given the root of a binary tree. You need to implement 2 functions:<BR><BR>1. serialize(root) which serializes the tree into a string representation<BR>2. deserialize(s) which deserializes the string back to the original tree that it represents<BR><BR>For this problem, often you will be asked to design your own serialization format.  However, for simplicity, let's use the pre-order traversal of the tree.  Here's your starting point:<BR><BR><div style="background: #f8f8f8; overflow:auto;width:auto;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; font-family:courier;font-size:12px; line-height: 100%"><span style="color: #204a87; font-weight: bold">class</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">:</span><BR>  <span style="color: #204a87; font-weight: bold">def</span> <span style="color: #000000">__init__</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">val</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">left</span><span style="color: #ce5c00; font-weight: bold">=</span><span style="color: #3465a4">None</span><span style="color: #000000; font-weight: bold">,</span> <span style="color: #000000">right</span><span style="color: #ce5c00; font-weight: bold">=</span><span style="color: #3465a4">None</span><span style="color: #000000; font-weight: bold">):</span><BR>    <span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">val</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">val</span><BR>    <span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">left</span><BR>    <span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">right</span><BR><BR>  <span style="color: #204a87; font-weight: bold">def</span> <span style="color: #000000">__str__</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #000000; font-weight: bold">):</span><BR>    <span style="color: #8f5902; font-style: italic"># pre-order printing of the tree.</span><BR>    <span style="color: #000000">result</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #4e9a06">&#39;&#39;</span><BR>    <span style="color: #000000">result</span> <span style="color: #ce5c00; font-weight: bold">+=</span> <span style="color: #204a87">str</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">val</span><span style="color: #000000; font-weight: bold">)</span><BR>    <span style="color: #204a87; font-weight: bold">if</span> <span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span><span style="color: #000000; font-weight: bold">:</span><BR>      <span style="color: #000000">result</span> <span style="color: #ce5c00; font-weight: bold">+=</span> <span style="color: #204a87">str</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span><span style="color: #000000; font-weight: bold">)</span><BR>    <span style="color: #204a87; font-weight: bold">if</span> <span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span><span style="color: #000000; font-weight: bold">:</span><BR>      <span style="color: #000000">result</span> <span style="color: #ce5c00; font-weight: bold">+=</span> <span style="color: #204a87">str</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #3465a4">self</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span><span style="color: #000000; font-weight: bold">)</span><BR>    <span style="color: #204a87; font-weight: bold">return</span> <span style="color: #000000">result</span><BR><BR><span style="color: #204a87; font-weight: bold">def</span> <span style="color: #000000">serialize</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #000000">root</span><span style="color: #000000; font-weight: bold">):</span><BR>  <span style="color: #8f5902; font-style: italic"># Fill this in.</span><BR><BR><span style="color: #204a87; font-weight: bold">def</span> <span style="color: #000000">deserialize</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #000000">data</span><span style="color: #000000; font-weight: bold">):</span><BR>  <span style="color: #8f5902; font-style: italic"># Fill this in.</span><BR><BR><span style="color: #8f5902; font-style: italic">#     1</span><BR><span style="color: #8f5902; font-style: italic">#    / \\</span><BR><span style="color: #8f5902; font-style: italic">#   3   4</span><BR><span style="color: #8f5902; font-style: italic">#  / \   \\</span><BR><span style="color: #8f5902; font-style: italic"># 2   5   7</span><BR><span style="color: #000000">tree</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">1</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #000000">tree</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">3</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #000000">tree</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">2</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #000000">tree</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">left</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">5</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #000000">tree</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">4</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #000000">tree</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span><span style="color: #ce5c00; font-weight: bold">.</span><span style="color: #000000">right</span> <span style="color: #ce5c00; font-weight: bold">=</span> <span style="color: #000000">Node</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #0000cf; font-weight: bold">7</span><span style="color: #000000; font-weight: bold">)</span><BR><BR><span style="color: #204a87; font-weight: bold">print</span> <span style="color: #000000">serialize</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #000000">tree</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #8f5902; font-style: italic"># 1 3 2 # # 5 # # 4 # 7 # #</span><BR><span style="color: #204a87; font-weight: bold">print</span> <span style="color: #000000">deserialize</span><span style="color: #000000; font-weight: bold">(</span><span style="color: #4e9a06">&#39;1 3 2 # # 5 # # 4 # 7 # #&#39;</span><span style="color: #000000; font-weight: bold">)</span><BR><span style="color: #8f5902; font-style: italic"># 132547</span><BR></pre></div><BR><BR>