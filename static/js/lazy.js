(function ($) {
  $("#lazyLoadLink").on("click", function () {
    var link = $(this);
    var page = link.data("page");
    console.log(page);
    $.ajax({
      type: "post",
      url: "/lazy_load_news/",
      data: {
        page: page,
        csrfmiddlewaretoken: window.CSRF_TOKEN, // from index.html
      },
      success: function (data) {
        console.log(data.news_html);
        // if there are still more pages to load,
        // add 1 to the "Load More Posts" link's page data attribute
        // else hide the link
        if (data.has_next) {
          link.data("page", page + 1);
        } else {
          link.hide();
        }
        // append html to the posts div
        $("#news").append(data.news_html);
      },
      error: function (xhr, status, error) {
        console.log("Shit HAPPENS");
        // shit happens friends!
      },
    });
  });
})(jQuery);
