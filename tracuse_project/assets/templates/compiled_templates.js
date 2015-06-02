(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["datum/datum_base.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<article class=\"datum\" template=\"";
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
env.getTemplate("datum/datum_base.html", true, "datum/datum_medium.html", function(t_2,parentTemplate) {
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
env.getTemplate("element/element.html", false, "datum/datum_medium.html", function(t_10,t_8) {
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
env.getTemplate("datum/datum_base.html", true, "datum/datum_small.html", function(t_2,parentTemplate) {
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
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/datum_filter.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<h3 class=\"title\">Object Filter</h3>\r\n\r\n<div class=\"content\">\r\n\r\n    <div class=\"section groups-types col-1\">\r\n        <h4 class=\"title\">Groups/Types</h4>\r\n\r\n        <div class=\"content\">\r\n            ";
frame = frame.push();
var t_3 = runtime.contextOrFrameLookup(context, frame, "datum_groups");
if(t_3) {var t_2 = t_3.length;
for(var t_1=0; t_1 < t_3.length; t_1++) {
var t_4 = t_3[t_1];
frame.set("datum_group", t_4);
frame.set("loop.index", t_1 + 1);
frame.set("loop.index0", t_1);
frame.set("loop.revindex", t_2 - t_1);
frame.set("loop.revindex0", t_2 - t_1 - 1);
frame.set("loop.first", t_1 === 0);
frame.set("loop.last", t_1 === t_2 - 1);
frame.set("loop.length", t_2);
output += "\r\n                <fieldset class=\"input-group col-";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "loop")),"index", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                    <button class=\"filter-input\" name=\"datum_group\" value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_4),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                            onclick=\"Tracuse.app.viewuse.clickDatumGroup(this, event)\">\r\n                        ";
output += runtime.suppressValue(runtime.memberLookup((t_4),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                    </button>\r\n\r\n                    ";
frame = frame.push();
var t_7 = runtime.contextOrFrameLookup(context, frame, "datum_types");
if(t_7) {var t_6 = t_7.length;
for(var t_5=0; t_5 < t_7.length; t_5++) {
var t_8 = t_7[t_5];
frame.set("datum_type", t_8);
frame.set("loop.index", t_5 + 1);
frame.set("loop.index0", t_5);
frame.set("loop.revindex", t_6 - t_5);
frame.set("loop.revindex0", t_6 - t_5 - 1);
frame.set("loop.first", t_5 === 0);
frame.set("loop.last", t_5 === t_6 - 1);
frame.set("loop.length", t_6);
output += "\r\n                        ";
if(runtime.memberLookup((t_8),"datum_group_id", env.opts.autoescape) == runtime.memberLookup((t_4),"datum_group_id", env.opts.autoescape)) {
output += "\r\n                            <button class=\"filter-input\" name=\"datum_type\" value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_8),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((t_8),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    onclick=\"Tracuse.app.viewuse.clickDatumType(this, event)\">\r\n                                ";
output += runtime.suppressValue(runtime.memberLookup((t_8),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                            </button>\r\n                        ";
;
}
output += "\r\n                    ";
;
}
}
frame = frame.pop();
output += "\r\n                </fieldset>\r\n            ";
;
}
}
frame = frame.pop();
output += "\r\n        </div>\r\n    </div>\r\n\r\n    <div class=\"section associations col-2\">\r\n        <h4 class=\"title\">Associations</h4>\r\n\r\n        <div class=\"content\">\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Groups</h5>\r\n                <select name=\"datum_groups\"\r\n                        onchange=\"Tracuse.app.viewuse.selectDatumGroup(this, event)\">\r\n                    <option></option>\r\n                    ";
frame = frame.push();
var t_11 = runtime.contextOrFrameLookup(context, frame, "datum_groups");
if(t_11) {var t_10 = t_11.length;
for(var t_9=0; t_9 < t_11.length; t_9++) {
var t_12 = t_11[t_9];
frame.set("datum_group", t_12);
frame.set("loop.index", t_9 + 1);
frame.set("loop.index0", t_9);
frame.set("loop.revindex", t_10 - t_9);
frame.set("loop.revindex0", t_10 - t_9 - 1);
frame.set("loop.first", t_9 === 0);
frame.set("loop.last", t_9 === t_10 - 1);
frame.set("loop.length", t_10);
output += "\r\n                        <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_12),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                            ";
output += runtime.suppressValue(runtime.memberLookup((t_12),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                        </option>\r\n                    ";
;
}
}
frame = frame.pop();
output += "\r\n                </select>\r\n            </fieldset>\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Types</h5>\r\n                <select name=\"datum_types\"\r\n                        onchange=\"Tracuse.app.viewuse.selectDatumType(this, event)\">\r\n                    <option></option>\r\n                    ";
frame = frame.push();
var t_15 = runtime.contextOrFrameLookup(context, frame, "datum_types");
if(t_15) {var t_14 = t_15.length;
for(var t_13=0; t_13 < t_15.length; t_13++) {
var t_16 = t_15[t_13];
frame.set("datum_type", t_16);
frame.set("loop.index", t_13 + 1);
frame.set("loop.index0", t_13);
frame.set("loop.revindex", t_14 - t_13);
frame.set("loop.revindex0", t_14 - t_13 - 1);
frame.set("loop.first", t_13 === 0);
frame.set("loop.last", t_13 === t_14 - 1);
frame.set("loop.length", t_14);
output += "\r\n                        <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_16),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((t_16),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                            ";
output += runtime.suppressValue(runtime.memberLookup((t_16),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                        </option>\r\n                    ";
;
}
}
frame = frame.pop();
output += "\r\n                </select>\r\n            </fieldset>\r\n            <br>\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Objects</h5>\r\n                <select name=\"datum_objects\">\r\n                    <option></option>\r\n                </select>\r\n                <button class=\"add-filter\" name=\"add-association\"\r\n                        onclick=\"Tracuse.app.viewuse.addAssociatedDatum(this, event)\">\r\n                    +\r\n                </button>\r\n            </fieldset>\r\n\r\n        </div>\r\n    </div>\r\n\r\n    <div class=\"section elements col-3\">\r\n        <h4 class=\"title\">Elements</h4>\r\n\r\n        <div class=\"content\">\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Types</h5>\r\n                <select name=\"element_types\"\r\n                        onchange=\"Tracuse.app.viewuse.selectElement(this, event)\">\r\n                    <option></option>\r\n                    ";
frame = frame.push();
var t_19 = runtime.contextOrFrameLookup(context, frame, "element_types");
if(t_19) {var t_18 = t_19.length;
for(var t_17=0; t_17 < t_19.length; t_17++) {
var t_20 = t_19[t_17];
frame.set("element_type", t_20);
frame.set("loop.index", t_17 + 1);
frame.set("loop.index0", t_17);
frame.set("loop.revindex", t_18 - t_17);
frame.set("loop.revindex0", t_18 - t_17 - 1);
frame.set("loop.first", t_17 === 0);
frame.set("loop.last", t_17 === t_18 - 1);
frame.set("loop.length", t_18);
output += "\r\n                        <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_20),"element_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                            ";
output += runtime.suppressValue(runtime.memberLookup((t_20),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                        </option>\r\n                    ";
;
}
}
frame = frame.pop();
output += "\r\n                </select>\r\n            </fieldset>\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Operators</h5>\r\n                <select name=\"element_operators\">\r\n                    <option></option>\r\n                </select>\r\n            </fieldset>\r\n            <br>\r\n            <fieldset class=\"input-group\">\r\n                <h5 class=\"title\">Filter Value</h5>\r\n                <input name=\"element_value\">\r\n                <button class=\"add-filter\" name=\"add-element-filter\"\r\n                        onclick=\"Tracuse.app.viewuse.addElementFilter(this, event)\">\r\n                    +\r\n                </button>\r\n            </fieldset>\r\n        </div>\r\n    </div>\r\n</div>";
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
output += "\"\r\n         onmouseenter=\"Tracuse.app.viewuse.viewuseActive(this, event)\"\r\n         onfocus=\"Tracuse.app.viewuse.viewuseActive(this, event)\"\r\n         onmouseleave=\"Tracuse.app.viewuse.viewuseInactive(this, event)\">\r\n    <input name=\"title\" value=\"View Title\">\r\n\r\n    <div class=\"content\">\r\n        ";
context.getBlock("viewuse_content")(env, context, frame, runtime, function(t_2,t_1) {
if(t_2) { cb(t_2); return; }
output += t_1;
output += "\r\n    </div>\r\n\r\n    <nav class=\"viewuse-controls\">\r\n        <button name=\"viewuse-options\" onclick=\"Tracuse.app.viewuse.showHidePanel('viewuse-options', this, event)\">View<br>Options</button>\r\n        <br>\r\n        <button name=\"new-object\" onclick=\"Tracuse.app.viewuse.openObjectPanel(this, event)\">New<br>Object</button>\r\n        <br>\r\n    </nav>\r\n\r\n    ";
env.getTemplate("viewuse/viewuse_options.html", false, "viewuse/viewuse_base.html", function(t_5,t_3) {
if(t_5) { cb(t_5); return; }
t_3.render(context.getVariables(), frame.push(), function(t_6,t_4) {
if(t_6) { cb(t_6); return; }
output += t_4
output += "\r\n</section>\r\n";
cb(null, output);
})})});
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
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/viewuse_options.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
output += "<aside class=\"viewuse-panel viewuse-options\">\r\n    <h3 class=\"title\">View Options</h3>\r\n\r\n    <div class=\"section viewuse-select col-1\">\r\n        <h4 class=\"title\">Select View</h4>\r\n\r\n        <div class=\"content\">\r\n\r\n            <div class=\"input-group viewuse-open\">\r\n                <div class=\"content\">\r\n                    <select name=\"viewuse_object\">\r\n                        ";
frame = frame.push();
var t_3 = runtime.contextOrFrameLookup(context, frame, "viewuse_objects");
if(t_3) {var t_2 = t_3.length;
for(var t_1=0; t_1 < t_3.length; t_1++) {
var t_4 = t_3[t_1];
frame.set("viewuse_object", t_4);
frame.set("loop.index", t_1 + 1);
frame.set("loop.index0", t_1);
frame.set("loop.revindex", t_2 - t_1);
frame.set("loop.revindex0", t_2 - t_1 - 1);
frame.set("loop.first", t_1 === 0);
frame.set("loop.last", t_1 === t_2 - 1);
frame.set("loop.length", t_2);
output += "\r\n                            <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_4),"viewuse_object_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    ";
output += runtime.suppressValue((runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "this_viewuse")),"viewuse_object_id", env.opts.autoescape) == runtime.memberLookup((t_4),"viewuse_object_id", env.opts.autoescape)?" selected":""), env.opts.autoescape);
output += ">\r\n                                ";
output += runtime.suppressValue(runtime.memberLookup((t_4),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                            </option>\r\n                        ";
;
}
}
frame = frame.pop();
output += "\r\n                    </select>\r\n                    <br>\r\n                    <button name=\"save-viewuse\">Save View</button>\r\n                    <button name=\"rename-viewuse\">Rename View</button>\r\n                </div>\r\n            </div>\r\n\r\n            <div class=\"input-group viewuse-arrangement\">\r\n                <h4 class=\"title\">Arrangement</h4>\r\n\r\n                <div class=\"content\">\r\n                    <select name=\"viewuse_arrangement\">\r\n                        <option></option>\r\n                        ";
frame = frame.push();
var t_7 = runtime.contextOrFrameLookup(context, frame, "viewuse_arrangements");
if(t_7) {var t_6 = t_7.length;
for(var t_5=0; t_5 < t_7.length; t_5++) {
var t_8 = t_7[t_5];
frame.set("viewuse_arrangement", t_8);
frame.set("loop.index", t_5 + 1);
frame.set("loop.index0", t_5);
frame.set("loop.revindex", t_6 - t_5);
frame.set("loop.revindex0", t_6 - t_5 - 1);
frame.set("loop.first", t_5 === 0);
frame.set("loop.last", t_5 === t_6 - 1);
frame.set("loop.length", t_6);
output += "\r\n                            <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_8),"viewuse_arrangement_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    ";
output += runtime.suppressValue((runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "this_viewuse")),"viewuse_arrangement_id", env.opts.autoescape) == runtime.memberLookup((t_8),"viewuse_arrangement_id", env.opts.autoescape)?" selected":""), env.opts.autoescape);
output += ">\r\n                                ";
output += runtime.suppressValue(runtime.memberLookup((t_8),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                            </option>\r\n                        ";
;
}
}
frame = frame.pop();
output += "\r\n                    </select>\r\n                </div>\r\n            </div>\r\n\r\n            <div class=\"input-group viewuse-datum\">\r\n                <h4 class=\"title\">Object Format</h4>\r\n\r\n                <div class=\"content\">\r\n                    <select name=\"viewuse_datum col-1\">\r\n                        <option></option>\r\n                        ";
frame = frame.push();
var t_11 = runtime.contextOrFrameLookup(context, frame, "viewuse_datums");
if(t_11) {var t_10 = t_11.length;
for(var t_9=0; t_9 < t_11.length; t_9++) {
var t_12 = t_11[t_9];
frame.set("viewuse_datum", t_12);
frame.set("loop.index", t_9 + 1);
frame.set("loop.index0", t_9);
frame.set("loop.revindex", t_10 - t_9);
frame.set("loop.revindex0", t_10 - t_9 - 1);
frame.set("loop.first", t_9 === 0);
frame.set("loop.last", t_9 === t_10 - 1);
frame.set("loop.length", t_10);
output += "\r\n                            <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_12),"viewuse_datum_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    ";
output += runtime.suppressValue((runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "this_viewuse")),"viewuse_datum_id", env.opts.autoescape) == runtime.memberLookup((t_12),"viewuse_datum_id", env.opts.autoescape)?" selected":""), env.opts.autoescape);
output += ">\r\n                                ";
output += runtime.suppressValue(runtime.memberLookup((t_12),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                            </option>\r\n                        ";
;
}
}
frame = frame.pop();
output += "\r\n                    </select>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n    <div class=\"section datum-filter col-2\">\r\n        ";
env.getTemplate("viewuse/datum_filter.html", false, "viewuse/viewuse_options.html", function(t_15,t_13) {
if(t_15) { cb(t_15); return; }
t_13.render(context.getVariables(), frame.push(), function(t_16,t_14) {
if(t_16) { cb(t_16); return; }
output += t_14
output += "\r\n    </div>\r\n\r\n    <div class=\"section viewuse-format col-3\">\r\n        <h4 class=\"title\">View Format</h4>\r\n\r\n        <div class=\"content\">\r\n        </div>\r\n    </div>\r\n\r\n    <button name=\"apply-view\" onclick=\"\">Apply<br>View</button>\r\n    <button name=\"close-panel\" onclick=\"Tracuse.app.viewuse.showHidePanel('viewuse-options', this, event)\">X</button>\r\n</aside>";
cb(null, output);
})});
} catch (e) {
  cb(runtime.handleError(e, lineno, colno));
}
}
return {
root: root
};
})();
})();
(function() {(window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["viewuse/viewuse_tile.html"] = (function() {function root(env, context, frame, runtime, cb) {
var lineno = null;
var colno = null;
var output = "";
try {
env.getTemplate("viewuse/viewuse_base.html", true, "viewuse/viewuse_tile.html", function(t_2,parentTemplate) {
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
var t_6 = runtime.contextOrFrameLookup(context, frame, "datum_objects");
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
t_8 = "datum/" + runtime.contextOrFrameLookup(context, frame, "datum_template") + ".html";
frame.set("template", t_8, true);
if(!frame.parent) {
context.setVariable("template", t_8);
context.addExport("template");
}
output += " ";
env.getTemplate(runtime.contextOrFrameLookup(context, frame, "template"), false, "viewuse/viewuse_tile.html", function(t_11,t_9) {
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
