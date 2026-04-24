(function ($) {
  $(document).ready(function () {
    // Find all inputs whose name ends with _0 (date part of SplitDateTimeWidget)
    $("input[name$='_0']").each(function () {
      var $dateInput = $(this);
      var baseName = $dateInput.attr("name").slice(0, -2); // strip _0
      var $timeInput = $("input[name='" + baseName + "_1']");

      if ($timeInput.length) {
        // Avoid adding duplicate buttons
        if ($timeInput.next(".set-now-btn").length) return;

        var $btn = $(
          '<button type="button" class="button set-now-btn" style="margin-left:8px;vertical-align:middle;">Set to Now</button>'
        );

        $btn.on("click", function () {
          var now = new Date();

          // Format date: YYYY-MM-DD
          var year = now.getFullYear();
          var month = String(now.getMonth() + 1).padStart(2, "0");
          var day = String(now.getDate()).padStart(2, "0");
          $dateInput.val(year + "-" + month + "-" + day);

          // Format time: HH:MM:SS
          var hours = String(now.getHours()).padStart(2, "0");
          var minutes = String(now.getMinutes()).padStart(2, "0");
          var seconds = String(now.getSeconds()).padStart(2, "0");
          $timeInput.val(hours + ":" + minutes + ":" + seconds);
        });

        $timeInput.after($btn);
      }
    });
  });
})(django.jQuery);
