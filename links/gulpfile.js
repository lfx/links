var gulp = require('gulp');
var jade = require('gulp-jade');

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
})
