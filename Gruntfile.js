module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),
        nunjucks: {
            precompile: {
                baseDir: "<%= pkg.dirAssets %>/templates/",
                src: ["<%= pkg.dirAssets %>/templates/*.html", "<%= pkg.dirAssets %>/templates/*/*.html"],
                dest: "<%= pkg.dirAssets %>/templates/compiled_templates.js"
            }
        },
        watch: {
            nunjucks: {
                files: ["<%= pkg.dirAssets %>/templates/*.html", "<%= pkg.dirAssets %>/templates/*/*.html"],
                tasks: ['nunjucks']
            }
        }
    });

    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-nunjucks");

    grunt.registerTask("default", ["watch"]);

};