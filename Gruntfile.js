module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),
        concat: {
            app: {
                src: [
                    "<%= pkg.dir.app %>main.js",
                    "<%= pkg.dir.app %>controller/utils.js", "<%= pkg.dir.app %>controller/*",
                    "<%= pkg.dir.app %>models/utils.js", "<%= pkg.dir.app %>models/*",
                    "<%= pkg.dir.app %>views/utils.js", "<%= pkg.dir.app %>views/**/*",
                    "<%= pkg.dir.app %>init.js"
                ],
                dest: "<%= pkg.dir.dist %>app.js"
            },
            styles_base: {
                src: [
                    "<%= pkg.dir.styles %>reset.css",
                    "<%= pkg.dir.styles %>base.css"
                ],
                dest: "<%= pkg.dir.dist %>styles_base.css"
            },
            styles_website: {
                src: [
                    "<%= pkg.dir.styles %>website/**"
                ],
                dest: "<%= pkg.dir.dist %>styles_website.css"
            },
            styles_app: {
                src: [
                    "<%= pkg.dir.styles %>app/base_app.css",
                    "<%= pkg.dir.styles %>app/**/**"
                ],
                dest: "<%= pkg.dir.dist %>styles_app.css"
            }
        },

        nunjucks: {
            precompile: {
                baseDir: "<%= pkg.dir.templates %>",
                src: ["<%= pkg.dir.templates %>**/*.html"],
                dest: "<%= pkg.dir.dist %>templates.js"
            }
        },

        watch: {
            nunjucks: {
                files: ["<%= pkg.dir.templates %>**/*.html"],
                tasks: ["nunjucks"]
            },
            concat_app: {
                files: ["<%= pkg.dir.app %>**/**/**"],
                tasks: ["concat:app"]
            },
            concat_styles_base: {
                files: ["<%= pkg.dir.styles %>*"],
                tasks: ["concat:styles_base"]
            },
            concat_styles_website: {
                files: ["<%= pkg.dir.styles %>website/*"],
                tasks: ["concat:styles_website"]
            },
            concat_styles_app: {
                files: ["<%= pkg.dir.styles %>app/**/**"],
                tasks: ["concat:styles_app"]
            }
        }
    });

    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks("grunt-nunjucks");

    grunt.registerTask("default", ["watch"]);

};