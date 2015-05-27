(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["datum/datum_base.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<article template=\"";
output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "template_name"), env.opts.autoescape);
output += "\" model=\"datum_objects\"\r\n         datum_object_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_object_id", env.opts.autoescape), env.opts.autoescape);
output += "\" datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\" datum_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n    ";
context.getBlock("datum_content")(env, context, frame, runtime, function(t_2,t_1) {
if(t_2) { cb(t_2); return; }
output += t_1;
output += "\r\n</article>";
cb(null, output);
});
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
env.getTemplate("datum/datum_base.html", true, "datum\\datum_medium.html", function(t_2,parentTemplate) {
if(t_2) { cb(t_2); return; }
for(var t_1 in parentTemplate.blocks) {
context.addBlock(t_1, parentTemplate.blocks[t_1]);
}
output += "\r\n";
var t_3;
t_3 = "datum_medium";
frame.set("template_name", t_3, true);
if(!frame.parent) {
context.setVariable("template_name", t_3);
context.addExport("template_name");
}
output += "\r\n\r\n";
parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
});
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
var t_6 = runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"elements", env.opts.autoescape);
if(t_6) {var t_5 = t_6.length;
for(var t_4=0; t_4 < t_6.length; t_4++) {
var t_7 = t_6[t_4];
frame.set("element", t_7);
frame.set("loop.index", t_4 + 1);
frame.set("loop.index0", t_4);
frame.set("loop.revindex", t_5 - t_4);
frame.set("loop.revindex0", t_5 - t_4 - 1);
frame.set("loop.first", t_4 === 0);
frame.set("loop.last", t_4 === t_5 - 1);
frame.set("loop.length", t_5);
output += "\r\n        ";
env.getTemplate("element/element.html", false, "datum\\datum_medium.html", function(t_10,t_8) {
if(t_10) { cb(t_10); return; }
t_8.render(context.getVariables(), frame.push(), function(t_11,t_9) {
if(t_11) { cb(t_11); return; }
output += t_9
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
env.getTemplate("datum/datum_base.html", true, "datum\\datum_small.html", function(t_2,parentTemplate) {
if(t_2) { cb(t_2); return; }
for(var t_1 in parentTemplate.blocks) {
context.addBlock(t_1, parentTemplate.blocks[t_1]);
}
output += "\r\n";
var t_3;
t_3 = "datum_small";
frame.set("template_name", t_3, true);
if(!frame.parent) {
context.setVariable("template_name", t_3);
context.addExport("template_name");
}
output += "\r\n\r\n";
parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_datum_content(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "\r\n\r\n    <p class=\"datum_type_name\">";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"datum_type_name", env.opts.autoescape), env.opts.autoescape);
output += "</p>\r\n    <p class=\"headline\" style=\"font-size: ";
output += runtime.suppressValue(100 - env.getFilter("length").call(context, runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"headline", env.opts.autoescape)), env.opts.autoescape);
output += "%\">";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "datum")),"headline", env.opts.autoescape), env.opts.autoescape);
output += "</p>\r\n\r\n";
cb(null, output);
;
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
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
output += "</label>\r\n<input class=\"element\"\r\n       model=\"element_datum_objects\"\r\n       element_datum_object_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_datum_object_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       element_datum_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       element_type_id=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       type=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"html_input_type", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       name=\"element_value\"\r\n       value=\"";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "element")),"element_value", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n       onchange=\"Tracuse.models.updateDataOne(this)\">";
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
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/viewuse_base.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<section class=\"viewuse\" template=\"";
output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "template_name"), env.opts.autoescape);
output += "\" id=\"";
output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "id"), env.opts.autoescape);
output += "\"\r\n         onmouseenter=\"Tracuse.ui.viewuse.mouseEnter(this, event)\"\r\n         onmouseleave=\"Tracuse.ui.viewuse.mouseLeave(this, event)\">\r\n    <input name=\"title\" value=\"View Title\">\r\n    <button name=\"new-object\" onclick=\"Tracuse.ui.viewuse.openObjectPanel(this, event)\"><i>+</i><span>New Object</span></button>\r\n    <button name=\"view-settings\" onclick=\"Tracuse.ui.viewuse.openViewPanel(this, event)\"><i>---------</i><span>View Settings</span></button>\r\n    <button name=\"close-view\" onclick=\"Tracuse.ui.viewuse.closeView(this, event)\"><i>X</i><span>Close View</span></button>\r\n    <div class=\"content\">\r\n        ";
context.getBlock("viewuse_content")(env, context, frame, runtime, function(t_2,t_1) {
if(t_2) { cb(t_2); return; }
output += t_1;
output += "\r\n    </div>\r\n</section>";
cb(null, output);
});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_viewuse_content(env, context, frame, runtime, cb) {
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
return {
b_viewuse_content: b_viewuse_content,
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/viewuse_tile.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
env.getTemplate("viewuse/viewuse_base.html", true, "viewuse\\viewuse_tile.html", function(t_2,parentTemplate) {
if(t_2) { cb(t_2); return; }
for(var t_1 in parentTemplate.blocks) {
context.addBlock(t_1, parentTemplate.blocks[t_1]);
}
output += "\r\n";
var t_3;
t_3 = "viewuse_tile";
frame.set("template_name", t_3, true);
if(!frame.parent) {
context.setVariable("template_name", t_3);
context.addExport("template_name");
}
output += "\r\n\r\n";
parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
function b_viewuse_content(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "\r\n    ";
frame = frame.push();
var t_6 = runtime.contextOrFrameLookup(context, frame, "datums");
if(t_6) {var t_5 = t_6.length;
for(var t_4=0; t_4 < t_6.length; t_4++) {
var t_7 = t_6[t_4];
frame.set("datum", t_7);
frame.set("loop.index", t_4 + 1);
frame.set("loop.index0", t_4);
frame.set("loop.revindex", t_5 - t_4);
frame.set("loop.revindex0", t_5 - t_4 - 1);
frame.set("loop.first", t_4 === 0);
frame.set("loop.last", t_4 === t_5 - 1);
frame.set("loop.length", t_5);
output += "\r\n        ";
var t_8;
t_8 = "datum/" + runtime.contextOrFrameLookup(context, frame, "datumTemplate") + ".html";
frame.set("template", t_8, true);
if(!frame.parent) {
context.setVariable("template", t_8);
context.addExport("template");
}
output += " ";
env.getTemplate(runtime.contextOrFrameLookup(context, frame, "template"), false, "viewuse\\viewuse_tile.html", function(t_11,t_9) {
if(t_11) { cb(t_11); return; }
t_9.render(context.getVariables(), frame.push(), function(t_12,t_10) {
if(t_12) { cb(t_12); return; }
output += t_10
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
b_viewuse_content: b_viewuse_content,
root: root
};
})();
})();

