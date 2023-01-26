const { series } = require('gulp');
const cleanCSS = require('gulp-clean-css');
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');
const terser = require('gulp-terser');

function cssCompile() {
    return gulp.src('./docs/_static/scss/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass.sync().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./docs/_static/css'));
}

function cssMinify() {
    return gulp.src('./docs/_static/css/*.css')
        .pipe(cleanCSS())
        .pipe(gulp.dest('./docs/_static/css'));
}

function jsMinify() {
    return gulp.src('./docs/_static/js/*.js')
        .pipe(terser())
        .pipe(gulp.dest('./docs/_static/js'));
}

exports.default = series(cssCompile);
exports.buildProd = series(cssCompile, cssMinify, jsMinify);
