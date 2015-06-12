module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),
        concat: {
            options: {
                banner: "loadTracuse();\n"
            },
            models: {
                src: ["<%= pkg.dir.app %>models/utils.js", "<%= pkg.dir.app %>/models/*"],
                dest: "<%= pkg.dir.app %>models.js"
            },
            views: {
                src: ["<%= pkg.dir.app %>views/utils.js", "<%= pkg.dir.app %>/views/*"],
                dest: "<%= pkg.dir.app %>views.js"
            },
            controller: {
                src: ["<%= pkg.dir.app %>controller/utils.js", "<%= pkg.dir.app %>/controller/*"],
                dest: "<%= pkg.dir.app %>controller.js"
            },
            templates: {
                src: ["<%= pkg.dir.templates %>compiled_templates.js", "<%= pkg.dir.templates %>template_init.js"],
                dest: "<%= pkg.dir.app %>templates.js"
            }
        },

        nunjucks: {
            precompile: {
                baseDir: "<%= pkg.dir.templates %>",
                src: ["<%= pkg.dir.templates %>**/*.html"],
                dest: "<%= pkg.dir.templates %>compiled_templates.js"
            }
        },

        watch: {
            nunjucks: {
                files: ["<%= pkg.dir.templates %>**/*.html"],
                tasks: ["nunjucks"]
            },
            concat_models: {
                files: ["<%= pkg.dir.app %>/models/*"],
                tasks: ["concat:models"]
            },
            concat_views: {
                files: ["<%= pkg.dir.app %>/views/*"],
                tasks: ["concat:views"]
            },
            concat_controller: {
                files: ["<%= pkg.dir.app %>/controller/*"],
                tasks: ["concat:controller"]
            },
            concat_templates: {
                files: ["<%= pkg.dir.app %>/templates/*"],
                tasks: ["concat:templates"]
            }
        }
    });

    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks("grunt-nunjucks");

    grunt.registerTask("default", ["watch"]);

};