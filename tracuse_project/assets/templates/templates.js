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
output += "\r\n    </div>\r\n    <aside class=\"panel object-panel\">\r\n        <h3 class=\"title\" onclick=\"Tracuse.ui.viewuse.showHidePanel(this, event)\">\r\n            Object Filter\r\n        </h3>\r\n\r\n        <div class=\"content\">\r\n            <div class=\"section groups-types\">\r\n                <h4 class=\"title\" onclick=\"Tracuse.ui.viewuse.showHidePanel(this, event)\">Groups/Types</h4>\r\n\r\n                <div class=\"content\">\r\n                    ";
frame = frame.push();
var t_5 = runtime.contextOrFrameLookup(context, frame, "datum_groups");
if(t_5) {var t_4 = t_5.length;
for(var t_3=0; t_3 < t_5.length; t_3++) {
var t_6 = t_5[t_3];
frame.set("datum_group", t_6);
frame.set("loop.index", t_3 + 1);
frame.set("loop.index0", t_3);
frame.set("loop.revindex", t_4 - t_3);
frame.set("loop.revindex0", t_4 - t_3 - 1);
frame.set("loop.first", t_3 === 0);
frame.set("loop.last", t_3 === t_4 - 1);
frame.set("loop.length", t_4);
output += "\r\n                        <fieldset class=\"input-group col-";
output += runtime.suppressValue(runtime.memberLookup((runtime.contextOrFrameLookup(context, frame, "loop")),"index", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                            <button class=\"filter-input\" name=\"datum_group\" value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_6),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                    onclick=\"Tracuse.ui.viewuse.clickDatumGroup(this, event)\">\r\n                                ";
output += runtime.suppressValue(runtime.memberLookup((t_6),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                            </button>\r\n\r\n                            ";
frame = frame.push();
var t_9 = runtime.contextOrFrameLookup(context, frame, "datum_types");
if(t_9) {var t_8 = t_9.length;
for(var t_7=0; t_7 < t_9.length; t_7++) {
var t_10 = t_9[t_7];
frame.set("datum_type", t_10);
frame.set("loop.index", t_7 + 1);
frame.set("loop.index0", t_7);
frame.set("loop.revindex", t_8 - t_7);
frame.set("loop.revindex0", t_8 - t_7 - 1);
frame.set("loop.first", t_7 === 0);
frame.set("loop.last", t_7 === t_8 - 1);
frame.set("loop.length", t_8);
output += "\r\n                                ";
if(runtime.memberLookup((t_10),"datum_group_id", env.opts.autoescape) == runtime.memberLookup((t_6),"datum_group_id", env.opts.autoescape)) {
output += "\r\n                                    <button class=\"filter-input\" name=\"datum_type\" value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_10),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                            datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((t_10),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                            onclick=\"Tracuse.ui.viewuse.clickDatumType(this, event)\">\r\n                                        ";
output += runtime.suppressValue(runtime.memberLookup((t_10),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                                    </button>\r\n                                ";
;
}
output += "\r\n                            ";
;
}
}
frame = frame.pop();
output += "\r\n                        </fieldset>\r\n                    ";
;
}
}
frame = frame.pop();
output += "\r\n                </div>\r\n            </div>\r\n\r\n            <div class=\"section associations\">\r\n                <h4 class=\"title\" onclick=\"Tracuse.ui.viewuse.showHidePanel(this, event)\">Associations</h4>\r\n\r\n                <div class=\"content\">\r\n                    <fieldset class=\"input-group\">\r\n                        <h5 class=\"title\">Groups</h5>\r\n                        <select name=\"datum_groups\"\r\n                                onchange=\"Tracuse.ui.viewuse.selectDatumGroup(this, event)\">\r\n                            <option></option>\r\n                            ";
frame = frame.push();
var t_13 = runtime.contextOrFrameLookup(context, frame, "datum_groups");
if(t_13) {var t_12 = t_13.length;
for(var t_11=0; t_11 < t_13.length; t_11++) {
var t_14 = t_13[t_11];
frame.set("datum_group", t_14);
frame.set("loop.index", t_11 + 1);
frame.set("loop.index0", t_11);
frame.set("loop.revindex", t_12 - t_11);
frame.set("loop.revindex0", t_12 - t_11 - 1);
frame.set("loop.first", t_11 === 0);
frame.set("loop.last", t_11 === t_12 - 1);
frame.set("loop.length", t_12);
output += "\r\n                                <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_14),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                                    ";
output += runtime.suppressValue(runtime.memberLookup((t_14),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                                </option>\r\n                            ";
;
}
}
frame = frame.pop();
output += "\r\n                        </select>\r\n                    </fieldset>\r\n                    <fieldset class=\"input-group\">\r\n                        <h5 class=\"title\">Types</h5>\r\n                        <select name=\"datum_types\"\r\n                                onchange=\"Tracuse.ui.viewuse.selectDatumType(this, event)\">\r\n                            <option></option>\r\n                            ";
frame = frame.push();
var t_17 = runtime.contextOrFrameLookup(context, frame, "datum_types");
if(t_17) {var t_16 = t_17.length;
for(var t_15=0; t_15 < t_17.length; t_15++) {
var t_18 = t_17[t_15];
frame.set("datum_type", t_18);
frame.set("loop.index", t_15 + 1);
frame.set("loop.index0", t_15);
frame.set("loop.revindex", t_16 - t_15);
frame.set("loop.revindex0", t_16 - t_15 - 1);
frame.set("loop.first", t_15 === 0);
frame.set("loop.last", t_15 === t_16 - 1);
frame.set("loop.length", t_16);
output += "\r\n                                <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_18),"datum_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\"\r\n                                        datum_group_id=\"";
output += runtime.suppressValue(runtime.memberLookup((t_18),"datum_group_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                                    ";
output += runtime.suppressValue(runtime.memberLookup((t_18),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                                </option>\r\n                            ";
;
}
}
frame = frame.pop();
output += "\r\n                        </select>\r\n                    </fieldset>\r\n                    <br>\r\n                    <fieldset class=\"input-group\">\r\n                        <h5 class=\"title\">Objects</h5>\r\n                        <select name=\"datum_objects\">\r\n                            <option></option>\r\n                        </select>\r\n                        <button name=\"add-association\"\r\n                                onclick=\"Tracuse.ui.viewuse.addAssociatedDatum(this, event)\">\r\n                            +\r\n                        </button>\r\n                    </fieldset>\r\n\r\n                </div>\r\n            </div>\r\n            <div class=\"section elements\">\r\n                <h4 class=\"title\" onclick=\"Tracuse.ui.viewuse.showHidePanel(this, event)\">Elements</h4>\r\n\r\n                <div class=\"content\">\r\n                    <fieldset class=\"input-group\">\r\n                        <h5 class=\"title\">Types</h5>\r\n                        <select name=\"element_types\"\r\n                                onchange=\"Tracuse.ui.viewuse.selectElement(this, event)\">\r\n                            <option></option>\r\n                            ";
frame = frame.push();
var t_21 = runtime.contextOrFrameLookup(context, frame, "element_types");
if(t_21) {var t_20 = t_21.length;
for(var t_19=0; t_19 < t_21.length; t_19++) {
var t_22 = t_21[t_19];
frame.set("element_type", t_22);
frame.set("loop.index", t_19 + 1);
frame.set("loop.index0", t_19);
frame.set("loop.revindex", t_20 - t_19);
frame.set("loop.revindex0", t_20 - t_19 - 1);
frame.set("loop.first", t_19 === 0);
frame.set("loop.last", t_19 === t_20 - 1);
frame.set("loop.length", t_20);
output += "\r\n                                <option value=\"";
output += runtime.suppressValue(runtime.memberLookup((t_22),"element_type_id", env.opts.autoescape), env.opts.autoescape);
output += "\">\r\n                                    ";
output += runtime.suppressValue(runtime.memberLookup((t_22),"readable_name", env.opts.autoescape), env.opts.autoescape);
output += "\r\n                                </option>\r\n                            ";
;
}
}
frame = frame.pop();
output += "\r\n                        </select>\r\n                        <br>\r\n                        <h5 class=\"title\">Operators</h5>\r\n                        <select name=\"element_operators\">\r\n                            <option></option>\r\n                        </select>\r\n                        <h5 class=\"title\">Filter Value</h5>\r\n                        <input name=\"element_value\">\r\n                    </fieldset>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n    </aside>\r\n    <aside class=\"panel view-panel\">\r\n        <h3 class=\"title\" onclick=\"Tracuse.ui.viewuse.showHidePanel(this, event)\">\r\n            View Settings\r\n        </h3>\r\n\r\n    </aside>\r\n</section>";
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
