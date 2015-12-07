var gulp = require('gulp');
var jade = require('gulp-jade');
var $ = require('gulp-load-plugins')();

gulp.task('jade', function() {
  var LOCALS = {};

  gulp.src('./shorts/templates/short_tpl/*.jade')
    .pipe(jade({
      locals: LOCALS
    }))
    .pipe(gulp.dest('./shorts/templates/short/'))
});

gulp.task('watch', function() {
  gulp.watch('./shorts/templates/short_tpl/*.jade', ['jade']);
  gulp.watch(['static_raw/zu/scss/**/*.scss'], ['sass']);
  gulp.watch(['static_raw/zu/js/*.js'], ['js']);
})

var sassPaths = [
  'static_raw/zu/bower_components/foundation-sites/scss',
  'static_raw/zu/bower_components/motion-ui/src'
];

gulp.task('js', function() {
  gulp.src('./static_raw/zu/js/app.js')
    .pipe(gulp.dest('./static/style/js'));
})

gulp.task('sass', function() {
  return gulp.src('static_raw/zu/scss/app.scss')
    .pipe($.sass({
        includePaths: sassPaths
      })
      .on('error', $.sass.logError))
    .pipe($.autoprefixer({
      browsers: ['last 2 versions', 'ie >= 9']
    }))
    .pipe(gulp.dest('./static/style'));
});
