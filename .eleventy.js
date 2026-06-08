module.exports = function (eleventyConfig) {
  // Copy static assets straight through to the built site
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/admin");

  // Friendly date filter for posts (e.g. "June 2026")
  eleventyConfig.addFilter("monthYear", (d) => {
    const date = new Date(d);
    return date.toLocaleDateString("en-US", { month: "long", year: "numeric" });
  });

  // Short year for publication lists (e.g. "'24")
  eleventyConfig.addFilter("shortYear", (y) => "'" + String(y).slice(-2));
eleventyConfig.addFilter("pad2", (n) => String(n).padStart(2, "0"));

  // Collections
  eleventyConfig.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/posts/*.md").reverse()
  );

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["njk", "md", "html"],
  };
};
