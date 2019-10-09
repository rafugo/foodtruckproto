'use strict';

// dependencies
var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var changed = require('gulp-changed');
var browserSync = require('browser-sync').create();



////////////////
// - SCSS/CSS
////////////////

var SCSS_SRC = './src/Assets/scss/**/*.scss';
var SCSS_DEST = './src/Assets/css';

// // Compile SCSS
// gulp.task('compile_scss', function(){
//
//   gulp.src(SCSS_SRC)
//   .pipe(sass().on('error', sass.logError))
//   .pipe(minifyCSS())
//   .pipe(rename({ suffix: '.min' }))
//   .pipe(changed(SCSS_DEST))
//   .pipe(gulp.dest(SCSS_DEST))
//   .pipe(browserSync.reload({
//     stream: true
//   }))
//
//
// });
//
// // browser sync
// gulp.task('browserSync', function() {
//   browserSync.init({
//     server: {
//       baseDir: "../foodtruckproject/",
//         directory: true
//     },
//   });
//
// });

gulp.task('sass', function() {
  return gulp.src(SCSS_SRC)
      .pipe(sass())
      .pipe(minifyCSS())
      .pipe(rename({ suffix: '.min' }))
      .pipe(changed(SCSS_DEST))
      .pipe(gulp.dest(SCSS_DEST))
      .pipe(browserSync.stream());
});

gulp.task('serve', gulp.series('sass', function() {

    browserSync.init({
      server: '../foodtruckproject/',
        directory: true
    });

    gulp.watch(SCSS_SRC, gulp.series('sass'));
    gulp.watch('../foodtruckproject/src/*.html').on('change', browserSync.reload);

}));



// // detect changes in SCSS
// gulp.task('watch_scss', gulp.series('browserSync', 'compile_scss'), function(){
//   gulp.series('browserSync')
//   .pipe(gulp.watch(SCSS_SRC, gulp.series('compile_scss')));
//
//   // gulp.watch(SCSS_SRC, gulp.series('compile_scss'));
// });

// Run tasks
gulp.task('default', gulp.parallel('serve'));
