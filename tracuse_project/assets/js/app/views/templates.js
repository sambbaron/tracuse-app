(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["datum/datum.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<x-datum template=\"";
context.getBlock("template_name")(env, context, frame, runtime, function(t_2,t_1) {
if(t_2) { cb(t_2); return; }
output += t_1;
output += "\"\r\n         datum_object_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_object_id", env.opts.autoescape), env.opts.autoescape);
output += "\" datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\" datum_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n    ";
context.getBlock("datum_content")(env, context, frame, runtime, function(t_4,t_3) {
if(t_4) { cb(t_4); return; }
output += t_3;
output += "\r\n</x-datum>";
cb(null, output);
})});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_template_name(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_datum_content(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "datum"), env.opts.autoescape);
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
b_template_name: b_template_name,
b_datum_content: b_datum_content,
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["datum/datum_medium.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
env.getTemplate("datum/datum.html", true, "datum\\datum_medium.html", function(t_2,parentTemplate) {
if(t_2) { cb(t_2); return; }
for(var t_1 in parentTemplate.blocks) {
context.addBlock(t_1, parentTemplate.blocks[t_1]);
}
output += "\r\n\r\n";
output += "\r\n\r\n";
parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_template_name(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "datum_medium";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_datum_content(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "\r\n    ";
frame = frame.push();
var t_5 = runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"elements", env.opts.autoescape);
if(t_5) {var t_4 = t_5.length;
for(var t_3=0; t_3 < t_5.length; t_3++) {
var t_6 = t_5[t_3];
frame.set("element", t_6);
frame.set("loop.index", t_3 + 1);
frame.set("loop.index0", t_3);
frame.set("loop.revindex", t_4 - t_3);
frame.set("loop.revindex0", t_4 - t_3 - 1);
frame.set("loop.first", t_3 === 0);
frame.set("loop.last", t_3 === t_4 - 1);
frame.set("loop.length", t_4);
output += "\r\n        ";
env.getTemplate("element/element.html", false, "datum\\datum_medium.html", function(t_9,t_7) {
if(t_9) { cb(t_9); return; }
t_7.render(context.getVariables(), frame.push(), function(t_10,t_8) {
if(t_10) { cb(t_10); return; }
output += t_8
output += "\r\n    ";
})});
}
}
frame = frame.pop();
output += "\r\n";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
b_template_name: b_template_name,
b_datum_content: b_datum_content,
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["datum/datum_small.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
env.getTemplate("datum/datum.html", true, "datum\\datum_small.html", function(t_2,parentTemplate) {
if(t_2) { cb(t_2); return; }
for(var t_1 in parentTemplate.blocks) {
context.addBlock(t_1, parentTemplate.blocks[t_1]);
}
output += "\r\n\r\n";
output += "\r\n\r\n";
parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_template_name(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "datum_small";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_datum_content(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "\r\n    <span class=\"headline\">";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"headline", env.opts.autoescape), env.opts.autoescape);
output += "</span>\r\n    <span class=\"datum_type_name\">";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_type_name", env.opts.autoescape), env.opts.autoescape);
output += "</span>\r\n";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
b_template_name: b_template_name,
b_datum_content: b_datum_content,
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["element/element.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<label>";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_name", env.opts.autoescape), env.opts.autoescape);
output += "</label>\r\n<input is=\"x-datum-element\"\r\n       element_datum_object_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_datum_object_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       element_datum_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       element_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       type=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"html_input_type", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       value=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_value", env.opts.autoescape), env.opts.autoescape);
output += "\">";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/viewuse_basic.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<x-viewuse template=\"viewuse_basic\">\r\n    ";
frame = frame.push();
var t_3 = runtime.contextOrFrameLookup(context, frame, "datums");
if(t_3) {var t_2 = t_3.length;
for(var t_1=0; t_1 < t_3.length; t_1++) {
var t_4 = t_3[t_1];
frame.set("datum", t_4);
frame.set("loop.index", t_1 + 1);
frame.set("loop.index0", t_1);
frame.set("loop.revindex", t_2 - t_1);
frame.set("loop.revindex0", t_2 - t_1 - 1);
frame.set("loop.first", t_1 === 0);
frame.set("loop.last", t_1 === t_2 - 1);
frame.set("loop.length", t_2);
output += "\r\n        ";
var t_5;
t_5 = "datum/" + runtime.contextOrFrameLookup(context, frame, "datumTemplate") + ".html";
frame.set("template", t_5, true);
if(!frame.parent) {
context.setVariable("template", t_5);
context.addExport("template");
}
output += " ";
env.getTemplate(runtime.contextOrFrameLookup(context, frame, "template"), false, "viewuse\\viewuse_basic.html", function(t_8,t_6) {
if(t_8) { cb(t_8); return; }
t_6.render(context.getVariables(), frame.push(), function(t_9,t_7) {
if(t_9) { cb(t_9); return; }
output += t_7
output += "\r\n    ";
})});
}
}
frame = frame.pop();
output += "\r\n</x-viewuse>";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
root: root
};
})();
})();

